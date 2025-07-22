from pysnmp.hlapi import (
    getCmd, SnmpEngine, CommunityData, UdpTransportTarget,
    ContextData, ObjectType, ObjectIdentity
)
import time

def snmp_get(oid, target=('127.0.0.1', 1161), community='bandwidth', version=1):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community),
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


def snmp_get_all(target=('127.0.0.1', 1161), community='bandwidth'):
    oids = [
        '1.3.6.1.2.1.1.1.0',        # sysDescr
        '1.3.6.1.2.1.1.2.0',        # sysObjectID
        '1.3.6.1.2.1.1.3.0',        # sysUpTime
        '1.3.6.1.2.1.1.4.0',        # sysContact
        '1.3.6.1.2.1.1.5.0',        # sysName
        '1.3.6.1.2.1.1.6.0',        # sysLocation
        '1.3.6.1.2.1.2.2.1.2.1',    # ifDescr.1
        '1.3.6.1.2.1.2.2.1.10.1',   # ifInOctets.1
        '1.3.6.1.2.1.2.2.1.16.1',   # ifOutOctets.1
    ]

    results = {}

    for oid in oids:
        data = snmp_get(oid, target=target, community=community)
        results.update(data)

    return results


if __name__ == '__main__':
    while True:
        data = snmp_get_all()
        for k, v in data.items():
            print(f'{k}: {v}')
        print('-' * 40)
        time.sleep(5)
