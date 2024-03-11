import customtkinter as ctk
import tkinter as tk

from tkinter import messagebox

parametre_label = {"fg_color": "transparent", "font":('Areal', 16, 'bold')}

parametre_entry = {"fg_color": "white"}


class Fen_ajouter_etudiant(ctk.CTk):

    def __init__(self, func, func2):
        super().__init__()
        self.geometry("1000x600")
        self.resizable(False, False)
        self.title("formulaire étudiant")
        self.func = func
        self.func2 = func2
        self.liste_classe = []
        

        self.recuperer_classe()
        
    
    
        # creation du titre
        lbl_titre = ctk.CTkLabel(self, text="FORMULAIRES DES ETUDIANTS", fg_color="transparent",text_color="blue", font=('AREAL BLACK', 30, "bold"))
        lbl_titre.place(relx=0.5, rely=0.1, anchor=tk.CENTER)


       

        #  création des label
        lbl_nom= ctk.CTkLabel(self, text="Nom (s) :", **parametre_label)
        lbl_nom.place(relx=0.1, rely=0.3, anchor=tk.N)

        self.entry_nom=ctk.CTkEntry(self, **parametre_entry)
        self.entry_nom.place(relx=0.3, rely=0.3, anchor=tk.N, relwidth= 0.3)


        lbl_prenom= ctk.CTkLabel(self, text="Prenom (s) :", **parametre_label)
        lbl_prenom.place(relx=0.1, rely=0.4, anchor=tk.N)

        self.entry_prenom=ctk.CTkEntry(self, **parametre_entry)
        self.entry_prenom.place(relx=0.3, rely=0.4, anchor=tk.N, relwidth= 0.3)



        self.lbl_email= ctk.CTkLabel(self, text="Email :", **parametre_label)
        self.lbl_email.place(relx=0.1, rely=0.5, anchor=tk.N)

        self.entry_email=ctk.CTkEntry(self, **parametre_entry)
        self.entry_email.place(relx=0.3, rely=0.5, anchor=tk.N, relwidth= 0.3)



        lbl_ad= ctk.CTkLabel(self, text="Adresse :", **parametre_label)
        lbl_ad.place(relx=0.1, rely=0.6, anchor=tk.N)

        self.entry_ad=ctk.CTkEntry(self,**parametre_entry)
        self.entry_ad.place(relx=0.3, rely=0.6, anchor=tk.N, relwidth= 0.3)

        


        lbl_sexe= ctk.CTkLabel(self, text="Sexe :", **parametre_label)
        lbl_sexe.place(relx=0.6, rely=0.3, anchor=tk.NE)

        self.entry_sexe = ctk.CTkComboBox(self, values=["M", "F"])
        self.entry_sexe.place(relx=0.8, rely=0.3, anchor=tk.NE)


        lbl_classe= ctk.CTkLabel(self, text="Classe :", **parametre_label)
        lbl_classe.place(relx=0.6, rely=0.5, anchor=tk.NE)

        self.entry_classe = ctk.CTkComboBox(self, values=self.liste_classe)
        self.entry_classe.place(relx=0.8, rely=0.5, anchor=tk.NE)


        

        # création du button s'inscrire

        btn_inscire = ctk.CTkButton(self, text="Valider", font=('AREAL BLACK', 20, "bold"), command=self.valider)
        btn_inscire.place(relx=0.4, rely=0.9, anchor=tk.S)

        # création du boutton annuler
        btn_annuler = ctk.CTkButton(self, text="Annuler", font=('AREAL BLACK', 20, "bold"), command=self.annuler)
        btn_annuler.place(relx=0.6, rely=0.9, anchor=tk.S)


        

    def valider(self):

       if self.func(self.entry_nom.get(),
                  self.entry_prenom.get(),
                  self.entry_sexe.get(),
                  self.entry_email.get(),
                  self.entry_ad.get(),
                  self.recuperer_id()[0]
                  ):
            messagebox.showinfo("Confirmation", "étudiant ajouté avec succès")
            self.destroy()
       
    def recuperer_classe(self):
        self.classes = self.func2() 
        for  classe in self.classes:
            self.liste_classe.append(classe[1])




    def recuperer_id(self):

        for classe in self.classes:
            if self.entry_classe.get() in classe:
                
                return classe

    def annuler(self):
         self.destroy()
















