'use client';
import { useEffect, useState } from 'react';

export default function Dashboard() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/v1/logs')
      .then(res => res.json())
      .then(data => setLogs(data))
      .catch(err => console.error("Error fetching logs:", err));
  }, []);

  return (
    <div className="min-h-screen bg-neutral-950 text-green-400 p-8 font-mono">
      <div className="max-w-7xl mx-auto">
        <header className="mb-8 border-b border-green-900 pb-4">
          <h1 className="text-3xl font-bold tracking-wider">PHANTOM-SIEM // <span className="text-neutral-500">ROOT_ACCESS</span></h1>
          <p className="text-neutral-500 text-sm mt-2">Live Threat Intelligence Feed</p>
        </header>

        <div className="overflow-x-auto border border-green-900 rounded bg-neutral-900/50">
          <table className="w-full text-left text-sm">
            <thead className="bg-neutral-900 text-green-600">
              <tr>
                <th className="p-4 border-b border-green-900">ID</th>
                <th className="p-4 border-b border-green-900">TIMESTAMP</th>
                <th className="p-4 border-b border-green-900">SOURCE IP</th>
                <th className="p-4 border-b border-green-900">EVENT TYPE</th>
                <th className="p-4 border-b border-green-900">PAYLOAD</th>
                <th className="p-4 border-b border-green-900">STATUS</th>
              </tr>
            </thead>
            <tbody>
              {logs.map((log: any) => (
                <tr key={log.id} className="border-b border-green-900/30 hover:bg-neutral-900/80 transition-colors">
                  <td className="p-4 text-neutral-500">{log.id}</td>
                  <td className="p-4 text-neutral-400">{new Date(log.timestamp).toLocaleString()}</td>
                  <td className="p-4">{log.source_ip}</td>
                  <td className="p-4">{log.event_type}</td>
                  <td className="p-4 truncate max-w-xs">{log.payload}</td>
                  <td className="p-4">
                    {log.is_anomalous ? (
                      <span className="bg-red-900/50 text-red-400 px-2 py-1 rounded border border-red-800 animate-pulse">
                        {log.threat_tags}
                      </span>
                    ) : (
                      <span className="text-neutral-500">CLEAN</span>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          {logs.length === 0 && (
            <div className="p-8 text-center text-neutral-600">No logs ingested yet.</div>
          )}
        </div>
      </div>
    </div>
  );
}
