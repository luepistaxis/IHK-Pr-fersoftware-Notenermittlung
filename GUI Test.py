import tkinter
from tkinter import *
from tkinter import ttk




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
mainwindow.geometry("1040x710")
mainwindow.resizable(0, 0)

#TabControl
tabControl = ttk.Notebook(mainwindow)

tab1= Frame(tabControl, width=1040, height=710)
tab2= Frame(tabControl, width=1040, height=710)

tabControl.add(tab1, text='Berechnung')
tabControl.add(tab2, text='PDF Vorlage')

tabControl.place(x=0, y=0)

#------------------------------------------------------------------------------------------------------------------
#Format verschönener mit Boxen
form1AP1 = Label(tab1, borderwidth=1, relief='solid')
form1AP1.place(x=0, y=60, height=520, width=250)

form2AP2 = Label(tab1, borderwidth=1, relief='solid')
form2AP2.place(x=250, y=60, height=520, width=250)

form3AP2 = Label(tab1, borderwidth=1, relief='solid')
form3AP2.place(x=500, y=90, height=490, width=250)

form4AP2 = Label(tab1, borderwidth=1, relief='solid')
form4AP2.place(x=750, y=90, height=490, width=250)

form5Ges1 = Label(tab1, borderwidth=1, relief='solid')
form5Ges1.place(x=0, y=580, height=50, width=500)

form6Ges2 = Label(tab1, borderwidth=1, relief='solid')
form6Ges2.place(x=500, y=580, height=50, width=500)

form7End = Label(tab1, borderwidth=1, relief='solid')
form7End.place(x=0, y=630, height=50, width=1000)
#---------------------------------------------------------------------------------------------------------------

#Button Endergebnis berechnen
endBerechnenButton = Button(tab1, borderwidth=0, command=berechnen, text="Ergebnis", font=('Arial', 10))
endBerechnenButton.place()

#ButtonTeil1 AP1 berechnen
ap1BerechnenButton = Button(tab1, borderwidth=0, text="Ergebnis", font=('Arial', 10))
ap1BerechnenButton.place()

#ButtonTeil2 Dokumentation berechnen
dokuButton = Button(tab1, borderwidth=0, text="Ergebnis", font=('Arial', 10))
dokuButton.place()

#ButtonTeil2 Präsentation berechnen 
praesButton =Button(tab1, borderwidth=0, text="Ergebnis", font=('Arial', 10))
praesButton.place()

#ButtonTeil2 Schriftlicher Test berechnen
schrifButton =Button(tab1, borderwidth=0, text="Ergebnis", font=('Arial', 10))
schrifButton.place()

#Exit
exitButton = Button(tab1, borderwidth=0, bg='white', text='Exit', command=mainwindow.destroy, font=('Arial', 10))
exitButton.place(x=1010, y=0, height='30', width='30')

#-----------------------------------------------------------------------------------------------
#TEIL1

teil1 = Label(tab1, text='Teil 1', borderwidth=1, justify='center', relief='solid', font=('Arial', 25))
teil1.place(x=0, y=0, height=30, width=250)

#AP1
#Überschrift
uAP1Label = Label(tab1, text='schriftliche Prüfung',justify='center', borderwidth=1, relief='solid', font=('Arial', 10))
uAP1Label.place(x=0, y=30, height=30, width=220)

#Beschreibung
ap1Label = Label(tab1, text='Einrichten eines IT-\ngestützten Arbeitsplatz',justify='center', borderwidth=1, relief='solid', font=('Arial', 10))
ap1Label.place(x=10, y=100, height=30, width=200)

#Gewichtung
apProzentL = Label(tab1, text='20%', borderwidth=1, relief='solid', font=('Arial', 10))
apProzentL.place(x=220, y=30, height=30, width=30)

#Eingabe

ap1Eintrag = Entry(tab1, borderwidth=1, relief='solid', font=('Arial', 10))
ap1Eintrag.insert(0,'0')

