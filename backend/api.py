from flask import Flask, jsonify
from flask_cors import CORS  # ✅ Add this
from poller import snmp_get_all

app = Flask(__name__)
CORS(app)  # ✅ Allow CORS from all origins (you can restrict later)

@app.route('/api/SNMP')
def status():
    return jsonify(snmp_get_all())

if __name__ == '__main__':
    app.run(debug=True)
