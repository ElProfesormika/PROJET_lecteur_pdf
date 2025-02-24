import PyPDF2
import pyttsx3
import tkinter as tk
from tkinter import filedialog

# Fonction pour lire un fichier PDF et le convertir en audio
def pdf_to_audio(pdf_file):
    # Initialiser le moteur de synthèse vocale
    engine = pyttsx3.init()
    
    # Ouvrir le fichier PDF en mode lecture binaire
    with open(pdf_file, 'rb') as file:
        # Créer un lecteur PDF
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        
        # Extraire et lire le texte de chaque page
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            if text:  # Vérifier si du texte est présent sur la page
                engine.say(text)  # Lire le texte avec la voix
                engine.runAndWait()  # Exécuter la commande

# Fonction pour ouvrir la boîte de dialogue de sélection de fichier
def select_pdf():
    # Ouvrir une boîte de dialogue pour choisir le fichier PDF
    pdf_file = filedialog.askopenfilename(
        title="Choisissez un fichier PDF", 
        filetypes=[("PDF Files", "*.pdf")]
    )
    if pdf_file:
        pdf_to_audio(pdf_file)  # Lancer la conversion du PDF en audio

# Interface graphique pour sélectionner un fichier PDF
def create_gui():
    # Création de la fenêtre principale
    window = tk.Tk()
    window.title("Lecteur PDF en Audio")

    # Titre dans la fenêtre
    label = tk.Label(window, text="Cliquez ci-dessous pour choisir un fichier PDF", font=('Arial', 14))
    label.pack(pady=20)

    # Bouton pour choisir un fichier PDF
    select_button = tk.Button(window, text="Choisir un PDF", command=select_pdf, font=('Arial', 12), bg="blue", fg="white")
    select_button.pack(pady=10)

    # Lancer l'interface graphique
    window.mainloop()

# Lancer l'interface graphique
create_gui()
