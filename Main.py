import Dati.Squadre
import Dati.campionati
import Dati.Conf
import tkinter as tk
import threading as Thread
import time
import random
from functools import partial

class Finestra(tk.Tk):
	def __init__(self):
		super().__init__()
		self.attributes('-fullscreen', True)
		self.resizable(0,0)
		self.title(Dati.Conf.Title)
		self.gira=Thread.Event()
		self.SquadreDaEstrarre=Dati.Squadre.squadre.copy()
		self.punteggio=tk.IntVar(value=0)
		self.nomiMostrati=0
		self.imgsquadra=tk.PhotoImage(file="Img/NoData300.png")
		self.camp1=tk.PhotoImage(file="Img/NoData250.png")
		self.camp2=tk.PhotoImage(file="Img/NoData250.png")
		self.camp3=tk.PhotoImage(file="Img/NoData250.png")
		self.scegli()
		
		
	def avvia_cronometro(self):
		self.gira.clear()
		self.thr=Thread.Thread(target=self.cronometro)
		self.thr.start()		
	
	def stop_cronometro(self):
		self.gira.set()
		self.thr.join()

	def cronometro(self):
		try:
			secondi=Dati.Conf.Tempo
			prima=time.localtime().tm_sec
			while not self.gira.is_set():
				ora=time.localtime().tm_sec
				if ora==prima+1:
					secondi-=1
					self.tempo.set(secondi)
					prima=ora
					if secondi==0:
						self.Finegioco("TEMPO SCADUTO")
						self.gira.set()
				

		except RuntimeError:
			print("Sono Esploso!")

	def Finegioco(self, testo):
		self.top.destroy()
		self.mf.destroy()
		self.mfexit.destroy()
		self.FineGmf=tk.Frame()
		self.FineGmf.pack()
		self.lb=tk.Label(self.FineGmf, text=testo, font=Dati.Conf.Font)
		self.lb.pack()
		self.punteggioFin=tk.Label(self.FineGmf, text="PUNTEGGIO FINALE: "+str(self.punteggio.get()), font=Dati.Conf.Font)
		self.punteggioFin.pack()
		self.AiutiFin=tk.Label(self.FineGmf, text="AIUTI USATI: "+str(self.nomiMostrati), font=Dati.Conf.Font)
		self.AiutiFin.pack()
		self.btRigioca=tk.Button(self.FineGmf, text="RIGIOCA", command=self.rigioca, font=Dati.Conf.Font, background="#00ff00")
		self.btRigioca.pack(pady=20)
		self.btesci=tk.Button(self.FineGmf, text="ESCI", command=self.destroy, font=Dati.Conf.Font, background="#ff0000")
		self.btesci.pack(pady=20)

	def rigioca(self):
		self.FineGmf.destroy()
		self.SquadreDaEstrarre=[]
		self.SquadreDaEstrarre=Dati.Squadre.squadre.copy()
		self.punteggio.set(0)
		self.nomiMostrati=0
		self.scegli()

	def crea(self):
		self.top=tk.Frame()
		self.top.pack()
		self.tm=tk.Frame(master=self.top)
		self.tm.pack(side=tk.LEFT, padx=75)
		self.pt=tk.Frame(master=self.top)
		self.pt.pack(side=tk.RIGHT, padx=75)
		self.mf=tk.Frame()
		self.mf.pack()
		self.text1=tk.Label(self.tm, text="Tempo Rimanente", font=Dati.Conf.Font)
		self.text1.pack()
		self.tempo=tk.IntVar(value=Dati.Conf.Tempo)
		self.templabel=tk.Label(self.tm, textvariable=self.tempo, font=Dati.Conf.Font)
		self.templabel.pack()
		self.text2=tk.Label(self.pt, text="Punteggio", font=Dati.Conf.Font)
		self.text2.pack()
		self.punti=tk.Label(self.pt, textvariable=self.punteggio, font=Dati.Conf.Font)
		self.punti.pack()
		self.squadralb=tk.Label(self.mf, image=self.imgsquadra, background="#ffffff")
		self.squadralb.pack()
		self.squadranb=tk.Button(self.mf, text="Clicca per il nome", font=Dati.Conf.Font, command=self.MostraNome)
		self.squadranb.pack(pady=10)
		self.bt1=tk.Button(self.mf, image=self.camp1, command=partial(self.controlla, "bt1"), background="#ffffff")
		self.bt1.pack(side=tk.LEFT, padx=75)
		self.bt2=tk.Button(self.mf, image=self.camp2, command=partial(self.controlla, "bt2"), background="#ffffff")
		self.bt2.pack(side=tk.LEFT, padx=75)
		self.bt3=tk.Button(self.mf, image=self.camp3, command=partial(self.controlla, "bt3"), background="#ffffff")
		self.bt3.pack(side=tk.LEFT, padx=75)
		self.mfexit=tk.Frame()
		self.mfexit.pack(side=tk.BOTTOM)
		self.exit=tk.Button(self.mfexit, text="TERMINA PARTITA", font=Dati.Conf.Font, command=self.TerminaPartita, background="#ff0000")
		self.exit.pack(pady=20)
		self.avvia_cronometro()
	
	def TerminaPartita(self):
		self.stop_cronometro()
		self.Finegioco("PARTITA TERMINATA")
	
	def scegli(self):
		self.squadra=""
		self.campionato1=""
		self.campionato2=""
		self.campionato3=""
		self.corretto=""
		nonvalidi=[]
		if len(self.SquadreDaEstrarre) > 0:
			indice=random.randint(0,len(self.SquadreDaEstrarre)-1)
			self.squadra=self.SquadreDaEstrarre[indice]
			self.SquadreDaEstrarre.pop(indice)
			pulsante=random.randint(0,2)
			nonvalidi.append(self.squadra["campionato"])
			if pulsante==0:
				self.campionato1=self.squadra["campionato"]
				self.campionato2=self.estraicampionato(nonvalidi)
				self.campionato3=self.estraicampionato(nonvalidi)
				self.corretto="bt1"
			else:
				if pulsante==1:
					self.campionato1=self.estraicampionato(nonvalidi)
					self.campionato2=self.squadra["campionato"]
					self.campionato3=self.estraicampionato(nonvalidi)
					self.corretto="bt2"
				else:
					self.campionato1=self.estraicampionato(nonvalidi)
					self.campionato2=self.estraicampionato(nonvalidi)
					self.campionato3=self.squadra["campionato"]
					self.corretto="bt3"

			self.imgsquadra=tk.PhotoImage(file=self.squadra["img"])
			self.camp1=tk.PhotoImage(file=Dati.campionati.campionati[self.campionato1])
			self.camp2=tk.PhotoImage(file=Dati.campionati.campionati[self.campionato2])
			self.camp3=tk.PhotoImage(file=Dati.campionati.campionati[self.campionato3])
			self.crea()
		else:
			self.stop_cronometro()
			self.Finegioco("SQUADRE TERMINATE")


	def estraicampionato(self, nonvalidi):
		gira=True
		while gira:
			campionato=random.randint(0, len(Dati.campionati.campionatiList)-1)
			if Dati.campionati.campionatiList[campionato] not in nonvalidi:
				gira=False
		nonvalidi.append(Dati.campionati.campionatiList[campionato])
		return Dati.campionati.campionatiList[campionato]

	def controlla(self, pulsante):
		if pulsante==self.corretto:
			self.stop_cronometro()
			self.top.destroy()
			self.mf.destroy()
			self.mfexit.destroy()
			self.punteggio.set(self.punteggio.get()+1)
			self.scegli()
			
		else:
			self.stop_cronometro()
			self.Finegioco("ERRORE \nLa risposta corretta era:\n" + self.squadra["campionato"])

	def MostraNome(self):
		self.squadranb.config(text=self.squadra["nome"])
		self.nomiMostrati+=1

f1=Finestra()
f1.mainloop()