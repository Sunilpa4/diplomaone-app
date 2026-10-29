"""Guided-only physical/OS observations; no fabricated hardware results."""
GUIDES={
 'guides/component_and_port_identification.md':'''# Practicals 1 and 4 — guided physical identification, NOT executed here

The sandbox did NOT open/photograph/handle a PC or laptop, identify a physical
port, insert/remove a component, access BIOS/UEFI or measure power. The SVGs
are labelled concept/recognition schematics, not service photos or pinouts.

Use only an owned/instructor-authorized device, the EXACT model's service
manual, appropriate trained supervision and an instructor-approved ESD setup.
1. Save work, shut down and isolate the power sources specified by the manual
   before authorized internal work. Internal laptop batteries require the
   model-specific safe procedure; do not invent one from a generic drawing.
2. Do not improvise mains/earth connections. Handle approved components by
   edges and avoid contacts; use proper ESD-safe surfaces/packaging as directed.
3. Have the instructor identify CPU/system board,RAM,firmware-storage context,
   storage and power/I/O connections without unnecessary removal. Record what
   was actually observed,documentation-only or unknown in components.csv.
4. Inspect exterior labels/ports without forcing plugs or inserting objects.
   Record USB/HDMI/8P8C Ethernet/audio/VGA/Thunderbolt where actually present.
   Absence of a legacy/optional port is not automatically a fault.
5. Use the manual/specification for capabilities. USB-C shape alone does not
   prove video/Power Delivery/Thunderbolt. Port locations and features vary.
6. Leave reassembly/reconnection checks to the relevant approved procedure and
   instructor. This introductory worksheet is not a full assembly/repair guide.

STOP for unsafe/damaged/swollen batteries,power connections or other hazards.
NEVER open SMPS/charger/monitor enclosures,probe mains/internal high-voltage
circuits,short terminals/pins,clear CMOS/passwords,flash firmware or change
Secure Boot/TPM settings for this unit. Hazardous stored charge can remain after
unplugging. Appropriate qualified service is required,not a classroom shortcut.

No voltage values,POST tones,BIOS screenshots,photos or physical practical
completion are invented. Do not include serial numbers,network MACs,accounts
or sensitive asset/customer information in a public/shared student journal.
''',
 'guides/specification_and_readonly_os.md':'''# Dated specification worksheet and read-only OS guidance

Status: four software examples are actually tested. Native Windows/macOS GUI,
BIOS screens and physical devices are GUIDED ONLY,not reference executions.
The inventory example reports this sandbox's OS/kernel view,NOT your laptop
or proof of installed physical CPU cores/DIMMs,ports,firmware mode or upgrades.

Use an authorized device/model and fill specification.csv:
  processor;memory;storage;GPU;display;ports;connectivity;OS;source URL;check date.
Record exact configuration and evidence class;write UNKNOWN/NOT OBSERVED when
necessary. Do not combine base model and upgrade options into a false profile.

Guided read-only observations,NOT executed on those OS devices here:
- Windows:Settings > System > About,Task Manager > Performance,or System
  Information(msinfo32) can report relevant OS-visible/model data. Avoid changing
  firmware,boot,security,device or registry settings.
- macOS:About This Mac/System Information and exact official model specs can
  provide relevant information. These are not Windows x86 BIOS procedures.
- Check the manufacturer's current specification/service manual,not just a
  seller headline or a sandbox result. Architecture,drivers/OS and upgrade
  paths vary;do not buy parts based on a generic worksheet alone.

reference_specs.json contains two FIRST/BASE official-page profiles checked
29Oct2026:MacBook Air 13-inch M5 and Mac mini M6. They are Apple Silicon/macOS
examples. No raw manufacturer images/pages,prices,stock promises or hardware
benchmarks are bundled. Read the selected-column notes;do not mix M5 Pro,
15-inch or configurable-memory/storage variants. Their stated memory is unified,
not a claim that standard DIMMs can be added.

The syllabus's13th-generation i5 sample is an illustrative specification,not
an automatic latest-in-2026 claim. The dated references are manufacturer-listed
examples,not a universal newest/purchase/compatibility recommendation. Recheck
sources for a new assignment/date. Complete fields do not prove physical truth.

GB(decimal) and GiB(binary) differ. The units script computes512 GB≈476.837 GiB
and 16 GiB=17,179,869,184 bytes;it does not measure formatted usable capacity.
No code probes firmware,serials,MAC addresses,charging,ports or device internals.
'''}
COMPONENTS=['CPU/ALU/CU role','Motherboard','RAM','ROM/firmware-storage context','HDD/SSD',
 'Keyboard/mouse','Monitor/display','SMPS/adapter/main battery','RTC/settings context',
 'Expansion/removable media','Cooling/thermal path','Speakers/webcam','Wi-Fi/Bluetooth']
PORTS=['USB Type-A','USB Type-C','HDMI','8P8C(RJ45-style) Ethernet','3.5mm audio','VGA(DE-15)','Thunderbolt(markings/generation)']
