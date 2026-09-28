from google import genai
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Ensaio do Mágico de Oz - Espantalho", page_icon="🌾", layout="centered"
)

# Base de dados expandida com todas as principais cenas e falas do Espantalho
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
        "deixa": (
            "É lá que eu moro, e estou indo para a cidade das esmeraldas pedir"
            " ajuda para o mágico de Oz para poder voltar para casa."
        ),
        "fala_espantalho": "Cê vai falar com o mágico?",
    },
    {
        "id": 5,
        "cena": "Cena 4 - O Encontro com o Espantalho",
        "personagem_deixa": "Dorothy",
        "deixa": "Aham",
        "fala_espantalho": (
            "E você acha que se eu for com ocê esse tal de mágico arruma um"
            " cérebro pra mim?"
        ),
    },
    {
        "id": 6,
        "cena": "Cena 4 - O Encontro com o Espantalho",
        "personagem_deixa": "Dorothy",
        "deixa": (
            "Eu acho que sim! O problema é que tem uma bruxa que tá uma fera"
            " comigo e pode acabar sobrando pra você."
        ),
        "fala_espantalho": (
            "Uma bruxa que tá uma fera com você? Eu não tenho medo de bruxa nem"
            " de fera, a única coisa que tenho medo mesmo é fósforo aceso!"
        ),
    },
    {
        "id": 7,
        "cena": "Cena 4 - O Encontro com o Espantalho",
        "personagem_deixa": "Dorothy",
        "deixa": "Mas e ai menina, você acha que pode me levar com ocê?",
        "fala_espantalho": "Mas é claro que eu posso!",
    },
    {
        "id": 8,
        "cena": "Cena 5 - O Homem de Lata e as Maçãs",
        "personagem_deixa": "Dorothy",
        "deixa": "Todos os seres vivos precisam comer.",
        "fala_espantalho": "Eu não preciso comer. Isso significa que não estou vivo?",
    },
    {
        "id": 9,
        "cena": "Cena 5 - O Homem de Lata e as Maçãs",
        "personagem_deixa": "Dorothy",
        "deixa": "Ah, não, Espantalho. Você é o amigo mais animado que já tive.",
        "fala_espantalho": "Ah obrigado!",
    },
    {
        "id": 10,
        "cena": "Cena 5 - O Homem de Lata e as Maçãs",
        "personagem_deixa": "Dorothy",
        "deixa": "Nas árvores.",
        "fala_espantalho": (
            "Você quer dizer, todos aqueles passarinhos vermelhos pendurados de"
            " cabeça para baixo por uma perna?"
        ),
    },
    {
        "id": 11,
        "cena": "Cena 5 - O Homem de Lata e as Maçãs",
        "personagem_deixa": "Primeira Árvore / Dorothy",
        "deixa": (
            "Desculpe! Sempre esqueço que não estou no Kansas. (Árvores"
            " reclamam de vermes)"
        ),
        "fala_espantalho": (
            "Vou te mostrar como conseguir maçãs. Claro que você tem minhocas."
            " Minhocas, lagartas e provavelmente um monte de piolhos também."
        ),
    },
    {
        "id": 12,
        "cena": "Cena 5 - O Homem de Lata (Encontro)",
        "personagem_deixa": "Homem de Lata",
        "deixa": "Claro. Veja Dorothy, se eu tivesse um cérebro...",
        "fala_espantalho": "Eu não quero ouvir isso!",
    },
    {
        "id": 13,
        "cena": "Cena 6 - O Leão Covarde",
        "personagem_deixa": "Dorothy",
        "deixa": "Você acha que encontraremos algum animal selvagem?",
        "fala_espantalho": (
            "Claro, não são muito inteligente, mas acho que vai escurecer antes"
            " de clarear."
        ),
    },
    {
        "id": 14,
        "cena": "Cena 6 - O Leão Covarde",
        "personagem_deixa": "Homem de Lata",
        "deixa": "Alguns mas principalmente leões, tigres e ursos.",
        "fala_espantalho": "E tigres!",
    },
    {
        "id": 15,
        "cena": "Cena 6 - O Leão Covarde",
        "personagem_deixa": "Homem de Lata",
        "deixa": "Levante as mãos, seu saco de feno torto!",
        "fala_espantalho": "Isso está ficando pessoal, Leão.",
    },
    {
        "id": 16,
        "cena": "Cena 6 - O Leão Covarde",
        "personagem_deixa": "Homem de Lata",
        "deixa": "Vai espantalho dá uma lição nele!",
        "fala_espantalho": "Eu não, vai você.",
    },
    {
        "id": 17,
        "cena": "Cena 6 - O Leão Covarde",
        "personagem_deixa": "Homem de Lata",
        "deixa": "Para conseguir um coração para ele",
        "fala_espantalho": "E para ele um cérebro",
    },
    {
        "id": 18,
        "cena": "Cena 7 - As Papoulas",
        "personagem_deixa": "Dorothy",
        "deixa": "Esta estrada de tijolos amarelos parece durar para sempre.",
        "fala_espantalho": (
            "Se você está cansada, Dorothy, podemos pegar um atalho."
        ),
    },
    {
        "id": 19,
        "cena": "Cena 7 - As Papoulas",
        "personagem_deixa": "Dorothy / Homem de Lata",
        "deixa": "É a Bruxa Má! O quê faremos? Ajuda! Ajuda!",
        "fala_espantalho": (
            "Não adianta gritar numa hora dessas. Ninguém vai ouvir você!"
            " Ajuda! Ajuda! Ajuda!"
        ),
    },
    {
        "id": 20,
        "cena": "Cena 8 - Portões da Cidade das Esmeraldas",
        "personagem_deixa": "Guarda 2",
        "deixa": "O aviso! Esse na porta, nítido como o nariz na minha cara",
        "fala_espantalho": "Ler o quê?",
    },
    {
        "id": 21,
        "cena": "Cena 11 - Floresta Assombrada",
        "personagem_deixa": "Leão",
        "deixa": "Alguém sabe onde algum de nós está?",
        "fala_espantalho": "Passamos por um aviso há algum tempo.",
    },
    {
        "id": 22,
        "cena": "Cena 13 - O Resgate no Castelo",
        "personagem_deixa": "Dorothy",
        "deixa": "Sim estou bem, mas a Bruxa me trancou!",
        "fala_espantalho": "Depressa, não temos tempo a perder!",
    },
    {
        "id": 23,
        "cena": "Cena 14 - A Farsa do Mágico",
        "personagem_deixa": "Homem de Lata",
        "deixa": "E o coração que você prometeu para o Homem de Lata?",
        "fala_espantalho": "E o cérebro do Espantalho?",
    },
    {
        "id": 24,
        "cena": "Cena 15 - Despedida",
        "personagem_deixa": "Dorothy",
        "deixa": (
            "Querido Espantalho, você foi meu primeiro amigo aqui. Sentirei"
            " muita saudade."
        ),
        "fala_espantalho": (
            "Ter um cérebro não torna a separação mais fácil. Adeus Dorothy!"
        ),
    },
]

