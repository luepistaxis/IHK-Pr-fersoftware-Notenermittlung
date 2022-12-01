import tkinter
from tkinter import *
from tkinter import ttk


def ap1Berechnen():
    return
    
def dokuBerechnen():
    return

def praesBerechnen():
    return

def schriftlBerechnen():
    ergebnisAP1 = float(ap1Eintrag.get()) * 0.2
    ergebisPlanEintrag = float(planEintrag.get()) * 0.1
    ergebnisEntwEintrag = float(entwEintrag.get()) * 0.1
    ergebnisWirtsEintrag = float(wirtsEintrag.get()) * 0.1
    ergebnisSchriftl = ergebnisAP1 + ergebisPlanEintrag + ergebnisEntwEintrag + ergebnisWirtsEintrag
    schriftlErgebnis.config(text=str(ergebnisSchriftl))

def berechnen():
    teil1= float(punkte1.get())
    teil2= float(punkte2.get())
    teil3= float(punkte3.get())
    teil4= float(punkte4.get())

    ergebnis= teil1 + teil2 + teil3 + teil4
    labelErgebnis.config(text=str(ergebnis))







#Fenster erstellen
mainwindow = Tk()
mainwindow.title('Notenberechnung')
mainwindow.geometry("1040x600")
mainwindow.resizable(0, 0)

#TabControl
tabControl = ttk.Notebook(mainwindow)

tab1= Frame(tabControl, width=1040, height=600)
tab2= Frame(tabControl, width=1040, height=600)

tabControl.add(tab1, text='Berechnung')
tabControl.add(tab2, text='PDF Vorlage')

tabControl.place(x=0, y=0)

#------------------------------------------------------------------------------------------------------------------

#Button Endergebnis berechnen
endBerechnenButton = Button(tab1, borderwidth=0, command=berechnen, text="Ergebnis")
endBerechnenButton.place()

#ButtonTeil1 AP1 berechnen
ap1BerechnenButton = Button(tab1, borderwidth=0, text="Ergebnis")
ap1BerechnenButton.place()

#ButtonTeil2 Dokumentation berechnen
dokuButton = Button(tab1, borderwidth=0, text="Ergebnis")
dokuButton.place()

#ButtonTeil2 Präsentation berechnen 
praesButton =Button(tab1, borderwidth=0, text="Ergebnis")
praesButton.place()

#ButtonTeil2 Schriftlicher Test berechnen
schrifButton =Button(tab1, borderwidth=0, text="Ergebnis")
schrifButton.place()

#Exit
exitButton = Button(tab1, borderwidth=0, bg='white', text='Exit', command=mainwindow.destroy)
exitButton.place(x=1010, y=0, height='30', width='30')

#-----------------------------------------------------------------------------------------------
#TEIL1

teil1 = Label(tab1, text='Teil 1', borderwidth=1, justify='center', font=25, relief='solid')
teil1.place(x=0, y=0, height=30, width=250)

#AP1
#Überschrift
uAP1Label = Label(tab1, text='schriftliche Prüfung',justify='center', borderwidth=1, relief='solid')
uAP1Label.place(x=0, y=30, height=30, width=220)

#Beschreibung
ap1Label = Label(tab1, text='Einrichten eines IT-\ngestützten Arbeitsplatz',justify='center', borderwidth=1, relief='solid')
ap1Label.place(x=10, y=100, height=30, width=200)

#Gewichtung
apProzentL = Label(tab1, text='20%', borderwidth=1, relief='solid')
apProzentL.place(x=220, y=30, height=30, width=30)

#Eingabe
ap1Eintrag = Entry(tab1, borderwidth=1, relief='solid')
ap1Eintrag.insert(0,'0')
ap1Eintrag.place(x=10, y=140, height=30, width=200)

#Umrechnung
ap1Umrechnung = Label(tab1,text='', justify='center', borderwidth=1, relief='solid')
ap1Umrechnung.place(x=220, y=140, height=30, width= 30)

#---------------------------------------------------------------------------------------

#TEIL 2

teil2 = Label(tab1, text='Teil 2', borderwidth=1, font=25, relief='solid')
teil2.place(x=250, y=0, height=30, width=750)

