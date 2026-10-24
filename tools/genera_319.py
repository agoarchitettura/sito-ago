"""Genera la scheda 319 (Chiesa dell'Immacolata, Macerata) da 20_PUBBLICAZIONE_SITO."""
import os,yaml
from PIL import Image,ImageOps,ImageFilter,ImageDraw
Image.MAX_IMAGE_PIXELS=None
SRC="/mnt/ago/AGO Lavori/319PR21RE - Chiesa Immacolata/20_PUBBLICAZIONE_SITO/"
SL=SRC+"220721_Presentazione_page-%04d.jpg"
OUT="src/content/progetti/chiesa-dellimmacolata/"
os.makedirs(OUT+"img",exist_ok=True)

def salva(im,n,w,q=86,nitidezza=True):
    im=im.convert("RGB")
    r=w/im.width
    if r!=1: im=im.resize((w,round(im.height*r)),Image.LANCZOS)
    if nitidezza: im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=55,threshold=2))
    im.save(OUT+"img/"+n+".jpg","JPEG",quality=q,optimize=True,progressive=True)
def foto(f): return ImageOps.exif_transpose(Image.open(SRC+f))
def slide(p,box): return Image.open(SL%p).crop(box)

# cantiere 2026: solo la parte alta (soffitto), senza le persone in lavorazione
cant=foto("IMG_20260908_122929970_HDR.jpg")
salva(cant.crop((0,20,1299,480)),"q-cantiere",1800)
# rilievo a colori del cassettonato
ril=foto("Rilievo cassettonato_01.JPG")
salva(ril.crop((440,0,1380,705)),"q-copertina",1300,nitidezza=False)
salva(ril,"q-rilievo",1813,nitidezza=False)
# dettagli delle modanature (tavola ad alta risoluzione)
tav=Image.open(SRC+"tav05_dettagli.png").convert("RGB")
salva(tav,"d-modanature",2400,nitidezza=False)
# sezione trasversale della chiesa
salva(slide(5,(590,90,1400,760)),"d-sezione",1300,nitidezza=False)
# modelli di studio dell'ordito ligneo
salva(slide(12,(100,150,1400,760)),"d-modelli",1800,nitidezza=False)
# disegni strutturali (8: tolto il cartiglio in alto a destra)
d8=Image.open(SRC+"8.JPG").convert("RGB"); dr=ImageDraw.Draw(d8); dr.rectangle((d8.width-110,0,d8.width,90),fill="white")
salva(d8,"d-capriata",2000,nitidezza=False)
d9=Image.open(SRC+"9.JPG").convert("RGB").crop((120,0,1179,696))
salva(d9,"d-navata-laterale",1800,nitidezza=False)
# stato di fatto del soffitto (dalla presentazione del 21/07/2022; riprese di sopralluogo)
salva(slide(16,(408,236,750,758)),"q-lesione",700)
salva(slide(16,(1095,240,1422,762)),"q-mensola",700)
salva(slide(19,(597,238,990,760)),"q-giglio",760)
salva(slide(20,(993,185,1445,789)),"q-rosone",760)
salva(slide(20,(55,185,507,789)),"q-camorcanna",760)
salva(slide(22,(931,211,1478,760)),"q-fregio",1100)

def F(n,c): return {"img":f"./img/{n}.jpg","didascalia":c}

