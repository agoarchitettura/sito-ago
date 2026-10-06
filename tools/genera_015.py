"""Genera la scheda 015 (Palazzina Le Torri, Pollenza) da 07 PUBBLICAZIONE SUL SITO."""
import os,yaml
from PIL import Image,ImageOps,ImageChops,ImageEnhance
SRC="/mnt/ago/AGO Lavori/015PR04AR - ERP Consorzio Le Torri - Pollenza/07 PUBBLICAZIONE SUL SITO/"
OUT="src/content/progetti/palazzina-le-torri/"
os.makedirs(OUT+"img",exist_ok=True)
def salva(im,n,w,q=84):
    im=im.convert("RGB"); r=w/im.width
    if r<1: im=im.resize((w,round(im.height*r)),Image.LANCZOS)
    im.save(OUT+"img/"+n+".jpg","JPEG",quality=q,optimize=True,progressive=True)
def apri(f): return ImageOps.exif_transpose(Image.open(SRC+f)).convert("RGB")
def rifila(im,taglio=0.035,margine=60):
    """toglie la cornice della tavola e il bianco in eccesso, lascia un margine uniforme"""
    w,h=im.size; im=im.crop((int(w*taglio),int(h*taglio),int(w*(1-taglio)),int(h*(1-taglio))))
    g=ImageOps.invert(im.convert("L")).point(lambda v:255 if v>40 else 0); b=g.getbbox()
    im=im.crop(b); c=Image.new("RGB",(im.width+2*margine,im.height+2*margine),"white"); c.paste(im,(margine,margine)); return c
def tavola(f):
    """tavola CAD: rifilata e con il tratto un po' più deciso"""
    return ImageEnhance.Contrast(rifila(apri(f))).enhance(1.25)
