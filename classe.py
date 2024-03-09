import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import connexion

class FenClasse(ctk.CTkFrame):
    """
        __class : InterfaceEtudiant
        __description : InterfaceEtudiant herite de ctk.CTkFrame
        __champs :
        __mathodes :
    """

    def __init__(self,master):

        super().__init__(master)
        self._corner_radius=0

        # creation de l'entete
        frame_entete = ctk.CTkFrame(self, height=50, corner_radius=0)

        
        # creation du titre
        lbl_titre = ctk.CTkLabel(frame_entete, text="FORMULAIRE CLASSE", fg_color="transparent", font=('AREAL BLACK', 20, "bold"))
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

        self.tab_classe = ttk.Treeview(frame_corps , columns=("identifiant","nom",))
        # formater les colonnes
        self.tab_classe.column("#0", width=0, stretch=tk.NO)
        self.tab_classe.column("identifiant", anchor=tk.CENTER, width=10)
        self.tab_classe.column("nom", anchor=tk.CENTER, width=10)
        


        # afficher les entetes
        self.tab_classe.heading("identifiant", text="id_classe")
        self.tab_classe.heading("nom", text="nom")
        

        self.recuperer_toutes_classes()

        # ajouter les valeurs
        #self.tab_etudiant.insert("", tk.END,"1", values=(1,"OLALA","raz", "M","olala@gmail.com", "kombo", 2))


        self.tab_classe.pack(fill=tk.BOTH, expand=True)

        frame_corps.pack( fill="both", expand=True)


    def recuperer_toutes_classes(self):
        
        classes = connexion.recuperer_toutes_les_classes()
        if classes:
            i = 1
            for classe in classes :
                self.tab_classe.insert("", tk.END,str(i), values=classe)
                i+=1


    def ajouter_classe(self):
        pass

    def modifier_classe(self):
        pass

    def supprimer_classe(self):
        pass

    def imprimer_classe(self):
        pass            










if __name__=="__main__":
    root = ctk.CTk()
    root.geometry("1000x600")
    frame = FenClasse(root)
    frame.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
