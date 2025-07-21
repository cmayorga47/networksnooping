# terminal_test_snmp.py
from pysnmp.hlapi import *

for (errorIndication,
     errorStatus,
     errorIndex,
     varBinds) in getCmd(
         SnmpEngine(),
         CommunityData('demo'),  # Make sure this matches your .snmprec community
         UdpTransportTarget(('127.0.0.1', 1161)),
         ContextData(),
         ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0'))  # sysDescr OID
     ):

    if errorIndication:
        print(f"Error: {errorIndication}")
    elif errorStatus:
        print(f'{errorStatus.prettyPrint()} at {errorIndex and varBinds[int(errorIndex) - 1][0] or "?"}')
    else:
        for varBind in varBinds:
            print(f'{varBind[0]} = {varBind[1]}')
