import tkinter as tk
from tkinter import messagebox
import sqlite3

# Fonction pour créer une nouvelle base de données et une table d'employés si elles n'existent pas
def create_database():
    conn = sqlite3.connect("employees.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employees (
                 id INTEGER PRIMARY KEY,
                 nom TEXT NOT NULL,
                 prenom TEXT NOT NULL,
                 email TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Fonction pour ajouter un nouvel employé
def ajouter_employe(nom, prenom, email):
    conn = sqlite3.connect("employees.db")
    c = conn.cursor()
    c.execute("INSERT INTO employees (nom, prenom, email) VALUES (?, ?, ?)", (nom, prenom, email))
    conn.commit()
    conn.close()

# Fonction pour afficher tous les employés dans une zone de texte
def afficher_employes():
    conn = sqlite3.connect("employees.db")
    c = conn.cursor()
    c.execute("SELECT * FROM employees")
    rows = c.fetchall()
    employee_list.delete(1.0, tk.END)  # Effacer le contenu précédent
    for row in rows:
        employee_list.insert(tk.END, f"{row[0]} - {row[1]} {row[2]} ({row[3]})\n")
    conn.close()

# Fonction pour modifier les détails d'un employé
def modifier_employe(id, nom, prenom, email):
    conn = sqlite3.connect("employees.db")
    c = conn.cursor()
    c.execute("UPDATE employees SET nom=?, prenom=?, email=? WHERE id=?", (nom, prenom, email, id))
    conn.commit()
    conn.close()

# Fonction pour supprimer un employé
def supprimer_employe(id):
    conn = sqlite3.connect("employees.db")
    c = conn.cursor()
    c.execute("DELETE FROM employees WHERE id=?", (id,))
    conn.commit()
    conn.close()

import re

def ajouter_employe_handler():
    nom = nom_entry.get()
    prenom = prenom_entry.get()
    email = email_entry.get()




    # Vérifier si le nom et le prénom sont en majuscules
    if not nom.isupper() or not prenom.isupper():
        messagebox.showerror("Erreur", "Le nom et le prénom doivent être en majuscules.")
        return

    # Vérifier si l'email contient "@gmail.com"
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email) or "@gmail.com" not in email:
        messagebox.showerror("Erreur", "L'email doit être une adresse Gmail valide.")
        return

    # Ajouter l'employé
    if nom and prenom and email:
        ajouter_employe(nom, prenom, email)
        afficher_employes()
        messagebox.showinfo("Success", "Employee ajouté avec succès.")
    else:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
# Fonction pour gérer la modification d'un employé par ID
def modifier_employe_par_id():
    id = id_entry.get()
    nom = nom_entry.get()
    prenom = prenom_entry.get()
    email = email_entry.get()
    
    # Vérifier si tous les champs sont remplis
    if id and nom and prenom and email:
        # Mettre à jour les informations de l'employé dans la base de données
        modifier_employe(id, nom, prenom, email)
        
        # Actualiser la liste des employés affichée dans la zone de texte
        afficher_employes()
        
        # Afficher un message de confirmation
        messagebox.showinfo("Success", "Employee modifié avec succès.")
    else:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

# Fonction pour gérer la suppression d'un employé par ID
def supprimer_employe_par_id():
    id = id_entry.get()
    
    # Vérifier si l'ID est rempli
    if id:
        # Supprimer l'employé de la base de données par ID
        supprimer_employe(id)
        
        # Actualiser la liste des employés affichée dans la zone de texte
        afficher_employes()
        
        # Afficher un message de confirmation
        messagebox.showinfo("Success", "Employee supprimé avec succès.")
    else:
        messagebox.showerror("Erreur", "Veuillez entrer l'ID de l'employé.")
                             
# Créer la base de données si elle n'existe pas
create_database()

#class 
class CrudWindow():
    def __init__(self):
        super().__init__()
        

# Créer la fenêtre principale
root = tk.Tk()
root.title("Gestion des Employés")
root.configure(bg="lightblue")# Créer et placer les étiquettes et les champs d'entrée
# Créer et placer les étiquettes et les champs d'entrée pour l'ID
id_label = tk.Label(root, text="ID:")
id_label.grid(row=7, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=7, column=1)

nom_label = tk.Label(root, text="Nom:")
nom_label.grid(row=0, column=0)
nom_entry = tk.Entry(root)
nom_entry.grid(row=0, column=1)

prenom_label = tk.Label(root, text="Prénom:")
prenom_label.grid(row=1, column=0)
prenom_entry = tk.Entry(root)
prenom_entry.grid(row=1, column=1)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)


# Boutons pour les opérations CRUD
ajouter_button = tk.Button(root, text="Ajouter Employé", command=ajouter_employe_handler)
ajouter_button.grid(row=3, column=0, pady=5)

modifier_button = tk.Button(root, text="Modifier Employé", command=modifier_employe_par_id)
modifier_button.grid(row=3, column=1, pady=5)

supprimer_button = tk.Button(root, text="Supprimer Employé", command=supprimer_employe_par_id)
supprimer_button.grid(row=4, column=0, columnspan=2, pady=5)

# Zone de texte pour afficher la liste des employés
employee_list = tk.Text(root, height=10, width=40)
employee_list.grid(row=6, column=0, columnspan=2, pady=10)

# Afficher la liste des employés au démarrage de l'application
afficher_employes()

# Exécuter la boucle principale de Tkinter
root.mainloop()
