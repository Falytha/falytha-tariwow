import streamlit as st

st.title("🎈Falytha TariwOw")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.image("IMG_0942.jpeg", width=400)
st.image("IMG_6916.jpeg", width=500)
st.write("\n")
st.subheader("lestari(kan bumi)")
st.write("Mari bersatu menjadi avenger")
st.write(
    """
    - captain ameridut >in pict
    - iron mancila >in pict
    - sapiderbalabalaba >anomali
    - wonder wokakamari >anomali
    - badboboiboy
    """
)
st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