ap1Eintrag.place(x=10, y=140, height=30, width=200)

#Umrechnung
ap1Umrechnung = Label(tab1,text='', justify='center', borderwidth=1, relief='solid', font=('Arial', 10))
ap1Umrechnung.place(x=220, y=140, height=30, width= 30)

#---------------------------------------------------------------------------------------

#TEIL 2

teil2 = Label(tab1, text='Teil 2', borderwidth=1, relief='solid', font=('Arial', 25))
teil2.place(x=250, y=0, height=30, width=750)

#Überschrift
uSchrift1 = Label(tab1, text="Schriftliche Prüfung", borderwidth=1, relief='solid', font=('Arial', 10))
uSchrift1.place(x=250, y=30, height=30, width=220)
uGewichtung1 = Label(tab1, text='30%', borderwidth=1, relief='solid', font=('Arial', 10))
uGewichtung1.place(x=470, y=30, height=30, width=30)

uSchrift2 = Label(tab1, text="Planen und Umsetzen eines Softwareprodukts", borderwidth=1, relief='solid', font=('Arial', 10))
uSchrift2.place(x=500, y=30, height=30, width=470)
uGewichtung2 = Label(tab1, text='50%', borderwidth=1, relief='solid', font=('Arial', 10))
uGewichtung2.place(x=970, y=30, height=30, width=30)

#-------------------------------------------------------------------------------------------------------------------

#Schriftliche Prüfung Teil 2
#Beschreibung
ap2Planen = Label(tab1, text='Planen eines Softwareprojekts', borderwidth=1, relief='solid', font=('Arial', 10))
ap2Planen.place(x=260, y=100, height=30, width=200)

ap2Entw = Label(tab1, text='Entwicklung und Umsetzung \nvon Algorithmen', borderwidth=1, relief='solid', font=('Arial', 10))
ap2Entw.place(x=260, y=180, height=30, width=200)

ap2Wirts = Label(tab1, text='Wirtschafts- und Sozialkunde',borderwidth=1, relief='solid', font=('Arial', 10))
ap2Wirts.place(x=260, y=260, height=30, width=200)

#Gewichtung AP2
ap2PlanProz = Label(tab1, text='10%', borderwidth=1, relief='solid', font=('Arial', 10))
ap2PlanProz.place(x=470, y=100, height=30, width=30)

ap2EntwProz = Label(tab1, text='10%', borderwidth=1, relief='solid', font=('Arial', 10))
ap2EntwProz.place(x=470, y=180, height=30, width=30 )

ap2WirtsProz = Label(tab1, text='10%', borderwidth=1, relief='solid', font=('Arial', 10))
ap2WirtsProz.place(x=470, y=260, height=30, width=30)



#Eingabe AP2
planEintrag = Entry(tab1, borderwidth=1, relief='solid', font=('Arial', 10))
planEintrag.insert(0,'0')
planEintrag.place(x=260, y=140, height=30, width=200)

entwEintrag = Entry(tab1, borderwidth=1, relief='solid', font=('Arial', 10))
entwEintrag.insert(0,'0')
entwEintrag.place(x=260, y=220, height=30, width=200)

wirtsEintrag = Entry(tab1, borderwidth=1, relief='solid', font=('Arial', 10))
wirtsEintrag.insert(0,'0')
wirtsEintrag.place(x=260, y=300, height=30, width=200)




