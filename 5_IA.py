import os
import tkinter as tk
from tkinter import filedialog
from scapy.all import rdpcap, TCP
import pandas as pd
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model

# Verifica si el modelo y el escalador existen
MODEL_PATH = "mlp_model.h5"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"El modelo '{MODEL_PATH}' no existe. Verifica la ruta.")

try:
    mlp_model = load_model(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Error al cargar el modelo: {e}")

# Configuración inicial del escalador y modelo
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