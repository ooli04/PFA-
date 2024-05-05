import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Vérifiez ici si les informations de connexion sont correctes
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


class LoginWindow():
    def __init__(self):
        super().__init__()
       

# Créer la fenêtre principale
root = tk.Tk()
root.title("Login")
root.configure(bg="lightblue")
root.geometry("400x250")

# Étiquette et champ de saisie pour le nom d'utilisateur
username_label = tk.Label(root, text="Username:", bg="lightblue")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Étiquette et champ de saisie pour le mot de passe
password_label = tk.Label(root, text="Password:", bg="lightblue")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Bouton pour se connecter avec un espacement vertical
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=5)  # Ajout d'un espacement vertical

# Exécutez la boucle principale de Tkinter
root.mainloop()
