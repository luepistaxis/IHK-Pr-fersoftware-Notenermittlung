#import fpdf
from fpdf import FPDF
   
#create object instance
pdf = FPDF()
  
#add page
pdf.add_page()
  
#variablen zur formatierung
hoehe0 = 17  
hoehe1 = 14  
hoehe2 = 11  
hoehe3 = 8
hoeheKommentar = 5
fontsize0 = 22
fontsize1 = 17
fontsize2 = 15
fontsize3 = 11
fontsize4 = 8
fontsizeNewLine = 2
tab = "\t\t"

#Variablen Person und Datum TEMPORÄR!!!
datum = 2022
name = "Alf Tanner von Melmac"
id = 1234567890

#Variablen (Zwischen-) Noten TEMPÖRÄR!!! bisherige bezeihcnungen
ergebnisAP1 = 42
ergebisPlanEintrag = 80.80
ergebnisEntwEintrag = 69
ergebnisWirtsEintrag = 39

# set font style and size
pdf.set_font("Arial", size = fontsize0)

# Überschrift IHK
pdf.cell(200, hoehe1, txt = "Industrie- und Handelskammer", ln = 1, align = 'L')
pdf.cell(114, hoehe1, txt = "Berlin " + str(datum) , ln = 2, align = 'L')

pdf.set_font("Arial", size = fontsize3) 
pdf.cell(100, hoehe3, txt = "Name: " + tab + name, ln = 2, align = 'L') 
pdf.cell(100, hoehe3, txt = "IHK-ID: "+ tab + str(id) +" ID12345", ln = 2, align = 'L') 
pdf.set_font("Arial", size = fontsizeNewLine)
pdf.cell(100, fontsizeNewLine, txt = "", ln = 2, align = 'L')

#Bewertungen
#Schriftliche Prüfung
#schr AP1
pdf.set_font("Arial", size = fontsize2) 
pdf.cell(100, hoehe2, txt = "Punkte"+tab+" Schriftliche Prüfungen", ln = 2, align = 'L')
pdf.set_font("Arial", size = fontsize3)
pdf.cell(100, hoehe3, txt = "AP1:", ln = 2, align = 'L')
pdf.set_font("Arial", size = fontsize4)
pdf.cell(100, hoehe3, txt = str(ergebnisAP1) + tab + " Einrichten eines IT-gestützten Arbeitsplatz", ln = 2, align = 'L') 
pdf.set_font("Arial", size = fontsizeNewLine) 
pdf.cell(100, hoehe3, txt = "", ln = 2, align = 'L')
pdf.set_font("Arial", size = fontsize3)

#schr AP2
pdf.cell(100, hoehe3, txt = "AP2:", ln = 2, align = 'L')
pdf.set_font("Arial", size = fontsize4)
pdf.cell(100, hoehe3, txt = str(ergebisPlanEintrag) +tab+" Planen eines Softwareprojekts", ln = 2, align = 'L') 
pdf.cell(100, hoehe3, txt = str(ergebnisEntwEintrag) +tab+" Entwicklung und Umsetzung von Algorithmen", ln = 2, align = 'L') 
pdf.cell(100, hoehe3, txt = str(ergebnisWirtsEintrag) + tab +" Wirtschafts- und Sozialkunde", ln = 2, align = 'L') 
pdf.set_font("Arial", size = fontsizeNewLine)
pdf.cell(100, hoehe3, txt = "", ln = 2, align = 'L')
pdf.set_font("Arial", size = fontsize2)

#Projekt
#Doku
pdf.cell(100, hoehe2, txt = "Planen und Umsetzen eines Softwareprojekts", ln = 2, align = 'L') 
pdf.set_font("Arial", size = fontsize3)
pdf.cell(100, hoehe3, txt = "Dokumentation", ln = 2, align = 'L')
pdf.set_font("Arial", size = fontsize4) 
pdf.cell(100, hoehe3, txt = "xy "+tab+" Gestaltung Projektbericht (äußere Form)", ln = 2, align = 'L') 
pdf.cell(100, hoeheKommentar, txt = "Kommentar: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", ln = 2, align = 'L') 
pdf.cell(100, hoehe3, txt = "xy "+tab+" Beschreibung des Auftrags, der Ausgangssituation und des Projektumfangs", ln = 2, align = 'L')
pdf.cell(100, hoeheKommentar, txt = "Kommentar: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", ln = 2, align = 'L')  
pdf.cell(100, hoehe3, txt = "xy "+tab+" Beschreibung der Prozessschritte", ln = 2, align = 'L')
pdf.cell(100, hoeheKommentar, txt = "Kommentar: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", ln = 2, align = 'L')  
pdf.cell(100, hoehe3, txt = "xy "+tab+" Darstellung der Projektergebnisse und praxisbezogene", ln = 2, align = 'L') 
pdf.cell(100, hoeheKommentar, txt = "Kommentar: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", ln = 2, align = 'L') 
pdf.set_font("Arial", size = fontsizeNewLine)
pdf.cell(100, hoehe3, txt = "", ln = 2, align = 'L') 
pdf.set_font("Arial", size = fontsize3)

#Prästenation
pdf.cell(100, hoehe3, txt = "Präsentation und Fachgeschpräch", ln = 2, align = 'L') 
pdf.set_font("Arial", size = fontsize4)
pdf.cell(100, hoehe3, txt = "xy "+tab+" Aufbau und inhaltliche Struktur", ln = 2, align = 'L') 
pdf.cell(100, hoeheKommentar, txt = "Kommentar: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", ln = 2, align = 'L') 
pdf.cell(100, hoehe3, txt = "xy "+tab+" Präsentationstechnik", ln = 2, align = 'L') 
pdf.cell(100, hoeheKommentar, txt = "Kommentar: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", ln = 2, align = 'L') 
pdf.set_font("Arial", size = fontsizeNewLine)
pdf.cell(100, hoehe3, txt = "", ln = 2, align = 'L') 

#Endnote
pdf.set_font("Arial", size = fontsize1)
pdf.cell(100, hoehe3, txt = "Endnote bezeichnung xy", ln = 2, align = 'L') 

# save the pdf with name .pdf
pdf.output("pdfZeugnis040.pdf")   

#ToDo: Kommentar in mehrere Spalten aufteilen, Kommazahlen fomatieren
