import streamlit as st

st.title("💖 Detector de Cariño By Exequielito")

st.write("Esto es importante… respondeme con sinceridad 😌")

nombre = st.text_input("¿Cómo te llamás?")
altura = st.number_input("¿Cuánto medís (en metros)?", step=0.01)

if st.button("Descubrir resultado ❤️"):
    if nombre and altura:
        st.write("🔍 Analizando...")
        
        st.success("Resultado final:")
        st.write("El contenedor es menor a la cantidad de cariño 💖")
        st.write(f"{nombre} mide {altura} metros.")
        st.write(f"Por ende, {nombre} mide {altura*100:.0f} cm de pura belleza y ternura, terremoto orgasmico de facha (L) ✨")
        
        st.balloons()
    else:
        st.warning("Tenés que completar todo, si no, no vale  -_- - TRAMPOSA! 😄")
