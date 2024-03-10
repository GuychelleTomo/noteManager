import customtkinter as ctk
from tkinter import messagebox


class Fen_ajouter_classe(ctk.CTk):
    def __init__(self , func):
        super().__init__()

        self.geometry("400x240")
        self.resizable(False,False)
        
        self.func = func
        
        self.title("Ajouter classe")
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(expand = True , fill ="both")
        
        self.lbl_titre = ctk.CTkLabel(self.frame , text=" FORMULAIRE CLASSE" ,font =("AREAL BLACK",20))
        self.lbl_titre.place(relx=0.5, rely = 0.15 , anchor ="n")
        
        self.lbl_nom = ctk.CTkLabel(self.frame , text=" nom ")
        self.lbl_nom.place(relx=0.10 , rely = 0.40 , anchor ="w")
        
        self.nom_classe = ctk.CTkEntry( self.frame)
        self.nom_classe.place(relx=0.90 , rely = 0.40 , anchor ="e" , relwidth = 0.6)
        
        self.btn_valider = ctk.CTkButton(self.frame , text= "valider" ,command=self.valider)
        self.btn_valider.place(relx=0.10 , rely = 0.60 , anchor ="w")
        
        self.btn_annuler = ctk.CTkButton(self.frame , text= "Annuler" ,command=self.annuler)
        self.btn_annuler.place(relx=0.90 , rely = 0.60 , anchor ="e")
        
    def valider(self):
        if self.func(self.nom_classe.get()):
            messagebox.showinfo("succes" ,"classe"+ self.nom_classe.get() +" enregistrer avec succes")
            self.destroy()
    
    def annuler(self):
        self.destroy()





class Fen_modifier_classe(ctk.CTk):
    def __init__(self,func,args):
        super().__init__()

        self.geometry("400x240")
        self.resizable(False,False)
        
        self.func = func
        self.args = args
        
        self.title("Ajouter classe")
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(expand = True , fill ="both")
        
        self.lbl_titre = ctk.CTkLabel(self.frame , text=" FORMULAIRE CLASSE" ,font =("AREAL BLACK",20))
        self.lbl_titre.place(relx=0.5, rely = 0.15 , anchor ="n")
        
        self.lbl_nom = ctk.CTkLabel(self.frame , text=" nom ")
        self.lbl_nom.place(relx=0.10 , rely = 0.40 , anchor ="w")
        
        self.nom_classe = ctk.CTkEntry( self.frame)
        self.nom_classe.place(relx=0.90 , rely = 0.40 , anchor ="e" , relwidth = 0.6)
        self.nom_classe.insert(0 ,self.args[1])
        
        self.btn_valider = ctk.CTkButton(self.frame , text= "valider" ,command=self.valider)
        self.btn_valider.place(relx=0.10 , rely = 0.60 , anchor ="w")
        
        self.btn_annuler = ctk.CTkButton(self.frame , text= "Annuler" ,command=self.annuler)
        self.btn_annuler.place(relx=0.90 , rely = 0.60 , anchor ="e")
        
        
    def valider(self):
        
        if self.func(self.nom_classe.get(),self.args[0]):
            messagebox.showinfo("succes" ,"classe"+ self.nom_classe.get() +" enregistrer avec succes")
        self.destroy()
        
    
    def annuler(self):
        self.destroy()



class Fen_imprimer_classe(ctk.CTk):
    pass



if __name__ == "__main__":
    def a(a):
        print(a)
        return True
        
