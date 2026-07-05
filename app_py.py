import streamlit as st
import math

st.set_page_config(
    page_title="🧠 MathMaster Calculator",
    page_icon="🧠",
    layout="wide"
)

# =========================
# HEADER
# =========================

st.title("🧠 MathMaster Calculator")

st.markdown("""
### 🚀 Selamat Datang di MathMaster Calculator

Aplikasi matematika multifungsi yang membantu Anda menyelesaikan berbagai perhitungan dengan cepat dan mudah.

💡 **Fitur yang tersedia:**
- ➕ Operasi Dasar
- 🔢 Faktorial
- 📊 Permutasi & Kombinasi
- 📈 Pangkat & Akar
- 📐 FPB & KPK
""")

# =========================
# SIDEBAR
# =========================

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=120)

    st.title("📚 Menu")

    menu = st.selectbox(
        "Pilih Fitur",
        [
            "🏠 Beranda",
            "➕ Operasi Dasar",
            "🔢 Faktorial",
            "📊 Permutasi & Kombinasi",
            "📈 Pangkat & Akar",
            "📐 FPB & KPK"
        ]
    )

    st.markdown("---")

    st.subheader("👥 Kelompok 4")
    st.write("""
    • Septi  
    • Reva  
    • Nafis  
    • Ovita
    """)

# =========================
# BERANDA
# =========================

if menu == "🏠 Beranda":

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📚 Total Fitur", "5")

    with col2:
        st.metric("🧮 Kategori", "Matematika")

    with col3:
        st.metric("💻 Platform", "Streamlit")

    st.markdown("---")

    st.info("""
    🎯 **Tujuan Aplikasi**

    MathMaster Calculator dibuat untuk membantu siswa dan mahasiswa
    melakukan berbagai perhitungan matematika secara cepat, mudah,
    dan interaktif.
    """)

    st.success("""
    Gunakan menu di sebelah kiri untuk memilih fitur yang ingin digunakan.
    """)

# =========================
# OPERASI DASAR
# =========================

elif menu == "➕ Operasi Dasar":

    st.header("➕ Operasi Dasar")

    a = st.number_input("Angka Pertama", value=0.0)
    b = st.number_input("Angka Kedua", value=0.0)

    operasi = st.selectbox(
        "Pilih Operasi",
        ["Tambah", "Kurang", "Kali", "Bagi"]
    )

    if st.button("🔍 Hitung"):

        if operasi == "Tambah":
            hasil = a + b

        elif operasi == "Kurang":
            hasil = a - b

        elif operasi == "Kali":
            hasil = a * b

        else:
            if b == 0:
                st.error("Tidak dapat membagi dengan nol!")
                st.stop()

            hasil = a / b

        st.success(f"🎉 Hasil = {hasil}")

# =========================
# FAKTORIAL
# =========================

elif menu == "🔢 Faktorial":

    st.header("🔢 Faktorial")

    n = st.number_input(
        "Masukkan Bilangan",
        min_value=0,
        step=1
    )

    if st.button("Hitung Faktorial"):

        hasil = math.factorial(int(n))

        st.success(f"🎉 {int(n)}! = {hasil}")

# =========================
# PERMUTASI & KOMBINASI
# =========================

elif menu == "📊 Permutasi & Kombinasi":

    st.header("📊 Permutasi & Kombinasi")

    n = st.number_input("Nilai n", min_value=0, step=1)
    r = st.number_input("Nilai r", min_value=0, step=1)

    jenis = st.radio(
        "Pilih",
        ["Permutasi", "Kombinasi"]
    )

    if st.button("Hitung"):

        if r > n:
            st.error("r tidak boleh lebih besar dari n")

        else:

            if jenis == "Permutasi":

                hasil = math.factorial(n) // math.factorial(n-r)

                st.success(f"🎉 {n}P{r} = {hasil}")

            else:

                hasil = math.factorial(n) // (
                    math.factorial(r) *
                    math.factorial(n-r)
                )

                st.success(f"🎉 {n}C{r} = {hasil}")

# =========================
# PANGKAT & AKAR
# =========================

elif menu == "📈 Pangkat & Akar":

    st.header("📈 Pangkat & Akar")

    pilihan = st.radio(
        "Pilih",
        ["Pangkat", "Akar"]
    )

    if pilihan == "Pangkat":

        angka = st.number_input("Angka")
        pangkat = st.number_input("Pangkat", step=1)

        if st.button("Hitung Pangkat"):

            hasil = angka ** pangkat

            st.success(f"🎉 Hasil = {hasil}")

    else:

        angka = st.number_input(
            "Masukkan Angka Positif",
            min_value=0.0
        )

        if st.button("Hitung Akar"):

            hasil = math.sqrt(angka)

            st.success(f"🎉 √{angka} = {hasil}")

# =========================
# FPB & KPK
# =========================

elif menu == "📐 FPB & KPK":

    st.header("📐 FPB & KPK")

    a = st.number_input(
        "Bilangan Pertama",
        min_value=1,
        step=1
    )

    b = st.number_input(
        "Bilangan Kedua",
        min_value=1,
        step=1
    )

    pilihan = st.radio(
        "Pilih",
        ["FPB", "KPK"]
    )

    if st.button("Hitung"):

        if pilihan == "FPB":

            hasil = math.gcd(a, b)

        else:

            hasil = abs(a*b) // math.gcd(a, b)

        st.success(f"🎉 Hasil {pilihan} = {hasil}")

# =========================
# FOOTER
# =========================
st.markdown("---")

st.info("""
### 👥 Kelompok 4

**Anggota:**
- Septi
- Reva
- Nafis
- Ovita
""")

st.caption("🧠 MathMaster Calculator | Dikembangkan oleh Kelompok 4")
