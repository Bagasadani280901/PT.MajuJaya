import streamlit as st
import math

# Fungsi untuk menghitung EOQ
def hitung_eoq(D, S, H):
    eoq = math.sqrt((2 * D * S) / H)
    total_biaya = (D / eoq) * S + (eoq / 2) * H
    jumlah_pesanan = D / eoq
    return eoq, total_biaya, jumlah_pesanan

# Judul aplikasi
st.set_page_config(page_title="Aplikasi EOQ", page_icon="📦")
st.title("📦 Aplikasi Perhitungan EOQ (Economic Order Quantity)")

st.markdown("""
Aplikasi ini menghitung jumlah pemesanan optimal untuk meminimalkan biaya persediaan berdasarkan model EOQ.
""")

# Input dari pengguna
with st.sidebar:
    st.header("🔧 Input Data")
    D = st.number_input("Permintaan Tahunan (unit)", min_value=1.0, value=12000.0)
    S = st.number_input("Biaya Pemesanan per pesanan (Rp)", min_value=1.0, value=500000.0)
    H = st.number_input("Biaya Penyimpanan per unit per tahun (Rp)", min_value=1.0, value=2000.0)

# Tombol hitung EOQ
if st.button("🔍 Hitung EOQ"):
    eoq, total_biaya, jumlah_pesanan = hitung_eoq(D, S, H)
    
    # Output hasil perhitungan
    st.subheader("📈 Hasil Perhitungan")
    st.success(f"**EOQ (Jumlah Pesanan Optimal):** {eoq:.2f} unit")
    st.info(f"**Jumlah Pemesanan per Tahun:** {jumlah_pesanan:.2f} kali")
    st.warning(f"**Total Biaya Persediaan:** Rp{total_biaya:,.2f}")
