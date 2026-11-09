import streamlit as st
from chatbot import mensagem_da_ia


st.markdown(
    """
    <h1 style="text-align: center;">ChatBot IA</h1>
    <h3 style="text-align: center;">Como posso ajudar você hoje?</h3>
    """,
    unsafe_allow_html=True
)
st.write(
    "Sou um assistente de inteligência artificial feito com Python, a base do modelo Gemini Flash Lite Latest.",
    "Posso ajudar com estudos, programação e muito mais!"
)
with st.container(border=True):
    st.write("## Ideias de perguntas:")
    col1, col2 = st.columns(2)

    with col1:
        st.info("Crie um programa em C++ para arduino para acender 5 leds")
        st.info("Me ensine o básico do Python.")

    with col2:
        st.info("Me ajude a criar um plano de estudos de matemática avançada.")
        st.info("Quais são as melhores faculdades da America Latina?")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []


for mensagem in st.session_state["lista_mensagens"]:
    quem_enviou = mensagem["role"]
    texto_mensagem = mensagem["content"]
    st.chat_message(quem_enviou).write(texto_mensagem)

mensagem_usuario = st.chat_input("Escreva sua menssgaem aqui.")


if mensagem_usuario:
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    try:
        with st.spinner("A IA está pensando..."):
            resposta_ia = mensagem_da_ia(
            st.session_state["lista_mensagens"]
        )

    except Exception:
        st.error("Não foi possível obter uma resposta da IA.")
        st.stop()

    with st.spinner("A IA está pensando..."):
        resposta_ia = mensagem_da_ia(
        st.session_state["lista_mensagens"]
    )

    st.chat_message("assistant").write(resposta_ia)
    mensagem2 = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem2)


