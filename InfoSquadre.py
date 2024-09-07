import Dati.Squadre
import Dati.Conf
import tkinter as tk

import Dati.campionati

class Finestra(tk.Tk):
	def __init__(self):
		super().__init__()
		self.geometry("1000x750")
		self.resizable(0,0)
		self.title("Controlla squadre")
		self.indice=0
		self.crea()

	def crea(self):
		self.mf=tk.Frame()
		self.mf.pack()
		self.ind=tk.Label(self.mf, text="Squadra numero: "+str(self.indice+1)+"/"+str(len(Dati.Squadre.squadre)), font=Dati.Conf.Font)
		self.ind.pack()
		try:
			self.sq=tk.PhotoImage(file=Dati.Squadre.squadre[self.indice]["img"])
		except :
			self.sq=tk.PhotoImage(file="Img/NoData300.png")
		self.sqlabel=tk.Label(self.mf, image=self.sq, background="#ffffff")
		self.sqlabel.pack()
		self.nome=tk.Label(self.mf, text="Nome: "+Dati.Squadre.squadre[self.indice]["nome"], font=Dati.Conf.Font)
		self.nome.pack()
		try:
			self.campionatoimg=tk.PhotoImage(file=Dati.campionati.campionati[Dati.Squadre.squadre[self.indice]["campionato"]])
		except:
			self.campionatoimg=tk.PhotoImage(file="Img/NoData250.png")
		self.campionatoimglabel=tk.Label(self.mf, image=self.campionatoimg)
		self.campionatoimglabel.pack()
		self.campionato=tk.Label(self.mf, text="Campionato: "+Dati.Squadre.squadre[self.indice]["campionato"], font=Dati.Conf.Font)
		self.campionato.pack()
		self.btindietro=tk.Button(self.mf, text="<", font=Dati.Conf.Font, command=self.indietro)
		self.btindietro.pack(side=tk.LEFT, padx=100)
		self.btavanti=tk.Button(self.mf, text=">", font=Dati.Conf.Font, command=self.avanti)
		self.btavanti.pack(side=tk.LEFT, padx=100)
	
	def avanti(self):
		if self.indice<len(Dati.Squadre.squadre)-1:
			self.indice+=1
			self.mf.destroy()
			self.crea()
		else:
			self.indice=0
			self.mf.destroy()
			self.crea()

	
	def indietro(self):
		if self.indice>0:
			self.indice-=1
			self.mf.destroy()
			self.crea()
		else:
			self.indice=len(Dati.Squadre.squadre)-1
			self.mf.destroy()
			self.crea()

f1=Finestra()
f1.mainloop()