#Überschrift
uSchrift1 = Label(tab1, text="Schriftliche Prüfung", borderwidth=1, relief='solid')
uSchrift1.place(x=250, y=30, height=30, width=220)
uGewichtung1 = Label(tab1, text='30%', borderwidth=1, relief='solid')
uGewichtung1.place(x=470, y=30, height=30, width=30)

uSchrift2 = Label(tab1, text="Planen und Umsetzen eines Softwareprodukts", borderwidth=1, relief='solid')
uSchrift2.place(x=500, y=30, height=30, width=470)
uGewichtung2 = Label(tab1, text='50%', borderwidth=1, relief='solid')
uGewichtung2.place(x=970, y=30, height=30, width=30)

#-------------------------------------------------------------------------------------------------------------------

#Schriftliche Prüfung Teil 2
#Beschreibung
ap2Planen = Label(tab1, text='Planen eines Softwareprojekts', borderwidth=1, relief='solid')
ap2Planen.place(x=260, y=100, height=30, width=200)

ap2Entw = Label(tab1, text='Entwicklung und Umsetzung \nvon Algorithmen', borderwidth=1, relief='solid')
ap2Entw.place(x=260, y=180, height=30, width=200)

ap2Wirts = Label(tab1, text='Wirtschafts- und Sozialkunde',borderwidth=1, relief='solid')
ap2Wirts.place(x=260, y=260, height=30, width=200)

#Gewichtung AP2
ap2PlanProz = Label(tab1, text='10%', borderwidth=1, relief='solid')
ap2PlanProz.place(x=470, y=100, height=30, width=30)

ap2EntwProz = Label(tab1, text='10%', borderwidth=1, relief='solid')
ap2EntwProz.place(x=470, y=180, height=30, width=30 )

ap2WirtsProz = Label(tab1, text='10%', borderwidth=1, relief='solid')
ap2WirtsProz.place(x=470, y=260, height=30, width=30)



#Eingabe AP2
planEintrag = Entry(tab1, borderwidth=1, relief='solid')
planEintrag.insert(0,'0')
planEintrag.place(x=260, y=140, height=30, width=200)

entwEintrag = Entry(tab1, borderwidth=1, relief='solid')
entwEintrag.insert(0,'0')
entwEintrag.place(x=260, y=220, height=30, width=200)

wirtsEintrag = Entry(tab1, borderwidth=1, relief='solid')
wirtsEintrag.insert(0,'0')
wirtsEintrag.place(x=260, y=300, height=30, width=200)




#Umrechnung AP2 
planUmrechnung = Label(tab1, text='', borderwidth=1, relief='solid')
planUmrechnung.place(x=470, y=100, height=30, width=30)
entwUmrechnung = Label(tab1, text='', borderwidth=1, relief='solid')
entwUmrechnung.place(x=470, y=180, height=30, width=30)
wirtsUmrechung = Label(tab1, text='', borderwidth=1, relief='solid')
wirtsUmrechung.place(x=470, y=260, height=30, width=30)

#----------------------------------------------------------------------------------------------------------------

#Projektarbeit & Dokumentation

#2 Aufteilung

uDoku = Label(tab1, text='Dokumentation', borderwidth=1, relief='solid')
uDoku.place(x=500, y=60, height=30, width=220)
dokuProzent = Label(tab1, text='50%', borderwidth=1, relief='solid')
dokuProzent.place(x=720, y=60, height=30, width=30)


#Beschreibung 

dokuGest= Label(tab1, text='Gestaltung Projektbericht \n(aeussere Form)', borderwidth=1, relief='solid')
dokuGest.place(x=510, y=100, height=30, width=200)



dokuPart1 = Label(tab1, text='Gestaltung Projektbericht\n(aeussere Form)', bg='white', fg='black',anchor="nw", padx=5, justify='left' )
dokuPart1.place()
dokuPart2 = Label(tab1, text='Beschreibung/Konkretisierung\ndes Auftrages, der Ausgangssituation und des Projektumfelds', bg='white', fg='black',anchor="nw", padx=5, justify='left' )
dokuPart2.place()
dokuPart3 = Label(tab1, text='Beschreibung der\nProzessschritte', bg='white', fg='black',anchor="nw", padx=5, justify='left' )
dokuPart3.place()
dokuPart4 = Label(tab1, text='Darstellung der\nProjektergebnisse und praxisbezogene', bg='white', fg='black',anchor="nw", padx=5, justify='left' )
dokuPart4.place()

