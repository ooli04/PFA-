import tkinter as tk 
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import messagebox

# Déclaration des variables globales
username_entry = None
password_entry = None

def afficher_image(image_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height))
    photo = ImageTk.PhotoImage(img)
    return photo

def ouvrir_page_login():
    root.destroy()  # Fermer la fenêtre principale
    from login import LoginWindow  # Importez la classe LoginWindow ici
    login_window = LoginWindow()  # Ouvrir la page de connexion
    login_window.mainloop()

def ouvrir_page_signup():
    root.destroy()  # Fermer la fenêtre principale
    from signup import SignWindow  # Importez la classe SignWindow ici
    sign_window = SignWindow()  # Ouvrir la page d'inscription
    sign_window.mainloop()

def ouvrir_page_crud():
    root.destroy()  # Fermer la fenêtre principale
    from crud import CrudWindow  # Importez la classe CrudWindow ici
    crud_window = CrudWindow()  # Ouvrir la page CRUD
    crud_window.mainloop()

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("Page d'accueil")
root.configure(bg="#ADD8E6")  # Bleu clair
# Définir les dimensions de la fenêtre
root.geometry("550x300")

# Titre en rouge centré
label_titre = tk.Label(root, text="Page d'accueil", font=("Helvetica", 16), fg="red", bg="#ADD8E6")  # Bleu clair
label_titre.pack(pady=10)

# Liste des titres et des chemins d'accès aux images
titres = ["Login", "Sign Up", "Reconnaissance Faciale", "CRUD"]
image_paths = ["img/12.png", "img/34.png", "img/4.png", "img/1.png"]

# Définir la taille cible des images
image_width = 100
image_height = 100

# Charger et redimensionner les images
images = [afficher_image(path, image_width, image_height) for path in image_paths]

# Frame pour contenir les boutons
button_frame = tk.Frame(root, bg="#ADD8E6")  # Bleu clair
button_frame.pack(pady=10)

# Création des boutons initiaux
for i, (titre, img) in enumerate(zip(titres, images)):
    if titre == "Login":
        button = tk.Button(button_frame, text=titre, image=img, compound=tk.TOP, command=ouvrir_page_login)
    elif titre == "Sign Up":
        button = tk.Button(button_frame, text=titre, image=img, compound=tk.TOP, command=ouvrir_page_signup)
    elif titre == "CRUD":
        button = tk.Button(button_frame, text=titre, image=img, compound=tk.TOP, command=ouvrir_page_crud)
    else:
        # Pour les autres boutons, vous pouvez ajouter des commandes ou les laisser vides pour l'instant
        button = tk.Button(button_frame, text=titre, image=img, compound=tk.TOP)
    button.grid(row=0, column=i, padx=10, pady=10)

# Exécution de la boucle principale
root.mainloop()
