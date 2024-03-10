import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import etudiant_model

class FenEtudiant(ctk.CTkFrame):
    """
        __class : InterfaceEtudiant
        __description : InterfaceEtudiant herite de ctk.CTkFrame
        __champs :
        __mathodes :
    """

    def __init__(self,master):

        super().__init__(master)
        self._corner_radius=0
        
        self.etudiant_model = etudiant_model.Etudiant()

        # creation de l'entete
        frame_entete = ctk.CTkFrame(self, height=50, corner_radius=0)

        
        # creation du titre
        lbl_titre = ctk.CTkLabel(frame_entete, text="LISTES ETUDIANTS", fg_color="transparent", font=('AREAL BLACK', 20, "bold"))
        lbl_titre.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


        frame_entete.pack(side = tk.TOP, fill="x")

         

        # creation de la zone des boutons
        frame_buttons = ctk.CTkFrame(self, corner_radius=0)

        # creation des bouttons
        btn_ajouter = ctk.CTkButton(frame_buttons, text="Ajouter")
        btn_ajouter.pack()

        btn_modifier = ctk.CTkButton(frame_buttons, text="modifier")
        btn_modifier.pack(padx=20, pady=5)

        btn_supprimer = ctk.CTkButton(frame_buttons, text="Spprimer")
        btn_supprimer.pack()

        btn_imprimer = ctk.CTkButton(frame_buttons, text="Imprimer")
        btn_imprimer.pack(padx=20, pady=5)


        frame_buttons.pack(side = tk.RIGHT, fill="y")




        # creation du body
        frame_corps = ctk.CTkFrame(self, corner_radius=0)

        self.tab_etudiant = ttk.Treeview(frame_corps , columns=("identifiant",
                                                           "nom",
                                                           "prenom",
                                                           "sexe",
                                                           "email",
                                                           "adresse",
                                                           "classe"))
        # formater les colonnes
        self.tab_etudiant.column("#0", width=0, stretch=tk.NO)
        self.tab_etudiant.column("#1", stretch=tk.NO, width=0)
        self.tab_etudiant.column("nom", anchor=tk.W, width=50)
        self.tab_etudiant.column("prenom", anchor=tk.W, width=50)
        self.tab_etudiant.column("sexe", anchor=tk.CENTER, width=10)
        self.tab_etudiant.column("email", anchor=tk.W, width=50)
        self.tab_etudiant.column("adresse", anchor=tk.W, width=50)
        self.tab_etudiant.column("classe", anchor=tk.W, width=50)


        # afficher les entetes
        self.tab_etudiant.heading("identifiant", text="id_etudiant")
        self.tab_etudiant.heading("nom", text="nom")
        self.tab_etudiant.heading("prenom", text="prenom")
        self.tab_etudiant.heading("sexe", text="sexe")
        self.tab_etudiant.heading("email", text="email")
        self.tab_etudiant.heading("adresse", text="adresse")
        self.tab_etudiant.heading("classe", text="id_classe")

        self.recuperer_tous_etudiants()

        # ajouter les valeurs
        #self.tab_etudiant.insert("", tk.END,"1", values=(1,"OLALA","raz", "M","olala@gmail.com", "kombo", 2))


        self.tab_etudiant.pack(fill=tk.BOTH, expand=True)

        frame_corps.pack( fill="both", expand=True)


    def recuperer_tous_etudiants(self):
        
        etudiants = self.etudiant_model.recuperer_tous_les_etudiants()
        if etudiants:
            i = 1
            for etudiant in etudiants :
                self.tab_etudiant.insert("", tk.END,str(i), values=etudiant)
                i+=1


    def ajouter_etudiant(self):
        pass

    def modifier_etudiant(self):
        pass

    def supprimer_etudiant(self):
        pass

    def imprimer_etudiant(self):
        pass            










if __name__=="__main__":
    root = ctk.CTk()
    root.geometry("1000x600")
    frame = FenEtudiant(root)
    frame.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
