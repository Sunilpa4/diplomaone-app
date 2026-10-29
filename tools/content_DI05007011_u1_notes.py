"""English-only Unit 1: diagram-focused hardware introduction, honest lab scope."""
import json
from subject_DI05007011 import ROOT,tr
from content_DI05007021_u1_notes import ul,table,topic
REFERENCE=json.loads((ROOT/'tools/fixtures_DI05007011_u1/reference_specs.json').read_text())
SOURCES=[
 ('GTU DI05007011 syllabus,2026–27','https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/DI05007011.pdf'),
 ('IBM history:the IBM 5150 PC (August 1981)','https://www.ibm.com/history/personal-computer'),
 ('UEFI Forum:UEFI and legacy BIOS concepts','https://uefi.org/faq'),
 ('USB-IF:USB Power Delivery and negotiated capability','https://www.usb.org/usb-charger-pd'),
 ('Intel:Thunderbolt 4 versus USB-C (protocol versus shape)','https://www.intel.com/content/www/us/en/architecture-and-technology/thunderbolt/thunderbolt-4-vs-usb-c.html'),
 ('Apple:identify ports,including older/newer Thunderbolt connectors','https://support.apple.com/en-us/109523'),
 ('Apple MacBook Air technical specifications (dated reference)','https://www.apple.com/macbook-air/specs/'),
 ('Apple Mac mini technical specifications (dated reference)','https://www.apple.com/mac-mini/specs/'),
 ('Dell:electrical/ESD safety and model-specific service-manual precautions','https://www.dell.com/support/kbdoc/en-us/000137973/safety-precautions-when-working-with-electrical-equipment'),
 ('Dell:BIOS/CMOS/NVRAM background (concepts only;no reset procedure is assigned)','https://www.dell.com/support/kbdoc/en-us/000124377/how-to-perform-a-bios-or-cmos-reset-and-clear-the-nvram-on-dell-systems')]
