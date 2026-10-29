"""Read-only/software worksheet support, not a physical hardware test suite."""
import datetime,os,platform
from pathlib import Path
from decimal import Decimal,InvalidOperation
REQUIRED=('processor','memory','storage','gpu','display','ports','connectivity','os','source_url','checked_on')

def environment_inventory():
    """Only generic kernel/OS resource reports; no hostname, DMI/serial, MAC or firmware probe."""
    memory=None;path=Path('/proc/meminfo')
    if path.is_file():
        lines=path.read_text().splitlines()
        record=next((l for l in lines if l.startswith('MemTotal:')),None)
        if record:memory=int(record.split()[1])*1024
    return {'scope':'Sandbox OS/kernel report, not physical PC/laptop identification',
            'system':platform.system(),'machine':platform.machine(),
            'reported_logical_cpus':os.cpu_count(),'kernel_MemTotal_bytes':memory,
            'physical_components_inspected':False,'BIOS_UEFI_or_CMOS_probed':False}

def decimal_gb_to_gib(gb):
    try:value=Decimal(str(gb))
    except InvalidOperation as error:raise ValueError('Use a numeric capacity') from error
    if not value.is_finite() or value<0:raise ValueError('Use a finite nonnegative capacity')
    return value*Decimal(10)**9/(Decimal(2)**30)

def missing_spec_fields(profile):
    missing=[field for field in REQUIRED if not isinstance(profile.get(field),str) or not profile[field].strip()]
    if 'source_url' not in missing and not profile['source_url'].startswith('https://'):missing.append('source_url')
    if 'checked_on' not in missing:
        try:datetime.date.fromisoformat(profile['checked_on'])
        except ValueError:missing.append('checked_on')
    return missing

def connector_fixture(profiles):
    if not profiles:raise ValueError('Use at least one declared fixture profile')
    for row in profiles:
        if row.get('connector')!='USB-C' or 'video_documented' not in row or (row.get('video_documented') is not None and type(row.get('video_documented')) is not bool):
            raise ValueError('Use the declared USB-C fixture format')
    known={row['video_documented'] for row in profiles if row['video_documented'] is not None}
    return {'same_connector':all(row['connector']=='USB-C' for row in profiles),
            'video_capability_varies_in_fixture':known=={False,True},
            'charging_unspecified_count':sum(row.get('charging_documented') is None for row in profiles),
            'actual_ports_or_PD_negotiation_tested':False}