class Fen_modifier_etudiant(ctk.CTk):

    def __init__(self, func, func2, args):
        super().__init__()
        self.geometry("1000x600")
        self.resizable(False, False)
        self.title("formulaire étudiant")
        self.func = func
        self.func2 = func2
        self.liste_classe = []
        self.valeurs  = []
        self.args = args
        

        self.recuperer_classe()
        
    
    
        # creation du titre
        lbl_titre = ctk.CTkLabel(self, text="FORMULAIRES DES ETUDIANTS", fg_color="transparent",text_color="blue", font=('AREAL BLACK', 30, "bold"))
        lbl_titre.place(relx=0.5, rely=0.1, anchor=tk.CENTER)


       

        #  création des label
        lbl_nom= ctk.CTkLabel(self, text="Nom (s) :", **parametre_label)
        lbl_nom.place(relx=0.1, rely=0.3, anchor=tk.N)

        self.entry_nom=ctk.CTkEntry(self, **parametre_entry)
        self.entry_nom.place(relx=0.3, rely=0.3, anchor=tk.N, relwidth= 0.3)
        self.entry_nom.insert(0, args[1]) # écrire les valeurs existants dans les entrés


        lbl_prenom= ctk.CTkLabel(self, text="Prenom (s) :", **parametre_label)
        lbl_prenom.place(relx=0.1, rely=0.4, anchor=tk.N)

        self.entry_prenom=ctk.CTkEntry(self, **parametre_entry)
        self.entry_prenom.place(relx=0.3, rely=0.4, anchor=tk.N, relwidth= 0.3)
        self.entry_prenom.insert(0, args[2]) # écrire les valeurs existants dans les entrés


        self.lbl_email= ctk.CTkLabel(self, text="Email :", **parametre_label)
        self.lbl_email.place(relx=0.1, rely=0.5, anchor=tk.N)

        self.entry_email=ctk.CTkEntry(self, **parametre_entry)
        self.entry_email.place(relx=0.3, rely=0.5, anchor=tk.N, relwidth= 0.3)
        self.entry_email.insert(0, args[4]) # écrire les valeurs existants dans les entrés



        lbl_ad= ctk.CTkLabel(self, text="Adresse :", **parametre_label)
        lbl_ad.place(relx=0.1, rely=0.6, anchor=tk.N)

        self.entry_ad=ctk.CTkEntry(self,**parametre_entry)
        self.entry_ad.place(relx=0.3, rely=0.6, anchor=tk.N, relwidth= 0.3)
        self.entry_ad.insert(0, args[5]) # écrire les valeurs existants dans les entrés
        


        lbl_sexe= ctk.CTkLabel(self, text="Sexe :", **parametre_label)
        lbl_sexe.place(relx=0.6, rely=0.3, anchor=tk.NE)

        self.entry_sexe = ctk.CTkComboBox(self, values=["M", "F"])
        self.entry_sexe.place(relx=0.8, rely=0.3, anchor=tk.NE)
        self.entry_sexe.set(args[3]) # écrire les valeurs existants dans les entrés


        lbl_classe= ctk.CTkLabel(self, text="Classe :", **parametre_label)
        lbl_classe.place(relx=0.6, rely=0.5, anchor=tk.NE)

        self.entry_classe = ctk.CTkComboBox(self, values=self.liste_classe)
        self.entry_classe.place(relx=0.8, rely=0.5, anchor=tk.NE)
        for valeur in self.valeurs:
            if args[6] in valeur:
                self.entry_classe.set(valeur[1]) # écrire les valeurs existants dans les entrés
                break


        

        # création du button s'inscrire

        btn_inscire = ctk.CTkButton(self, text="Valider", font=('AREAL BLACK', 20, "bold"), command=self.valider)
        btn_inscire.place(relx=0.4, rely=0.9, anchor=tk.S)

        # création du boutton annuler
        btn_annuler = ctk.CTkButton(self, text="Annuler", font=('AREAL BLACK', 20, "bold"), command=self.annuler)
        btn_annuler.place(relx=0.6, rely=0.9, anchor=tk.S)


        

    def valider(self):
        
        if self.func(self.entry_nom.get(),
                  self.entry_prenom.get(),
                  self.entry_sexe.get(),
                  self.entry_email.get(),
                  self.entry_ad.get(),
                  self.recuperer_id()[0], 
                  self.args[0]
                  ):
            messagebox.showinfo("Confirmation", "étudiant modifié avec succès")
            self.destroy()



    def recuperer_id(self):

        for classe in self.classes:
            if self.entry_classe.get() in classe:
                
                return classe


       
    def recuperer_classe(self):
        self.classes = self.func2() 
        for  classe in self.classes:
            # alimenter le combobox
            self.liste_classe.append(classe[1])
            # ajouter 
            self.valeurs.append(classe)
                  


    def annuler(self):
         self.destroy()





if __name__=="__main__":
    def func():
        pass

    def func2():
        pass

    root= Fen_ajouter_etudiant(func, func2)
    
    root.mainloop()