import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def ouvrir_page_login():
    messagebox.showinfo("Info", "Page de connexion")

def ouvrir_page_signup():
    messagebox.showinfo("Info", "Page d'inscription")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Page principale")

# Définition de la couleur de fond de la fenêtre
root.configure(bg="lightblue")

# Définition de la géométrie de la fenêtre
window_width = 400
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Titre en haut de la fenêtre
label_titre = tk.Label(root, text="Bienvenue", font=("Helvetica", 16), bg="lightblue")
label_titre.place(relx=0.5, rely=0.3, anchor="center")  # Centrer horizontalement

# Charger les images
image_login = Image.open("img/12.png")  # Assurez-vous que le fichier "12.png" existe dans le même répertoire que votre script
image_signup = Image.open("img/34.png")  # Assurez-vous que le fichier "34.png" existe dans le même répertoire que votre script

# Redimensionner les images si nécessaire
image_login = image_login.resize((100, 100), Image.ANTIALIAS)
image_signup = image_signup.resize((100, 100), Image.ANTIALIAS)

# Convertir les images en format compatible avec Tkinter
photo_login = ImageTk.PhotoImage(image_login)
photo_signup = ImageTk.PhotoImage(image_signup)

# Frame pour contenir les boutons
button_frame = tk.Frame(root, bg="lightblue")  # Mettre la même couleur que le fond de la fenêtre
button_frame.place(relx=0.5, rely=0.5, anchor="center")

# Bouton "Login" avec image
button_login = tk.Button(button_frame, text="Login", image=photo_login, command=ouvrir_page_login, compound=tk.TOP)
button_login.grid(row=0, column=0, padx=5)

# Bouton "Sign Up" avec image
button_signup = tk.Button(button_frame, text="Sign Up", image=photo_signup, command=ouvrir_page_signup, compound=tk.TOP)
button_signup.grid(row=0, column=1, padx=5)

# Exécution de la boucle principale
root.mainloop()