NOTES=[
 {'title':tr('1. Computer Systems and Development'),'items':[
  topic('1.1 Computer systems,IPO and PC development',
   '<p>A computer system accepts <b>input</b>, processes instructions/data, retains working/persistent information and produces <b>output</b>. Hardware, software,firmware and the user’s task work together; a system is not only its CPU.</p>'+ul(
    'Personal computers brought programmable computing to individual users. IBM introduced the IBM 5150 Personal Computer in August 1981; it was an influential PC standard, <b>not the first personal computer ever</b>.',
    'PC development includes more integration, memory/storage capacity, graphical/networked use, portable systems and specialized workloads. Do not assume each new generation is faster for every task merely from clock speed.',
    'A desktop may use separate display/keyboard/power components; a laptop integrates many into one portable device. Form factor and integration affect servicing and upgrade options.',
    'This unit identifies roles and interfaces. Detailed 8085 architecture/buses belong to Unit 2; detailed memory/storage to Unit 3; peripheral working principles to Unit 4 and troubleshooting/assembly to Unit 5.') ),
  topic('1.2 Types of computers:use,scale and deployment are different axes',
   table(['Syllabus type','Idea / example context','Important distinction'],[
    ('Microcomputer','Personal computing built around microprocessor-based processing;desktop/laptop examples.','A workstation can also be a microcomputer;categories may overlap.'),
    ('Minicomputer','Historical midrange/multiuser computer category.','Not the same as a modern small-form-factor miniPC or a product named Mac mini.'),
    ('Mainframe','Enterprise multiuser/transaction and reliability-oriented computing.','Not defined simply as a physically large box or the fastest scientific computer.'),
    ('Supercomputer','Large-scale parallel/high-performance computing for suitable computational workloads.','Application/workload and architecture matter,not just cabinet size.'),
    ('Workstation','Professional/technical personal system for suitable engineering/creative/scientific work.','A role/capability category,not automatically a separate size tier.'),
    ('Cloud','Access/deployment model for remotely provided computing resources/services.','Uses underlying physical hardware;not a single CPU class or a replacement for all local devices.'),
    ('Embedded system','Computing integrated into a device for particular functions.','May use a microcontroller/SoC and need not look like a desktop or run a general-purpose desktop OS.')])+
   '<p>Do not arrange every row as one mutually exclusive “smallest to largest” ladder. A cloud-hosted resource can use server-class hardware,and a professional workstation can have a desktop form factor.</p>','hw1_types')]},
 {'title':tr('2. PC Block Diagram and Core Components'),'items':[
  topic('2.1 The PC block diagram',
   '<p>Read the diagram as <b>functional relationships</b>,not an exact wiring/pinout or a measured board. Input devices supply data/control; CPU executes operations; RAM holds active working state; persistent storage retains programs/files; output devices present results.</p>'+ul(
    'The motherboard/interconnects allow components to communicate;device controllers and firmware/OS software also participate.',
    'Storage data is typically brought into working memory when used. RAM and a storage drive are different resources.',
    'Power delivery supports the components,not the logical data path. A CPU alone cannot supply power,display a result or store every persistent file.',
    'Modern integration varies:memory controllers,graphics or other functions may share a CPU/SoC package. The conceptual blocks need not be separate removable chips.') ,'hw1_block'),
  topic('2.2 CPU:ALU,Control Unit and internal state',
   '<p>The <b>central processing unit (CPU)</b> executes instructions. A simplified teaching view includes:</p>'+table(['Part','Role'],[
    ('Arithmetic Logic Unit (ALU)','Performs relevant arithmetic and logical operations under the instruction/control design.'),
    ('Control Unit (CU)','Coordinates instruction/control sequencing and signals needed for operations.'),
    ('Registers/internal state','Fast internal storage used while executing instructions;not the same as the installed RAM capacity.')])+
   '<p>Fetch/decode/execute is a useful simplified cycle,not a complete description of every modern pipeline. A core count,clock number or brand name alone is not a universal performance score. The ALU/CU are functional parts of processing,not parts a student removes from a CPU package.</p>','hw1_cpu'),
  topic('2.3 Motherboard and component interconnection',
   '<p>The <b>motherboard / system board</b> is the main circuit board interconnecting/supporting system components. A typical modular desktop may expose a CPU socket,RAM slots,firmware storage,expansion connectors,storage interfaces,power connectors and rear/front-I/O connections.</p>'+ul(
    'Actual layouts differ by model/form factor. Do not identify a connector solely by approximate position in a generic drawing.',
    'A laptop/compact system may integrate/solder CPU or memory instead of offering ordinary desktop sockets/slots. Do not assume a component is removable or upgradeable.',
    'A chipset/controller supports relevant I/O/connectivity;historical northbridge/southbridge and bus details are studied in Unit 2. Modern integration does not always follow that old two-chip layout.',
    'Our labelled board drawing is a schematic role map,not a photograph,service manual or proof that an actual motherboard was handled.') ,'hw1_board'),
  topic('2.4 RAM,ROM and persistent HDD/SSD storage',
   table(['Component','Purpose','Persistence / common trap'],[
    ('RAM','Active program/data workspace.','Ordinary system RAM is volatile;power-off loses its active contents. More RAM is not more SSD capacity.'),
    ('ROM/nonvolatile firmware storage','Retain suitable low-level code/data.','ROM is a historical/read-only category;modern firmware often resides in updateable flash. Do not conclude all firmware can never change.'),
    ('HDD','Persistent storage using rotating magnetic media and mechanisms.','Not the same working resource as RAM;internal mechanisms are not opened in this exercise.'),
    ('SSD','Persistent solid-state storage,commonly flash-based.','SSDs have different interfaces/form factors;not every SSD is NVMe or an interchangeable module.')])+
   '<p>SATA and NVMe are not synonyms;M.2 is a form-factor/connector family rather than a guarantee of one protocol. A common M.2 NVMe module plugs into a suitable slot instead of needing a SATA-style data cable. RAID describes a storage arrangement,not an interface. These distinctions are developed further in Units2/3.</p>'),
  topic('2.5 Keyboard,mouse and monitor as system I/O',
   '<p>A <b>keyboard</b> supplies key events; a <b>mouse/pointing device</b> supplies pointing/button information. The device/controller and OS interpret those inputs;an unresponsive app is not automatically proof of a broken peripheral.</p><p>A <b>monitor/display</b> presents visual output through an appropriate graphics/display path. In common PC terminology,an “LED monitor” is often an <b>LED-backlit LCD</b>,not automatically a direct-emissive LED or OLED panel. LCD/LED construction/operation is studied in Unit 4.</p>'+ul(
    'A desktop may require external keyboard/mouse/display; laptops typically integrate keyboard/pointing/display while also supporting appropriate external devices.',
    'Check the actual connector,signal support,cable,display input and settings rather than forcing a plug or assuming every similar socket provides video.') ),
  topic('2.6 SMPS,laptop adapter/battery and safe power concepts',
   '<p>A desktop <b>switched-mode power supply (SMPS)</b> converts suitable input power into regulated outputs required by the system. It is not RAM,storage or a data connector. Laptop power commonly involves an appropriate external adapter/charging circuitry and a battery.</p>'+ul(
    'Power ratings,connector compatibility and charging protocols must match the manufacturer’s requirements. A same-shaped plug does not establish electrical compatibility.',
    'Disconnect appropriate power sources before authorized internal identification;internal batteries require model-specific service instructions. Do not improvise mains/grounding connections.',
    '<b>Never open an SMPS/charger/monitor enclosure or probe mains/internal high-voltage circuitry for this unit.</b> Hazardous stored charge may remain after unplugging;refer such work to qualified service personnel.',
    'Stop if batteries are swollen,leaking,damaged or hot abnormally;do not bend,puncture,short terminals or continue using a damaged pack.',
    'No voltage measurement,power-supply repair,battery removal or physical component handling is executed in this sandbox.') )]},
 {'title':tr('3. Hardware,Software,Firmware and Startup'),'items':[
  topic('3.1 Hardware versus software versus firmware',
   table(['Term','Meaning','Example'],[
    ('Hardware','Physical electronic/mechanical components.','CPU package,RAM module,system board,keyboard,storage drive.'),
    ('Software','Instructions/programs and associated data used by the system.','OS,drivers,applications.'),
    ('Firmware','Software for low-level device/platform functions,typically stored in nonvolatile memory.','Platform startup firmware or device-controller firmware.')])+
   '<p>The flash chip is hardware;the firmware contents are software. Firmware may be updateable through a manufacturer-supported process,but this unit does not flash,reset or modify firmware. A driver generally operates with the OS and is not interchangeable with the device’s firmware.</p>','hw1_layers'),
  topic('3.2 BIOS and UEFI concepts',
   '<p><b>Legacy BIOS</b> is rooted in older PC platform-firmware conventions. <b>UEFI</b>(Unified Extensible Firmware Interface) defines interfaces between platform firmware,the OS loader and suitable pre-boot services. It is not simply a prettier BIOS setup screen.</p>'+ul(
    'Firmware initializes relevant platform hardware and participates in transferring control to the OS boot process. Setup menus/features vary by manufacturer and platform.',
    'UEFI supports different architectures;an example using Apple Silicon/macOS must not be assumed to have the same Windows x86 setup screens or servicing workflow.',
    'Secure Boot is a related verification feature under platform policy,not proof that all software/firmware is safe. Do not disable it or change TPM/boot/security settings for this identification unit.',
    'BIOS/UEFI observation is guided/read-only only. No BIOS screen is accessed,firmware version measured,setting changed or update performed here.') ,'hw1_firmware'),
  topic('3.3 CMOS,RTC battery and nonvolatile settings are not the firmware program',
   '<p><b>CMOS</b> names a semiconductor technology and,in traditional PC vocabulary,the small battery-backed configuration-memory context. The <b>real-time clock (RTC)</b> and its backup battery are related but are not the BIOS/UEFI program itself.</p>'+ul(
    'Platform firmware code commonly resides in nonvolatile flash. Modern settings may use NVRAM;not every system stores all settings in one classic battery-backed CMOS arrangement.',
    'The coin-cell/RTC battery is not the laptop’s main operating battery and does not power the full RAM/SSD when a machine is switched off.',
    'Removing a battery does not universally erase firmware,reset every setting or solve all faults. Procedures differ by model and can affect startup/security state.',
    'No CMOS clear,jumper/password reset,battery removal or NVRAM/TPM change is assigned/executed. Follow a specific authorized service procedure only when relevant later.') )]},
 {'title':tr('4. Laptop Components and External Identification'),'items':[
  topic('4.1 Laptop core board,memory,expansion and storage',
   '<p>A laptop integrates core processing and interfaces into a portable assembly. Identify roles using the exact model/service manual rather than assuming a universal internal layout.</p>'+table(['Syllabus component','Role / variation'],[
    ('CPU / system board','Executes/control-supports processing;may be integrated rather than socket-replaceable.'),
    ('Memory (RAM)','Working state;may be slot-based,soldered or unified/integrated. Do not infer upgradeability from the capacity label.'),
    ('Expansion slots/interfaces','Provide supported extra functions where implemented;not every laptop has every desktop expansion option.'),
    ('Internal storage','Persistent HDD/SSD or integrated storage,depending on model.'),
    ('Removable-media drive/support','Optical/removable readers may be absent,external or model-dependent;absence is not automatically a fault.'),
    ('Power supply/battery','Appropriate adapter,charging circuitry and main battery support operation;not interchangeable with the RTC cell.')])+
   '<p>The supplied Apple profiles illustrate modern integration,not instructions to remove memory or storage modules. No laptop has been opened or serviced here.</p>','hw1_laptop'),
  topic('4.2 Laptop video,input,cooling,audio,camera and wireless',
   table(['Component group','Function / caution'],[
    ('Video display controller/GPU and display','Generate/drive visual output;graphics may be integrated,discrete or part of a SoC.'),
    ('Input','Integrated keyboard/touchpad and supported external input interfaces.'),
    ('Ports','External physical connections;their capabilities depend on the actual implementation.'),
    ('Cooling:fan/heat sink/thermal path','Transfers heat;many systems use fans,but some designs are fanless. Do not block vents or assume every model has a replaceable fan.'),
    ('Speakers,webcam and microphones','Audio/video input/output;privacy,drivers and permissions can affect operation.'),
    ('Wireless module:Wi-Fi/Bluetooth','Wireless connectivity through suitable radios/antennas/OS support;may be integrated or separately serviceable.')])+
   '<p>A webcam not working may involve software permissions,not necessarily a failed physical part. A cooling diagram is a concept illustration,not a thermal measurement or instruction to dismantle a powered device.</p>'),
  topic('4.3 Front/back panels:ports and matching connectors',
   '<p>A <b>port</b> is the device-side connection point;the <b>connector</b> is the matching cable/device plug arrangement. Desktop front/back and laptop-side positions vary. Use markings and the exact manual;drawn shapes here are simplified recognition aids,not electrical pinouts.</p>'+table(['Port/connector','Typical purpose','Do not assume'],[
    ('USB(Type-A/Type-C and other variants)','Supported peripherals/data and,where implemented,appropriate power/display modes.','Connector shape alone does not determine USB version,charging or video.'),
    ('HDMI','Supported digital display/audio connection.','A mechanically fitting cable guarantees every resolution/refresh feature.'),
    ('RJ45-style Ethernet(8P8C)','Common wired Ethernet connection.','It is a telephone/RJ11 jack or that physical link proves Internet access.'),
    ('3.5mm audio jack','Supported headphones/speakers/microphone or combined analog role.','Every jack has the same TRS/TRRS/microphone function.'),
    ('VGA(DE-15)','Traditional analog video connection.','It carries HDMI-style digital audio/video features.'),
    ('Thunderbolt','Supported high-speed data/video/expansion functions under the relevant standard.','All same-shaped USB-C or Mini DisplayPort sockets are Thunderbolt.')])+
   '<p>Never force a connector,insert tools into contacts/vents or test an unknown power connection by trial. Inspect external labels/manufacturer documentation before connecting an appropriate device.</p>','hw1_ports'),
  topic('4.4 USB-C versus USB/Thunderbolt capabilities',
   '<p><b>USB-C is a connector form</b>. USB data protocols,DisplayPort alternate modes,Power Delivery and Thunderbolt are capability/standard questions that require compatible implementations and cables—not merely that form.</p>'+ul(
    'Thunderbolt 1/2 used a Mini DisplayPort-style connector;Thunderbolt 3/4/5 use USB-C. An identical outline alone is not identification of the protocol.',
    'Power Delivery is negotiated under compatible source/sink/cable capabilities. Do not infer universal charging wattage or video from a USB-C socket.',
    'The actual Mac mini reference distinguishes front USB-C/USB 3 data ports from rear Thunderbolt 4(USB-C) ports;the page/support guide directs display connections to appropriate rear Thunderbolt/HDMI ports. Do not combine unlike ports into one guaranteed feature list.',
    'The software exercise compares explicitly fictional USB-C profiles to show how declared video support can differ. It probes no hardware and performs no PD/cable/Thunderbolt certification.',
    'Published interface rates are not measured application file-transfer performance;the complete host/cable/device/path and workload matter.') ,'hw1_usb',programs=['hw1p03'])]},
 {'title':tr('5. Dated Specifications and Safe Practical Work'),'items':[
  topic('5.1 Prepare a current specification:dated manufacturer-listed examples',
   '<p>For a “latest” specification exercise,record the <b>exact model/configuration,source and check date</b>. The two profiles below were checked against the first/base columns of official manufacturer pages on <b>29 October 2026</b>. They are dated educational references,not a claim of globally newest hardware,local stock/price,purchasing suitability,upgrade compatibility or measured performance.</p>'+table(['Field','Laptop reference','Desktop reference'],[
    ('Selected configuration','MacBook Air 13-inch M5,first/base column','Mac mini M6,first/base column—not M5 Pro'),
    ('Processor/GPU','M5: 10-core CPU,8-core integrated GPU','M6: 12-core CPU,12-core integrated GPU'),
    ('Memory/storage','16GB unified memory;512 GB SSD','16GB unified memory;256GB SSD'),
    ('Display','13.6-inch LED-backlit IPS,2560×1664','External display;no built-in panel'),
    ('Ports','2 Thunderbolt 4(USB-C),MagSafe3,3.5mm headphone','Front: 2 USB-C/USB 3 and 3.5mm;rear: 3 Thunderbolt 4,HDMI,2.5Gb Ethernet'),
    ('Connectivity/OS','Wi-Fi 7,Bluetooth 6;macOS','Wi-Fi 7,Bluetooth 6,2.5Gb Ethernet;macOS')])+
   '<p><b>Platform boundary:</b> these are Apple Silicon/macOS examples,not a Windows x86 BIOS/assembly guide. Unified-memory labels do not mean removable DIMMs. Choose your own authorized Windows/Linux/OEM system if that is your class bench,and verify its exact documentation.</p><p>The syllabus’s 13th-generation Core i5/16GB DDR4/512 GB/Windows 11 laptop is an <b>illustrative sample</b>,not automatically the newest configuration in October 2026. Do not mix base and upgraded columns or the largest advertised RAM/storage options into a false single model.</p>','hw1_specs'),
  topic('5.2 Four tested software helpers and the specification worksheet',
   '<p>The supporting programs are <b>software-only</b>,not physical practical evidence:</p>'+ul(
    '<b>Read-only sandbox inventory:</b> generic OS/kernel architecture,logical CPU count and exposed Linux MemTotal. These do not identify the learner’s physical laptop,installed DIMMs,ports or firmware mode.',
    '<b>Unit arithmetic:</b>16 GiB=17,179,869,184 bytes;512 decimal GB≈476.837 GiB. This is not measured formatted capacity or proof that a real drive lost space.',
    '<b>Connector fixture:</b> same USB-C shape can accompany different declared video support;charging remains unspecified in the fictional rows.',
    '<b>Specification completeness:</b> verify CPU,RAM,storage,GPU,display,ports,connectivity,OS and source/date fields are filled. Completeness is not accuracy,compatibility or benchmark proof.')+
   '<p>Use the CSV specification sheet for your own evidence. Report <b>not observed / unknown</b> rather than guessing. Manufacturer webpages can change;use the recorded date and update/verify sources for new work. No serial numbers,network MACs,hostnames,personal accounts or private records are needed in a shared student report.</p>',programs=[f'hw1p{i:02d}' for i in range(1,5)]),
  topic('5.3 Practicals 1 and4:guided physical identification and safe reporting',
   '<p><b>Practical 1:</b> identify internal desktop components/functions. <b>Practical 4:</b> identify front/back-panel ports/functions. The supplied observation guides/CSV sheets are <b>guided-only</b>;no physical PC/laptop,BIOS screen,electrical output or component insertion/removal was actually inspected/tested here.</p>'+ul(
    'Use an owned/instructor-authorized device,its exact service manual and appropriate trained supervision. Save work,shut down and isolate the specified power sources before authorized internal work. Handle internal batteries only as the model/instructor permits.',
    'Use an instructor-approved ESD-safe work area/grounding procedure;handle parts by edges and avoid touching contacts. Do not improvise connections to mains earth or powered equipment.',
    'Do not open the SMPS/charger/monitor case,probe hazardous circuitry,short pins/terminals,clear firmware/passwords or change Secure Boot/TPM settings in this unit. Stop for damaged/swollen batteries or unsafe conditions.',
    'Classify evidence as manufacturer documentation,read-only software observation or actual supervised physical observation. A sandbox result or schematic is not a substitute relabelled as hands-on work.',
    '<b>Assessment:</b>theory 70+30 and practical 20+30=150. Unit 1 is 7 hours/16% syllabus weight,not guaranteed question marks. The 16 answered questions use visibly suggested 3/4/7-mark revision sizes,not official GTU papers or predictions.')+
   '<p><b>References:</b> '+', '.join('<a href="'+u+'">'+n+'</a>' for n,u in SOURCES)+'. Explanations and schematics are original. Manufacturer pages support stated dated examples,not an endorsement or an assertion that devices were purchased/handled.</p>','hw1_safety')]}]

