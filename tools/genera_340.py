"""Genera la scheda 340 (piazza Umberto I, Belforte del Chienti) da 26_PUBBLICAZIONE_SITO."""
import os,yaml
from PIL import Image,ImageOps
SRC="/mnt/ago/AGO Lavori/340PU22AU - Piazza Umberto I Belforte del Chienti (MC)/26_PUBBLICAZIONE_SITO/"
OUT="src/content/progetti/piazza-umberto-i/"
os.makedirs(OUT+"img",exist_ok=True)
IMG={ # nome: (file, larghezza)
 "pu-realizzato-01":("FOTO intervento realaizzato/20250919_DSC7481.jpg",2200),
 "pu-getti":("FOTO intervento realaizzato/IMG_20250601_155515652.jpg",2200),
 "pu-chiesa":("FOTO intervento realaizzato/Figura2.jpg",2200),
 "pu-fontana-raso":("FOTO intervento realaizzato/Figura4.jpg",2200),
 "pu-fontanile":("FOTO intervento realaizzato/20250919_DSC7487.jpg",1700),
 "pu-fontanile-bocche":("FOTO intervento realaizzato/20250919_DSC7516.jpg",1700),
 "pu-fontanile-largo":("FOTO intervento realaizzato/20250919_DSC7494.jpg",2000),
 "pu-chiesa-loggiato":("FOTO intervento realaizzato/20250919_DSC7532.jpg",1500),
 "pu-campanile":("FOTO intervento realaizzato/Figura3.jpg",1500),
 "pu-catasto-1835":("1835 ca Gregoriano 03.jpg",900),
 "pu-catasto-impianto":("1939 ca BELFORTE DEL CHIENTI_Foglio 019RR.jpg",1100),
 "pu-schema":("Schema di progetto 00.JPG",1100),
 "pu-modello-storica":("Vista modello porzione piazza storica.jpg",1100),
 "pu-modello-nuova":("Vista modello porzione piazza nuova.jpg",1400),
 "pu-planimetria":("Planimetira di progetto.png",1500),
 "pu-tavola-fontanile":("Tavola dettagli fontanile.JPG",1852),
 "pu-cantiere-20231214":("Cantiere/IMG_20231214_090812163-PANO.jpg",2200),
 "pu-cantiere-20240322":("Cantiere/IMG_20240322_105651900.jpg",1800),
 "pu-cantiere-20240613":("Cantiere/IMG_20240613_094043052.jpg",1500),
 "pu-cantiere-20241021":("Cantiere/IMG_20241021_115650926.jpg",1800),
 "pu-cantiere-20250418":("Cantiere/IMG_20250418_091631725.jpg",1800),
}
for n,(f,w) in IMG.items():
    im=ImageOps.exif_transpose(Image.open(SRC+f)).convert("RGB")
    r=w/im.width
    if r<1: im=im.resize((w,round(im.height*r)),Image.LANCZOS)
    im.save(OUT+"img/"+n+".jpg","JPEG",quality=82,optimize=True,progressive=True)
