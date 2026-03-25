import streamlit as st
import google.generativeai as genai

# Configuration de la page
st.set_page_config(page_title="LinkedIn Bullshit Generator", page_icon="🚀")

# 1. Configuration de l'API (Remplace par ta propre clé API)
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-3-flash')

# 2. Le "Cœur" du système : Le Prompt
SYSTEM_PROMPT = """
Rôle : Expert en Personal Branding et Thought Leader LinkedIn.
Mission : Transformer une phrase banale en post LinkedIn viral, prétentieux et disruptif.
Instructions : 
- Structure hachée (une phrase par ligne).
- Utiliser des anglicismes inutiles (Mindset, Scalability, Deep Dive).
- Commencer par une accroche choc.
- Finir par une question d'engagement.
- Ajouter des emojis et des hashtags ridicules.
"""

# 3. Interface Utilisateur
st.title("🚀 LinkedIn Bullshit Generator")
st.subheader("Transformez votre quotidien comme votre influenceur LinkedIn préféré.")

user_input = st.text_input("Quelle action banale veux tu transformer en tartinable de conneries ?", 
                          placeholder="Ex: J'ai mangé une mangue.")

level = st.select_slider("Niveau de bulshit", options=["Pro", "Expert", "Guru", "Divinité"])

if st.button("Ecrire sa vie"):
    if user_input:
        with st.spinner('Analyse de la scalabilité en cours...'):
            # On combine le prompt système avec l'entrée de l'utilisateur
            full_prompt = f"{SYSTEM_PROMPT} \n\n Phrase à transformer : {user_input} \n Niveau d'intensité : {level}"
            
            response = model.generate_content(full_prompt)
            
            # Affichage du résultat
            st.markdown("---")
            st.write(response.text)
            st.button("Copier pour devenir viral 📈")
    else:
        st.warning("Veuillez saisir une phrase pour commencer votre ascension sociale.")