def pianta(f,lato=1300):
    """pianta d'alloggio su un quadrato bianco uguale per tutte"""
    im=rifila(apri(f),taglio=0,margine=0); im.thumbnail((lato-120,lato-120),Image.LANCZOS)
    c=Image.new("RGB",(lato,lato),"white"); c.paste(im,((lato-im.width)//2,(lato-im.height)//2)); return c
# viste di progetto (render): ritocco leggero di contrasto
for n,f in {"lt-contesto":"v04.jpg","lt-strada":"v01.jpg","lt-risalita":"v03.jpg","lt-terrazza":"v05.jpg"}.items():
    salva(ImageEnhance.Contrast(apri(f)).enhance(1.04),n,1600)
im=apri("v04.jpg"); h=im.height; w=round(h*4/3); x=im.width-w-20
salva(im.crop((x,0,x+w,h)),"lt-copertina",1000)
for n,f in {"lt-alloggio-a":"planimetria-letorri3_page-0001.jpg","lt-alloggio-b":"planimetria-letorri4_page-0001.jpg",
            "lt-alloggio-c":"planimetria-letorri12_page-0001.jpg","lt-villino":"planimetria-letorri14_page-0001.jpg"}.items():
    salva(pianta(f) if n!="lt-villino" else rifila(apri(f)),n,1300)
for n,f in {"lt-v116-prospetto":"V1 16_page-0001.jpg","lt-v115-sezione":"V1 15_page-0001.jpg",
            "lt-v105-pianta":"V1 05_page-0001.jpg","lt-v108-copertura":"V1 08_page-0001.jpg"}.items():
    salva(tavola(f),n,2400)
def F(n,c): return {"img":f"./img/{n}.jpg","didascalia":c}
sez=[
 {"titolo":"Un opificio a mezza costa","testo":[
  "Pollenza sta in cima a un colle. Sul margine sud del centro storico, quasi di fronte alla Porta del Colle, una scarpata separa il nucleo antico dalla zona di espansione residenziale cresciuta in basso. A metà della scarpata c'era un opificio abbandonato, visibile da lontano e da vicino.",
  "Intorno, l'area chiamata «Le Torri»: interventi edilizi sparsi, alcuni di edilizia residenziale pubblica, e strade che si muovono per conto loro, indifferenti alle case e al centro storico. Un luogo senza «effetto città», in cui chi ci abita fatica a riconoscersi.",
  "Il Contratto di Quartiere II «Complesso Le Torri», promosso dal Comune di Pollenza e finanziato dalla Regione Marche e dal Ministero delle Infrastrutture, mette insieme interventi pubblici e privati con un solo obiettivo: ricucire la valle e il centro storico. La palazzina è la parte privata del programma: dieci alloggi di edilizia residenziale agevolata, destinati alla locazione o al godimento per almeno otto anni, al posto dell'opificio."],
  "tuttoschermo":[F("lt-contesto","Vista di progetto: la palazzina sotto il centro storico, con il primo ascensore e l'ex Casali-Battaglia")]},
 {"titolo":"Ricucire la valle e il centro storico","testo":[
  "Il lotto si trova alla quota d'arrivo del primo dei due ascensori che salgono dalla valle al centro storico, già realizzati dal Comune. È il punto in cui le persone cambiano mezzo, si fermano, guardano il paesaggio: per questo la palazzina diventa il fulcro del programma.",
  "Accanto agli ascensori, due risalite pedonali: una rampa a pendenza unica con una scalinata, lungo il lato nord del lotto, fino ai giardini davanti alla Porta del Colle; e un percorso in rampe sulla scarpata, costruito con opere di ingegneria naturalistica e pochi muri di sostegno. La copertura del nuovo locale per i box auto diventa una terrazza pubblica lungo il percorso.",
  "Tutto il programma è pensato per abbattere le barriere architettoniche: chi abita a valle deve poter salire al centro storico senza ostacoli."],
  "extra":"le-torri-risalita",
  "tuttoschermo":[F("lt-risalita","Vista di progetto: il primo ascensore, il percorso pedonale e i box interrati con i muri in gabbioni")]},
 {"titolo":"Tredici alloggi","testo":[
  "L'opificio era in condizioni troppo cattive per un recupero ragionevole. Si è scelto di demolirlo e ricostruire: una scelta che pesa per le macerie, da riciclare in cantiere, ma che lascia libero il progetto di concepire un edificio a basso impatto ambientale fin dalle fondamenta.",
  "Il progetto del Contratto di Quartiere prevedeva dieci alloggi e un locale commerciale al piano terra, con un parcheggio sotterraneo per i residenti, così da non caricare le strade vicine. Nel 2012 una variante con il «Piano Casa» regionale ha aggiunto un piano alla palazzina e un piccolo villino su due livelli: in tutto tredici alloggi, da 46 a 121 metri quadrati.",
  "La palazzina con il piano in più resta comunque sotto la quota di calpestio dei giardini comunali: chi guarda la valle dal centro storico continua a vederla."],
  "extra":"le-torri-volumi",
  "figure":[F("lt-alloggio-a","Un alloggio con due camere"),F("lt-alloggio-b","Un alloggio con una camera"),F("lt-alloggio-c","Un secondo taglio con due camere"),F("lt-villino","Il villino, piano terra e piano primo")],
  "tabella":[{"voce":"Piano seminterrato","valore":"10 box auto, cantine, locali tecnici"},{"voce":"Piano terra","valore":"2 alloggi"},{"voce":"Piani primo e secondo","valore":"3 alloggi per piano"},{"voce":"Piano terzo (aggiunto)","valore":"2 alloggi"},{"voce":"Piano attico","valore":"2 alloggi"},{"voce":"Villino (aggiunto)","valore":"1 alloggio su due livelli"},{"voce":"Locale interrato","valore":"3 box auto"}],
  "nota_tabella":"Superficie utile complessiva degli alloggi: 1.015,66 m²."},
 {"titolo":"Il fronte a sud","testo":[
  "Verso sud e verso la valle la palazzina si apre con logge e balconi, protetti da un brise-soleil: una struttura in acciaio con lamelle frangisole in cotto, su cui scorrono le tende esterne che oscurano gli alloggi. Il cotto richiama i mattoni del centro storico; la struttura leggera ripara gli alloggi dal sole estivo senza chiuderli.",
  "Verso nord, contro la paratia che trattiene la scarpata, stanno la scala e l'ascensore, staccati dall'edificio e collegati ai piani da passerelle in acciaio. La copertura è a un'unica falda, con il manto in rame e i collettori solari; al centro, davanti all'attico, una terrazza.",
  "Le pareti esterne, i solai e i serramenti sono progettati per una bassa trasmittanza: tamponamenti con isolante continuo, solai coibentati e con feltro anticalpestio, serramenti in alluminio con vetrocamera."],
  "figure":[F("lt-terrazza","Vista di progetto: la terrazza dell'attico verso la valle")],
  "tuttoschermo":[F("lt-strada","Vista di progetto: la strada di accesso, il villino e la palazzina con il brise-soleil")]},
 {"titolo":"Una sperimentazione ITACA","testo":[
  "Il Contratto di Quartiere II riservava una quota di finanziamento pubblico alla sperimentazione. Per la palazzina, una delle prime applicazioni del protocollo ITACA all'edilizia residenziale pubblica, le scelte ambientali sono misurate requisito per requisito: acqua calda dal sole, acqua piovana per gli usi che non richiedono acqua potabile, consumi contati alloggio per alloggio.",
  "Ogni alloggio ha due reti d'acqua: quella potabile e quella dell'acqua piovana, raccolta dal tetto, filtrata e accumulata in una cisterna per le cassette dei wc, le lavatrici e le lavastoviglie. Il risciacquo resta sempre con acqua potabile. L'acqua piovana, poco calcarea, chiede anche meno detersivo.",
  "Il programma di sperimentazione prevedeva sopralluoghi e rapporti in tre fasi di cantiere, a confronto con lo stesso tipo di impianti installati nel vicino complesso ex Casali-Battaglia, un edificio storico in muratura recuperato dal Comune: un edificio progettato da subito per ospitarli e uno tradizionale da adattare."],
  "extra":"le-torri-risorse"},
 {"titolo":"Un progetto sulla carta","testo":[
  "Il protocollo d'intesa del Contratto di Quartiere è stato firmato in Regione il 28 aprile 2007, insieme a quelli di altri quattro comuni marchigiani. L'intervento è stato finanziato e autorizzato e ha ottenuto il permesso di costruire anche per la variante, ma non è stato realizzato.",
  "Restano il progetto e il metodo: un edificio di edilizia agevolata pensato come pezzo di città, che lega la valle e il centro storico e misura le proprie prestazioni ambientali."]},
]
meta={"titolo":"Palazzina Le Torri","sottotitolo":"Tredici alloggi di edilizia residenziale agevolata nel Contratto di Quartiere II, Pollenza",
 "sintesi":"Al posto di un opificio abbandonato sotto il centro storico, una palazzina di edilizia agevolata all'arrivo dell'ascensore dalla valle: brise-soleil in cotto, acqua piovana, sole, protocollo ITACA.",
 "categoria":"Nuova edificazione","stato":"Progetto","luogo":"Pollenza","anni":"2007–2013","committente":"Privato","in_evidenza":False,"ordine":15,
 "copertina":"./img/lt-copertina.jpg","apertura":"./img/lt-contesto.jpg","carosello":["./img/lt-contesto.jpg","./img/lt-strada.jpg"],
 "dati":[{"voce":"Luogo","valore":"Pollenza (MC), margine sud del centro storico"},{"voce":"Anni","valore":"2007–2013"},{"voce":"Stato","valore":"Progetto autorizzato, non realizzato"},
  {"voce":"Committente","valore":"Privato (edilizia residenziale agevolata)"},
  {"voce":"Programma","valore":"Contratto di Quartiere II «Complesso Le Torri», Comune di Pollenza"},
  {"voce":"Ruolo dello studio","valore":"Progetto architettonico (capogruppo), sperimentazione ITACA, variante «Piano Casa»"},
  {"voce":"Con","valore":"arch. Antonio Pagnanelli · arch. Daniela Giammarco (gruppo di progettazione)"},
  {"voce":"Responsabile del procedimento","valore":"ing. Federico Canullo"},
  {"voce":"Impresa","valore":"Scisciani & Frascarelli S.r.l."},
  {"voce":"Importo stimato delle opere","valore":"circa 1.800.000 €"},
  {"voce":"Alloggi","valore":"13 (10 nel programma, 3 con la variante)"},
  {"voce":"Finanziamento","valore":"Contratto di Quartiere II (L. 21/2001, D.M. 27/12/2001), quota pubblica per la sperimentazione"}],
 "sezioni":sez,"cronologia":[],"superfici":[],
 "disegni":[F("lt-v116-prospetto","Sezione longitudinale sulla scarpata, con il fronte sud"),F("lt-v115-sezione","Sezione trasversale, con la paratia e il corpo scale"),
  F("lt-v105-pianta","Pianta dei piani primo e secondo"),F("lt-v108-copertura","Pianta delle coperture, con i collettori solari")],
 "galleria":[]}
open(OUT+"index.md","w",encoding="utf-8").write("---\n"+yaml.safe_dump(meta,allow_unicode=True,sort_keys=False,width=100000)+"---\n")
print(sum(os.path.getsize(OUT+"img/"+f) for f in os.listdir(OUT+"img"))//1024,"KB immagini")
