"""IPv4 / IPv6 helpers for CN Unit 4: every numerical answer is computed here (and cross-checked with the
standard ipaddress module in self_test)."""
import ipaddress
import re

CLASS_INFO = {  # class: (first-octet range, leading bits, default mask prefix)
    "A": ((0, 127), "0", 8), "B": ((128, 191), "10", 16), "C": ((192, 223), "110", 24),
    "D": ((224, 239), "1110", None), "E": ((240, 255), "1111", None)}


def octets(ip):
    return [int(x) for x in ip.split(".")]


def to_int(ip):
    a = octets(ip)
    return (a[0] << 24) | (a[1] << 16) | (a[2] << 8) | a[3]


def to_ip(n):
    return ".".join(str((n >> s) & 255) for s in (24, 16, 8, 0))


def to_bin(ip, sep=" "):
    return sep.join(f"{o:08b}" for o in octets(ip))


def bin_to_ip(b):
    parts = b.replace(".", " ").split()
    return ".".join(str(int(p, 2)) for p in parts)


def prefix_mask(p):
    return to_ip((0xFFFFFFFF << (32 - p)) & 0xFFFFFFFF) if p else "0.0.0.0"


def mask_prefix(mask):
    return bin(to_int(mask)).count("1")


def ip_class(ip):
    f = octets(ip)[0]
    for c, ((lo, hi), _, _) in CLASS_INFO.items():
        if lo <= f <= hi:
            return c


def v4_check(s):
    """Return (valid, reason_en, reason_gu)."""
    parts = s.split(".")
    if len(parts) != 4:
        return False, f"It has {len(parts)} octets; an IPv4 address must have exactly 4 octets.", \
            f"તેમાં {len(parts)} octets છે; IPv4 address માં બરાબર 4 octets હોવા જોઈએ."
    for p in parts:
        if not p.isdigit():
            return False, f"'{p}' is not a decimal number.", f"'{p}' decimal સંખ્યા નથી."
    bad = [p for p in parts if int(p) > 255]
    if bad:
        p = bad[0]
        if set(p) <= {"0", "1"} and len(p) == 8:
            return False, f"Binary and dotted-decimal notation are mixed: {p} is binary but the other octets are decimal (read as a decimal number, {p} is far greater than 255).", \
                f"Binary અને dotted-decimal notation ભેગા છે: {p} binary છે પણ બાકીના octets decimal છે (decimal સંખ્યા તરીકે વાંચતાં {p} એ 255 કરતાં ઘણો મોટો છે)."
        return False, f"Octet {p} is greater than 255; each octet must be 0-255.", f"Octet {p} એ 255 થી મોટો છે; દરેક octet 0-255 હોવો જોઈએ."
    lead = [p for p in parts if len(p) > 1 and p[0] == "0"]
    if lead:
        return False, f"Octet '{lead[0]}' has a leading zero, which is not allowed.", f"Octet '{lead[0]}' માં આગળ શૂન્ય છે, જે માન્ય નથી."
    return True, "", ""


def classful(ip):
    """Class, net id, host id, network address, broadcast for a classful address (A/B/C)."""
    c = ip_class(ip)
    p = CLASS_INFO[c][2]
    o = octets(ip)
    if p is None:
        return {"class": c, "prefix": None}
    k = p // 8
    net = to_int(ip) & to_int(prefix_mask(p))
    return {"class": c, "prefix": p, "mask": prefix_mask(p), "net_id": ".".join(map(str, o[:k])),
            "host_id": ".".join(map(str, o[k:])), "network": to_ip(net), "broadcast": to_ip(net | (~to_int(prefix_mask(p)) & 0xFFFFFFFF)),
            "hosts": 2 ** (32 - p) - 2}


def block(ip, p):
    """Network (first), broadcast (last), first/last host, count for ip/p."""
    m = to_int(prefix_mask(p))
    net = to_int(ip) & m
    bc = net | (~m & 0xFFFFFFFF)
    return {"network": to_ip(net), "broadcast": to_ip(bc), "first_host": to_ip(net + 1), "last_host": to_ip(bc - 1),
            "count": 2 ** (32 - p), "hosts": 2 ** (32 - p) - 2, "mask": prefix_mask(p)}


def and_rows(ip, mask):
    """Rows for the AND table: (label, dotted, binary)."""
    net = to_ip(to_int(ip) & to_int(mask))
    return [("IP address", ip, to_bin(ip)), ("Subnet mask", mask, to_bin(mask)), ("AND = network", net, to_bin(net))]


