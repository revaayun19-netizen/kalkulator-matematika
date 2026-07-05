import streamlit as st
import math
import numpy as np

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="MathMaster Calculator",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 MathMaster Calculator")
st.write("Kalkulator Matematika Interaktif Berbasis Python dan Streamlit")

st.sidebar.title("📚 Menu")
menu = st.sidebar.selectbox(
    "Pilih Fitur",
    [
        "Operasi Dasar",
        "Faktorial",
        "Permutasi & Kombinasi",
        "Pangkat & Akar",
        "FPB & KPK"
    ]
)

# =========================
# OPERASI DASAR
# =========================
if menu == "Operasi Dasar":

    st.header("➕ Operasi Dasar")

    a = st.number_input("Masukkan angka pertama", value=0.0)
    b = st.number_input("Masukkan angka kedua", value=0.0)

    operasi = st.selectbox(
        "Pilih Operasi",
        ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"]
    )

    if st.button("Hitung"):

        if operasi == "Penjumlahan":
            hasil = a + b

        elif operasi == "Pengurangan":
            hasil = a - b

        elif operasi == "Perkalian":
            hasil = a * b

        else:
            if b == 0:
                st.error("Tidak dapat membagi dengan nol.")
                st.stop()
            hasil = a / b

        st.success(f"Hasil = {hasil}")

# =========================
# FAKTORIAL
# =========================
elif menu == "Faktorial":

    st.header("🔢 Faktorial")

    n = st.number_input(
        "Masukkan bilangan bulat",
        min_value=0,
        step=1
    )

    if st.button("Hitung Faktorial"):

        hasil = math.factorial(int(n))

        st.success(f"{int(n)}! = {hasil}")

# =========================
# PERMUTASI & KOMBINASI
# =========================
elif menu == "Permutasi & Kombinasi":

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
        ["Permutasi (nPr)", "Kombinasi (nCr)"]
    )

    if st.button("Hitung Permutasi/Kombinasi"):

        if r > n:
            st.error("Nilai r tidak boleh lebih besar dari n.")
        else:

            if jenis == "Permutasi (nPr)":
                hasil = math.factorial(int(n)) // math.factorial(int(n-r))

                st.success(
                    f"Hasil {int(n)}P{int(r)} = {hasil}"
                )

                st.latex(
                    rf"P(n,r)=\frac{{n!}}{{(n-r)!}}"
                )

            else:
                hasil = math.factorial(int(n)) // (
                    math.factorial(int(r))
                    * math.factorial(int(n-r))
                )

                st.success(
                    f"Hasil {int(n)}C{int(r)} = {hasil}"
                )

                st.latex(
                    rf"C(n,r)=\frac{{n!}}{{r!(n-r)!}}"
                )

# =========================
# PANGKAT & AKAR
# =========================
elif menu == "Pangkat & Akar":

    st.header("📈 Pangkat & Akar")

    pilihan = st.selectbox(
        "Pilih Perhitungan",
        ["Pangkat", "Akar Kuadrat"]
    )

    if pilihan == "Pangkat":

        angka = st.number_input("Masukkan angka")
        pangkat = st.number_input(
            "Masukkan pangkat",
            step=1
        )

        if st.button("Hitung Pangkat"):

            hasil = angka ** pangkat

            st.success(
                f"{angka}^{int(pangkat)} = {hasil}"
            )

    else:

        angka = st.number_input(
            "Masukkan angka positif",
            min_value=0.0
        )

        if st.button("Hitung Akar"):

            hasil = math.sqrt(angka)

            st.success(
                f"√{angka} = {hasil}"
            )

# =========================
# FPB & KPK
# =========================
elif menu == "FPB & KPK":

    st.header("📐 FPB & KPK")

    a = st.number_input(
        "Masukkan bilangan pertama",
        min_value=1,
        step=1
    )

    b = st.number_input(
        "Masukkan bilangan kedua",
        min_value=1,
        step=1
    )

    jenis = st.radio(
        "Pilih Perhitungan",
        ["FPB", "KPK"]
    )

    if st.button("Hitung FPB/KPK"):

        a = int(a)
        b = int(b)

        if jenis == "FPB":

            hasil = math.gcd(a, b)

            st.success(
                f"FPB({a}, {b}) = {hasil}"
            )

        else:

            hasil = abs(a * b) // math.gcd(a, b)

            st.success(
                f"KPK({a}, {b}) = {hasil}"
            )


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