#Eingabe
dPunkte1 = Entry(tab1,text='', bg='white', fg="black", justify='center')
dPunkte1.place()

dPunkte2 = Entry(tab1,text='', bg='white', fg="black", justify='center')
dPunkte2.place()

dPunkte3 = Entry(tab1,text='', bg='white', fg="black", justify='center')
dPunkte3.place()

dPunkte4 = Entry(tab1,text='', bg='white', fg="black", justify='center')
dPunkte4.place()

#Gewichtung
dProzent1 = Label(tab1, text='10%', bg='white', fg='black')
dProzent1.place()
dProzent2 = Label(tab1, text='30%', bg='white', fg='black')
dProzent2.place()
dProzent3 = Label(tab1, text='45%', bg='white', fg='black')
dProzent3.place()
dProzent4 = Label(tab1, text='15%', bg='white', fg='black')
dProzent4.place()




#-----------------------------------------------------------------------------------------------------------------------------
#Praesentation und Fachgespraech

praeBeschreibung = Label(tab1, text='Praesentation und Fachgespraech')
praeBeschreibung.place()
praeProzentL = Label(tab1, text='50%')
praeProzentL.place()

#Eingabe


praePunkte2 = Entry(tab1,text='', bg='white', fg="black", justify='center')
praePunkte2.place()

praePunkte3 = Entry(tab1,text='', bg='white', fg="black", justify='center')
praePunkte3.place()

#Gewichtung

praeProz1 = Label(tab1, text='50%', bg='white', fg='black')
praeProz1.place()
praeProz2 = Label(tab1, text='20%', bg='white', fg='black')
praeProz2.place()
praeProz3 = Label(tab1, text='30%', bg='white', fg='black')
praeProz3.place()

#Kriterien Teil A2
prae1 = Label(tab1, text='Praesentation und Fachgespraech', bg='white', fg='black',anchor="nw", padx=5, justify='left' )
prae1.place()
prae2 = Label(tab1, text='Aufbau und inhaltliche Struktur', bg='white', fg='black',anchor="nw", padx=5, justify='left' )
prae2.place()
prae3 = Label(tab1, text='Praesentationstechnik', bg='white', fg='black',anchor="nw", padx=5, justify='left' )
prae3.place()

#-------------------------------------------------------------------------------------------------------------------
#Teil B

#Eingabe

ganzHeA1P = Entry(tab1,text='', bg='white', fg="black", justify='center')
ganzHeA1P.place()

ganzHeA2P = Entry(tab1,text='', bg='white', fg="black", justify='center')
ganzHeA2P.place()

wirtSoziaP = Entry(tab1,text='', bg='white', fg="black", justify='center')
wirtSoziaP.place()

#Gewichtung

teilBProz1 = Label(tab1, text='40%', bg='white', fg='black')
teilBProz1.place()
teilBProz2 = Label(tab1, text='20%', bg='white', fg='black')
teilBProz2.place()
teilBProz3 = Label(tab1, text='30%', bg='white', fg='black')
teilBProz3.place()

#Kriterien Teil A2
prae1 = Label(tab1, text='Praesentation und Fachgespraech', bg='white', fg='black',anchor="nw", padx=5, justify='left' )
prae1.place()
prae2 = Label(tab1, text='Aufbau und inhaltliche Struktur', bg='white', fg='black',anchor="nw", padx=5, justify='left' )
prae2.place()
prae3 = Label(tab1, text='Praesentationstechnik', bg='white', fg='black',anchor="nw", padx=5, justify='left' )
prae3.place()

#-----------------------------------------------------------------------------------------------------------------
#Ergebnis Schriftliche Prüfungen Gesamt
schriftlErgebnis = Label(tab1, text='', borderwidth=1, relief='solid')
schriftlErgebnis.place(x=260, y=500, height=30, width=30 )

schriftlGesamtB = Button(tab1, text='schriftliche Prüfungen gesamt berechnen', borderwidth=1, relief='solid', command=schriftlBerechnen)
schriftlGesamtB.place(x=10, y=500, height=30, width=250)


#ErgebnisTeil2
labelErgebnis2 = Label(tab1, text='', bg='white', fg='black',)
labelErgebnis2.place()

#Start
mainwindow.mainloop()