PRACTICE=[
 ('Define a computer system and explain input,processing,storage and output.',3,
  '<p>A computer system accepts input,executes instructions on data,retains working/persistent information and produces output. Keyboard/mouse are input examples;CPU executes operations,RAM holds active workspace,HDD/SSD retain files,and a monitor presents output. Hardware,software,firmware,power and interconnection work together. The functional diagram is not a literal wiring layout and the CPU alone is not the full computer.</p>'),
 ('Explain PC development and distinguish the seven syllabus computer categories.',7,
  '<p>The IBM 5150 PC introduced in August 1981 was influential but not the first personal computer. Later systems grew in integration,portability and connectivity. Microcomputer is a personal microprocessor-based category;minicomputer is historical midrange/multiuser;mainframe emphasizes enterprise transactions/reliability;supercomputer targets suitable large-scale parallel computation;workstation is a professional/technical role;cloud is a remote service/deployment model;embedded computing is integrated for particular functions. These are overlapping axes,not one exclusive smallest-to-largest ladder. A modern miniPC is not automatically a historical minicomputer.</p>'),
 ('Draw a PC block diagram and explain the main components.',7,
  '<p>Show input→CPU processing with working memory↔persistent storage and output,with motherboard/interconnect and suitable power support. CPU includes simplified ALU/control/register roles;RAM holds active state;nonvolatile firmware/storage retain suitable code/data;controllers support I/O. Label keyboard,mouse,monitor and HDD/SSD as examples. Explain that modern integration varies and blocks may not be separate removable devices. A schematic is not actual board-location or electrical-test evidence.</p>'),
 ('Differentiate ALU,Control Unit and registers.',4,
  '<p>ALU performs arithmetic/logical operations;CU coordinates relevant instruction/control sequencing;registers/internal state provide fast working values within processing. Fetch/decode/execute is a simplified teaching model rather than every detail of a modern pipeline. None is a separate replaceable classroom part inside a packaged CPU. Core count,clock and brand alone are not universal performance scores.</p>'),
 ('Explain the motherboard and why a generic layout cannot establish upgradeability.',4,
  '<p>The motherboard/system board interconnects/supports CPU,memory,firmware,I/O,storage,power and expansion functions. A modular desktop may have visible sockets/slots;some laptops/compact systems integrate or solder components. Locations and capabilities differ by exact model/form factor. Check the specific service manual and supported parts. A generic drawing or capacity label cannot prove a module is removable/compatible or that an upgrade was performed.</p>'),
 ('Compare RAM,ROM/firmware storage,HDD and SSD.',4,
  '<p>Ordinary RAM is volatile active workspace. ROM/nonvolatile firmware storage retains suitable low-level code/data;modern firmware can use updateable flash. HDD stores persistent data with rotating magnetic media;SSD provides persistent solid-state storage with different interfaces/form factors. RAM capacity is not SSD capacity. SATA and NVMe are not synonyms,M.2 is not a guaranteed protocol,and RAID is an arrangement rather than an interface. No physical drive/RAM measurement is claimed by the units exercise.</p>'),
 ('Differentiate hardware,software and firmware with examples.',4,
  '<p>Hardware is physical components,such as a flash chip,RAM or system board. Software includes OS/drivers/apps and associated instructions/data. Firmware is software for low-level device/platform functions,typically in nonvolatile memory. A chip is hardware;its firmware contents are software. A driver is not interchangeable with device firmware. Firmware can be updateable,but no flash/reset/change is performed in this introductory unit.</p>'),
 ('Compare legacy BIOS and UEFI without treating UEFI as just a graphical menu.',4,
  '<p>Legacy BIOS follows older PC-firmware conventions. UEFI defines standard interfaces/tables/services between platform firmware and OS loaders/pre-boot functions across supported architectures. Implementations initialize relevant hardware and participate in booting;setup screens vary. Secure Boot is a related policy-dependent verification feature,not a guarantee of total safety. The Apple Silicon examples are not a Windows x86 setup guide. No BIOS/UEFI screen,setting update or security bypass is executed here.</p>'),
 ('Explain CMOS,RTC battery,firmware flash and modern settings storage.',4,
  '<p>CMOS is a semiconductor term and a traditional PC configuration-memory context. RTC and its backup battery are related to keeping time/configuration in the relevant design,not the BIOS program itself. Firmware code often resides in nonvolatile flash;modern settings may use NVRAM. The RTC coin cell is not the laptop’s operating battery and does not preserve all RAM contents. Battery removal does not universally erase firmware/reset every setting;no clear/jumper/password/TPM operation is assigned.</p>'),
 ('Identify the core components of a laptop and their model-dependent nature.',7,
  '<p>Cover CPU/system board,RAM,expansion support,main battery/power circuitry,video controller/GPU/display,internal storage,optional removable drives,input devices,external ports,cooling,speakers/webcam and Wi-Fi/Bluetooth. Some functions are integrated/soldered,an optical drive may be absent and some cooling designs are fanless. Do not infer replacement/upgrade paths from a generic image. Use the exact model/service manual under appropriate authorization/supervision;no physical servicing is claimed.</p>'),
 ('Explain laptop input/output,wireless,cooling and power precautions.',4,
  '<p>Keyboard/touchpad provide input;GPU/display and speakers/camera/microphone support I/O;Wi-Fi/Bluetooth provide relevant wireless functions. A failure may involve permissions/drivers,not necessarily broken hardware. Cooling needs suitable airflow/thermal design;do not block vents or insert objects. Use correct manufacturer power requirements and stop for unsafe/swollen batteries. Never open a PSU/charger/monitor enclosure or probe mains/high-voltage circuits for this identification lesson.</p>'),
 ('Compare USB,HDMI,RJ45-style Ethernet,audio,VGA and Thunderbolt ports.',7,
  '<p>USB supports implemented peripheral/data/power modes;HDMI supports appropriate digital display/audio;8P8C commonly called RJ45 serves wired Ethernet;3.5mm jacks have model-dependent analog headphone/mic roles;VGA(DE-15) is traditional analog video;Thunderbolt supports defined data/video/expansion capability. Positions and features vary. Verify the matching connector,markings,model and cable;do not force plugs or infer protocol/electrical compatibility solely from outline. Drawn shapes are recognition aids,not pinouts.</p>'),
 ('Explain why USB-C shape does not guarantee video,charging or Thunderbolt.',4,
  '<p>USB-C is a connector form,while USB/Thunderbolt/data,alternate display modes and negotiated Power Delivery are capability questions involving host,cable and device. Thunderbolt 1/2 used Mini DisplayPort-style connectors;3/4/5 use USB-C,so shape alone is insufficient. The fictional profile model demonstrates different declared video support with charging unspecified;it performs no port/cable/PD test. Mac mini front USB 3 and rear Thunderbolt 4 descriptions must not be mixed into a universal feature list. Published rates are not measured file-transfer results.</p>'),
 ('Prepare a defensible current PC/laptop specification sheet.',7,
  '<p>Record exact model/configuration and CPU,RAM/storage,GPU,display,ports,connectivity,OS,source URL/check date and evidence scope. Use current official model-specific data and appropriate authorized observations,marking unknowns rather than guessing. Do not merge base and upgrade columns. The29Oct2026 MacBook Air M5/Mac mini M6 first/base examples are dated manufacturer-listed Apple Silicon/macOS profiles,not worldwide-newest,Indian stock/price,physical-device,upgrade or benchmark guarantees. The syllabus13th-gen i5 sample is illustrative,not automatically latest.</p>'),
 ('Compute 16 GiB in bytes and convert 512 decimal GB to GiB.',3,
  '<p>1 GiB=2^30=1,073,741,824 bytes,so 16 GiB=17,179,869,184 bytes.512 decimal GB=512×10^9 bytes;divide by 2^30 to obtain approximately476.837 GiB. This difference is units,not automatic proof of missing storage;formatted usable capacity also depends on filesystem/reserved areas. The calculation does not measure an installed RAM module/drive or define every manufacturer memory label.</p>'),
 ('State safe identification and evidence boundaries for Practicals 1 and4.',4,
  '<p>Use an owned/instructor-authorized system,its service manual and appropriate supervision. Isolate specified power sources before authorized internal work;use approved ESD handling and avoid contacts. Do not open PSU/charger/monitor cases,probe hazardous circuits,short pins,improvise mains grounding,remove unsafe batteries or change/clear firmware/security settings. Record actual component/port observations in the journal. Guided checklists,manufacturer facts,sandbox software reports and diagrams are not falsely relabelled physical practical completion.</p>')]
