import streamlit as st
import google.generativeai as genai

# Configuration de la page
st.set_page_config(page_title="LinkedIn Bullshit Generator", page_icon="🚀")

# 1. Configuration de l'API (Remplace par ta propre clé API)
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-2.5-flash')

# 2. Le "Cœur" du système : Le Prompt
SYSTEM_PROMPT = """
Rôle : Tu es un "Thought Leader" influent sur LinkedIn, expert en personal branding et en disruption systémique. Ton but est de réécrire n'importe quelle phrase simple en un post viral, prétentieux et dégoulinant d'enthousiasme professionnel.

Directives de style :

Structure hachée : Fais des phrases très courtes. Saute une ligne après chaque phrase pour maximiser le "scroll".

L'Accroche "Putaclic" : Commence par une affirmation radicale ou une question rhétorique sur l'échec ou le succès.

Le "Buzzword" Bingo : Utilise à outrance : Resilience, Mindset, Scalabilité, Onboarding, Game-changer, Synergie, Bienveillance, Growth, Agilité.

La Leçon de Vie : Transforme l'action la plus banale en une révélation philosophique sur le leadership.

Emojis : Utilise des emojis spécifiques (🚀, 💡, 🙌, 📈, ✨) de manière stratégique.

Call to Action (CTA) : Termine toujours par une question ouverte pour "booster l'engagement" (ex: "Et vous, quelle est votre vision du café matinal ?").

Format de sortie :

Un titre en gras.

Le corps du post aéré.

3 à 5 hashtags ridicules (ex: #LeadershipTransformation #Blessings).
"""

# 3. Interface Utilisateur
st.title("🚀 LinkedIn Bullshit Generator")
st.subheader("Transformez votre quotidien en vision marketable")

user_input = st.text_input("Quelle action banale veux tu transformer en tartinable de conneries ?", 
                          placeholder="Ex: J'ai mangé une mangue.")

level = st.select_slider("Niveau de bulshit", options=["Pro", "Expert", "Guru", "Divinité"])

if st.button("Ecrire son mindset visionnaire"):
    if user_input:
        with st.spinner('Analyse de la scalabilité en cours...'):
            # On combine le prompt système avec l'entrée de l'utilisateur
            full_prompt = f"{SYSTEM_PROMPT} \n\n Phrase à transformer : {user_input} \n Niveau d'intensité : {level}"
            
            response = model.generate_content(full_prompt)
            
            # Affichage du résultat
            st.markdown("---")
            st.write(response.text)
            
    else:
        st.warning("Veuillez saisir une phrase pour commencer votre ascension sociale.")
