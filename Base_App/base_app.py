import streamlit as st
# Aufgabe 1
#TODO Nutze st. title() für Titel und st.write()Beschreibung
st.title("Meine App")
st.write("Meine app macht...")
# Aufgabe 2
#TODO Eingabe für die Eissorte
auswahl = st.text_input("Was möchtest du bewerten?")
    
#TODO Slider für Bewertung
bewertung = st.slider("Bewertung", 1, 5)

# Aufgabe 3
#TODO Button zum Absenden und Anzeigen der Bewertung
if st.button("Absenden"):
    st.write(f"Du hast {auswahl} mit {bewertung}/5 Punkten bewertet!")
    