EXAM=[{'q':tr('Practice: '+q),'marks':m} for q,m,a in PRACTICE]
ANSWERED={'title':tr('6. Answered Exam-Style Practice — Suggested Marks Only'),'role':'practice',
 'items':[topic(f'Practice {i}. {q}',a) for i,(q,m,a) in enumerate(PRACTICE,1)]}
CARDS=[
 ('System model','Input -> processing / working state -> output\nPersistent storage retains suitable programs/files','Conceptual functions,not literal wiring or a whole computer contained in one CPU.'),
 ('Types are different axes','Micro / historical mini / mainframe / super\nWorkstation / cloud / embedded','Cloud is deployment/service context;workstation may also be a microcomputer.'),
 ('CPU roles','ALU:arithmetic / logic\nCU:instruction/control sequencing\nRegisters:internal fast state','Simplified architecture,not removable parts or a universal performance ranking.'),
 ('Working versus persistent storage','RAM:ordinary active volatile workspace\nFlash/ROM:nonvolatile low-level code/data\nHDD/SSD:persistent files/programs','Firmware content and the physical storage chip are different concepts.'),
 ('Hardware/software/firmware','Physical parts / programs-data / low-level code','Firmware is software in a hardware storage device;it is not necessarily permanently unchangeable.'),
 ('Firmware concepts','BIOS:legacy PC conventions\nUEFI:firmware/OS interface\nCMOS/RTC:NVRAM/settings/time context varies','No BIOS screen,flash,reset,clear,TPM or security-setting changes performed.'),
 ('Laptop groups','CPU/RAM/board/storage/expansion\nPower/display/input/ports/cooling\nAudio/camera/Wi-Fi/Bluetooth','Check exact integration,removability and optional absent components.'),
 ('External connectors','USB;HDMI;8P8C(RJ45-style Ethernet)\n3.5mm audio;VGA;Thunderbolt','Identify markings/manual,cable and implemented capability. Schematics are not electrical pinouts.'),
 ('Shape versus capability','USB-C shape != every USB/video/PD mode\nThunderbolt 3/4/5 use USB-C\nOlder Thunderbolt 1/2 used MiniDP-style','Do not assume every same-shaped port/cable has identical functions.'),
 ('Common display naming','Many PC LED monitors = LED-backlit LCD','Not every LED-related display is the same technology;peripheral operation is studied in Unit 4.'),
 ('Capacity units','1 GiB=2^30 bytes\n512 GB(decimal)≈476.837 GiB','Exercise only;not a physical measurement or formatted-capacity guarantee.'),
 ('Specification fields','CPU,RAM,storage,GPU,display\nPorts,connectivity,OS,source/date','Exact selected configuration matters;complete fields do not prove compatibility/performance.'),
 ('Reference scope','Official pages checked 29 Oct2026\nApple Silicon/macOS first/base examples','Not a Windows BIOS/assembly guide,worldwide latest assertion or purchase/stock recommendation.'),
 ('Safety / evidence','Authorized device + specific manual + supervision\nPower isolation + approved ESD handling','Never open PSU/charger/monitor housing or probe hazardous power. Physical observations are guided only.')]
