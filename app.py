import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Data asli dari laporan PT Solusi Bangun Indonesia (Kelompok 11)
a = 1382320  # Choke Price [cite: 71]
b = 38979    # Koefisien produksi [cite: 42, 64]
mc = 719136  # Rata-rata Biaya Marginal [cite: 53, 57]

st.set_page_config(page_title="Simulasi PT SBI", layout="wide")
st.title("⚒️ Alat Simulasi Harga Batu Kapur PT SBI")
st.write("Analisis Ekonomi Sumber Daya Alam - Kelompok 11")

# Sidebar untuk memilih mekanisme pasar
st.sidebar.header("Pilih Bentuk Pasar")
pasar = st.sidebar.selectbox("Mekanisme:", ["Persaingan Sempurna", "Monopoli", "Oligopoli"])

# Logika Perhitungan Berdasarkan Struktur Pasar
if pasar == "Persaingan Sempurna":
    q_opt = (a - mc) / b
    p_opt = mc
elif pasar == "Monopoli":
    q_opt = (a - mc) / (2 * b)
    p_opt = a - (b * q_opt)
else: # Oligopoli (Asumsi Duopoli)
    q_opt = (2 * (a - mc)) / (3 * b)
    p_opt = a - (b * q_opt)

# Menampilkan hasil simulasi
col1, col2 = st.columns(2)
col1.metric("Harga (P) per Ton", f"Rp {p_opt:,.0f}")
col2.metric("Produksi (Q) Ton", f"{q_opt:.2f}")

st.info(f"Waktu optimal habis cadangan (T*) diproyeksikan selama 13 tahun. [cite: 77, 94]")

# Grafik Kurva Permintaan
q_range = np.linspace(0, 40, 100)
p_demand = a - b * q_range
fig, ax = plt.subplots()
ax.plot(q_range, p_demand, label="Fungsi Permintaan [cite: 46]", color="blue")
ax.axhline(y=mc, color='red', linestyle='--', label="Marginal Cost (MC) [cite: 72]")
ax.scatter(q_opt, p_opt, color='green', s=100, label=f"Titik {pasar}")
ax.set_ylim(0, 1500000)
ax.set_xlabel("Kuantitas (Q)")
ax.set_ylabel("Harga (P)")
ax.legend()
st.pyplot(fig)