# Inicializa o cliente do Gemini usando os Secrets do Streamlit
# (Você configurará a chave GEMINI_API_KEY nas configurações do app no Streamlit Cloud)
try:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    client = None

if "indice_atual" not in st.session_state:
    st.session_state.indice_atual = 0

# Título do Aplicativo
st.title("🌾 Ensaio por Voz com Gemini: O Espantalho")
st.markdown(
    "Ouça a deixa, grave sua fala e deixe o Gemini avaliar sua interpretação!"
)

# Sidebar para escolha manual
st.sidebar.header("Navegação de Cenas")
escolha_indice = st.sidebar.selectbox(
    "Ir diretamente para a fala:",
    options=range(len(cenas_espantalho)),
    index=st.session_state.indice_atual,
    format_func=lambda x: (
        f"{cenas_espantalho[x]['cena']} (Fala {x+1})"
    ),
)

if escolha_indice != st.session_state.indice_atual:
    st.session_state.indice_atual = escolha_indice
    st.rerun()

cena_atual = cenas_espantalho[st.session_state.indice_atual]

# Exibição principal da cena
st.subheader(
    f"{cena_atual['cena']} (Fala {st.session_state.indice_atual + 1} de"
    f" {len(cenas_espantalho)})"
)
st.markdown("---")

# Bloco da Deixa
st.markdown(
    f"🗣️ **Deixa ({cena_atual['personagem_deixa']}):**"
    f" *\"{cena_atual['deixa']}\"*"
)

if st.button("🔊 Ouvir Deixa"):
    st.info(f'*(Simulando áudio da deixa)*: "{cena_atual["deixa"]}"')

st.markdown("---")

# Bloco de Referência do Espantalho
st.markdown("🌾 **Texto original da sua fala (Espantalho):**")
st.info(f"_{cena_atual['fala_espantalho']}_")

# Gravador de voz limpo por cena
audio_gravado = st.audio_input(
    "Grave sua fala como Espantalho:",
    key=f"gravador_cena_{cena_atual['id']}",
)

if audio_gravado:
    if client is None:
        st.error(
            "⚠️ Chave GEMINI_API_KEY não configurada nos Secrets do Streamlit."
        )
    else:
        with st.spinner(
            "🤖 O Gemini está a ouvir e a analisar a sua atuação..."
        ):
            try:
                # Salva o áudio temporariamente para enviar ao Gemini
                audio_bytes = audio_gravado.read()
                audio_file_path = "temp_audio.wav"
                with open(audio_file_path, "wb") as f:
                    f.write(audio_bytes)

                # Faz upload do áudio para a API do Gemini
                audio_ref = client.files.upload(file=audio_file_path)

                # Prompt avaliador
                prompt = (
                    "Você é um diretor de teatro avaliador. A fala esperada do"
                    f" ator (que interpreta o Espantalho) é: '{cena_atual['fala_espantalho']}'."
                    " Ouça atentamente o áudio enviado, transcreva o que o ator"
                    " disse e avalie se ele acertou a fala de forma correta"
                    " (permitindo pequenas variações naturais de dicção)."
                    " Responda em Português de Portugal/Brasil de forma curta e"
                    " encorajadora, indicando se a fala foi correta ou se"
                    " precisa de ajuste."
                )

                response = client.models.generate_content(
                    model="gemini-3.8-flash", contents=[audio_ref, prompt]
                )

                st.success("✨ Análise do Diretor (Gemini):")
                st.write(response.text)
                st.balloons()

            except Exception as e:
                st.error(f"Erro ao processar o áudio com o Gemini: {e}")

    # Botão para avançar para a próxima fala
    if st.session_state.indice_atual < len(cenas_espantalho) - 1:
        if st.button("Próxima Fala ➡️", type="primary"):
            st.session_state.indice_atual += 1
            st.rerun()
    else:
        st.success("🎉 Parabéns! Você concluiu todas as falas do Espantalho!")
