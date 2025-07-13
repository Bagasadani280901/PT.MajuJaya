import streamlit as st
import math

# Fungsi EOQ
def hitung_eoq(D, S, H):
    eoq = math.sqrt((2 * D * S) / H)
    total_biaya = (D / eoq) * S + (eoq / 2) * H
    jumlah_pesanan = D / eoq
    return eoq, total_biaya, jumlah_pesanan

# Konfigurasi halaman
st.set_page_config(page_title="EOQ Optimizer", page_icon="📦", layout="wide")

# Header aplikasi
st.markdown("<h1 style='text-align: center;'>📦 EOQ Optimizer</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Economic Order Quantity Calculator</h4>", unsafe_allow_html=True)
st.markdown("---")

# Layout input dan penjelasan
col1, col2 = st.columns([1, 2])

with col1:
    st.header("🔧 Input Data")
    D = st.number_input("📦 Permintaan Tahunan (unit)", min_value=1.0, value=10000.0)
    S = st.number_input("📋 Biaya Pemesanan per Pesanan (Rp)", min_value=1.0, value=250000.0)
    H = st.number_input("🏬 Biaya Penyimpanan per Unit per Tahun (Rp)", min_value=1.0, value=1500.0)

with col2:
    st.info("""
    **📘 Apa itu EOQ?**  
    Economic Order Quantity adalah jumlah pembelian optimal untuk meminimalkan total biaya persediaan (biaya pemesanan + penyimpanan).
    
    Model ini cocok untuk sistem persediaan yang stabil dan terprediksi.
    """)

st.markdown("---")

# Tombol hitung
if st.button("🚀 Hitung EOQ Sekarang!"):
    eoq, total_biaya, jumlah_pesanan = hitung_eoq(D, S, H)

    st.subheader("📊 Hasil Perhitungan")
    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(label="EOQ (Jumlah Pesanan Optimal)", value=f"{eoq:.2f} unit", delta=None)

    with c2:
        st.metric(label="Jumlah Pemesanan per Tahun", value=f"{jumlah_pesanan:.2f} kali")

    with c3:
        st.metric(label="Total Biaya Persediaan", value=f"Rp {total_biaya:,.2f}")

    st.success("✅ Perhitungan berhasil! Gunakan EOQ sebagai acuan untuk mengelola stok secara efisien.")

else:
    st.warning("Klik tombol 'Hitung EOQ Sekarang!' untuk melihat hasil perhitungan.")

