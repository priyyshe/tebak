import streamlit as st

st.set_page_config(page_title="Tebak Apriyanti", page_icon=":tada:", layout="centered")
st.title("Tebak Siapa Apriyanti? :tada:")
st.image("https://i.pinimg.com/736x/4d/55/13/4d551349a06c0f47da8141a2114d5419.jpg", width=300)
st.write("Emang tau siapa apri? wkwkwk!")

# Inisialisasi skor
score = {
    "Bole la": 0,
    "Salah kocak": 0,
    "Cie bener": 0
}

# Pertanyaan 1
q1 = st.radio("1. Siapa nama kucing apri?", ["manyinyo", "spiderman", "upin"])
if q1 == "manyinyo":
    score["Cie bener"] += 1
elif q1 == "spiderman":
    score["Salah kocak"] += 1
elif q1 == "upin":
    score["Bole la"] += 1
    
if st.button("🎯 Lihat Hasil"):
    if q1:
        hasil = max(score, key=score.get)
        st.success(f"✅ Kamu cocok jadi: **{hasil}**!")
        st.balloons()
        
        # Tampilkan gambar dan penjelasan SESUAI hasil
        if hasil == "Cie bener":
            st.image("https://i.pinimg.com/736x/d8/8d/61/d88d61e44ac46002f95110c684606c85.jpg", width=300)
            st.write("Tau dari mana? wkwk")
        elif hasil == "Salah kocak":
            st.image("https://i.pinimg.com/736x/35/e7/96/35e796fb1b50c718f516a184b4bbb947.jpg", width=300)
            st.write("Salah kocak, coba lagi!")
        elif hasil == "Bole la":
            st.image("https://i.pinimg.com/736x/8f/a1/31/8fa131367020ed5b94a1273e378df9be.jpg", width=300)
            st.write("Bole la, tapi coba lagi!")
        else:
            st.warning("⚠️ Harap jawab semua pertanyaan dulu.")
