import customtkinter as ctk
import tkinter as tk
import classe
import etudiant


class Fen_noteManager(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        self.geometry("1000x600")

        frame_nav = ctk.CTkFrame(self, height=90, fg_color="#000000", corner_radius=0)
        frame_nav.pack(fill="x", side=tk.TOP)




        frame_menu = ctk.CTkFrame(self, fg_color="#000000", corner_radius=0)
        frame_menu.pack(side = tk.LEFT, fill="y")

        # fenetres



        self.acceuil = Fen_acceuil(self)
        self.classe =classe.FenClasse(self)
        self.etudiant =  etudiant.FenEtudiant(self)

        self.acceuil.pack(fill=tk.BOTH, expand=True)

        #rajout des bouttons
        btn_etudiant = ctk.CTkButton(frame_menu, text="Acceuil", command=self.afficher_acceuil)
        btn_etudiant.pack(padx=20, pady=10) 

        btn_etudiant = ctk.CTkButton(frame_menu, text="Etudiant", command=self.afficher_etudiant)
        btn_etudiant.pack(padx=20, pady=10)    

        btn_classe = ctk.CTkButton(frame_menu, text="Classe", command=self.afficher_classe)
        btn_classe.pack(padx=20, pady=10) 


    def afficher_acceuil(self):
        self.etudiant.pack_forget()
        self.classe.pack_forget()
        self.acceuil.pack(fill=tk.BOTH, expand=True)


    def afficher_etudiant(self):
        
        self.acceuil.pack_forget()
        self.classe.pack_forget()
        self.etudiant.pack(fill=tk.BOTH, expand=True)


    def afficher_classe(self):
        self.acceuil.pack_forget()
        self.etudiant.pack_forget()
        self.classe.pack(fill=tk.BOTH, expand=True)


class Fen_acceuil(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        

        lbl_titre = ctk.CTkLabel(self, text="BIENVENUE", font=("AREAL BLACK", 50, "bold"), fg_color="transparent")
        lbl_titre.place(relx=0.5, rely=0.5, anchor=tk.CENTER)














noteManager = Fen_noteManager()
noteManager.mainloop()