# FTIR
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Analisi Spettrale FTIR", layout="wide")

st.title("📈 Selezione Interattiva delle Aree di Analisi FTIR")
st.markdown("Modifica le concentrazioni dei gas e osserva le sovrapposizioni spettrali.")

gas_data = {
    "CO": {"peak": 2185, "width": 20, "intensity": 1.0},
    "CO2": {"peak": 2350, "width": 25, "intensity": 1.0},
    "NO": {"peak": 1895, "width": 15, "intensity": 0.8},
    "NO2": {"peak": 1605, "width": 15, "intensity": 0.7},
    "NH3": {"peak": 975, "width": 10, "intensity": 0.6},
    "CH4": {"peak": 1330, "width": 15, "intensity": 0.9},
    "H2O": {"peak": 1600, "width": 50, "intensity": 1.2},
}

def gaussian(x, peak, width, intensity):
    return intensity * np.exp(-0.5 * ((x - peak) / width) ** 2)

def calculate_area(gas, concentration, x):
    return gaussian(x, gas["peak"], gas["width"], gas["intensity"]) * concentration

x = np.linspace(900, 4200, 1000)

st.sidebar.title("🎚️ Imposta concentrazioni (ppm o %vol)")
gas_concentrations = {
    gas: st.sidebar.slider(
        gas,
        min_value=0.0,
        max_value=1000.0,
        value=(5.0 if gas in ["CO2", "H2O"] else 100.0),
        step=1.0
    )
    for gas in gas_data
}

fig, ax = plt.subplots(figsize=(12, 6))
total_spectrum = np.zeros_like(x)

for name, conc in gas_concentrations.items():
    spec = calculate_area(gas_data[name], conc, x)
    total_spectrum += spec
    ax.plot(x, spec, label=f"{name} ({conc})")

ax.plot(x, total_spectrum, label="Totale", color="black", linewidth=2)
ax.set_title("Spettri di Assorbanza – Sovrapposizione dei Gas")
ax.set_xlabel("Numero d'onda (cm⁻¹)")
ax.set_ylabel("Assorbanza")
ax.legend()
ax.grid(True)

st.pyplot(fig)
st.markdown("---")
st.markdown("👈 Usa la barra laterale per cambiare le concentrazioni e analizzare sovrapposizioni spettrali.")
