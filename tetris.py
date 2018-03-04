#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from Tkinter import *
import random
import datetime
class App:
	def __init__(self, master):
		root.title("Tetris")
		root.geometry("200x482")
		root.bind("<Up>", self.kaanna1)
		root.bind("<Left>", self.vasen)
		root.bind("<Right>", self.oikea)
		root.bind("<Down>", self.alas)
		self.aloita = Button(root, text="Uusi peli", command=self.uusipeli)
		self.aloita.place(relx=0.5, rely=0.2, anchor=CENTER)
		self.huiput = Button(root, text="Huipputulokset", command=self.huipputulokset)
		self.huiput.place(relx=0.5, rely=0.5, anchor=CENTER)
		self.lopeta = Button(root, text="Lopeta", command=root.quit)
		self.lopeta.place(relx=0.5, rely=0.8, anchor=CENTER)
	def uusipeli(self):
		self.aloita.destroy()
		self.huiput.destroy()
		self.lopeta.destroy()
		self.huippu = Frame(root, width = 200, height = 80)
		self.huippu.pack()
		self.pohja = Frame(root)
		self.pohja.pack()
		try:
			self.pistenaytto.destroy()
			self.ennatys.destroy()
		except:
			pass
		self.kartta = [[0 for x in range(10)] for y in range(24)]
		self.pudonneet = []
		self.pisteet = 0
		self.pistenaytto = Label(self.huippu, font = ("arial", 20), text=str(self.pisteet))
		self.pistenaytto.place(relx = 0.15, rely = 0.5, anchor = CENTER)
		self.snaytto = Canvas(self.huippu, width = 120, height = 80, bg = "black")
		self.snaytto.place(relx = 0.65, rely = 0.5, anchor = CENTER)
		self.kentta = Canvas(self.pohja, width = 200, height = 400, bg = "black")
		self.kentta.pack()
		self.luotetro()
	def luotetro(self):
		try:
			self.muoto = self.smuoto
		except:
			self.muoto = random.choice(["I", "J", "L", "S", "Z", "T", "O"])
		self.tetro = []
		if self.muoto == "I":
			for i in range(4):
				self.tetro.append(self.kentta.create_rectangle(80, -80+20*i, 100, -60+20*i, fill="brown"))
		if self.muoto == "J":
			for i in range(3):
				self.tetro.append(self.kentta.create_rectangle(80, -60+20*i, 100, -40+20*i, fill="blue"))
			self.tetro.append(self.kentta.create_rectangle(60, -20, 80, 0, fill="blue"))
		if self.muoto == "L":
			for i in range(3):
				self.tetro.append(self.kentta.create_rectangle(80, -60+20*i, 100, -40+20*i, fill="orange"))
			self.tetro.append(self.kentta.create_rectangle(100, -20, 120, 0, fill="orange"))
		if self.muoto == "T":
			self.tetro.append(self.kentta.create_rectangle(80, -40, 100, -20, fill="violet"))
			self.tetro.append(self.kentta.create_rectangle(80, -20, 100, 0, fill="violet"))
			self.tetro.append(self.kentta.create_rectangle(60, -20, 80, 0, fill="violet"))
			self.tetro.append(self.kentta.create_rectangle(100, -20, 120, 0, fill="violet"))
		if self.muoto == "S":
			for i in range(2):
				self.tetro.append(self.kentta.create_rectangle(80, -60+20*i, 100, -40+20*i, fill="green"))
			for i in range(2):
				self.tetro.append(self.kentta.create_rectangle(100, -40+20*i, 120, -20+20*i, fill="green"))
		if self.muoto == "Z":
			for i in range(2):
				self.tetro.append(self.kentta.create_rectangle(80, -60+20*i, 100, -40+20*i, fill="red"))
			for i in range(2):
				self.tetro.append(self.kentta.create_rectangle(60, -40+20*i, 80, -20+20*i, fill="red"))
		if self.muoto == "O":
			for i in range(2):
				for j in range(2):
					self.tetro.append(self.kentta.create_rectangle(80+20*i, -40+20*j, 100+20*i, -20+20*j, fill="yellow"))
		self.asento = 0
		self.smuoto = random.choice(["I", "J", "L", "S", "Z", "T", "O"])
		self.snaytto.delete("all")
		if self.smuoto == "I":
			for i in range(4):
				self.snaytto.create_rectangle(20 + 20*i, 20, 40 + 20*i, 40, fill="brown")
		if self.smuoto == "J":
			for i in range(3):
				self.snaytto.create_rectangle(20 + 20*i, 40, 40 + 20*i, 60, fill="blue")
			self.snaytto.create_rectangle(20, 20, 40, 40, fill="blue")
		if self.smuoto == "L":
			for i in range(3):
				self.snaytto.create_rectangle(20 + 20*i, 20, 40 + 20*i, 40, fill="orange")
			self.snaytto.create_rectangle(20, 40, 40, 60, fill="orange")
		if self.smuoto == "T":
			for i in range(3):
				self.snaytto.create_rectangle(20 + 20*i, 40, 40 + 20*i, 60, fill="violet")
			self.snaytto.create_rectangle(40, 20, 60, 40, fill="violet")
		if self.smuoto == "S":
			for i in range(2):
				self.snaytto.create_rectangle(40 + 20*i, 20, 60 + 20*i, 40, fill="green")
			for i in range(2):
				self.snaytto.create_rectangle(20 + 20*i, 40, 40 + 20*i, 60, fill="green")
		if self.smuoto == "Z":
			for i in range(2):
				self.snaytto.create_rectangle(20 + 20*i, 20, 40 + 20*i, 40, fill="red")
			for i in range(2):
				self.snaytto.create_rectangle(40 + 20*i, 40, 60+20*i, 60, fill="red")
		if self.smuoto == "O":
			for i in range(2):
				for j in range(2):
					self.snaytto.create_rectangle(20+20*i, 20+20*j, 40+20*i, 40+20*j, fill="yellow")
		try:
			self.pudota()
		except:
			self.loppu()

	def kaanna1(self, event):
		if self.muoto == "O":
			return
		elif self.kentta.coords(self.tetro[1])[0] == 0 or self.kentta.coords(self.tetro[1])[0] == 180:
			return
		elif self.muoto == "I":
			if self.asento == 0:
				if self.kentta.coords(self.tetro[1])[0] > 20:
					if all(self.kartta[j][i] == 0 for j in range(int(self.kentta.coords(self.tetro[1])[1]/20)-1, int(self.kentta.coords(self.tetro[1])[1]/20)+3) for i in range(int(self.kentta.coords(self.tetro[1])[0]/20)-2, int(self.kentta.coords(self.tetro[1])[0]/20)+2)):
						self.kaanna3(-2, -2, 2, -2, 2, 2, -2, 2)
			elif self.asento == 1:
				if all(self.kartta[j][i] == 0 for j in range(int(self.kentta.coords(self.tetro[1])[1]/20)-2, int(self.kentta.coords(self.tetro[1])[1]/20)+2) for i in range(int(self.kentta.coords(self.tetro[1])[0]/20)-2, int(self.kentta.coords(self.tetro[1])[0]/20)+2)):
					self.kaanna3(-2, -2, 2, -2, 2, 2, -2, 2)
			elif self.asento == 2:
				if self.kentta.coords(self.tetro[1])[0] < 160:
					if all(self.kartta[j][i] == 0 for j in range(int(self.kentta.coords(self.tetro[1])[1]/20)-2, int(self.kentta.coords(self.tetro[1])[1]/20)+2) for i in range(int(self.kentta.coords(self.tetro[1])[0]/20)-1, int(self.kentta.coords(self.tetro[1])[0]/20)+3)):
						self.kaanna3(-2, -2, 2, -2, 2, 2, -2, 2)
			elif self.asento == 3:
				if all(self.kartta[j][i] == 0 for j in range(int(self.kentta.coords(self.tetro[1])[1]/20)-1, int(self.kentta.coords(self.tetro[1])[1]/20)+3) for i in range(int(self.kentta.coords(self.tetro[1])[0]/20)-1, int(self.kentta.coords(self.tetro[1])[0]/20)+3)):
					self.kaanna3(-2, -2, 2, -2, 2, 2, -2, 2)
						
		else:
			if all(self.kartta[j][i] == 0 for j in range(int(self.kentta.coords(self.tetro[1])[1]/20)-1, int(self.kentta.coords(self.tetro[1])[1]/20)+2) for i in range(int(self.kentta.coords(self.tetro[1])[0]/20)-1, int(self.kentta.coords(self.tetro[1])[0]/20)+2)):
				if self.muoto == "L":
					self.kaanna3(-2, 0, 0, -2, 2, 0, 0, 2)
				if self.muoto == "J":
					self.kaanna3(0, -2, 2, 0, 0, 2, -2, 0)
				if self.muoto == "T":
					self.kaanna2(1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1)
				if self.muoto == "S":
					self.kaanna2(-1, 1, -1, -1, 1, -1, 1, 1, -2, 0, 0, -2, 2, 0, 0, 2)
				if self.muoto == "Z":
					self.kaanna2(1, -1, 1, 1, -1, 1, -1, -1, 0, -2, 2, 0, 0, 2, -2, 0)

	def kaanna2(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
		if self.asento == 0:
			self.kentta.move(self.tetro[0], 20, 20)
			self.kentta.move(self.tetro[2], a*20, b*20)
			self.kentta.move(self.tetro[3], i*20, j*20)
			self.asento = 1
		elif self.asento == 1:
			self.kentta.move(self.tetro[0], -20, 20)
			self.kentta.move(self.tetro[2], c*20, d*20)
			self.kentta.move(self.tetro[3], k*20, l*20)
			self.asento = 2
		elif self.asento == 2:
			self.kentta.move(self.tetro[0], -20, -20)
			self.kentta.move(self.tetro[2], e*20, f*20)
			self.kentta.move(self.tetro[3], m*20, n*20)
			self.asento = 3
		elif self.asento == 3:
			self.kentta.move(self.tetro[0], 20, -20)
			self.kentta.move(self.tetro[2], g*20, h*20)
			self.kentta.move(self.tetro[3], o*20, p*20)
			self.asento = 0

	def kaanna3(self, a, b, c, d, e, f, g, h):
		self.kaanna2(-1, -1, 1, -1, 1, 1, -1, 1, a, b, c, d, e, f, g, h)

	def pudota(self):
		# jos ei pohjassa
		if all(self.kentta.coords(pala)[1] < 380 for pala in self.tetro) and all(self.kartta[int(self.kentta.coords(pala)[1]/20)+1][int(self.kentta.coords(pala)[0]/20)] == 0 for pala in self.tetro):
			for pala in self.tetro:
				self.kentta.move(pala, 0, 20)
			global putous
			putous = root.after(250, self.pudota)
		else:
			# osuu pohjaan
			root.after_cancel(putous)
			for pala in self.tetro:
				self.pudonneet.append(pala)
				self.kartta[int(self.kentta.coords(pala)[1]/20)][int(self.kentta.coords(pala)[0]/20)] = 1
			self.luotetro()
			for rivi in range(20):
				if min(self.kartta[rivi]) == 1:
					if min(self.kartta[rivi+1]) == 1:
						if min(self.kartta[rivi+2]) == 1:
							if min(self.kartta[rivi+3]) == 1:
								self.tyhjenna(rivi, 4)
								self.pisteet += 27
								self.pistenaytto["text"] = str(self.pisteet)
								break
							else:
								self.tyhjenna(rivi, 3)
								self.pisteet += 9
								self.pistenaytto["text"] = str(self.pisteet)
								break
						else:
							self.tyhjenna(rivi, 2)
							self.pisteet += 3
							self.pistenaytto["text"] = str(self.pisteet)
							break
					else:
						self.tyhjenna(rivi, 1)
						self.pisteet += 1
						self.pistenaytto["text"] = str(self.pisteet)
						break
	def vasen(self, event):
		# ei saa olla reunassa
		if all(0 < self.kentta.coords(pala)[0] for pala in self.tetro):
			# kaikkien ruutujen vasemmalla puolella oltava tilaa
			if all(self.kartta[int(self.kentta.coords(pala)[1]/20)][int(self.kentta.coords(pala)[0]/20) - 1] == 0 for pala in self.tetro):
				for pala in self.tetro:
					self.kentta.move(pala, -20, 0)
	def oikea(self, event):
		# ei reunassa
		if all(self.kentta.coords(pala)[0] < 180 for pala in self.tetro):
			# kaikkien oikealla puolella oltava tilaa
			if all(self.kartta[int(self.kentta.coords(pala)[1]/20)][int(self.kentta.coords(pala)[0]/20) + 1] == 0 for pala in self.tetro):
				for pala in self.tetro:
					self.kentta.move(pala, 20, 0)
	def alas(self, event):
		# ei pohjalla
		if all(self.kentta.coords(pala)[1] < 380 for pala in self.tetro):
			# kaikkien alla oltava tilaa
			if all(self.kartta[int(self.kentta.coords(pala)[1]/20)+1][int(self.kentta.coords(pala)[0]/20)] == 0 for pala in self.tetro):
				for pala in self.tetro:
					self.kentta.move(pala, 0, 20)
	def tyhjenna(self, eka, rivit):
		for pala in reversed(self.pudonneet):
			if self.kentta.coords(pala)[1] in range(eka*20, (eka+(rivit-1))*20+20, 20):
				self.pudonneet.remove(pala)
				self.kentta.delete(pala)
			elif self.kentta.coords(pala)[1] < eka*20:
				self.kentta.move(pala, 0, 20*rivit)
		for j in reversed(range(rivit, eka+rivit)):
			self.kartta[j] = self.kartta[j-rivit]
		for k in range(rivit):
			self.kartta[k] = [0 for x in range(10)]
	def loppu(self):
		self.kentta.destroy()
		self.snaytto.destroy()
		self.pistenaytto.destroy()
		self.huippu.destroy()
		self.pohja.destroy()
		self.pistenaytto = Label(root, text = "Pisteet: " + str(self.pisteet))
		self.pistenaytto.place(relx=0.5, rely=0.2, anchor=CENTER)
		self.aloita = Button(root, text="Uusi peli", command=self.uusipeli)
		self.aloita.place(relx=0.5, rely=0.4, anchor=CENTER)
		self.huiput = Button(root, text="Huipputulokset", command=self.huipputulokset)
		self.huiput.place(relx=0.5, rely=0.6, anchor=CENTER)
		self.lopeta = Button(root, text="Lopeta", command=root.quit)
		self.lopeta.place(relx=0.5, rely=0.8, anchor=CENTER)
		tulokset = open("/home/ilari-perus/omatohjelmat/tetris-tulokset.txt", "r")
		tuloshistoria = tulokset.readlines()
		tulokset.close()
		pisteet = tuloshistoria[0::2]
		pisteet = map(int, [s.strip('\n') for s in pisteet])
		if max(pisteet) < self.pisteet:
			self.ennatys = Label(root, text = "ENNÄTYS!")
			self.ennatys.place(relx=0.5, rely=0.3, anchor=CENTER)
		tulokset = open("/home/ilari-perus/omatohjelmat/tetris-tulokset.txt", "a")
		tulokset.write(str(self.pisteet) + "\n")
		tulokset.write(str(datetime.datetime.now()) + "\n")
		tulokset.close()
	def huipputulokset(self):
		tulokset = open("/home/ilari-perus/omatohjelmat/tetris-tulokset.txt", "r")
		tuloshistoria = tulokset.readlines()
		tulokset.close()
		pisteet = tuloshistoria[0::2]
		paivaykset = tuloshistoria[1::2]
		pisteet = map(int, [s.strip('\n') for s in pisteet])
		top = Toplevel()
		top.title("Huipputulokset")
		tulos1 = Label(top, text = "1. tulos: " + str(max(pisteet)) + " pistettä, " + paivaykset[pisteet.index(max(pisteet))][0:19])
		tulos1.pack()
		paivaykset.remove(paivaykset[pisteet.index(max(pisteet))])
		pisteet.remove(max(pisteet))
		tulos2 = Label(top, text = "2. tulos: " + str(max(pisteet)) + " pistettä, " + paivaykset[pisteet.index(max(pisteet))][0:19])
		tulos2.pack()
		paivaykset.remove(paivaykset[pisteet.index(max(pisteet))])
		pisteet.remove(max(pisteet))
		tulos3 = Label(top, text = "3. tulos: " + str(max(pisteet)) + " pistettä, " + paivaykset[pisteet.index(max(pisteet))][0:19])
		tulos3.pack()
	
root = Tk()
app = App(root)
root.mainloop()
