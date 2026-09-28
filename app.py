import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Ensaio do Mágico de Oz - Espantalho", page_icon="🌾", layout="centered"
)

# Base de dados com as falas do Espantalho extraídas do roteiro
# (Você pode adicionar quantas cenas quiser aqui!)
cenas_espantalho = [
    {
        "id": 1,
        "cena": "Cena 4 - O Encontro com o Espantalho",
        "personagem_deixa": "Dorothy",
        "deixa": (
            "Ora, você disse alguma coisa, não foi? Você está fazendo isso de"
            " propósito ou não consegue se decidir?"
        ),
        "fala_espantalho": (
            "Não tenho cérebro, só palha. Então não estou pensando em me"
            " decidir."
        ),
    },
    {
        "id": 2,
        "cena": "Cena 4 - O Encontro com o Espantalho",
        "personagem_deixa": "Dorothy",
        "deixa": "Bem, como você pode falar se não tem cérebro?",
        "fala_espantalho": (
            "Não sei, mas algumas pessoas sem cérebro falam muito não é?"
        ),
    },
    {
        "id": 3,
        "cena": "Cena 4 - O Encontro com o Espantalho",
        "personagem_deixa": "Dorothy",
        "deixa": "Tem como eu te ajudar?",
        "fala_espantalho": (
            "Bem, é claro, não sou muito inteligente, mas se você dobrar o"
            " prego pra trás talvez eu escorregue."
        ),
    },
    {
        "id": 4,
        "cena": "Cena 4 - O Encontro com o Espantalho",
        "personagem_deixa": "Dorothy",
        "deixa": "Onde fica esse tal de Kansas?",
        "fala_espantalho": (
            "É lá que eu moro, e estou indo para a cidade das esmeraldas pedir"
            " ajuda para o mágico de Oz para poder voltar para casa."
        ),  # Nota: Ajustável conforme o fluxo da cena
    },
]

# Título do Aplicativo
st.title("🌾 Ensaio Interativo: O Espantalho")
st.markdown(
    "Bem-vindo ao assistente de ensaio do Rafael! Selecione a fala abaixo,"
    " ouça a deixa e pratique o seu texto."
)

# Sidebar para escolha da cena/fala
st.sidebar.header("Navegação de Cenas")
escolha_indice = st.sidebar.selectbox(
    "Escolha a fala:",
    options=range(len(cenas_espantalho)),
    format_func=lambda x: (
        f"{cenas_espantalho[x]['cena']} (Fala {x+1})"
    ),
)

cena_atual = cenas_espantalho[escolha_indice]

# Exibição principal da cena
st.subheader(cena_atual["cena"])

st.markdown("---")

# Bloco da Deixa (Outro personagem / App)
st.markdown(
    f"🗣️ **Deixa ({cena_atual['personagem_deixa']}):**"
    f" *\"{cena_atual['deixa']}\"*"
)

# Botão para simular a fala do app em voz alta (Text-to-Speech)
if st.button("🔊 Ouvir Deixa"):
    # Aqui podemos integrar a API de Text-to-Speech do Google futuramente
    st.info(
        "*(Simulando áudio da deixa)*: " + cena_atual["deixa"]
    )

st.markdown("---")

# Bloco da Resposta do Espantalho (Rafael)
st.markdown("🌾 **Sua vez (Espantalho):**")
st.markdown(f"> *{cena_atual['fala_espantalho']}*")

# Área de interação por voz ou texto para o Rafael testar
modo_teste = st.radio(
    "Como deseja ensaiar esta fala?",
    ["Praticar Falando (Microfone)", "Digitar / Conferir Texto"],
)

if modo_teste == "Praticar Falando (Microfone)":
    st.warning(
        "🎙️ O componente de gravação de voz será ativado aqui para comparar"
        " sua fala com o roteiro usando a IA do Gemini."
    )
    # Placeholder para o componente de áudio do Streamlit
    audio_gravado = st.audio_input("Grave sua fala como Espantalho:")
    if audio_gravado:
        st.success(
        "Áudio capturado! Analisando entonação e precisão da fala..."
        )
        # Aqui entraremos com a chamada para a API do Gemini processar o áudio

else:
    fala_usuario = st.text_input("Digite sua fala para testar:")
    if st.button("Validar Fala"):
        if (
            fala_usuario.strip().lower()
            == cena_atual["fala_espantalho"].strip().lower()
        ):
            st.success("🎉 Perfeito, Rafael! A fala está exata.")
        else:
            st.error(
                "❌ Quase lá! Confira o texto original: "
                f"_{cena_atual['fala_espantalho']}_"
            )
