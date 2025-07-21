## testSNMP.py
from flask import Flask, jsonify
from flask_cors import CORS
from pysnmp.hlapi import *

app = Flask(__name__)
CORS(app)

@app.route('/api/SNMP')
def get_snmp():
    result = {}
    print("⏳ Starting SNMP getCmd...")  # Debug log
    for (errorIndication, errorStatus, errorIndex, varBinds) in getCmd(
        SnmpEngine(),
        CommunityData('demo'),  # MUST match the one that works in test.py
        UdpTransportTarget(('127.0.0.1', 1161), timeout=2, retries=6),
        ContextData(),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0'))  # sysDescr
    ):
        if errorIndication:
            print(f"⚠️ SNMP errorIndication: {errorIndication}")
            result['error'] = str(errorIndication)
        elif errorStatus:
            print(f"⚠️ SNMP errorStatus: {errorStatus.prettyPrint()} at {errorIndex}")
            result['error'] = f"{errorStatus.prettyPrint()} at {errorIndex}"
        else:
            for varBind in varBinds:
                print(f"✅ SNMP Response: {varBind[0]} = {varBind[1]}")
                result[str(varBind[0])] = str(varBind[1])
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
