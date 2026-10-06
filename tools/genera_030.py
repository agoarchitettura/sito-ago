"""Genera la scheda 030 (piazza Vittorio Emanuele II, Belforte del Chienti) da 10 PUBBLICAZIONE_SITO."""
import os,yaml
from PIL import Image,ImageOps
SRC="/mnt/ago/AGO Lavori/030PU05AR - DOCUP Piazza V. Emanuele - Belforte/10 PUBBLICAZIONE_SITO/"
OUT="src/content/progetti/piazza-vittorio-emanuele-ii/"
os.makedirs(OUT+"img",exist_ok=True)
def salva(im,n,w,q=84):
    im=im.convert("RGB"); r=w/im.width
    if r<1: im=im.resize((w,round(im.height*r)),Image.LANCZOS)
    im.save(OUT+"img/"+n+".jpg","JPEG",quality=q,optimize=True,progressive=True)
def apri(f): return ImageOps.exif_transpose(Image.open(SRC+f))
def pad45(im,bg=(255,255,255)):
    """porta l'immagine a proporzione 4:5 aggiungendo bordo bianco, senza ritagliare nulla"""
    im=im.convert("RGB"); w,h=im.size
    if w/h>0.8: H=round(w/0.8); W=w
    else: W=round(h*0.8); H=h
    c=Image.new("RGB",(W,H),bg); c.paste(im,((W-w)//2,(H-h)//2)); return c
std={"pu2-01":("Foto/01.jpg",1516),"pu2-00":("Foto/00.jpg",1737),"pu2-04":("Foto/04.jpg",1518),"pu2-02":("Foto/02.jpg",1483),"pu2-03":("Foto/03.jpg",1424),"pu2-05":("Foto/05.jpg",1024),
 "pu2-concetto-01":("schema concettuale 01.jpg",1243),"pu2-concetto-03":("schema concettuale 03.jpg",1244),"pu2-schema-posa":("Schema di posa 01.JPG",637),
 "pu2-cantiere-tracciamento":("Cantiere/DSC04993 traccamento ellissi con metodo giardiniere.JPG",1800),"pu2-cantiere-platea":("Cantiere/006.JPG",1800),
 "pu2-cantiere-selciato":("Cantiere/027.JPG",1800),"pu2-cantiere-mattoni":("Cantiere/050.JPG",1800),
 "pu2-pe04-planimetria":("PE 04 piante_page-0001.jpg",2600),"pu2-pe05-pantheon":("PE 05 piante det _page-0001.jpg",1398),"pu2-pe06-dettagli":("PE 06 piante det _page-0001.jpg",2600),"pu2-pe07-sezione":("PE 07 sezione 50 _page-0001.jpg",2600)}
for n,(f,w) in std.items(): salva(apri(f),n,w)
# copertina: ritaglio 4:3 centrato sul prato a lente
im=apri("Foto/01.jpg").convert("RGB"); h=im.height; w=round(h*4/3); x=330
salva(im.crop((x,0,x+w,h)),"pu2-copertina",1000)
salva(pad45(apri("schizzo idea schema progetto.jpg")),"pu2-schizzo",900)
salva(pad45(apri("Schema geometrico piazza.JPG")),"pu2-schema-geometrico",900)
def F(n,c): return {"img":f"./img/{n}.jpg","didascalia":c}
sez=[
 {"titolo":"Un'ellisse e un cerchio","testo":[
  "Piazza Vittorio Emanuele II, nel centro storico di Belforte del Chienti, è un luogo riparato e accogliente, raccolto in un giro di gelsi. Ma è anche uno spazio irregolare, senza una forma riconoscibile. I gelsi disegnano sul terreno due figure geometriche precise: un'ellisse al centro della piazza (28 metri l'asse maggiore, 16 il minore) e un cerchio di 6 metri di diametro nell'angolo meridionale.",
  "Chi visitava la piazza non le vedeva. Il terreno in pendenza e una serie di elementi incongrui le nascondevano: un parterre di bosso e alloro, due palme intorno al busto di Anselmo Ciappi nella metà est, una fontanella e i giochi dei bambini nella metà ovest. Il piccolo giro di gelsi, poi, aveva perso due delle sue sei piante: la sua forma circolare si riconosceva solo con il compasso su una planimetria.",
  "Il progetto parte da qui: riconfermare e sottolineare, rendendola percepibile, la geometria tracciata dai gelsi che restano."],
  "figure":[F("pu2-schizzo","Lo schizzo dell'idea: un'ellisse e un cerchio"),F("pu2-schema-geometrico","La geometria dell'ellisse, con i due fuochi")]},
 {"titolo":"Un anfiteatro e un piccolo pantheon","testo":[
  "Dalle stesse geometrie nascono due ambiti pubblici. Al centro, un anfiteatro ellittico: lo spazio pubblico per eccellenza, tradizionalmente destinato a spettacoli, manifestazioni e giochi. A sud, un piccolo pantheon, la cui forma circolare accoglie da sempre le personalità del luogo. Qui trova posto il busto di Anselmo Ciappi, rivolto verso la piazza e illuminato.",
  "Il busto ricollocato nel pantheon libera l'ellisse, che si legge finalmente per intero. La strada che la attraversa la divide in due metà, e ciascuna è distinta in due piani, con un dislivello di circa 45 centimetri, raccordati da rampe (al massimo del 10%) o da piccole scalinate tra i gelsi. I quattro ambiti sono orizzontali e rendono più facile l'uso di tutto lo spazio: i due più grandi sono prati, le due «lenti» minori sono pavimentate in ammattonato, come i passaggi tra le piante."],
  "figure":[F("pu2-concetto-01","Schema concettuale: l'anfiteatro ellittico e il pantheon"),F("pu2-concetto-03","Il pantheon con il busto di Anselmo Ciappi")],
  "tuttoschermo":[F("pu2-00","La piazza e i gelsi potati")]},
 {"titolo":"Il disegno sul campo","testo":[
  "L'ellisse è stata tracciata sul terreno con il «metodo del giardiniere»: due fuochi, una corda e un picchetto che la tende. È lo stesso procedimento con cui si disegna un'aiuola, portato alla scala di una piazza."],
  "figure":[F("pu2-cantiere-tracciamento","Il tracciamento dell'ellisse sul terreno"),F("pu2-cantiere-platea","L'armatura della pavimentazione circolare del pantheon")]},
 {"titolo":"Pietra, mattoni e prato","testo":[
  "Le pavimentazioni nascono dalla salvaguardia dei gelsi. Il selciato è posato direttamente sul piano esistente, su un sottofondo di sabbia e cemento di almeno 10 centimetri, senza variare le quote e senza massetto cementizio, che renderebbe la superficie troppo impermeabile e altererebbe l'equilibrio idrico del terreno sotto le piante.",
  "Il selciato è in blocchi di pietra arenaria (8×8 o 10×10 centimetri), simili a quelli del resto del centro storico, posati «ad archi contrastanti» come nelle pavimentazioni esistenti. Gli ammattonati sono in mattoni pieni fatti a mano, disposti di costa a spina di pesce e stuccati con calce e sabbia nei toni tradizionali del centro. Una fascia di mattoni a coltello, la zanella, corre lungo l'attacco a terra degli edifici, come già avveniva sul lato est. I prati sono realizzati a idrosemina.",
  "Lo stesso selciato sostituisce l'asfalto in via Giacomo Leopardi, la strada principale del centro storico, e dà continuità alla piazza."],
  "figure":[F("pu2-schema-posa","Lo schema di posa del selciato, ad archi contrastanti"),F("pu2-cantiere-selciato","La posa del selciato in pietra arenaria"),F("pu2-cantiere-mattoni","L'ammattonato di mattoni pieni, con il bordo curvo")],
  "extra":"superfici","tuttoschermo":[F("pu2-04","I gelsi, il prato e il selciato in pietra")]},
 {"titolo":"Arredi, luce, accessibilità","testo":[
  "Tre panchine in acciaio e legno trovano posto nei raccordi dell'anfiteatro. Dissuasori in ghisa, alti un metro, sottolineano il cerchio dei gelsi intorno al busto e il bordo della carreggiata che attraversa l'ellisse; una balaustra in ferro battuto, sul disegno di quelle del centro storico, corre per circa 10 metri sul muretto in pietra a ovest.",
  "L'illuminazione è stata riprogettata. Le lanterne moderne, di fattura scadente, sono sostituite da lanterne a parete con sbraccio in ghisa, simili a quelle già installate nel resto del centro. Nei dissuasori lungo la carreggiata sono inseriti dei led, lampade segnapasso a incasso segnano i raccordi dell'anfiteatro e due proiettori illuminano il monumento a Ciappi.",
  "Tutti gli spazi sono accessibili con raccordi a raso o con rampe di pendenza non superiore al 10%; solo i prati restano in piano."],
  "figure":[F("pu2-05","La rampa e la balaustra in ferro battuto lungo il muro di pietra")]},
 {"titolo":"Una geometria che si legge","testo":[
  "Oggi la piazza conserva il carattere di luogo riparato nel giro dei gelsi e mostra la sua geometria: due prati a forma di lente al centro, i passaggi in mattoni tra le piante, il selciato in pietra che prosegue in via Leopardi. È un intervento fatto con i materiali del centro storico e attento agli alberi esistenti, che accresce la capacità della piazza di ospitare eventi e manifestazioni."]},
]
meta={"titolo":"Piazza Vittorio Emanuele II","sottotitolo":"Riqualificazione della piazza e di un tratto di via Leopardi, Belforte del Chienti",
 "sintesi":"Un'ellisse e un cerchio disegnati dai gelsi, resi finalmente leggibili: un anfiteatro verde, un piccolo pantheon, selciato di pietra e mattoni fatti a mano.",
 "categoria":"Arredo urbano e light design","stato":"Realizzato","luogo":"Belforte del Chienti","anni":"2006–2007","committente":"Comune di Belforte del Chienti","in_evidenza":True,"ordine":30,
 "copertina":"./img/pu2-copertina.jpg","apertura":"./img/pu2-01.jpg","carosello":["./img/pu2-01.jpg","./img/pu2-04.jpg"],
 "dati":[{"voce":"Luogo","valore":"Belforte del Chienti (MC), centro storico"},{"voce":"Anni","valore":"2006–2007"},{"voce":"Stato","valore":"Realizzato"},{"voce":"Committente","valore":"Comune di Belforte del Chienti"},
  {"voce":"Ruolo dello studio","valore":"Progetto esecutivo (capogruppo) e direzione lavori"},{"voce":"Con","valore":"arch. Antonio Pagnanelli (gruppo di progettazione)"},{"voce":"Responsabile del procedimento","valore":"geom. Mauro Paglialunga"},
  {"voce":"Impresa esecutrice","valore":"F.lli Deangelis G.R. S.n.c."},{"voce":"Importo dei lavori","valore":"107.925,77 €"},{"voce":"Finanziamento","valore":"DOCUP Marche 2000–2006, Obiettivo 2, Asse 3, Misura 3.5 (centri storici)"}],
 "sezioni":sez,"cronologia":[],
 "superfici":[{"voce":"Prato (piazza)","mq":258.80},{"voce":"Selciato (piazza)","mq":224.30},{"voce":"Selciato (via Giacomo Leopardi)","mq":210.00},{"voce":"Ammattonato (piazza)","mq":105.00},{"voce":"Scale e gradini in ammattonato","mq":28.00}],
 "disegni":[F("pu2-pe04-planimetria","Pianta della piazza"),F("pu2-pe05-pantheon","Pianta e sezione del pantheon"),F("pu2-pe06-dettagli","Particolari della pavimentazione e sezioni"),F("pu2-pe07-sezione","Sezione sulla piazza, con gli elementi di arredo")],
 "galleria":[F("pu2-02","I gelsi e il prato a lente"),F("pu2-03","Il prato, la strada e i gelsi")]}
open(OUT+"index.md","w",encoding="utf-8").write("---\n"+yaml.safe_dump(meta,allow_unicode=True,sort_keys=False,width=100000)+"---\n")
print(sum(os.path.getsize(OUT+"img/"+f) for f in os.listdir(OUT+"img"))//1024,"KB immagini")
