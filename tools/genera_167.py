"""Genera la scheda 167 (Palazzetto Liberty, Macerata) da 71_PUBBLICAZIONE_SITO."""
import os,yaml
from PIL import Image,ImageOps,ImageFilter
Image.MAX_IMAGE_PIXELS=None
SRC="/mnt/ago/AGO Lavori/167PR17RE - Palazzo p.zza Mazzini - Macerata/+ EDIT/71_PUBBLICAZIONE_SITO/"
OUT="src/content/progetti/palazzetto-liberty/"
os.makedirs(OUT+"img",exist_ok=True)

def salva(f,n,w,crop=None,q=86,nitidezza=False):
    im=ImageOps.exif_transpose(Image.open(SRC+f)).convert("RGB")
    if crop: im=im.crop(crop)
    r=w/im.width
    if r!=1: im=im.resize((w,round(im.height*r)),Image.LANCZOS)
    if nitidezza: im=im.filter(ImageFilter.UnsharpMask(radius=1.4,percent=60,threshold=2))
    im.save(OUT+"img/"+n+".jpg","JPEG",quality=q,optimize=True,progressive=True)

# fotografie dell'opera finita (sorgenti di ~1000 px: ingrandite con cura, non oltre 1,5x)
salva("c003 post opera.jpg","q-hero",1488,crop=(0,40,992,701),nitidezza=True)            # 3:2
salva("03 Foto prospetti piazza Mazzini.png","q-copertina",1300,crop=(0,0,1086,814),nitidezza=True)  # 4:3
salva("03 Foto prospetti piazza Mazzini.png","q-angolo",1086)
salva("c003 post opera.jpg","q-post",992)
# prima
salva("a001 condizioni originarie.jpg","q-storica",1500)
salva("b002 ante opera .jpg","q-ante",896)
# tavola della scelta del colore: senza il piè di pagina con il nome dell'intestatario
salva("167_scelta colori copia.jpg","q-colori",2400,crop=(0,300,4961,3140))
# cantiere
salva("IMG_20230111_154941844.jpg","q-scala-archi",1800)
salva("IMG_20241129_093209613.jpg","q-cantonale",1800)
salva("IMG_20241129_093724088_HDR.jpg","q-rosoni",1800)
# interni
salva("DSCN6311.JPG","q-scala-acciaio",1600)
salva("DSCN6374.JPG","q-attico",1600)
salva("IMG_20250916_103636841_HDR.jpg","q-cucina",1800)
# disegni
salva("Dettaglio str P3.JPG","d-murature-p3",906)
salva("Dettaglio strutture copertura.JPG","d-nodo-copertura",1162)
salva("Dettaglio ventaglia.JPG","d-ventaglia",1271)
salva("Dettaglio str SCALA P4.JPG","d-scala",1050)
salva("gronda dett A 02.jpg","d-gronda-a",1800)
salva("gronda dett B 02.jpg","d-gronda-b",1800)

def F(n,c): return {"img":f"./img/{n}.jpg","didascalia":c}

