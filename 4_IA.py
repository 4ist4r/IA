import os
import tkinter as tk
from tkinter import filedialog
from scapy.all import rdpcap, TCP
import pandas as pd
from sklearn.preprocessing import StandardScaler
import torch
import torch.nn as nn

# Verifica si el modelo y el escalador existen
MODEL_PATH = "mlp_model.pth"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"El modelo '{MODEL_PATH}' no existe. Verifica la ruta.")

# Definir la arquitectura del modelo
class MLPModel(nn.Module):
    def __init__(self):
        super(MLPModel, self).__init__()
        self.fc1 = nn.Linear(4, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x

# Cargar el modelo
mlp_model = MLPModel()
mlp_model.load_state_dict(torch.load(MODEL_PATH))
mlp_model.eval()

# Configuración inicial del escalador
scaler = StandardScaler()

# Función para procesar archivos PCAP
def process_pcap(file_path):
    packets = rdpcap(file_path)
    features = []

    for pkt in packets:
        try:
            packet_size = len(pkt)
            connection_duration = pkt.time  # Tiempo relativo
            packets_per_session = 1  # Simplificación
            anomaly_score = 0.1 if pkt.haslayer(TCP) else 0.3  # Heurística simple
            features.append([packet_size, connection_duration, packets_per_session, anomaly_score])
        except Exception:
            continue

    return pd.DataFrame(features, columns=['packet_size', 'connection_duration', 'packets_per_session', 'anomaly_score'])

# Función para cargar archivo y procesarlo
def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("PCAP files", "*.pcap")])
    if not file_path:
        return