SYNTAX=[{'title':tr('Hardware Identification Quick Reference'),'items':[{'name':tr(n),'f':f,'terms':tr(t)} for n,f,t in CARDS]}]
QA=[
 ('What is a computer system?','Cooperating hardware,software/firmware and associated data/power/interconnection that accept input,process/store information and produce output.'),
 ('Was the IBM 5150 the first personal computer ever?','No. Its August 1981 introduction was influential,but personal computers existed earlier.'),
 ('Is a modern miniPC the same as a historical minicomputer?','No. Compact form-factor naming is different from the historical midrange/multiuser category.'),
 ('Is cloud computing a single physical CPU size class?','No. It is an access/service/deployment context using underlying hardware.'),
 ('Can a workstation also be a microcomputer?','Yes. The categories describe overlapping role/architecture/scale dimensions.'),
 ('What is an embedded system?','Computing integrated for particular device functions;it need not resemble or run the OS of a desktop.'),
 ('What does the ALU do?','Relevant arithmetic and logical operations under the instruction/control design.'),
 ('What does the CU do?','Coordinates relevant instruction/control sequencing and signals.'),
 ('Do more cores or GHz alone prove universally better performance?','No. Architecture,workload,memory,software and operating/thermal conditions matter.'),
 ('What is the motherboard?','The main circuit board supporting/interconnecting relevant system components and interfaces.'),
 ('Does every laptop have replaceable CPU/RAM modules?','No. Integration/soldering/model design varies;check the exact service specification.'),
 ('How does RAM differ from SSD capacity?','RAM is active working state;SSD is persistent storage. They are different resources.'),
 ('Is firmware the same as the flash chip?','No. The chip is hardware;firmware is low-level software/content stored in suitable memory.'),
 ('Can modern firmware be updateable?','Yes,but this unit performs no firmware flash/reset/change.'),
 ('Is UEFI just a graphical BIOS menu?','No. It specifies interfaces/services between platform firmware and OS/pre-boot components.'),
 ('Does a missing sandbox EFI directory prove the physical machine uses legacy BIOS?','No. A sandbox exposes only a limited view,and no such inference/probe is used here.'),
 ('Is the RTC coin cell the laptop’s main battery?','No. Their roles differ,and settings/time behaviour is model-dependent.'),
 ('Does removing a battery universally erase BIOS firmware or reset every setting?','No. Firmware flash and settings storage differ;no such procedure is assigned here.'),
 ('What may a laptop video controller/GPU do?','Generate/drive appropriate display output;it may be integrated,discrete or part of a SoC.'),
 ('Must every laptop have an optical drive and fan?','No. Removable-media and cooling implementations are model-dependent;some are absent/external/fanless.'),
 ('What do Wi-Fi/Bluetooth components provide?','Supported wireless connectivity through appropriate hardware/antennas/software.'),
 ('What is a common meaning of LED monitor?','An LED-backlit LCD;not automatically a direct-emissive LED or OLED panel.'),
 ('What is USB-C?','A connector form;protocol,video and charging capability must be checked separately.'),
 ('Do all Thunderbolt generations use USB-C?','No. Thunderbolt 1/2 used Mini DisplayPort-style connectors;3/4/5 use USB-C.'),
 ('What does RJ45-style commonly refer to on a PC?','The8P8C wired Ethernet connection,not a telephone jack.'),
 ('What is VGA?','A traditional DE-15 analog video interface,not HDMI-style digital audio/video.'),
 ('Does every 3.5mm jack support the same microphone/headphone combination?','No. Device wiring/role and compatible plugs vary.'),
 ('What is an SMPS?','A switched-mode power supply providing appropriate regulated power outputs;not a data/storage component.'),
 ('Should a learner open PSU/charger/monitor internals for identification?','No. Hazardous stored charge/high voltage and other risks require appropriate qualified service.'),
 ('What does 512 decimal GB equal approximately in GiB?','476.837 GiB by unit conversion,not a measured formatted-capacity result.'),
 ('What do the four software examples actually establish?','Read-only sandbox reports,capacity arithmetic,declared connector-profile differences and spec-field completeness—not physical practical completion.'),
 ('What is the limit of the dated manufacturer reference examples?','They are selected official-page base profiles checked 29 Oct2026,not globally newest/local availability,Windows servicing,upgrade or performance proof.')]
VIVA=[{'title':tr('Unit 1 Viva and Short Revision'),'items':[{'q':tr(q),'a':tr(a)} for q,a in QA]}]
