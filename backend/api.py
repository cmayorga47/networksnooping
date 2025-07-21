from flask import Flask, jsonify
from flask_cors import CORS  # ✅ Add this
from poller import snmp_get

app = Flask(__name__)
CORS(app)  # ✅ Allow CORS from all origins (you can restrict later)

@app.route('/api/SNMP')
def status():
    return jsonify(snmp_get('1.3.6.1.2.1.1.1.0'))

if __name__ == '__main__':
    app.run(debug=True)
