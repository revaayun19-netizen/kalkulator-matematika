
import streamlit as st
import math

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="MathMaster Calculator",
    page_icon="🧠",
    layout="wide"
)

# =========================
# HEADER
# =========================
st.title("🧠 MathMaster Calculator")

st.markdown("""
## 🎯 Matematika Jadi Lebih Mudah!

Selamat datang di **MathMaster Calculator**, aplikasi matematika interaktif yang membantu menghitung sekaligus memahami langkah penyelesaian.

### 📚 Fitur yang Tersedia
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
    st.header("📚 Menu")

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
Septi  
Reva  
Nafis  
Ovita
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

    st.success(
        "Selamat datang di MathMaster Calculator. Pilih menu di sebelah kiri untuk mulai menggunakan aplikasi."
    )

# =========================
# OPERASI DASAR
# =========================
elif menu == "➕ Operasi Dasar":

    st.header("➕ Operasi Dasar")

    a = st.number_input("Masukkan angka pertama", value=0.0)
    b = st.number_input("Masukkan angka kedua", value=0.0)

    operasi = st.selectbox(
        "Pilih Operasi",
        ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"]
    )

    if st.button("Hitung Operasi"):

        if operasi == "Penjumlahan":
            hasil = a + b
            simbol = "+"

        elif operasi == "Pengurangan":
            hasil = a - b
            simbol = "-"

        elif operasi == "Perkalian":
            hasil = a * b
            simbol = "×"

        else:
            if b == 0:
                st.error("Tidak dapat membagi dengan nol!")
                st.stop()

            hasil = a / b
            simbol = "÷"

        st.success(f"Hasil = {hasil}")

        st.subheader("📝 Langkah Penyelesaian")
        st.write(f"{a} {simbol} {b}")
        st.write(f"= {hasil}")

# =========================
# FAKTORIAL
# =========================
elif menu == "🔢 Faktorial":

    st.header("🔢 Faktorial")

    n = st.number_input(
        "Masukkan bilangan",
        min_value=0,
        step=1
    )

    if st.button("Hitung Faktorial"):

        hasil = math.factorial(int(n))

        st.success(f"{int(n)}! = {hasil}")

        st.subheader("📝 Langkah Penyelesaian")

        if n == 0:
            st.write("0! = 1")
        else:
            langkah = " × ".join(
                [str(i) for i in range(int(n), 0, -1)]
            )

            st.write(f"{int(n)}! = {langkah}")
            st.write(f"{int(n)}! = {hasil}")

# =========================
# PERMUTASI & KOMBINASI
# =========================
elif menu == "📊 Permutasi & Kombinasi":

    st.header("📊 Permutasi & Kombinasi")

    n = st.number_input(
        "Masukkan nilai n",
        min_value=0,
        step=1,
        key="n"
    )

    r = st.number_input(
        "Masukkan nilai r",
        min_value=0,
        step=1,
        key="r"
    )

    jenis = st.radio(
        "Pilih Perhitungan",
        ["Permutasi", "Kombinasi"]
    )

    if st.button("Hitung Permutasi/Kombinasi"):

        if r > n:
            st.error("Nilai r tidak boleh lebih besar dari n")

        else:

            if jenis == "Permutasi":

                hasil = math.factorial(int(n)) // math.factorial(int(n-r))

                st.success(f"{int(n)}P{int(r)} = {hasil}")

                st.subheader("📝 Langkah Penyelesaian")

                st.latex(r"P(n,r)=\frac{n!}{(n-r)!}")

                st.latex(
                    rf"P({int(n)},{int(r)})=\frac{{{int(n)}!}}{{({int(n-r)})!}}"
                )

                st.write(
                    f"= {math.factorial(int(n))} ÷ {math.factorial(int(n-r))}"
                )

                st.write(f"= {hasil}")

            else:

                hasil = math.factorial(int(n)) // (
                    math.factorial(int(r))
                    * math.factorial(int(n-r))
                )

                st.success(f"{int(n)}C{int(r)} = {hasil}")

                st.subheader("📝 Langkah Penyelesaian")

                st.latex(r"C(n,r)=\frac{n!}{r!(n-r)!}")

                st.latex(
                    rf"C({int(n)},{int(r)})=\frac{{{int(n)}!}}{{{int(r)}!({int(n-r)})!}}"
                )

                st.write(
                    f"= {math.factorial(int(n))} ÷ ({math.factorial(int(r))} × {math.factorial(int(n-r))})"
                )

                st.write(f"= {hasil}")

# =========================
# PANGKAT & AKAR
# =========================
elif menu == "📈 Pangkat & Akar":

    st.header("📈 Pangkat & Akar")

    pilihan = st.radio(
        "Pilih Perhitungan",
        ["Pangkat", "Akar Kuadrat"]
    )

    if pilihan == "Pangkat":

        angka = st.number_input("Masukkan angka")
        pangkat = st.number_input("Masukkan pangkat", step=1)

        if st.button("Hitung Pangkat"):

            hasil = angka ** pangkat

            st.success(f"Hasil = {hasil}")

            st.subheader("📝 Langkah Penyelesaian")
            st.write(f"{angka}^{int(pangkat)}")
            st.write(f"= {hasil}")

    else:

        angka = st.number_input(
            "Masukkan angka positif",
            min_value=0.0
        )

        if st.button("Hitung Akar"):

            hasil = math.sqrt(angka)

            st.success(f"√{angka} = {hasil}")

            st.subheader("📝 Langkah Penyelesaian")
            st.write(f"√{angka}")
            st.write(f"= {hasil}")

# =========================
# FPB & KPK
# =========================
elif menu == "📐 FPB & KPK":

    st.header("📐 FPB & KPK")

    a = st.number_input(
        "Masukkan bilangan pertama",
        min_value=1,
        step=1,
        key="fpb_a"
    )

    b = st.number_input(
        "Masukkan bilangan kedua",
        min_value=1,
        step=1,
        key="fpb_b"
    )

    pilihan = st.radio(
        "Pilih Perhitungan",
        ["FPB", "KPK"]
    )

    if st.button("Hitung FPB/KPK"):

        a = int(a)
        b = int(b)

        if pilihan == "FPB":

            hasil = math.gcd(a, b)

            st.success(f"FPB({a},{b}) = {hasil}")

            st.subheader("📝 Langkah Penyelesaian")
            st.write(f"FPB({a},{b}) = {hasil}")

        else:

            fpb = math.gcd(a, b)
            hasil = abs(a * b) // fpb

            st.success(f"KPK({a},{b}) = {hasil}")

            st.subheader("📝 Langkah Penyelesaian")
            st.write(f"FPB({a},{b}) = {fpb}")
            st.write(f"KPK = ({a} × {b}) ÷ {fpb}")
            st.write(f"KPK = {a*b} ÷ {fpb}")
            st.write(f"KPK = {hasil}")



st.caption("🧠 MathMaster Calculator | Dikembangkan oleh Kelompok 4")
