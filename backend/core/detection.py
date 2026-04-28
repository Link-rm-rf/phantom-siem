import re
from typing import List, Dict

class ThreatDetector:
    def __init__(self):
        self.signatures = {
            "SQL_INJECTION": re.compile(r"(?i)(UNION.*SELECT|SELECT.*FROM|DROP\s+TABLE|OR\s+1=1|--$)"),
            "XSS_ATTACK": re.compile(r"(?i)(<script>|javascript:|onerror=|onload=)"),
            "PATH_TRAVERSAL": re.compile(r"(?i)(\.\./\.\./|\.\.\\\.\.\\|/etc/passwd)")
        }

    def scan_payload(self, payload: str) -> Dict[str, any]:
        flags: List[str] = []
        
        for threat_name, pattern in self.signatures.items():
            if pattern.search(payload):
                flags.append(threat_name)
                
        return {
            "is_anomalous": len(flags) > 0,
            "threat_tags": flags
        }

detector = ThreatDetector()
