import requests
import time
import random

URL = "http://127.0.0.1:8000/api/v1/ingest"

IPS = ["192.168.1.15", "10.0.0.55", "172.16.0.4", "45.22.19.11", "10.10.10.7"]
EVENTS = ["web_request", "login_attempt", "api_call", "file_upload"]

PAYLOADS = [
    # Clean Traffic 
    "GET /index.html HTTP/1.1",
    "POST /api/settings {'theme': 'dark'}",
    "GET /images/avatar.png HTTP/1.1",
    "GET /dashboard HTTP/1.1",
    
    #  Malicious Traffic 
    "GET /login?user=admin' OR 1=1--",                   # SQLi
    "POST /comment <script>alert('pwned')</script>",     # XSS
    "GET /../../../../etc/passwd",                       # Path Traversal
    "SELECT * FROM users WHERE username = 'admin'--",    # SQLi
    "<img src=x onerror=fetch('http://evil.com')>"       # XSS
]

print("💀 Initiating Phantom Botnet Simulator...")
print("Target: http://127.0.0.1:8000/api/v1/ingest")
print("Press Ctrl+C to abort.\n")

try:
    while True:
        payload = random.choice(PAYLOADS)
        data = {
            "source_ip": random.choice(IPS),
            "event_type": random.choice(EVENTS),
            "payload": payload
        }
        
        try:
            res = requests.post(URL, json=data)
            status = "🚨 THREAT" if res.json().get("anomalies") else "✅ CLEAN"
            print(f"[{status}] Fired from {data['source_ip']} -> {payload[:30]}...")
        except Exception:
            print("❌ Connection refused. Is the backend running?")
            
       
        time.sleep(random.uniform(0.5, 2.0))

except KeyboardInterrupt:
    print("\n🛑 Simulation terminated.")
