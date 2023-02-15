#import fpdf
from fpdf import FPDF
from datetime import date
import os
from os.path import exists
#import textwrap
   
def PunkteAusgabeFormatieren(zahl):
    formatierteZahl = ""

    if zahl >= 10 and zahl < 100:
        formatierteZahl  = "\t\t" + str(zahl)
    elif zahl < 10 :
        formatierteZahl = "\t\t\t\t" + str(zahl)
    else:
        formatierteZahl = "" + str(zahl)

    return formatierteZahl

def DatumAusgeben(datum):
    string = ""
    for d in datum:
        string = d + "." + string
    return string[:-1]

#create object instance
pdf = FPDF()
  
#add page
pdf.add_page()
  
#variablen zur formatierung
hoehe0 = 17  
hoehe1 = 14  
hoehe2 = 11  
hoehe3 = 6
hoeheKommentar = 5
weiteKommentar = 180
fontsize0 = 22
fontsize1 = 17
fontsize2 = 15
fontsize3 = 12
fontsize4 = 10
fontsize5 = 8
fontsizeNewLine = 2
tab1 = "\t\t\t\t\t\t\t\t\t\t\t\t"
tab2 = "\t\t"

#Variablen Person und Datum TEMPORÄR!!!
datum = str(date.today()).split("-")
jahr = datum[0]
name = "Alf Tanner von Melmac"
id = 1234567890

version = "V_082"

#Variablen (Zwischen-) Noten TEMPÖRÄR!!! bisherige bezeihcnungen
ergebnisAP1 = 42.0
ergebisPlanEintrag = 80.80
ergebnisEntwEintrag = 100.0
ergebnisWirtsEintrag = 0.0

ergebnisGestaltung = 00.0
ergebnisKonkretisierung = 10.0
ergebnisBeschreibung = 100.0
ergebnisDarstellung = 00.0

ergebnisAufbau = 100.0
ergebnisPraesentation = 00.0

endnote = 100.0


ergebnisGestaltungKommentar = "Kommentar: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
ergebnisKonkretisierungKommentar = "Kommentar: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
ergebnisBeschreibungKommentar = "Kommentar: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
ergebnisDarstellungKommentar = "Kommentar: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
ergebnisAufbauKommentar = "Kommentar: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Kommentar: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
ergebnisPraesentationKommentar = "Kommentar: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n"



name_x = name.split(" ");
nameUnderscore = ""


for n in name_x:
    nameUnderscore = nameUnderscore + n + "_"

pdfBezeichnung = version + "_" + str(jahr) + "_" + nameUnderscore + str(id) + ".pdf"



# Überschrift IHK
# set font style and size
pdf.set_font("Arial", size = fontsize0)
pdf.cell(200, hoehe1, txt = "Industrie- und Handelskammer", ln = 1, align = 'L')
pdf.cell(114, hoehe1, txt = "Berlin " + str(jahr) , ln = 2, align = 'L')

pdf.set_font("Arial", size = fontsize3) 
pdf.cell(100, hoehe3, txt = "Name:   " + tab1 + name, ln = 2, align = 'L') 
pdf.cell(100, hoehe3, txt = "IHK-ID: "+ tab1 + str(id), ln = 2, align = 'L') 
pdf.set_font("Arial", size = fontsizeNewLine)
pdf.cell(100, fontsizeNewLine, txt = "", ln = 2, align = 'L')

#Bewertungen
#Schriftliche Prüfung
#schr AP1
pdf.set_font("Arial", 'I', size = fontsize2) 
pdf.cell(100, hoehe2, txt = "Punkte"+tab1+" Schriftliche Prüfungen", ln = 2, align = 'L')
pdf.set_font("Arial", size = fontsize3)
pdf.cell(100, hoehe3, txt = "AP1:", ln = 2, align = 'L')
pdf.set_font("Arial", size = fontsize4)
pdf.cell(100, hoehe3, txt = tab2+ PunkteAusgabeFormatieren(ergebnisAP1) +tab1+ " Einrichten eines IT-gestützten Arbeitsplatz", ln = 2, align = 'L') 
pdf.set_font("Arial", size = fontsizeNewLine) 
pdf.cell(100, hoehe3, txt = "", ln = 2, align = 'L')


#schr AP2
pdf.set_font("Arial", size = fontsize3)
pdf.cell(100, hoehe3, txt = "AP2:", ln = 2, align = 'L')
pdf.set_font("Arial", size = fontsize4)
pdf.cell(100, hoehe3, txt = tab2+ PunkteAusgabeFormatieren(ergebisPlanEintrag) +tab1+ " Planen eines Softwareprojekts", ln = 2, align = 'L') 
#pdf.cell(100, hoehe3, txt = tab2+ str(ergebnisEntwEintrag) +tab1+ " Entwicklung und Umsetzung von Algorithmen", ln = 2, align = 'L') 
pdf.cell(100, hoehe3, txt = tab2+ PunkteAusgabeFormatieren(ergebnisEntwEintrag) +tab1+ " Entwicklung und Umsetzung von Algorithmen", ln = 2, align = 'L') 
pdf.cell(100, hoehe3, txt = tab2+ PunkteAusgabeFormatieren(ergebnisWirtsEintrag) +tab1+ " Wirtschafts- und Sozialkunde", ln = 2, align = 'L') 
pdf.set_font("Arial", size = fontsizeNewLine)
pdf.cell(100, hoehe3, txt = "", ln = 2, align = 'L')


