import streamlit as st
import math

# Fungsi menghitung EOQ
def hitung_eoq(D, S, H):
    eoq = math.sqrt((2 * D * S) / H)
    total_biaya = (D / eoq) * S + (eoq / 2) * H
    jumlah_pesanan = D / eoq
    return eoq, total_biaya, jumlah_pesanan

# Konfigurasi halaman
st.set_page_config(page_title="EOQ Optimizer", page_icon="📦", layout="wide")

# Judul dan Deskripsi Aplikasi
st.markdown("""
    <div style='text-align: center; padding: 10px'>
        <h1 style='color:#2c3e50;'>📦 EOQ Optimizer App</h1>
        <h4 style='color:gray;'>Economic Order Quantity Calculator for Inventory Efficiency</h4>
        <hr style='border: 1px solid #bbb;'>
    </div>
""", unsafe_allow_html=True)

# Layout input dan info
col1, col2 = st.columns([1, 1.2])
with col1:
    with st.container():
        st.markdown("### 🔧 Masukkan Data")
        D = st.number_input("📦 Permintaan Tahunan (unit)", min_value=1.0, value=10000.0)
        S = st.number_input("📋 Biaya Pemesanan per pesanan (Rp)", min_value=1.0, value=250000.0)
        H = st.number_input("🏬 Biaya Penyimpanan per unit per tahun (Rp)", min_value=1.0, value=1500.0)

with col2:
    with st.expander("PT. MAJU JAYA", expanded=True):
        st.markdown("""
        PT. Maju Jaya adalah perusahaan dagang yang bergerak di bidang distribusi alat tulis kantor (ATK). 
        Salah satu produk andalan mereka adalah kertas HVS A4, yang sangat dibutuhkan oleh pelanggan dari 
        instansi pemerintahan, perkantoran, hingga sektor pendidikan.

        Manajer gudang ingin melakukan evaluasi terhadap sistem pengelolaan persediaan yang selama ini dilakukan 
        berdasarkan perkiraan. Akibatnya, sering terjadi kelebihan atau kekurangan stok yang menyebabkan biaya tinggi. 
        Untuk mengoptimalkan biaya, manajer memutuskan menggunakan pendekatan Economic Order Quantity (EOQ).

        """)

# Tombol perhitungan
if st.button("🚀 Hitung EOQ Sekarang!", use_container_width=True):
    eoq, total_biaya, jumlah_pesanan = hitung_eoq(D, S, H)

    st.markdown("---")
    st.markdown("## 📊 Hasil Perhitungan")

    # Tampilan hasil dengan 3 kolom metrik
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("📦 EOQ Optimal", f"{eoq:.2f} unit")
    col_b.metric("📈 Jumlah Pesanan / Tahun", f"{jumlah_pesanan:.2f} kali")
    col_c.metric("💰 Total Biaya Persediaan", f"Rp {total_biaya:,.2f}")

    st.success("✅ Perhitungan selesai. Gunakan hasil EOQ untuk merencanakan persediaan Anda secara efisien.")
else:
    st.info("Isi semua input, lalu klik tombol di atas untuk menghitung EOQ.")

# Footer
st.markdown("""
    <hr>
    <div style='text-align: center; color: green; font-size: big;'>
       ----------DIBUAT OLEH BAGAS ADANI MUKTI----------
    </div>
""", unsafe_allow_html=True)
