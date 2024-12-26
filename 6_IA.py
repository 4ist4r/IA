class CyberSecurityAI:
    def __init__(self):
        self.tools = {
            "malware_detection": ["VirusTotal", "MalwareBazaar", "ClamAV"],
            "vulnerability_analysis": ["Nessus", "OpenVAS", "Burp Suite"],
            "password_management": ["LastPass", "1Password", "KeePass"],
            "pentesting": ["Metasploit", "Nmap", "Wireshark"],
            "activity_monitoring": ["Snort", "Suricata"],
            "data_encryption": ["GPG", "VeraCrypt"],
            "firewalls": ["pfSense", "Cisco ASA"],
            "incident_response": ["TheHive", "Cortex"]
        }

    def recommend_tool(self, task):
        if task in self.tools:
            return f"Para {task}, puedes usar: {', '.join(self.tools[task])}."
        else:
            return "Lo siento, no tengo información sobre esa tarea."

    def explain_concept(self, concept):
        concepts = {
            "malware_detection": "La detección de malware implica identificar y eliminar software malicioso.",
            "vulnerability_analysis": "El análisis de vulnerabilidades busca identificar y mitigar debilidades en los sistemas.",
            "password_management": "La gestión de contraseñas asegura que las contraseñas sean fuertes y seguras.",
            "pentesting": "El pentesting es la práctica de probar la seguridad de un sistema mediante ataques simulados.",
            "activity_monitoring": "La monitorización de actividad implica supervisar el tráfico de red para detectar actividades sospechosas.",
            "data_encryption": "La encriptación de datos protege la información convirtiéndola en un formato ilegible sin una clave.",
            "firewalls": "Los firewalls controlan el tráfico de red basado en reglas de seguridad predefinidas.",
            "incident_response": "La respuesta a incidentes implica gestionar y mitigar los efectos de un incidente de seguridad."
        }
        return concepts.get(concept, "Lo siento, no tengo información sobre ese concepto.")

# Ejemplo de uso
ai = CyberSecurityAI()
print(ai.recommend_tool("malware_detection"))
print(ai.explain_concept("pentesting"))