#Projekt
#Doku
pdf.set_font("Arial", size = fontsize2)
pdf.cell(100, hoehe2, txt = "Planen und Umsetzen eines Softwareprojekts", ln = 2, align = 'L') 
pdf.set_font("Arial", size = fontsize3)
pdf.cell(100, hoehe3, txt = "Dokumentation", ln = 2, align = 'L')
pdf.set_font("Arial", size = fontsize4) 
pdf.cell(100, hoehe3, txt = tab2+ PunkteAusgabeFormatieren(ergebnisGestaltung) +tab1+" Gestaltung Projektbericht (äußere Form)", ln = 2, align = 'L') 
pdf.set_font("Arial", size = fontsize5) 
pdf.multi_cell(weiteKommentar, hoeheKommentar, ergebnisGestaltungKommentar) 
pdf.set_font("Arial", size = fontsize4) 
pdf.cell(100, hoehe3, txt = tab2+ PunkteAusgabeFormatieren(ergebnisKonkretisierung) +tab1+" Beschreibung des Auftrags, der Ausgangssituation und des Projektumfangs", ln = 2, align = 'L')
pdf.set_font("Arial", size = fontsize5) 
pdf.multi_cell(weiteKommentar, hoeheKommentar, ergebnisKonkretisierungKommentar)   
pdf.set_font("Arial", size = fontsize4) 
pdf.cell(100, hoehe3, txt = tab2+ PunkteAusgabeFormatieren(ergebnisBeschreibung) +tab1+" Beschreibung der Prozessschritte", ln = 2, align = 'L')
pdf.set_font("Arial", size = fontsize5) 
pdf.multi_cell(weiteKommentar, hoeheKommentar, ergebnisBeschreibungKommentar)   
pdf.set_font("Arial", size = fontsize4) 
pdf.cell(100, hoehe3, txt = tab2+ PunkteAusgabeFormatieren(ergebnisDarstellung) +tab1+" Darstellung der Projektergebnisse und praxisbezogene", ln = 2, align = 'L') 
pdf.set_font("Arial", size = fontsize5) 
pdf.multi_cell(weiteKommentar, hoeheKommentar, ergebnisDarstellungKommentar) 
pdf.set_font("Arial", size = fontsizeNewLine)
pdf.cell(100, hoehe3, txt = "", ln = 2, align = 'L') 


#Prästenation
pdf.set_font("Arial", size = fontsize3)
pdf.cell(100, hoehe3, txt = "Präsentation und Fachgeschpräch", ln = 2, align = 'L') 
pdf.set_font("Arial", size = fontsize4)
pdf.cell(100, hoehe3, txt = tab2+ PunkteAusgabeFormatieren(ergebnisAufbau) +tab1+" Aufbau und inhaltliche Struktur", ln = 2, align = 'L') 
pdf.set_font("Arial", size = fontsize5) 
pdf.multi_cell(weiteKommentar, hoeheKommentar, ergebnisAufbauKommentar) 
pdf.set_font("Arial", size = fontsize4) 
pdf.cell(100, hoehe3, txt = tab2+ PunkteAusgabeFormatieren(ergebnisPraesentation) +tab1+" Präsentationstechnik", ln = 2, align = 'L') 
pdf.set_font("Arial", size = fontsize5) 
pdf.multi_cell(weiteKommentar, hoeheKommentar, ergebnisPraesentationKommentar) 
pdf.set_font("Arial", size = fontsize4)
pdf.cell(100, hoehe3, txt = "", ln = 2, align = 'L') 

#Endnote
pdf.set_font("Arial", size = fontsize1)
pdf.cell(100, hoehe3, txt = "Gesamtnote " + PunkteAusgabeFormatieren(endnote), ln = 2, align = 'L') 
pdf.cell(100, hoehe3, txt = "", ln = 2, align = 'L') 
pdf.cell(100, hoehe3, txt = "Berlin, " + DatumAusgeben(datum), ln = 2, align = 'L') 


#######
pathToFolder = os.getcwd()
pathToFile = pathToFolder + "\\" + pdfBezeichnung
print("File location using os.getcwd(): ", os.getcwd())

if exists(pathToFile):
    os.remove(pathToFile)

# save the pdf with name .pdf
pdf.output(pdfBezeichnung)   

#ToDo: Kommazahlen fomatieren (mit leerzeichen)
#ToDo File überschreiben

#ToDo Fehler wenn datei schon vorhanden (erledigt?!)
#ToDo Kommentar auf gleicher höhe wie