sez=[
 {"titolo":"Una basilica neorinascimentale","testo":[
  "La chiesa dell'Immacolata sorge a Macerata, su corso Cavour. Il progetto è dell'architetto fermano Giuseppe Rossi: approvato nel 1893, con la posa della prima pietra il 20 agosto. La chiesa è aperta al pubblico nel 1895, ancora senza facciata né decorazioni, e inaugurata il 20 agosto 1905. Nel 1898 mons. Jacoboni stipula il capitolato delle decorazioni di soffitto, cornicioni, archi e capitelli con Lorenzo Natali, che le esegue su disegni e modelli del Rossi. La facciata arriva nel 1917, in graniglia di cemento, con i mosaici delle lunette di Angelo Gianese e le cinque statue di Giulio Tadolini. La torre campanaria prevista non è mai stata costruita: al suo posto resta un campanile a vela, nato come soluzione provvisoria.",
  "L'impianto è basilicale, a tre navate con abside e cappelle laterali: 30 metri di lunghezza per 22 di larghezza, e una facciata alta circa 22,5. I muri sono di mattoni, spessi 50 centimetri dal piede alla sommità; otto colonne monolitiche di marmo rosso Verona reggono le arcate. All'interno ogni superficie è decorata, in marmi, stucchi e pitture."],
  "figure":[F("d-sezione","Sezione trasversale: la navata centrale, con il soffitto a quota 15,40 m, e le navate laterali")]},
 {"titolo":"Un soffitto di stucco","testo":[
  "Il soffitto a cassettoni della navata centrale misura circa 19,35 per 8,12 metri e si imposta a 15,40 metri da terra. Una maglia di 5 per 14 moduli quadrati, di circa 126 centimetri di passo, ospita al centro l'altorilievo ligneo della Vergine; ai lati, due croci con gli stemmi del vescovo Giambattista Ricci e di papa Leone XIII. I cassettoni restanti sono di tre tipi, diversi per il fondo, azzurro o rosso, e per il rosone che porta ciascuno. Le navate laterali, a quota 9 metri, ripetono su ogni campata un modulo di tre metri per tre, con nove cassettoni di forme diverse. Il gusto è quello archeologico di fine Ottocento: su una base gialla, fondi rossi e azzurri, decori bianchi, modanature dorate.",
  "Il soffitto è tutto in stucco. Sul fondo c'è un'incannucciata: una stuoia di canne, inchiodata a un ordito di travi e travicelli, su cui sono modellati gli strati di gesso, a stampo o tirati con la sagoma. I rosoni e i fiori pendenti sono legati con filo di ferro. L'intera struttura è appesa alle capriate del tetto con diciotto catene, per lo più non in tensione: l'ordito di legno è nato per portare da solo il peso, e le catene fanno da presidio. Le superfici decorate sono quasi 600 metri quadrati."],
  "tuttoschermo":[F("q-rilievo","Il rilievo a colori del soffitto: la navata centrale, con le croci e il campo centrale, e parte delle navate laterali")],
  "figure":[F("d-modelli","Modello di studio dell'ordito ligneo del soffitto, visto dall'estradosso")],
  "extra":"immacolata-superfici"},
 {"titolo":"Il danno e il rilievo","testo":[
  "Dopo il sisma del 2016 la chiesa risultò danneggiata in modo lieve nell'insieme: le murature spesse e regolari, la facciata e il campanile a vela hanno risposto bene. Il danno si è concentrato in alto, nelle murature sopra le sei finestre dell'aula e nei soffitti: lesioni passanti sulle chiavi d'arco, una lesione sull'arcone trionfale, e sui cassettoni lesioni diffuse, elementi in stucco disconnessi o in pericolo di caduta, fiori pendenti in equilibrio precario.",
  "Il progetto parte da un rilievo ravvicinato del soffitto, dal basso e dall'alto. Sopra il soffitto non c'è un piano calpestabile e si entra da un solo accesso, in cima all'arcone trionfale: per ispezionarlo è stato costruito un camminamento provvisorio ancorato alle capriate. Si misurano geometrie, modanature e colore di ogni tipo di cassettone, e per le strutture di copertura si fanno indagini sul degrado biologico del legno e prove resistografiche."],
  "figure":[F("q-lesione","Una lesione sul fregio, sotto la finestra"),F("q-mensola","Lesione e distacco su una mensola, misurati sul posto"),F("q-giglio","Un fiore pendente con la lesione alla base"),F("q-rosone","Un rosone staccato: l'ancoraggio era un filo di ferro"),F("q-camorcanna","L'estradosso: stuoia di canne, tavolato e malta")],
  "tuttoschermo":[F("d-modanature","Le modanature rilevate in sezione, con le misure dei profili: cassettone, cornici e mensola")]},
 {"titolo":"Sostenere senza toccare","testo":[
  "Il progetto segue i criteri del restauro critico: distinguibilità, reversibilità, compatibilità, minimo intervento. Le travi del soffitto sono sottodimensionate e deformate, ma sostituirle o rinforzarle, con il peso di stucco che portano, avrebbe voluto dire scuotere la decorazione. Si è scelto di lasciarle dove sono e di sostenere il soffitto dall'alto.",
  "Le capriate e gli arcarecci della navata centrale sono consolidati con profili d'acciaio affiancati al legno, in modo da poter portare, se serve, l'intero peso del soffitto. Da lì scendono i pendini: 80 sulla navata centrale, uno a ogni incrocio delle coste, e 20 per ciascuna navata laterale. Sono trefoli d'acciaio che finiscono all'intradosso in una piastra quadrata d'acciaio inox di dieci centimetri di lato, nascosta sotto i fiori pendenti. Per posarla bisogna smontare i fiori, che vengono poi rimontati su un perno inox saldato alla piastra; il tratto di gesso che coprivano è ricostruito. Gli ancoraggi esistenti, chiodi e fili di ferro ossidati, sono verificati uno per uno e, dove serve, sostituiti da perni, trefoli o cavi in kevlar, in posizioni che non si vedono. Ogni nuovo ancoraggio è mappato."],
  "tuttoschermo":[F("d-capriata","La capriata della navata centrale: profili d'acciaio affiancati al legno e, in rosso, le funi che reggono il soffitto"),F("d-navata-laterale","Lo stesso principio sotto la falda di una navata laterale")],
  "extra":"immacolata-sospensione"},
 {"titolo":"Restaurare le superfici","testo":[
  "Sugli stucchi policromi e dorati il restauro è conservativo: rimozione dei depositi con metodi delicati, preconsolidamento della pellicola pittorica e delle dorature, riadesione di scaglie e frammenti, microstuccatura delle fessure, consolidamento degli intonaci con iniezioni dove non aderiscono più al supporto. Le parti mancanti del modellato sono integrate su calco degli originali; le lacune di colore sono reintegrate in modo mimetico, e dove manca l'oro si applica la foglia. Prima di ogni pulitura si fanno test e indagini stratigrafiche: sono esclusi prodotti e metodi aggressivi.",
  "Lo stesso approccio vale per le opere in legno e per i dipinti su tela, con lavorazioni descritte una per una nel progetto. Le tre voci sono quelle che a cantiere compongono il restauro delle superfici decorate."],
  "figure":[F("q-fregio","Il fregio di una navata laterale: stucco dipinto e dorato, con le riprese di restauri precedenti")]},
 {"titolo":"Sei fasi di cantiere","testo":[
  "Il progetto distingue sei fasi. Il soffitto resta al suo posto per tutto il tempo: prima si mette in sicurezza e si sostiene, poi si restaura."],
  "tabella":[
   {"voce":"1 · Ponteggi interni","valore":"Piani di lavoro sotto il soffitto e camminamenti ancorati alle capriate sopra; mappatura fotografica prima dei lavori; distacco degli elementi pericolanti"},
   {"voce":"2 · Capriate","valore":"Consolidamento con profili d'acciaio affiancati al legno"},
   {"voce":"3 · Pendinatura diffusa","valore":"Posa dei pendini dall'intradosso ai vertici dei cassettoni; rimontaggio dei fiori pendenti"},
   {"voce":"4 · Estradosso","valore":"Pulitura e restauro, con controllo dell'ordito ligneo e dell'incannucciata"},
   {"voce":"5 · Cassettonato","valore":"Restauro delle superfici decorate: stucchi, pitture, dorature"},
   {"voce":"6 · Passerella","valore":"Una passerella sopra il soffitto, per le manutenzioni future"}],
  "nota_tabella":"Fasi secondo la presentazione del progetto, luglio 2022.",
  "tuttoschermo":[F("q-cantiere","La navata centrale dal piano di lavoro, a settembre 2026")]},
 {"titolo":"Quello che i ponteggi hanno mostrato","testo":[
  "Montati i ponteggi, il quadro è cambiato. Le superfici verticali di navate e presbiterio (stucchi, intonaci, apparati decorativi) risultano molto più compromesse del previsto: lesioni, distacchi, elementi pericolanti da rimuovere in sicurezza. Anche le vetrate, con gli infissi lignei deformati dal sisma, e le lastre di marmo rosso Verona, staccate dal supporto, chiedono un intervento.",
  "Durante il rinforzo delle capriate è emerso un cordolo sommitale in calcestruzzo senza armatura, che corre lungo il perimetro: ha capacità strutturale molto limitata e compromette il comportamento scatolare dell'edificio. La risposta è una cerchiatura in profili d'acciaio, continua e collegata alle capriate.",
  "Il 5 giugno 2026, in un sopralluogo congiunto con la Soprintendenza, con la direzione dei lavori e l'impresa, la situazione è stata verificata sul posto e la Soprintendenza ha espresso parere favorevole alla variante. La variante, ancora in definizione, impiega le somme del ribasso d'asta per restaurare le superfici verticali, per la cerchiatura e per rifare gli impianti di illuminazione, amplificazione e videosorveglianza, che i lavori avevano reso da smontare; vi rientra anche il progetto degli arredi. L'importo complessivo dell'intervento resta invariato."]},
]
cron=[
 {"data":"1893","titolo":"Il progetto","testo":"Il progetto dell'architetto Giuseppe Rossi è approvato; il 20 agosto è posta la prima pietra."},
 {"data":"20 agosto 1905","titolo":"L'inaugurazione","testo":"La chiesa, aperta al pubblico dal 1895, è inaugurata.","img":"./img/q-rilievo.jpg"},
 {"data":"1917","titolo":"La facciata","testo":"In graniglia di cemento, con mosaici e statue."},
 {"data":"2016","titolo":"Il sisma","testo":"La scheda del danno ai beni culturali è del 30 novembre."},
 {"data":"30 settembre 2021","titolo":"L'incarico","testo":"Il gruppo di progettazione, guidato da Ago Architettura, riceve l'incarico."},
 {"data":"Gennaio 2023","titolo":"La relazione generale","testo":"Rilievo, quadro del danno e progetto del consolidamento e del restauro del soffitto.","img":"./img/d-modanature.jpg"},
 {"data":"5 giugno 2025","titolo":"Il contributo","testo":"Decreto di concessione del contributo, n. 526."},
 {"data":"Luglio 2025","titolo":"I lavori","testo":"Il cantiere si avvia."},
 {"data":"5 giugno 2026","titolo":"Il sopralluogo","testo":"Con la Soprintendenza, sul ponteggio: la variante prende forma."},
 {"data":"Settembre 2026","titolo":"Il soffitto sotto restauro","testo":"La navata centrale dal piano di lavoro.","img":"./img/q-cantiere.jpg"},
 {"data":"Dicembre 2026","titolo":"La fine dei lavori","testo":"Data prevista dalla notifica di cantiere."},
]
meta={"titolo":"Chiesa dell'Immacolata",
 "sottotitolo":"Riparazione dei danni sismici e restauro del soffitto a cassettoni di una chiesa neorinascimentale, Macerata",
 "sintesi":"Un soffitto di stucco di quasi seicento metri quadrati, appeso alle capriate del tetto con centoventi pendini d'acciaio: sostenere ciò che c'è, senza toccarlo, e restaurarlo.",
 "categoria":"Restauro","stato":"In costruzione","luogo":"Macerata, corso Cavour","anni":"Dal 2021","committente":"Diocesi di Macerata-Tolentino-Recanati-Cingoli-Treia",
 "in_evidenza":False,"ordine":319,
 "copertina":"./img/q-copertina.jpg","apertura":"./img/q-cantiere.jpg","carosello":["./img/q-cantiere.jpg","./img/q-copertina.jpg"],
 "dati":[{"voce":"Luogo","valore":"Macerata, corso Cavour"},{"voce":"Anni","valore":"Dal 2021"},{"voce":"Stato","valore":"In costruzione"},
  {"voce":"Committente","valore":"Diocesi di Macerata-Tolentino-Recanati-Cingoli-Treia"},
  {"voce":"Ruolo dello studio","valore":"Coordinamento del gruppo di progetto, progetto architettonico, direzione dei lavori, coordinamento della sicurezza"},
  {"voce":"Con","valore":"ing. Chiara Antolini (progetto e direzione lavori delle strutture) · ing. Aldo Tuzio (impianti) · geol. Daniele Piatti (indagini geologiche)"},
  {"voce":"Importo dei lavori","valore":"887.910,71 € in appalto"},
  {"voce":"Intervento","valore":"Riparazione dei danni e miglioramento sismico, Ordinanza n. 105/2020 del Commissario straordinario per la ricostruzione"},
  {"voce":"Tutela","valore":"Edificio di culto di interesse storico-artistico, con opere decorative: lavori sotto la sorveglianza della Soprintendenza"}],
 "sezioni":sez,"cronologia":cron,"superfici":[],"disegni":[],"galleria":[]}
open(OUT+"index.md","w",encoding="utf-8").write("---\n"+yaml.safe_dump(meta,allow_unicode=True,sort_keys=False,width=100000)+"---\n")
print(sum(os.path.getsize(OUT+"img/"+f) for f in os.listdir(OUT+"img"))//1024,"KB immagini")
