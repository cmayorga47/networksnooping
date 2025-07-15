# backend/app.py

#currently configuring python and import versions
from contextvars import ContextVar
from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, jsonify
from flask_cors import CORS
from pysnmp.hlapi import (
    SnmpEngine,
    CommunityData,
    UdpTransportTarget,
    ContextData,
    ObjectType,
    ObjectIdentity,
    getCmd
)


app = Flask(__name__)
CORS(app)  # Allow requests from frontend

def snmp_poll(ip, oid, community='public'):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community),
        UdpTransportTarget((ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    if errorIndication or errorStatus:
        return {'error': str(errorIndication or errorStatus)}

    for varBind in varBinds:
        return {'oid': str(varBind[0]), 'value': str(varBind[1])}

@app.route('/api/snmp/<ip>/<oid>', methods=['GET'])
def snmp_data(ip, oid):
    data = snmp_poll(ip, oid)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
