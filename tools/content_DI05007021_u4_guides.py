"""Honest guided-only Wireshark GUI / Packet Tracer exercises for Practicals 7–10."""
GUIDES={
 'guides/wireshark_offline.md':'''# Practical 7 — protocol analysis: actual CLI evidence, guided GUI

Status: real TShark 4.4.19 offline analysis was executed. The Wireshark GUI and
live capture were NOT executed. synthetic.pcap was constructed by our code:
16 frames / fake local MACs / documentation IPv4 addresses / .test names.
It is not captured traffic, Packet Tracer output or a network benchmark.

1. Install Wireshark through its official OS instructions if needed.
2. Open the supplied synthetic.pcap with File > Open (GUI steps are guided).
3. Inspect packet list, protocol tree and bytes. Filter arp (2 frames), dns
   (2), tcp (10), http (2), and vlan (2) separately. Display-filter counts
   overlap: HTTP is carried by TCP, DNS by UDP.
4. DNS shows portal.diploma.test ->198.51.100.10; the HTTP request is GET
   /course and response 200. Frames 15/16 carry VLAN IDs 10/20.
5. Follow the single HTTP TCP stream if desired; this is only benign fixture
   text. No TLS packets are included in this PCAP. The separate TLS example
   is a real private exchange, not a captured record in this file.
6. With appropriate checksum checking enabled, IP/TCP/UDP checksums are Good.
   In the tested 4.4.19 field enumeration, Good=1, Bad=0, Unverified=2.
7. Record observations, interpretation and limits. Fixed synthetic timestamps
   do not support throughput/latency or production-IDS accuracy claims.

Actual offline commands can be rerun without capture permission:
    tshark -n -r synthetic.pcap -Y dns
    tshark -n -r synthetic.pcap -Y http
    tshark -n -r synthetic.pcap -Y 'vlan.id == 10'
Capture BPF syntax 'tcp port 80' is different from display syntax
 'tcp.port == 80'. Never run a live capture on others' traffic. Capture needs
explicit authorization and appropriate OS privileges; do not disable host
protection to force this lesson to work.
''',
 'guides/packet_tracer_vlan.md':'''# Practical 8 — VLAN simulation (GUIDED ONLY)

Packet Tracer was NOT installed/run. No .pkt/.pka file or successful simulator
result is fabricated. The Python VLAN model and tagged PCAP are separate
illustrations, NOT proof of a configured switch. Use your authorized Packet
Tracer installation from https://www.netacad.com/cisco-packet-tracer.

Suggested topology: two 2960-style switches, linked via Gi0/1 trunk. On each,
Fa0/1 serves a VLAN10 host; Fa0/2 serves a VLAN20 host. Interface names and
features vary by selected device/version: inspect first, adapt with instructor.

Address plan (separate from the synthetic PCAP):
  SW1/VLAN10 host A:10.10.10.11/24; SW2/VLAN10 B:10.10.10.12/24
  SW1/VLAN20 host C:10.20.20.11/24; SW2/VLAN20 D:10.20.20.12/24
No gateway/router is configured in this simple L2-only exercise.

Common illustrative switch CLI, apply on each simulated switch after checking
its interface names; these commands were NOT executed here:
    enable
    configure terminal
    vlan 10
     name STAFF
    vlan 20
     name STUDENTS
    interface fastEthernet0/1
     switchport mode access
     switchport access vlan 10
    interface fastEthernet0/2
     switchport mode access
     switchport access vlan 20
    interface gigabitEthernet0/1
     switchport mode trunk
     switchport trunk allowed vlan 10,20
    end
    show vlan brief
    show interfaces trunk

Suggested expected tests, NOT observed simulator results:
  A->B and C->D: same-VLAN communication across trunk should work once setup
  is correct. A->C/B->D should not route in this L2-only, no-gateway setup.
A failed ping alone is not proof of isolation: also verify IPs, masks, link
state, access membership, trunk/allowed VLANs and lack of inter-VLAN routing.
VLAN tags do not encrypt data. Controlled L3 routing can later connect VLANs;
apply explicit policy there. Save your own .pkt and observation journal.
''',
 'guides/packet_tracer_dmz.md':'''# Practical 9 — DMZ topology (GUIDED ONLY)

Packet Tracer, routers and switches were NOT executed/configured here. This
is a build-and-observe guide, not a supplied .pkt or a production design.

Use a simulated router with three routed Ethernet interfaces (for example a
2911-style device if available) and three separate segments:
  G0/0 WAN-lab:192.0.2.1/24; test PC192.0.2.10/24, gateway192.0.2.1
  G0/1 DMZ:172.16.20.1/24; web server172.16.20.10/24, gateway172.16.20.1
  G0/2 INSIDE:10.10.10.1/24; test PC10.10.10.10/24, gateway10.10.10.1
Use appropriate switches/cables. This separate Packet Tracer IP plan is NOT
where the synthetic PCAP was captured (there was no real capture).

Guided example; adapt interface names to the chosen simulator/device:
    enable
    configure terminal
    interface gigabitEthernet0/0
     ip address 192.0.2.1 255.255.255.0
     no shutdown
    interface gigabitEthernet0/1
     ip address 172.16.20.1 255.255.255.0
     no shutdown
    interface gigabitEthernet0/2
     ip address 10.10.10.1 255.255.255.0
     no shutdown
    end
    show ip interface brief
    show ip route

Configure host addresses/gateways and the simulated server's HTTP service.
Before filtering, directly connected routes may permit inter-segment traffic:
naming a network DMZ is NOT enforcement. Apply the separate firewall guide to
create the intended allowed/denied paths. All tests stay inside your simulated
lab; never attach this exercise to a real WAN or reuse it as deployment policy.
''',
 'guides/packet_tracer_firewall.md':'''# Practical 10 — packet-filter policy simulation (GUIDED ONLY)

No Cisco CLI, Packet Tracer/ASA, host firewall or kernel rules were executed
here. The following common router extended-ACL example is a stateless packet
filter, NOT a stateful/NGFW appliance or a complete production security policy.
Use the separate three-interface DMZ guide and an authorized simulator. Check
selected device/version syntax with your instructor before applying commands.

Minimal intended flows for this specific lab:
  WAN PC -> DMZ web TCP80: expected allow.
  WAN -> INSIDE: expected deny.
  DMZ -> INSIDE: expected deny.
  WAN ping -> DMZ: expected deny (ICMP is not permitted by this policy).
Other flows, including LAN browsing, are NOT configured as guaranteed working
services. Do not infer a full ingress/egress/return-traffic design from this
minimal lab. The HTTP service is plaintext and teaches policy, not secrecy.

Guided CLI, NOT executed reference output:
    enable
    configure terminal
    ip access-list extended WAN_IN
     permit tcp 192.0.2.0 0.0.0.255 host 172.16.20.10 eq 80
     deny ip 192.0.2.0 0.0.0.255 10.10.10.0 0.0.0.255
     deny ip any any
    ip access-list extended DMZ_IN
     deny ip 172.16.20.0 0.0.0.255 10.10.10.0 0.0.0.255
     permit tcp host 172.16.20.10 eq 80 192.0.2.0 0.0.0.255
     deny ip any any
    interface gigabitEthernet0/0
     ip access-group WAN_IN in
    interface gigabitEthernet0/1
     ip access-group DMZ_IN in
    end
    show access-lists
    show ip interface gigabitEthernet0/0
    show ip interface gigabitEthernet0/1

Use the WAN test PC's simulated browser to http://172.16.20.10 and verify the
permitted/denied cases, rule directions/counters and router/host addressing.
These are EXPECTED tests, not observed results. TCP source-port80 matching in
the return rule is not genuine connection-state tracking; spoofed or unusual
traffic is not comprehensively handled. A router ACL 'established' keyword,
when available, tests TCP flags; it is not a replacement for a real state table.
If the assignment requires a particular ASA/stateful appliance, follow the
instructor's supported simulator model/file instead. Save your own .pkt and
record actual observations, failures and limitations. Never copy this minimal
fixture directly onto production equipment.
'''}
