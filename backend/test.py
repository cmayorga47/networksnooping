from pysnmp.hlapi import (
    getCmd, SnmpEngine, CommunityData,
    UdpTransportTarget, ContextData,
    ObjectType, ObjectIdentity
)

def snmp_get(oid, target=('127.0.0.1', 1161), community='demo'):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community),
        UdpTransportTarget(target),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        return {oid: f"Error: {errorIndication}"}
    elif errorStatus:
        return {oid: f"{errorStatus.prettyPrint()} at {errorIndex}"}
    else:
        return {str(varBind[0]): str(varBind[1]) for varBind in varBinds}


def test_snmp_all():
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

    for oid in oids:
        result = snmp_get(oid)
        for k, v in result.items():
            print(f'{k} = {v}')


if __name__ == '__main__':
    test_snmp_all()