#Umrechnung AP2 
planUmrechnung = Label(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
planUmrechnung.place(x=470, y=140, height=30, width=30)
entwUmrechnung = Label(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
entwUmrechnung.place(x=470, y=220, height=30, width=30)
wirtsUmrechung = Label(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
wirtsUmrechung.place(x=470, y=300, height=30, width=30)

#----------------------------------------------------------------------------------------------------------------

#Projektarbeit & Dokumentation

#2 Aufteilung

uDoku = Label(tab1, text='Dokumentation', borderwidth=1, relief='solid', font=('Arial', 10))
uDoku.place(x=500, y=60, height=30, width=220)
dokuProzent = Label(tab1, text='50%', borderwidth=1, relief='solid', font=('Arial', 10))
dokuProzent.place(x=720, y=60, height=30, width=30)
uPraeFach = Label(tab1, text='Praesentation und Fachgespräch', borderwidth=1, relief='solid', font=('Arial', 10))
uPraeFach.place(x=750, y=60, height=30, width=220)
praeFachProzent = Label(tab1, text='50%', borderwidth=1, relief='solid', font=('Arial', 10))
praeFachProzent.place(x=970, y=60, height=30, width=30)


#Beschreibung 

dokuGest= Label(tab1, text='Gestaltung Projektbericht \n(aeussere Form)', borderwidth=1, relief='solid', font=('Arial', 10))
dokuGest.place(x=510, y=100, height=30, width=200)

dokuKonkr = Label(tab1, text='Konkretisierung des Auftrages, der \nAusgangssituation & des Projektumfelds', borderwidth=1, relief='solid', font=('Arial', 8))
dokuKonkr.place(x=510, y=220, height=30, width=200)
dokuBeschr = Label(tab1, text='Beschreibung der\nProzessschritte', borderwidth=1, relief='solid', font=('Arial', 10))
dokuBeschr.place(x=510, y=340, height=30, width=200)
dokuDars = Label(tab1, text='Darstellung der Projektergebnisse \nund praxisbezogene', borderwidth=1, relief='solid', font=('Arial', 10))
dokuDars.place(x=510, y=460, height=30, width=200)

#Eingabe
gestEintrag = Entry(tab1,text='', borderwidth=1, relief='solid', font=('Arial', 10))
gestEintrag.place(x=510, y=140, height=30, width=200)

dPunkte2 = Entry(tab1,text='', borderwidth=1, relief='solid', font=('Arial', 10))
dPunkte2.place(x=510, y=260, height=30, width=200)

dPunkte3 = Entry(tab1,text='', borderwidth=1, relief='solid', font=('Arial', 10))
dPunkte3.place(x=510, y=380, height=30, width=200)

dPunkte4 = Entry(tab1,text='', borderwidth=1, relief='solid', font=('Arial', 10))
dPunkte4.place(x=510, y=500, height=30, width=200)

#Kommentar Dokumentation
gestaltKomment = Entry(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
gestaltKomment.place(x=510, y=180, height=30, width=200)

konkretKomment = Entry(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
konkretKomment.place(x=510, y=300, height=30, width=200)

beschreibKomment = Entry(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
beschreibKomment.place(x=510, y=420, height=30, width=200)

darstKomment = Entry(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
darstKomment.place(x=510, y=540, height=30, width=200)

#Kommentar Dokumentation Punkte

gestKoPunkte = Entry(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
gestKoPunkte.place(x=720, y=180, height=30, width=30)

konkKomPunkte = Entry(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
konkKomPunkte.place(x=720, y=300, height=30, width=30)

beschKomPunkte = Entry(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
beschKomPunkte.place(x=720, y=420, height=30, width=30)

darstKomPunkte = Entry(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
darstKomPunkte.place(x=720, y=540, height=30, width=30)



#Gewichtung
dProzent1 = Label(tab1, text='10%', borderwidth=1, relief='solid', font=('Arial', 10))
dProzent1.place(x=720, y=100, height=30, width=30)
dProzent2 = Label(tab1, text='30%', borderwidth=1, relief='solid', font=('Arial', 10))
dProzent2.place(x=720, y=220, height=30, width=30)
dProzent3 = Label(tab1, text='45%', borderwidth=1, relief='solid', font=('Arial', 10))
dProzent3.place(x=720, y=340, height=30, width=30)
dProzent4 = Label(tab1, text='15%', borderwidth=1, relief='solid', font=('Arial', 10))
dProzent4.place(x=720, y=460, height=30, width=30)

#Umrechnung
gestUmrechnung= Label(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
gestUmrechnung.place(x=720, y=140, height=30, width=30)
konkrUmrechnung= Label(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
konkrUmrechnung.place(x=720, y=260, height=30, width=30)
beschrUmrechnung= Label(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
beschrUmrechnung.place(x=720, y=380, height=30, width=30)
darsUmrechnung= Label(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
darsUmrechnung.place(x=720, y=500, height=30, width=30)



#-----------------------------------------------------------------------------------------------------------------------------
#Praesentation und Fachgespraech Teilpunkte

aufbBeschreibung = Label(tab1, text='Aufbau und inhaltliche Struktur', borderwidth=1, relief='solid', font=('Arial', 10))
aufbBeschreibung.place(x=760, y=100, height=30, width=200)

praeTech = Label(tab1, text='Praesentationstechnik', borderwidth=1, relief='solid', font=('Arial', 10))
praeTech.place(x=760, y=220, height=30, width=200)

#Eingabe

aufbEingabe = Entry(tab1, text='', justify='center', borderwidth=1, relief='solid', font=('Arial', 10))
aufbEingabe.place(x=760, y=140, height=30, width=200)

praePunkte3 = Entry(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
praePunkte3.place(x=760, y=260, height=30, width=200)

#Kommentar Präsentation und Fachgespräch
aufbKomment = Entry(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
aufbKomment.place(x=760, y=180, height=30, width=200)

praeTechKomment = Entry(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
praeTechKomment.place(x=760, y=300, height=30, width=200)

#Kommentar Präsentation und Fachgespräch Punkte
aufbKomPunkte = Entry(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
aufbKomPunkte.place(x=970, y=180, height=30, width=30)

praeKomPunkte = Entry(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
praeKomPunkte.place(x=970, y=300, height=30, width=30)


#Gewichtung
aufbProzL = Label(tab1, text='40%', borderwidth=1, relief='solid', font=('Arial', 10))
aufbProzL.place(x=970, y=100, height=30, width=30)
praeProz = Label(tab1, text='60%', borderwidth=1, relief='solid', font=('Arial', 10))
praeProz.place(x=970, y=220, height=30, width=30)

#Umrechnung
aufbUmrechnung = Label(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
aufbUmrechnung.place(x=970, y=140, height=30, width=30)
praeUmrechnung = Label(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
praeUmrechnung.place(x=970, y=260, height=30, width=30)

#-----------------------------------------------------------------------------------------------------------------
#Ergebnis Schriftliche Prüfungen Gesamt
schriftlErgebnis = Label(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
schriftlErgebnis.place(x=320, y=590, height=30, width=30 )

schriftlGesamtB = Button(tab1, text='schriftliche Prüfungen gesamt berechnen', borderwidth=1, relief='solid', bg='grey77', command=schriftlBerechnen, font=('Arial', 10))
schriftlGesamtB.place(x=10, y=590, height=30, width=300)

planUmsErgebnis = Label(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
planUmsErgebnis.place(x=820, y=590, height=30, width=30)

planUmsGesamtB = Button(tab1, text='Planen und Umsetzen eines \nSoftwareprodukts gesamt berechnen', borderwidth=1, relief='solid', bg='grey77', font=('Arial', 10))
planUmsGesamtB.place(x=510, y=590, height=30, width=300)

#Endnote

endNoteGesamtB = Button(tab1, text='Endnote', borderwidth=1, relief='solid', bg='grey77', font=('Arial', 10))
endNoteGesamtB.place(x=140, y=640, height=30, width=250)

endNoteErgebnis = Label(tab1, text='', borderwidth=1, relief='solid', font=('Arial', 10))
endNoteErgebnis.place(x=400, y=640, height=30, width=250)

bestandenMeldung = Label(tab1,  text='', borderwidth=1, relief='solid', font=('Arial', 10), )
bestandenMeldung.place(x=660, y=640, height=30, width=250)

#Start
mainwindow.mainloop()
