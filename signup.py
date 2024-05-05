import tkinter as tk
from tkinter import messagebox
import re

def create_account(nom_entry, prenom_entry, email_entry, password_entry):
    nom = nom_entry.get()
    prenom = prenom_entry.get()
    email = email_entry.get()
    password = password_entry.get()


    # Vérification des conditions
    if not nom or not prenom or not email or not password:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
    elif not nom[0].isupper() or not prenom[0].isupper():
        messagebox.showerror("Erreur", "Le nom et le prénom doivent commencer par une majuscule.")
    elif not re.match(r"[^@]+@gmail\.com", email):
        messagebox.showerror("Erreur", "L'email doit être de la forme 'votreadresse@gmail.com'.")
    elif not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
        messagebox.showerror("Erreur", "Le mot de passe doit contenir à la fois des lettres et des chiffres.")
    else:
        messagebox.showinfo("Création de compte", f"Compte créé avec succès pour {prenom} {nom} avec l'email {email}.")

class SignWindow():
    def __init__(self):
        super().__init__()
        

# Créer la fenêtre principale
root = tk.Tk()
root.title("Sign Up")
root.configure(bg="lightblue")
root.geometry("300x350")

# Labels et champs d'entrée pour nom, prénom, email et mot de passe
nom_label = tk.Label(root, text="Nom:", bg="lightblue")
nom_label.pack()
nom_entry = tk.Entry(root)
nom_entry.pack()

prenom_label = tk.Label(root, text="Prénom:", bg="lightblue")
prenom_label.pack()
prenom_entry = tk.Entry(root)
prenom_entry.pack()

email_label = tk.Label(root, text="Email:", bg="lightblue")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

password_label = tk.Label(root, text="Mot de passe:", bg="lightblue")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Bouton pour créer un compte avec un espacement vertical
create_button = tk.Button(root, text="Créer un compte", command=lambda: create_account(nom_entry, prenom_entry, email_entry, password_entry))
create_button.pack(pady=5)  # Ajout d'un espacement vertical

# Exécutez la boucle principale de Tkinter
root.mainloop()
