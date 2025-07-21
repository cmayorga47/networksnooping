import React, { useEffect, useState } from 'react';

type SnmpData = Record<string, string>;

const SNMPDashboard: React.FC = () => {
  const [snmpData, setSnmpData] = useState<SnmpData | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch('http://localhost:5000/api/SNMP')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch SNMP data');
        }
        return response.json();
      })
      .then((data: SnmpData) => {
        setSnmpData(data);
        setLoading(false);
      })
      .catch((err: Error) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
      <h2>SNMP Device Status</h2>

      {loading && <p>Loading SNMP data...</p>}
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}

      {snmpData && (
        <table style={{ borderCollapse: 'collapse', width: '100%' }}>
          <thead>
            <tr>
              <th style={{ border: '1px solid #ccc', padding: '8px' }}>OID</th>
              <th style={{ border: '1px solid #ccc', padding: '8px' }}>Value</th>
            </tr>
          </thead>
          <tbody>
            {Object.entries(snmpData).map(([oid, value]) => (
              <tr key={oid}>
                <td style={{ border: '1px solid #eee', padding: '8px' }}>{oid}</td>
                <td style={{ border: '1px solid #eee', padding: '8px' }}>{value}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default SNMPDashboard;