def subnet_for_hosts(net, p, hosts):
    """Smallest host bits h with 2^h - 2 >= hosts; returns dict with new prefix and list of subnets."""
    h = 1
    while 2 ** h - 2 < hosts:
        h += 1
    newp = 32 - h
    n = 2 ** (newp - p)
    size = 2 ** h
    base = to_int(net)
    subs = []
    for i in range(n):
        s = base + i * size
        subs.append((to_ip(s), to_ip(s + 1), to_ip(s + size - 2), to_ip(s + size - 1)))
    return {"h": h, "borrowed": newp - p, "prefix": newp, "mask": prefix_mask(newp), "count": n, "size": size,
            "usable": size - 2, "subnets": subs}


def subnet_for_count(net, p, count):
    s = 0
    while 2 ** s < count:
        s += 1
    newp = p + s
    size = 2 ** (32 - newp)
    base = to_int(net)
    subs = [(to_ip(base + i * size), to_ip(base + i * size + 1), to_ip(base + (i + 1) * size - 2), to_ip(base + (i + 1) * size - 1))
            for i in range(2 ** s)]
    return {"borrowed": s, "prefix": newp, "mask": prefix_mask(newp), "count": 2 ** s, "size": size, "usable": size - 2, "subnets": subs}


# ---------------------------------------------------------------- IPv6
HEX = re.compile(r"^[0-9a-fA-F]{1,4}$")


def v6_check(s):
    """Return (valid, reason_en, reason_gu) for a textbook IPv6 check."""
    if "." in s and ":" not in s:
        return False, "It is written in dotted-decimal form; this is an IPv4 address, not IPv6.", \
            "તે dotted-decimal સ્વરૂપમાં લખેલું છે; આ IPv4 address છે, IPv6 નહીં."
    if s.count("::") > 1:
        return False, "'::' is used more than once; it may appear only once.", "'::' એક કરતાં વધુ વાર વપરાયું છે; તે ફક્ત એક જ વાર આવી શકે."
    if s == "::":
        return True, "", ""
    if "::" in s:
        a, b = s.split("::")
        groups = [g for g in (a.split(":") if a else [])] + [g for g in (b.split(":") if b else [])]
        if len(groups) > 7:
            return False, "Too many groups with '::'.", "'::' સાથે વધુ પડતા groups."
    else:
        groups = s.split(":")
        if len(groups) != 8:
            return False, f"It has only {len(groups)} groups and no '::' to show omitted zero groups; a full IPv6 address needs 8 groups.", \
                f"તેમાં ફક્ત {len(groups)} groups છે અને છોડેલા zero groups બતાવવા '::' નથી; પૂર્ણ IPv6 address માં 8 groups જોઈએ."
    for g in groups:
        if not HEX.match(g):
            if len(g) > 4:
                return False, f"Group '{g}' has more than 4 hex digits.", f"Group '{g}' માં 4 થી વધુ hex અંકો છે."
            return False, f"Group '{g}' contains a non-hexadecimal character.", f"Group '{g}' માં non-hexadecimal અક્ષર છે."
    return True, "", ""


def v6_expand(s):
    return ipaddress.IPv6Address(s).exploded


def v6_compress(s):
    return ipaddress.IPv6Address(s).compressed


def self_test():
    for ip, p in [("205.16.37.39", 28), ("172.16.45.14", 20), ("10.6.24.20", 20)]:
        n = ipaddress.ip_network(f"{ip}/{p}", strict=False)
        b = block(ip, p)
        assert b["network"] == str(n.network_address) and b["broadcast"] == str(n.broadcast_address), ip
    for s in ["2001:db8:3333:4444:5555:6666:7777:8888", "2001:0db8:0001:0000:0000:0ab9:C0A8:0102", "225.1.4.2", "::",
              "fe80:2030:31:24", "2001:db8::1::2", "fe80::1"]:
        try:
            ipaddress.IPv6Address(s); ok = True
        except ValueError:
            ok = False
        assert v6_check(s)[0] == ok, s
    for s in ["298.27.5.6", "1.4.5.5", "11100010.23.14.67", "192.226.12.11.9"]:
        try:
            ipaddress.IPv4Address(s); ok = True
        except ValueError:
            ok = False
        assert v4_check(s)[0] == ok, s
    r = subnet_for_hosts("216.21.5.0", 24, 30)
    assert r["prefix"] == 27 and r["count"] == 8 and r["subnets"][1][0] == "216.21.5.32"
    assert bin_to_ip("10000001 00001011 00001011 11101111") == "129.11.11.239"
    return True


if __name__ == "__main__":
    print(self_test())
    print(classful("1.4.5.5"), block("10.6.24.20", 20), subnet_for_hosts("216.21.5.0", 24, 30)["subnets"][:3])