def F(n,c): return {"img":f"./img/{n}.jpg","didascalia":c}
sez=[
 {"titolo":"Rigenerare una piazza dopo il sisma","testo":[
  "Il progetto di riqualificazione di piazza Umberto I e delle vie limitrofe a Belforte del Chienti mostra come la ricostruzione post-sisma possa diventare una vera operazione di rigenerazione urbana. L'intervento rientra nella sub-misura A3 del Piano Nazionale Complementare (PNC) al PNRR, dedicata alla rinascita dei territori colpiti dagli eventi sismici del 2009 e del 2016.",
  "L'obiettivo dell'Amministrazione comunale non era ripristinare soltanto le superfici danneggiate, ma restituire alla collettività uno spazio pubblico identitario, capace di accogliere la vita sociale. Per questo l'accessibilità universale e la sostenibilità ambientale hanno guidato le scelte progettuali, verso una qualità diffusa e inclusiva dello spazio urbano.",
  "In questo quadro il progetto di Ago Architettura è un'azione di ricucitura filologica: riconfigura uno spazio reso indefinito dalle demolizioni del passato in un nuovo «interno urbano». Ne nasce un luogo che custodisce la memoria storica e la mette in dialogo con le esigenze della città di oggi, tra continuità e trasformazione."]},
 {"titolo":"Una piazza ferita dalle demolizioni","testo":[
  "Il nucleo storico di Belforte del Chienti sorge su un'altura panoramica, alla confluenza del torrente Fiastrone con il fiume Chienti. L'impianto urbano conserva ancora tracce dell'originario castrum medievale e della cinta muraria trecentesca, anche se è stato molto rimaneggiato nel tempo.",
  "Il confronto tra il Catasto Gregoriano (1835) e il Catasto d'impianto ha mostrato un vero «trauma» nella forma della piazza. Tra la fine dell'Ottocento e i primi decenni del Novecento le demolizioni sul fronte sud-occidentale, tra cui quella di una significativa «casa con corte», fecero perdere un margine edilizio compatto: un perimetro chiuso divenne uno spazio indefinito.",
  "A questo si erano aggiunti, negli anni Ottanta, interventi incongrui: pavimentazioni in klinker e alberi (tigli e cedri) le cui radici avevano via via compromesso le superfici, creando rischi per i passanti e limitando l'uso pedonale della piazza.",
  "La sfida era dunque restituire leggibilità alla piazza storica, intesa non solo come luogo fisico ma come spazio civico, «corpo» radicato nell'urbs e depositario dei valori della comunità."],
  "figure":[F("pu-catasto-1835","Il Catasto Gregoriano, 1835 circa"),F("pu-catasto-impianto","Il catasto d'impianto, inizio Novecento")]},
 {"titolo":"La memoria nel disegno del suolo","testo":[
  "Il progetto rinuncia a un disegno ex novo e restituisce la configurazione della piazza agli inizi dell'Ottocento: uno spazio diviso in due dall'asse viario, da un lato la piazza del Comune, dall'altro quella della chiesa di Sant'Eustachio.",
  "Il disegno del suolo evoca poi le impronte degli edifici demoliti, come documentate nel Catasto Gregoriano, e le trasforma in elementi attivi della nuova composizione. Quelle tracce definiscono due nuovi ambiti pubblici: un «palco» permanente di 9×9 metri, di fronte alla chiesa di Sant'Eustachio, con una torretta elettrica a scomparsa per concerti e spettacoli estivi; e un'area polifunzionale di circa 326 m², ombreggiata da sei bagolari, per attività collettive ed eventi.",
  "Anche il ridisegno della strada secondaria di accesso alla piazza ha ristabilito la leggibilità dell'antica trama urbana, rafforzando le relazioni spaziali tra le parti."],
  "figure":[F("pu-schema","Lo schema di progetto: le impronte degli edifici demoliti e i nuovi ambiti"),F("pu-modello-storica","Il modello della piazza storica"),F("pu-modello-nuova","Il modello della nuova piazza")]},
 {"titolo":"Pietra e laterizi del luogo","testo":[
  "Un'attenzione particolare è stata dedicata alla compatibilità dei materiali, discussa con la cittadinanza e con la Soprintendenza. Dal confronto è stata esclusa la pietra d'Istria, inizialmente ipotizzata per fasce, gradini e segnapassi.",
  "In coerenza con la tavolozza del borgo, fatta di pietra di gesso, arenaria e laterizi dal giallo paglierino al rosa e al rosso, si è scelta una pietra arenaria a grana compatta e laterizi tradizionali di recupero, lavorati a mano e posati con malta idraulica naturale. La nuova piazza ha così la stessa materia e lo stesso colore del contesto storico."],
  "tuttoschermo":[F("pu-chiesa","La piazza davanti alla chiesa di Sant'Eustachio")]},
 {"titolo":"L'acqua: la Fontana dei Fiumi","testo":[
  "La «Fontana dei Fiumi» è insieme un dispositivo funzionale e un segno simbolico, che evoca il rapporto fondativo tra Belforte del Chienti e il suo territorio. È fatta di due fontanili in laterizio, che rappresentano il torrente Fiastrone e il fiume Chienti; da qui l'acqua scende fino a confluire in una fontana a raso pavimento, che richiama il Lago di Santa Maria.",
  "Oltre al valore narrativo, la fontana migliora il microclima urbano: attenua le temperature estive e riduce l'effetto isola di calore.",
  "Un secondo sistema recupera le acque piovane: una cisterna raccoglie quelle delle coperture degli edifici comunali e le destina all'irrigazione automatizzata di alberi e prati, riducendo il consumo di acqua potabile."],
  "figure":[F("pu-fontanile","Uno dei fontanili in laterizio, con il fondo di ciottoli"),F("pu-fontanile-bocche","Le bocche del fontanile")],
  "tuttoschermo":[F("pu-fontana-raso","La fontana a raso pavimento")]},
 {"titolo":"Il cantiere e le scoperte","testo":[
  "Il cantiere ha posto domande tecniche e scientifiche, affrontate in un confronto costante tra la direzione lavori e gli enti di tutela, in un processo capace di integrare ciò che emergeva in corso d'opera.",
  "L'area ha un grado elevato di interesse archeologico, perciò tutti gli scavi sono stati eseguiti sotto sorveglianza specialistica. Sono emersi un piccolo vano interrato voltato in laterizio, di circa 4 m², la cantina di un edificio demolito, messa in sicurezza e poi tombata per il suo stato di conservazione; e un tratto fognario in cemento non censito e molto deteriorato, sostituito per intero per ridare stabilità al sottofondo e prevenire cedimenti.",
  "Le pavimentazioni della parte storica dialogano con le architetture. Davanti al Palazzo Comunale una maglia a griglia richiama gli assi dei loggiati seicenteschi; davanti alla chiesa di Sant'Eustachio fasce parallele seguono il ritmo dei contrafforti e la centralità del portale. In corso d'opera il progetto ha aggiunto una nuova scala e una rampa accessibile in pietra arenaria all'ingresso laterale della chiesa, che legano la scala esistente alla nuova pavimentazione."],
  "extra":"cronologia"},
 {"titolo":"Accessibile, luminosa, permeabile","testo":[
  "Il superamento delle barriere architettoniche è stato affrontato con un approccio prestazionale, secondo i principi dell'Universal Design: spazi pensati per un uso equo e inclusivo, con pendenze curate, superfici antiscivolo e soluzioni che garantiscono sicurezza e comfort nell'uso quotidiano.",
  "L'illuminazione a LED, con proiettori sotto gronda e segnapassi incassati, valorizza la piazza di notte e offre livelli adeguati di sicurezza e comfort visivo.",
  "Dal punto di vista ambientale, le maggiori superfici a verde hanno migliorato la permeabilità del suolo. La piazza risponde meglio alle piogge intense, riduce i ristagni e gli allagamenti superficiali, e rende il tessuto urbano più resiliente."]},
 {"titolo":"Custodire la memoria","testo":[
  "L'intervento su piazza Umberto I è un esempio riuscito di equilibrio tra restauro scientifico e rigenerazione urbana contemporanea. La ricomposizione filologica del tessuto, resa leggibile dal disegno del suolo e dalle impronte degli edifici demoliti, restituisce alla piazza la dignità di interno urbano, mentre le nuove funzioni sociali, il «palco» e il giardino polifunzionale, ridanno vita al perimetro storico perduto.",
  "I materiali locali, pietra arenaria e laterizi fatti a mano, armonizzano le superfici con il contesto. Il dialogo con le architetture monumentali, mediato dai motivi pavimentali, valorizza la gerarchia spaziale. I sistemi per la gestione sostenibile dell'acqua e il comfort microclimatico, insieme ai principi dell'Universal Design, garantiscono un uso sicuro, inclusivo e resiliente.",
  "L'intervento mostra che «custodire la memoria» non significa fissare lo spazio in un passato statico, ma saper leggere i segni del tempo per costruire territori più sicuri, inclusivi e resilienti, dove la comunità può riconoscersi di nuovo ed esercitare il proprio diritto di cittadinanza."]},
]
cron=[("14 dicembre 2023","Gli scavi","Lo scavo e i casseri in legno all'inizio dei lavori.","pu-cantiere-20231214"),
 ("22 marzo 2024","La pietra","La posa della pavimentazione in pietra, con gli scavi ancora aperti.","pu-cantiere-20240322"),
 ("13 giugno 2024","Il disegno del suolo","La pavimentazione in pietra con il suo disegno a ventaglio.","pu-cantiere-20240613"),
 ("21 ottobre 2024","Le scale","La scalinata in pietra arenaria e laterizio.","pu-cantiere-20241021"),
 ("18 aprile 2025","Il verde","Lo spazio verde ancora da sistemare, al termine dei lavori.","pu-cantiere-20250418")]
