from pysnmp.hlapi import *
import time

def snmp_get(oid, target=('127.0.0.1', 1161), community='public', version=1):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData('demo'),
        UdpTransportTarget(target),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    if errorIndication:
        return {'error': str(errorIndication)}
    elif errorStatus:
        return {'error': f'{errorStatus.prettyPrint()} at {errorIndex}'}
    else:
        return {str(varBind[0]): str(varBind[1]) for varBind in varBinds}

if __name__ == '__main__':
    while True:
        print(snmp_get('1.3.6.1.2.1.1.1.0'))  # sysDescr
        time.sleep(5)