sez=[
 {"titolo":"Un palazzetto di piazza","testo":[
  "A Macerata, in piazza Mazzini, a ridosso della porta urbica, sorge un palazzetto di cinque piani fuori terra. I suoi locali interrati poggiano sulle mura cittadine di epoca rinascimentale; più in alto, la costruzione è il risultato di rifusioni successive. Ancora nell'Ottocento erano due edifici affiancati; ai primi del Novecento ne contava quattro, di piani. Negli anni Trenta fu sopraelevato di uno e rifuso in un'unica facciata in stile liberty sulla piazza, che allora si chiamava piazza del Littorio.",
  "È una facciata semplice e armoniosa. Il cantonale è stondato e porta due medaglioni, a metà altezza e in sommità. Un alto bugnato in malta, dalla finitura rustica, regge i primi due piani; sopra, riquadri romboidali e cornici legano a due a due le aperture, e un balcone poggia su quattro mensole. In cima l'altana segna l'angolo, e la gronda termina in una ventaglia di rame, sotto la quale è un tavolato con una serie di rosoni."],
  "figure":[F("q-storica","Il palazzetto in una fotografia storica"),F("q-ante","Il palazzetto prima dei lavori, con la finitura rosa a tinta unita")],
  "extra":"mazzini-fasi"},
 {"titolo":"Il sisma e la scelta di conservare","testo":[
  "L'edificio è in muratura portante, con muri a sacco in mattoni pieni, solai di legno e una copertura lignea a padiglione parzialmente spingente. Dopo gli eventi sismici del 24 agosto 2016 e successivi risultava temporaneamente inagibile (scheda AeDES, esito B, marzo 2017). Dopo il sisma del 1997 un risanamento aveva già rinforzato alcuni solai e inserito due catene.",
  "L'intervento è un miglioramento sismico con restauro delle facciate, ai sensi dell'Ordinanza n. 19/2017 del Commissario straordinario per la ricostruzione. Il metodo è dichiarato nella relazione di progetto: un costante avvicinamento alla realtà materica dell'edificio, in cui ogni scelta progettuale ed esecutiva trova riscontro diretto nel manufatto, misurato e verificato di volta in volta. L'edificio è classificato A2 dal Piano di recupero del centro storico, tra quelli di interesse storico-artistico non soggetti a vincolo monumentale: l'intervento ammesso è il risanamento conservativo."],
  "figure":[F("q-scala-archi","Il vano scala, a muratura vista durante i lavori: archi rampanti in laterizio")]},
 {"titolo":"Strutture: riparare con i materiali dell'edificio","testo":[
  "Le strutture sono riparate, integrate o sostituite con materiali analoghi o compatibili, e dove possibile con tecniche tradizionali, completate dai presìdi antisismici necessari. Le lesioni e le nicchie sono ricucite con lo scuci-cuci; al piano interrato un sotto-arco e un contrafforte in mattoni pieni sostengono l'arco più sollecitato. I solai più degradati sono rifatti in legno, con travi di massello o di lamellare, e collegati alle murature; volte e archi sono rinforzati all'intradosso con rete d'acciaio e geomalta.",
  "A ogni piano una cerchiatura in profili d'acciaio, ancorata alla muratura e alle travi principali, e controventi metallici formano la «scatola muraria» che prima mancava. Le pareti perimetrali sono placcate a fasce con tessuto in fibra d'acciaio e cucite con diatoni artificiali; i muri di spina hanno l'intonaco armato; un cordolo in acciaio corre in sommità, dove non c'erano né cordoli né solette."],
  "figure":[F("d-murature-p3","Le murature del piano terzo: interventi sui muri e impalcato a quota +13,45 m"),F("d-scala","La scala metallica verso il piano quarto: sezione e particolari")]},
 {"titolo":"Una copertura nuova, la ventaglia al suo posto","testo":[
  "La copertura è sostituita: nuova orditura principale in legno lamellare, elementi secondari e controventi in acciaio all'estradosso, tavolato in abete, guaina impermeabilizzante, coibentazione e i coppi di riuso ricollocati. Serve a renderla adeguata alle azioni sismiche e, insieme, alle prestazioni energetiche richieste.",
  "La ventaglia di rame e il tavolato con i rosoni, che per il progetto sono tra gli elementi più qualificanti del palazzetto, sono smontati e rimontati. Gronde, pluviali e discendenti, in buono stato, sono rimontati nella stessa posizione; solo il discendente del fronte sud si sposta a monte, sul confine con l'edificio adiacente."],
  "figure":[F("q-rosoni","Il tavolato con i rosoni sotto la gronda, visto dal ponteggio"),F("d-ventaglia","Sezione della nuova copertura: il pacchetto sopra la ventaglia"),F("d-nodo-copertura","Il particolare del nodo di colmo, con l'appoggio del cosciale")],
  "schizzi":[],
  "tuttoschermo":[F("d-gronda-a","La gronda, modello tridimensionale del particolare (1)"),F("d-gronda-b","La gronda, modello tridimensionale del particolare (2)")]},
 {"titolo":"Il colore ritrovato","testo":[
  "Sulle facciate verso la piazza gli elementi decorativi sono quelli che più qualificano il palazzetto, e la loro lettura ha guidato il progetto. La tinta rosa uniforme che le copriva non era quella originaria. Una fotografia degli anni Trenta, i giunti stilati ancora leggibili sull'intonaco e edifici coevi della città mostrano che l'edificio nasceva con una finta cortina laterizia: un intonaco stilato, dipinto a velature su ogni singolo mattone, dal giallo al rosso, con cornici e partiture di un colore chiaro e gli infissi a contrasto.",
  "Il progetto ripristina quella finitura, ripara cornici e bugnato con modine, ne consolida i medaglioni e tinteggia paraste, cornici e bugnato basamentale tono su tono, per restituire la profondità di piano. Gli infissi sono ora grigio tortora, in accordo con le bugne e i riquadri sotto le finestre. Il fronte sud, su piazza Nazario Sauro, è in mattoni a faccia vista in buono stato: è prevista la sola pulitura."],
  "tuttoschermo":[F("q-colori","Scelta del colore: la fotografia storica, lo stato prima dei lavori, l'elaborazione grafica dell'intervento")],
  "figure":[F("q-cantonale","Il cantonale stondato con la finta cortina in corso di esecuzione")]},
 {"titolo":"Come si dipinge una cortina","testo":[
  "Il progetto descrive la finta cortina in dieci passaggi. Le fasi, riassunte qui, sono precedute da saggi di caratterizzazione: l'analisi petrografica e la diffrattometria XRD delle malte, e le prove di aderenza degli intonaci."],
  "tabella":[
   {"voce":"Il fondo","valore":"Una mano di acido cloridrico diluito 1:10, poi neutralizzato con una soluzione di allume"},
   {"voce":"L'acqua","valore":"La superficie è bagnata abbondantemente la sera prima e di nuovo al mattino"},
   {"voce":"Le tinte","valore":"Tre strati molto diluiti, a spruzzo, con una bagnatura fra uno e l'altro, secondo le coloriture e gli schemi concordati con la direzione dei lavori"},
   {"voce":"La velatura","valore":"Uno strato di pittura a base di latte di calce"},
   {"voce":"I giunti","valore":"Risegnati con il chiodo, dove serve"},
   {"voce":"La protezione","valore":"Un ultimo strato di resine acriliche in soluzione"}],
  "nota_tabella":"Fasi previste dal progetto del 2021; i toni sono stati definiti in cantiere con la direzione lavori."},
 {"titolo":"Dentro, la variante","testo":[
  "Nel corso dei lavori le unità immobiliari hanno cambiato in più punti la distribuzione interna, con pareti e controsoffitti a secco. Al quarto piano i controsoffitti sono stati demoliti e non ricostruiti: le falde e le travi di copertura restano a vista nelle parti basse, vicino alla gronda. Una scala leggera in acciaio, di profili scatolari ancorati alla muratura, sale al sottotetto, ad uso dell'alloggio del quarto piano.",
  "Altri interventi sono di cucitura e di ripristino dei prospetti: tre piccole aperture murate sul fronte est, prive di funzione e in contrasto con il ripristino strutturale, sono chiuse a scuci-cuci; due finestre tamponate soltanto dall'interno, che avevano conservato persiane e scuri, sono riaperte; le tre bacheche in alluminio anodizzato del negozio al piano terra sono sostituite da due in acciaio color ferro micaceo, ai lati dell'ingresso, e il prospetto principale ne resta libero."],
  "figure":[F("q-scala-acciaio","La scala in acciaio, con il lucernario"),F("q-attico","Un soggiorno sotto la copertura, con le travi a vista"),F("q-cucina","Un alloggio ultimato: il solaio in legno a vista")]},
 {"titolo":"Dal sisma alla fine dei lavori","testo":[
  "Il percorso, dall'ordinanza di inagibilità alla sua revoca, è durato dieci anni."],
  "extra":"cronologia"},
]
cron=[
 {"data":"Anni Trenta","titolo":"La facciata liberty","testo":"L'edificio è sopraelevato e rifuso in un'unica facciata sulla piazza.","img":"./img/q-storica.jpg"},
 {"data":"24 agosto 2016","titolo":"Il sisma","testo":"Al sisma seguono, nel marzo 2017, la scheda AeDES con esito B e, il 17 luglio 2017, l'ordinanza di inagibilità n. 313."},
 {"data":"Agosto 2018","titolo":"Il livello operativo","testo":"Richiesta di valutazione preventiva, con esito favorevole: livello operativo L3."},
 {"data":"Febbraio 2021","titolo":"Il progetto","testo":"Relazione tecnico-illustrativa del progetto di miglioramento sismico e restauro delle facciate.","img":"./img/q-colori.jpg"},
 {"data":"Novembre 2021","titolo":"Il contributo","testo":"Decreto di concessione del contributo, n. 6795 del 26 novembre."},
 {"data":"26 febbraio 2022","titolo":"L'inizio dei lavori","testo":"Il cantiere apre con un tempo previsto di ventiquattro mesi."},
 {"data":"Gennaio 2023","titolo":"Il vano scala","testo":"Le murature sono a vista, con gli archi rampanti in laterizio.","img":"./img/q-scala-archi.jpg"},
 {"data":"Novembre 2024","titolo":"Le facciate sotto il ponteggio","testo":"Prende forma la finta cortina del cantonale; sotto la gronda, i rosoni.","img":"./img/q-cantonale.jpg"},
 {"data":"Marzo 2025","titolo":"La variante","testo":"Presentata la perizia di variante, prot. n. 30645 del 4 marzo."},
 {"data":"25 agosto 2026","titolo":"La fine dei lavori","testo":"Il 26 agosto sono trasmessi agibilità, collaudo e certificazioni; l'8 settembre l'ordinanza di inagibilità è revocata.","img":"./img/q-hero.jpg"},
]
meta={"titolo":"Palazzetto Liberty",
 "sottotitolo":"Miglioramento sismico e restauro delle facciate di un palazzetto di piazza Mazzini, Macerata",
 "sintesi":"Un palazzetto degli anni Trenta riparato con i materiali e le tecniche dell'edificio: murature ricucite, solai e copertura in legno, e la finta cortina laterizia delle facciate ritrovata.",
 "categoria":"Restauro","stato":"Realizzato","luogo":"Macerata, piazza Mazzini","anni":"2018–2026","committente":"Privato (condominio)",
 "in_evidenza":False,"ordine":167,
 "copertina":"./img/q-copertina.jpg","apertura":"./img/q-hero.jpg","carosello":["./img/q-hero.jpg","./img/q-copertina.jpg"],
 "dati":[{"voce":"Luogo","valore":"Macerata, piazza Mazzini"},{"voce":"Anni","valore":"2018–2026"},{"voce":"Stato","valore":"Realizzato"},
  {"voce":"Committente","valore":"Privato (condominio)"},
  {"voce":"Ruolo dello studio","valore":"Progetto architettonico, direzione dei lavori, coordinamento della sicurezza"},
  {"voce":"Con","valore":"ing. Ainelen Daniela Bracalente (progetto strutturale) · ing. Giorgio Del Brutto (direzione lavori strutturale) · arch. Maria Francesca Iurescia (collaborazione al progetto)"},
  {"voce":"Impresa","valore":"Sardellini Costruzioni S.r.l."},
  {"voce":"Importo dei lavori ammessi","valore":"1.137.913,37 € (IVA esclusa), all'avvio dei lavori"},
  {"voce":"Intervento","valore":"Miglioramento sismico, Ordinanza n. 19/2017 del Commissario straordinario per la ricostruzione"},
  {"voce":"Tutela","valore":"Edificio di interesse storico-artistico (classe A2 del Piano di recupero del centro storico), accanto a una porta urbica vincolata"}],
 "sezioni":sez,"cronologia":cron,"superfici":[],
 "disegni":[],"galleria":[]}
open(OUT+"index.md","w",encoding="utf-8").write("---\n"+yaml.safe_dump(meta,allow_unicode=True,sort_keys=False,width=100000)+"---\n")
print(sum(os.path.getsize(OUT+"img/"+f) for f in os.listdir(OUT+"img"))//1024,"KB immagini")
