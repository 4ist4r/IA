import subprocess

class CyberSecurityAI:
    def __init__(self):
        self.tools = {
            "whatweb": "whatweb",
            "nmap": "nmap",
            "burpsuite": "burpsuite"
        }

    def run_whatweb(self, domain):
        print(f"Running WhatWeb on {domain}...")
        result = subprocess.run([self.tools["whatweb"], domain], capture_output=True, text=True)
        return result.stdout

    def run_nmap(self, domain):
        print(f"Running Nmap on {domain}...")
        result = subprocess.run([self.tools["nmap"], "-A", domain], capture_output=True, text=True)
        return result.stdout

    def run_burpsuite(self, domain):
        print(f"Running Burp Suite on {domain}...")
        # Note: Burp Suite typically requires manual interaction, so this is a placeholder
        return "Burp Suite scan initiated. Please complete the scan manually."

    def audit_domain(self, domain, tool):
        if tool == "whatweb":
            return self.run_whatweb(domain)
        elif tool == "nmap":
            return self.run_nmap(domain)
        elif tool == "burpsuite":
            return self.run_burpsuite(domain)
        else:
            return "Herramienta no reconocida. Por favor, elige entre 'whatweb', 'nmap' o 'burpsuite'."

# Ejemplo de uso
domain = "example.com"  # Reemplaza con el dominio de tu entorno controlado
tool = "nmap"  # Reemplaza con la herramienta que deseas usar: 'whatweb', 'nmap' o 'burpsuite'
ai = CyberSecurityAI()
result = ai.audit_domain(domain, tool)
print(result)