meta={"titolo":"Piazza Umberto I","sottotitolo":"Riqualificazione della piazza e delle vie del centro storico, Belforte del Chienti",
 "sintesi":"La piazza storica di Belforte del Chienti ricostruita sulle tracce degli edifici demoliti: pietra arenaria, laterizi fatti a mano, la Fontana dei Fiumi.",
 "categoria":"Arredo urbano e light design","stato":"Realizzato","luogo":"Belforte del Chienti","anni":"2022–2025","committente":"Comune di Belforte del Chienti","in_evidenza":True,"ordine":2.5,
 "copertina":"./img/pu-getti.jpg","apertura":"./img/pu-realizzato-01.jpg","carosello":["./img/pu-realizzato-01.jpg","./img/pu-getti.jpg"],
 "dati":[{"voce":"Luogo","valore":"Belforte del Chienti (MC), centro storico"},{"voce":"Anni","valore":"2022–2025"},{"voce":"Stato","valore":"Realizzato"},{"voce":"Committente","valore":"Comune di Belforte del Chienti"},
  {"voce":"Ruolo dello studio","valore":"Progetto definitivo ed esecutivo, direzione lavori, CAM e coordinamento della sicurezza"},{"voce":"Responsabile del procedimento","valore":"geom. Mauro Paglialunga"},
  {"voce":"Importo dei lavori","valore":"890.290,15 €"},{"voce":"Finanziamento","valore":"PNC, sub-misura A3 (ricostruzione post-sisma)"},{"voce":"Spazi","valore":"un palco di 9×9 m e un'area polifunzionale di circa 326 m²"}],
 "sezioni":sez,
 "cronologia":[{"data":a,"titolo":t,"testo":x,"img":f"./img/{i}.jpg"} for a,t,x,i in cron],
 "disegni":[F("pu-planimetria","Planimetria di progetto"),F("pu-tavola-fontanile","Dettagli dei fontanili")],
 "galleria":[F("pu-chiesa-loggiato","La chiesa e il loggiato dal fontanile"),F("pu-campanile","La torre dell'orologio specchiata nel fontanile"),F("pu-fontanile-largo","I fontanili e i gradini in laterizio")]}
# sezioni: assicura i campi vuoti ammessi
open(OUT+"index.md","w",encoding="utf-8").write("---\n"+yaml.safe_dump(meta,allow_unicode=True,sort_keys=False,width=100000)+"---\n")
print(sum(os.path.getsize(OUT+"img/"+f) for f in os.listdir(OUT+"img"))//1024,"KB immagini")
