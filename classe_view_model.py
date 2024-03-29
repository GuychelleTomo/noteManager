import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import classe_model
from Etats import classe_etat

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
        
        self._classe_model = classe_model.Classe()

        # creation de l'entete
        frame_entete = ctk.CTkFrame(self, height=50, corner_radius=0)

        
        # creation du titre
        lbl_titre = ctk.CTkLabel(frame_entete, text="LISTES CLASSES", fg_color="transparent", font=('AREAL BLACK', 20, "bold"))
        lbl_titre.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


        frame_entete.pack(side = tk.TOP, fill="x")

         

        # creation de la zone des boutons
        frame_buttons = ctk.CTkFrame(self, corner_radius=0)

        # creation des bouttons
        btn_ajouter = ctk.CTkButton(frame_buttons, text="Ajouter" ,command=self.ajouter_classe)
        btn_ajouter.pack()

        btn_modifier = ctk.CTkButton(frame_buttons, text="modifier",command=self.modifier_classe)
        btn_modifier.pack(padx=20, pady=5)

        btn_supprimer = ctk.CTkButton(frame_buttons, text="Supprimer",command=self.supprimer_classe)
        btn_supprimer.pack()

        btn_imprimer = ctk.CTkButton(frame_buttons, text="Imprimer",command=self.imprimer_classe)
        btn_imprimer.pack(padx=20, pady=5)
        
        btn_imprimer = ctk.CTkButton(frame_buttons, text="Actualiser",command=self.actualiser)
        btn_imprimer.pack(padx=20)


        frame_buttons.pack(side = tk.RIGHT, fill="y")




        # creation du body
        frame_corps = ctk.CTkFrame(self, corner_radius=0)
    
        self.tab_classe = ttk.Treeview(frame_corps , columns=("identifiant","nom",))
        # formater les colonnes
        self.tab_classe.column("#0", width=0, stretch=tk.NO)
        self.tab_classe.column("identifiant", stretch=tk.NO, width=0)
        self.tab_classe.column("nom", anchor=tk.CENTER, width=10)
        


        # afficher les entetes
        self.tab_classe.heading("identifiant", text="id_classe")
        self.tab_classe.heading("nom", text="nom")
        
        # selectionner la ligne du tableau et recupère les valeurs de la ligne selectionner à partir de la fonction obtenir_ligne_selectionner
        self.tab_classe.bind("<Button-1>" , self.obtenir_ligne_selectionner)

        # stocke les valeurs de la ligne selectionner du tableau si ils sont recupérés
        self.tab_values = ""

        # instanciation de la fonction pour recuperer les classes
        self.recuperer_toutes_classes()

        # ajouter les valeurs
        #self.tab_etudiant.insert("", tk.END,"1", values=(1,"OLALA","raz", "M","olala@gmail.com", "kombo", 2))

        
        self.tab_classe.pack(fill=tk.BOTH, expand=True)

        frame_corps.pack( fill="both", expand=True)

        # fonction pour obtenir la ligne selectionner
    def obtenir_ligne_selectionner(self,event):

        # recuperer les valeurs de la ligne selectionner
        self.tab_values = self.tab_classe.item(self.tab_classe.identify_row(event.y))["values"]
        
         # creation de la fonction pour recuperer les classes 
    def recuperer_toutes_classes(self):
        # suprimer tous les données du tableau
        self.tab_classe.delete(*self.tab_classe.get_children())

        classes = self._classe_model.recuperer_toutes_les_classes()
        # inserer les données dans le tableau mais à la fin
        if classes:
            i = 1
            for classe in classes :
                self.tab_classe.insert("", tk.END, values=classe)
                i+=1
                
    # fonction pour ajouter les classes
    def ajouter_classe(self):
        # fen_ajouter fait un callback de la fonction self._classe_model.ajouter_classe
        ajout = classe_etat.Fen_ajouter_classe(self._classe_model.ajouter_classe)
        ajout.mainloop()

    # creation de la fonction modifier_classe
    def modifier_classe(self,):


        # verifie si les valeurs ont été recuperer
        if self.tab_values:
            # fenetre Fen_modifier_classe fait un callback de la fonction self._classe_model.modifier_classe et prend en paramètre la valeur selectionner
            mod = classe_etat.Fen_modifier_classe(self._classe_model.modifier_classe,self.tab_values)
            mod.mainloop()
       
        else:
            # affiche un message "Veuillez sellectionner une ligne " si aucune ligne n'est séletionner 
            messagebox.showwarning("Ligne non selectionnée" , "Veuillez sellectionner une ligne ")    




    # création de la fonction supprimer_classe
    def supprimer_classe(self):
        

        # verifie si les valeurs ont été recuperer
        if self.tab_values:


            # affiche un message d'option si l'utilisateur veux supprimer une classe
            sup = messagebox.askyesno("Suppression", "voulez vous supprimez cette classe ?")
            if sup :
                # la fonction self._classe_model.supprimer_classe qui prend en paramètre la valeur selectionnée dans le tableau
                self._classe_model.supprimer_classe(self.tab_values[0])
  
        else:
            messagebox.showwarning("Ligne non selectionnée" , "Veuillez sellectionner une ligne ")    


    def imprimer_classe(self):
        
        if self.tab_values:
            pass

     # création de la fonction actualisée      
    def actualiser(self):
        self.recuperer_toutes_classes()









if __name__=="__main__":
    root = ctk.CTk()
    root.geometry("1000x600")
    frame = FenClasse(root)
    frame.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
