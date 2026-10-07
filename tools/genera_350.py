"""Genera la scheda 350 (Parco e giardino storico di Villa La Quiete, Treia) da 18 PUBBLICAZIONE_SUL_SITO."""
import os,yaml
from PIL import Image,ImageOps
Image.MAX_IMAGE_PIXELS=None
SRC="/mnt/ago/AGO Lavori/350PU22RE - Parco Storico di villa  La Quiete - Treia (MC)/18 PUBBLICAZIONE_SUL_SITO/"
OUT="src/content/progetti/parco-villa-la-quiete/"
os.makedirs(OUT+"img",exist_ok=True)
def salva(f,n,w,q=84):
    im=ImageOps.exif_transpose(Image.open(SRC+f)).convert("RGB"); r=w/im.width
    if r<1: im=im.resize((w,round(im.height*r)),Image.LANCZOS)
    im.save(OUT+"img/"+n+".jpg","JPEG",quality=q,optimize=True,progressive=True)
SF="Selezione Foto/"; C="Cantiere/"; IL=SF+"Foto illuminazione/"
img={
 # foto finite
 "q-orto-aerea":(SF+"Orto pomario 01.jpg",2400),"q-orto-arco":(SF+"Orto pomario 03.jpg",2000),"q-orto-ortive":(SF+"Orto pomario 04.jpg",1532),
 "q-orto-muro":(SF+"Orto pomario 02.jpg",1532),
 "q-atrio-viale":(SF+"Atrio ingresso 02.jpg",2400),"q-atrio":(SF+"Atrio ingresso 01.jpg",1532),
 "q-giardiniere-viale":(SF+"Casa del Giardiniere 02.jpg",2000),"q-giardiniere":(SF+"Casa del Giardiniere 04.jpg",2000),
 "q-roseto":(SF+"Roseto 01.jpg",2400),"q-roseto-colonne":(SF+"Roseto 02.jpg",1532),"q-roseto-villa":(SF+"Roseto 03.jpg",1532),
 "q-serra":(SF+"Serra 02.jpg",2400),"q-gazebo":(SF+"Gazebo 01.jpg",2000),"q-gazebo-interno":(SF+"Gazebo 02.jpg",2400),
 # cantiere
 "q-serra-profilo-ossidato":(C+"Serra/IMG_20231116_102229295.jpg",1600),"q-serra-merli":(C+"Serra/IMG_20241008_115956769_HDR.jpg",1400),
 "q-serra-profili-nuovi":(C+"Serra/IMG_20250129_163646552_HDR.jpg",1800),"q-serra-profili-nuovi2":(C+"Serra/IMG_20250129_163728710_HDR.jpg",1800),
 "q-serra-cantiere":(C+"Serra/IMG_20250505_124304108.jpg",1800),
 "q-gazebo-crollo":(C+"Gazebo/IMG_20240119_110834144.jpg",1800),"q-gazebo-macerie":(C+"Gazebo/IMG_20240125_100724438.jpg",1800),
 "q-gazebo-laterizi":(C+"Gazebo/IMG_20240430_113511454_HDR.jpg",1600),"q-gazebo-gru":(C+"Gazebo/IMG_20250404_112657299_HDR.jpg",1600),
 "q-gazebo-rame":(C+"Gazebo/IMG_20250522_174902042_HDR.jpg",1800),"q-gazebo-pavimento":(C+"Gazebo/IMG_20250621_164823877_HDR.jpg",1800),
 "q-colonne-scalone":(C+"Colonne/IMG_20240201_081140082.jpg",1800),"q-colonna-abaco":(C+"Colonne/IMG_20240321_120543791_HDR.jpg",1600),
 "q-colonna-sfere":(C+"Colonne/IMG_20250609_170022361_HDR.jpg",1600),"q-colonna-finita":(C+"Colonne/IMG_20250621_164056679.jpg",1400),
 "q-colonna-finita2":(C+"Colonne/IMG_20250621_164136628_HDR.jpg",1400),"q-colonne-viale":(C+"Colonne/IMG_20250621_164154775.jpg",2200),
 "q-muro-scarnito":(C+"Muri/IMG_20240422_112327951.jpg",1800),"q-muro-archi":(C+"Muri/IMG_20241120_152102207_HDR.jpg",2000),
 "q-muro-nicchioni":(C+"Muri/IMG_20250527_112407424_HDR.jpg",2000),
 "q-pav-campioni":(C+"Pavimentazioni/IMG_20250224_160321817.jpg",1800),"q-pav-griglia":(C+"Pavimentazioni/IMG_20250225_144839512.jpg",1400),
 "q-vasca":(C+"Pavimentazioni/IMG_20250606_112406432.jpg",1800),"q-pav-orto":(C+"Pavimentazioni/IMG_20250609_172455001_HDR.jpg",2400),
 "q-parapetto-curvo":(C+"Parapetti/IMG_20250621_163430727_HDR.jpg",1800),"q-parapetto-orto":(C+"Parapetti/IMG_20250621_163539152_HDR.jpg",1800),
 # luce
 "q-luce-planimetria":("planimetria illuminazione.jpg",2600),"q-luce-profili":("profili illuminazione 01.jpg",2600),
 "q-luce-orto":(IL+"IMG_20250424_212812213~2.jpg",1400),"q-luce-viale":(IL+"IMG_20250424_213130534~2.jpg",1400),
 "q-luce-scalone":(IL+"IMG_20250424_210114001.jpg",1400),"q-luce-viale2":(IL+"original_282c7778-2934-452a-bf41-37414cedbe8a_IMG_20250424_203954495.jpg",1479),
 # disegni e rendering di progetto
 "q-tav-planimetria":("350_TAV_VAR 01_ARC 01_Planimetria_generale_R06_page-0001.jpg",2600),
 "q-tav-gazebo":("350_TAV_VAR 01_ARC 02_Gazebo_Neogotico_R04_page-0001.jpg",2600),
 "q-tav-serra":("350_TAV_VAR 01_ARC 03_Serra_Neogotica_R03_page-0001.jpg",2600),
 "q-colonna-disegno":("Colonna onoraria.JPG",567),
 "q-render-serra":("serra5.png",1920),"q-render-gazebo":("gazebo inerno copertura.png",1920),
}
for n,(f,w) in img.items(): salva(f,n,w)
# copertina 4:3 dalla vista aerea dell'orto (gia' 4:3)
salva(SF+"Orto pomario 01.jpg","q-copertina",1000)
def F(n,c): return {"img":f"./img/{n}.jpg","didascalia":c}
RP="Rendering di progetto: "
sez=[
 {"titolo":"Mille anni di storie","testo":[
  "Villa La Quiete sorge a Treia, in contrada San Marco Vecchio, su un sito di cui si hanno notizie dal 1036, quando vi è attestata la chiesa di San Savino. Nel 1578 la chiesa entra a far parte di un convento di frati cappuccini, soppresso in epoca napoleonica. Nel 1812 il gonfaloniere Luigi Angelini acquista il convento e ne affida la trasformazione a Giuseppe Valadier: nasce la villa neoclassica, con il loggiato a due piani sul fronte orientale.",
  "L'assetto del parco si deve soprattutto al conte Lavinio de' Medici Spada, che la possiede dal 1828 al 1864: prelato, mineralogista, segretario della Società Romana di Orticoltura. Ne fa un luogo di sperimentazione botanica e di architetture eclettiche, dalla Casa del Giardiniere alla serra e al gazebo neogotici. Dopo un lungo abbandono nel Novecento il complesso viene acquisito dal Comune di Treia, nel 2016."],
  "tuttoschermo":[F("q-atrio-viale","Il viale d'ingresso, tra le quinte di lecci")]},
 {"titolo":"Restaurare un monumento vivente","testo":[
  "L'intervento, finanziato dal PNRR (M1C3, investimento 2.3, «parchi e giardini storici»), considera il parco un monumento vivente: architetture, murature, alberi e coltivazioni sono tutti materiale di restauro. Si opera secondo la Carta di Firenze e le Linee guida per il restauro dei giardini storici, con l'obiettivo di riportare il parco a uno «stato normale» documentabile, quello del suo disegno storico.",
  "Le scelte nascono da un processo di avvicinamento progressivo al manufatto: indagini diagnostiche su intonaci e malte, campionature in sito, sopralluoghi congiunti e un dialogo costante con la Soprintendenza. Per questo il progetto esecutivo, del dicembre 2022, è cambiato in corso d'opera, sempre nella direzione di conservare di più e aggiungere di meno. I materiali sono quelli della tradizione locale (legno, acciaio, laterizio, calce naturale), scelti per durabilità, manutenibilità e compatibilità."]},
 {"titolo":"Quattro ambiti, un solo disegno","testo":[
  "Il parco si articola in quattro ambiti, che il progetto rilegge insieme. L'atrio d'ingresso è una macchina scenografica: un tridente di viali, chiuso da una quinta di lecci, converge sulla Casa del Giardiniere, un arco trionfale eclettico su tre livelli affiancato da due coppie di propilei. Attorno alla Casa di Villa, disegnata da Valadier, si dispongono i giardini formali e il roseto. L'orto pomario è un giardino pensile sostenuto da imponenti murature di sostruzione, con la serra neogotica. In alto, il bosco cappuccino conserva i tracciati cinquecenteschi del convento e custodisce il gazebo neogotico."],
  "figure":[F("q-atrio","L'atrio d'ingresso, con il tridente dei viali"),F("q-giardiniere-viale","La Casa del Giardiniere in fondo al viale"),F("q-giardiniere","La Casa del Giardiniere, restaurata")]},
 {"titolo":"Il roseto","testo":[
  "Sul retro della villa un giardino semicircolare ospita il roseto storico e conduce al bosco, attraverso lo scalone a tenaglia inquadrato dalle colonne onorarie. Le antiche cultivar di rose e camelie sono state reintrodotte sulla base del catalogo ottocentesco di Raffaele Amicucci, con lo stesso criterio filologico che guida il restauro delle architetture: il recupero dell'agrobiodiversità è parte del recupero del monumento.",
  "I viali sono in ghiaia stabilizzata e la vasca al centro del roseto è stata tinteggiata di un giallo chiaro, accordato alle tonalità originali della facciata della villa, su indicazione della Soprintendenza."],
  "figure":[F("q-roseto-colonne","Le due colonne onorarie che inquadrano il roseto"),F("q-roseto-villa","Il roseto e la Casa di Villa, il cui restauro è in corso"),F("q-vasca","La vasca al centro del roseto")],
  "tuttoschermo":[F("q-roseto","Il roseto visto dall'alto")]},
 {"titolo":"L'orto pomario","testo":[
  "L'orto pomario è un giardino pensile racchiuso dai muri di sostruzione. Il progetto ne ripristina la funzione di serbatoio di agrobiodiversità, con antiche cultivar di fruttiferi e specie ortive allevate con le tecniche ottocentesche del «fusetto» e del «vaso basso», ricavate dai cataloghi storici. I parterre sono definiti da bordure in laterizio fatto a mano; le antiche vasche diventano bacini di accumulo per l'irrigazione, che sfrutta le acque meteoriche captate dalle architetture vicine.",
  "I parapetti in ferro lavorato hanno un disegno semplice e lineare, con finitura opaca color corten: montanti in quadrelli da 30 mm, come nella tradizione, e piattine di controvento per la resistenza richiesta dalle norme. Il percorso è accessibile; i viali sono in ghiaia stabilizzata con bordure in acciaio corten."],
  "figure":[F("q-orto-arco","Un arco in ferro corten, tra le ortive"),F("q-orto-ortive","Le ortive e il muro di sostruzione sullo sfondo"),F("q-parapetto-curvo","Il parapetto sul muro curvo dell'orto"),F("q-parapetto-orto","Il muro curvo e il parapetto, visti dall'orto")],
  "tuttoschermo":[F("q-orto-aerea","L'orto pomario visto dall'alto")]},
 {"titolo":"Murature che reggono il giardino","testo":[
  "Il parco è sostenuto da murature controterra di sei tipologie diverse, riconducibili a varie fasi edilizie. Molte erano degradate, per perdita di legante, erosione e crolli, aggravati dal sisma del 2016 e dalle radici degli alberi. Sono state lavate a bassissima pressione, scarnite nelle connessure incoerenti e riprese con conci in arenaria o laterizi simili agli esistenti.",
  "La malta è stata scelta dopo l'analisi di sette campioni prelevati da porzioni indisturbate di muratura ottocentesca: una calce idraulica naturale di colore nocciola chiaro, come l'originale. Le connessure sono stuccate «a raso» con la faccia dei conci, secondo la pratica costruttiva locale, che protegge meglio pietra e laterizio dall'erosione. Alcune lavorazioni previste sono state escluse in corso d'opera: il consolidante superficiale, per l'eccessiva umidità delle murature, e le velature di armonizzazione cromatica, perché i muri, ai primi cicli di umidità e di lavaggio, hanno acquisito da soli le variazioni di colore tipiche dell'invecchiamento naturale."],
  "figure":[F("q-muro-scarnito","Il paramento con le connessure scarnite, prima della ripresa"),F("q-muro-archi","La muratura con le arcate, a lavori ultimati"),F("q-muro-nicchioni","Il muro di sostruzione dopo il restauro")],
  "tuttoschermo":[F("q-orto-muro","Le murature di sostruzione sul fronte dell'orto pomario")]},
 {"titolo":"La serra neogotica","testo":[
  "Nell'orto pomario sorge la serra neogotica: un edificio in muratura portante con due torri merlate alla ghibellina e un volume un tempo vetrato, che serviva a ricoverare agrumi e piante esotiche. Aveva perso la copertura vetrata.",
  "Le indagini hanno confermato una finitura originaria rosso mattone, a base di ossidi di ferro. In sede esecutiva, d'intesa con la Soprintendenza, si è scelto di non ricostruirla e di mantenere la muratura a faccia vista, conservando tutte le tracce di intonaco ancora presenti: nessuna integrazione mimetica.",
  "Lo stesso criterio vale per la struttura. I profili in acciaio di fine Ottocento, pur ossidati agli appoggi, sono stati mantenuti e affiancati da nuovi profili, che portano i carichi senza alterare l'aspetto storico della serra. La nuova copertura vetrata ha profili sottili in acciaio con taglio termico e vetri di sicurezza, e parti apribili per regolare la temperatura. Tutti i metalli hanno una finitura opaca ferro-micacea, simile a quella originaria."],
  "figure":[F("q-serra-profilo-ossidato","Un profilo ottocentesco di acciaio, ossidato all'appoggio nella muratura"),F("q-serra-merli","Le merlature, danneggiate, prima del restauro"),F("q-serra-profili-nuovi","I nuovi profili in acciaio, affiancati agli esistenti"),F("q-render-serra",RP+"la serra con la nuova copertura vetrata")],
  "tuttoschermo":[F("q-serra","La serra a lavori finiti")]},
 {"titolo":"Il gazebo neogotico","testo":[
  "Nel punto più alto del parco il gazebo è un padiglione ottagonale, con archi a sesto acuto, che segna il passaggio tra i giardini formali e quelli romantici; il modello è nei repertori di Johann Gottfried Grohmann (1805). La copertura a pagoda era crollata del tutto.",
  "Il progetto ne ricostruisce la geometria e la volumetria con una struttura in acciaio, ancorata a spezzoni di profilo inseriti nei pilastri, e un manto in lamiera di rame: restituisce il volume originario senza produrre un falso storico nei materiali. Con le murature in laterizio si è lavorato di restauro, con mattoni fatti a mano e calce naturale; a faccia vista, come nella serra, e con un intonaco «alla cappuccina» sulle murature irregolari interne in alto.",
  "Su indicazione della Soprintendenza non sono stati realizzati gli infissi, di cui non si conosce con certezza la forma originale, e i corpi illuminanti non sono sulla copertura. I sedili mancanti sono in arenaria di colore analogo agli originali, perché la pietra di gesso recuperata dalle colonne onorarie era troppo frammentata per essere lavorata."],
  "figure":[F("q-gazebo-macerie","La copertura crollata, con le macerie ancora sul posto"),F("q-gazebo-laterizi","Campioni di laterizio a confronto"),F("q-gazebo-pavimento","Il pavimento in laterizio, a spina di pesce"),F("q-render-gazebo",RP+"la struttura della copertura vista dall'interno"),F("q-gazebo","Il gazebo nel bosco")],
  "tuttoschermo":[F("q-gazebo-interno","La volta del gazebo vista dall'interno")]},
 {"titolo":"Le colonne onorarie","testo":[
  "Sul retro della villa, ai lati dello scalone, due colonne decorative in laterizio erano state danneggiate dal sisma del 2016: le sfere in cotto che le coronavano erano crollate. Durante i lavori si è scoperto che le sfere, che si credeva fossero conservate dentro la villa, erano andate distrutte nel crollo.",
  "Il restauro ha mantenuto la cortina di laterizio a vista e ha integrato i pezzi mancanti con mattoni di recupero, sagomati in opera. Gli abachi in pietra di gesso, degradati, sono stati sostituiti da elementi in arenaria grigia di analoghe dimensioni, di una pietra locale simile a quella originale; le sfere con piedistallo sono nuove, in cotto di fornaci locali. Le ringhiere in ferro battuto sui capitelli sono originali, con le parti mancanti integrate da elementi di fattura analoga."],
  "figure":[F("q-colonna-disegno","Il particolare di progetto: cosa si ricostruisce e con quali materiali"),F("q-colonna-abaco","L'abaco in gesso, degradato e fessurato"),F("q-colonna-sfere","Sfere e piedistalli in cotto, da fornaci locali"),F("q-colonna-finita","Una colonna restaurata")],
  "tuttoschermo":[F("q-colonne-viale","Le due colonne ai lati del roseto")]},
 {"titolo":"Ghiaia, corten e mattoni","testo":[
  "Il progetto esecutivo prevedeva calcestruzzo drenante, terre stabilizzate e calcestruzzo architettonico per i percorsi. In sito, con le campionature, la Soprintendenza ha giudicato quelle soluzioni poco adatte a un giardino di pregio; una pavimentazione di granulati naturali legati con resina trasparente è risultata troppo costosa.",
  "La soluzione adottata è più semplice e più vicina al luogo: ghiaia stabilizzata su una griglia a nido d'ape, con bordure in acciaio corten. È permeabile, accessibile, facile da sostituire e capace di reggere il passaggio dei mezzi pesanti per il futuro cantiere della Casa di Villa. È stata usata per l'atrio d'ingresso, per l'orto pomario e per il roseto."],
  "figure":[F("q-pav-campioni","Le campionature di ghiaia e di griglie in cantiere"),F("q-pav-griglia","La griglia a nido d'ape riempita di ghiaia")],
  "tuttoschermo":[F("q-pav-orto","I viali in ghiaia stabilizzata dell'orto pomario")]},
 {"titolo":"Ciò che il cantiere ha cambiato","testo":[
  "Un restauro non si chiude sul progetto: le prove, le analisi e il confronto con la Soprintendenza hanno portato scelte diverse da quelle previste. Le principali, riassunte qui, hanno quasi sempre tolto qualcosa al progetto."],
  "tabella":[
   {"voce":"Serra e gazebo, finiture","valore":"Dalla sagramatura rosso mattone prevista alla muratura a faccia vista, con le tracce di intonaco conservate"},
   {"voce":"Serra, copertura","valore":"Profili ottocenteschi mantenuti e affiancati da nuovi profili in acciaio"},
   {"voce":"Gazebo, infissi","valore":"Non realizzati: la forma originale non è documentata con certezza"},
   {"voce":"Gazebo, copertura","valore":"Struttura in acciaio e manto in rame, che restituiscono la volumetria senza falso storico"},
   {"voce":"Colonne onorarie","valore":"Sfere in cotto nuove, da fornaci locali; abachi in arenaria al posto del gesso"},
   {"voce":"Murature","valore":"Escluse le velature e il consolidante superficiale; stuccature a raso"},
   {"voce":"Pavimentazioni","valore":"Da calcestruzzo drenante e terre stabilizzate a ghiaia stabilizzata con bordure in corten"},
   {"voce":"Vasche","valore":"Reti di protezione sotto il livello dell'acqua al posto dei cancelletti"}],
  "nota_tabella":"Le autorizzazioni della Soprintendenza sono del 26 gennaio 2023, del 10 maggio 2023 e del 22 novembre 2024.",
  "extra":"cronologia"},
 {"titolo":"La luce","testo":[
  "L'impianto di illuminazione è stato pensato per far leggere di notte la geometria del parco, senza introdurre corpi illuminanti «in stile» privi di riscontro storico: un approccio mimetico e minimale, con apparecchi discreti.",
  "Tre scenari (base, evento e sicurezza) si accendono secondo l'uso. Gli edifici più significativi, come il gazebo e la serra, sono trattati come «edifici lanterna»: si illumina il volume dall'interno e si accentuano solo alcuni punti, per leggere meglio il parco di notte."],
  "tuttoschermo":[F("q-luce-planimetria","La planimetria dell'illuminazione: i coni di luce e le aree illuminate"),F("q-luce-profili","I profili longitudinali del parco, negli scenari «sicurezza» (sopra) ed «evento» (sotto)")],
  "figure":[F("q-luce-viale2","Il viale d'ingresso di sera"),F("q-luce-viale","Il viale e la Casa del Giardiniere"),F("q-luce-orto","L'orto pomario e la villa di sera"),F("q-luce-scalone","Lo scalone verso il bosco")]},
 {"titolo":"Un giardino per la comunità","testo":[
  "Il restauro del parco restituisce a Treia un giardino storico accessibile e un luogo in cui storia dell'arte e botanica si intrecciano. Il recupero delle architetture di Valadier continua con il restauro in corso della Casa di Villa. Villa La Quiete torna a essere una «storia nelle storie»: un parco dove custodire la memoria vuol dire anche coltivarla."]},
]
cron=[
 {"data":"Gennaio 2024","titolo":"Il gazebo senza copertura","testo":"La muratura messa a nudo dal crollo della copertura.","img":"./img/q-gazebo-crollo.jpg"},
 {"data":"Febbraio 2024","titolo":"Le colonne onorarie","testo":"Le due colonne ponteggiate ai lati del viale, prima del restauro.","img":"./img/q-colonne-scalone.jpg"},
 {"data":"Gennaio 2025","titolo":"I nuovi profili della serra","testo":"I profili nuovi in acciaio affiancano quelli ottocenteschi.","img":"./img/q-serra-profili-nuovi2.jpg"},
 {"data":"Aprile 2025","titolo":"La struttura del gazebo","testo":"La struttura in acciaio della nuova copertura portata in quota con la gru.","img":"./img/q-gazebo-gru.jpg"},
 {"data":"Maggio 2025","titolo":"La serra in cantiere","testo":"La copertura della serra, con i nuovi serramenti.","img":"./img/q-serra-cantiere.jpg"},
 {"data":"Maggio 2025","titolo":"Il rame","testo":"Il manto in lamiera di rame del gazebo.","img":"./img/q-gazebo-rame.jpg"},
 {"data":"Giugno 2025","titolo":"Le colonne restaurate","testo":"Una colonna onoraria, restaurata e completa della sfera in cotto.","img":"./img/q-colonna-finita2.jpg"},
]
meta={"titolo":"Parco e giardino storico di Villa La Quiete","sottotitolo":"Recupero e valorizzazione del parco, del giardino storico e delle architetture annesse, Treia",
 "sintesi":"Un parco ottocentesco restaurato come monumento vivente: serra e gazebo neogotici, murature di sostruzione, orto pomario, roseto e luce, con materiali compatibili e senza falsi storici.",
 "categoria":"Restauro","stato":"Realizzato","luogo":"Treia (MC)","anni":"2022–2025","committente":"Comune di Treia","in_evidenza":True,"ordine":350,
 "copertina":"./img/q-copertina.jpg","apertura":"./img/q-orto-aerea.jpg","carosello":["./img/q-orto-aerea.jpg","./img/q-roseto.jpg","./img/q-serra.jpg","./img/q-gazebo.jpg","./img/q-giardiniere.jpg"],
 "dati":[{"voce":"Luogo","valore":"Treia (MC), contrada San Marco Vecchio"},{"voce":"Anni","valore":"2022–2025"},{"voce":"Stato","valore":"Realizzato"},{"voce":"Committente","valore":"Comune di Treia"},
  {"voce":"Ruolo dello studio","valore":"Progetto architettonico (capogruppo del raggruppamento), direzione dei lavori, coordinamento della sicurezza"},
  {"voce":"Con","valore":"ing. Chiara Antolini (strutture), ing. Franco Marini (impianti), dott. agr. Isabella Dalla Ragione (progetto del verde e aspetti botanici), arch. Maria Francesca Iurescia (coprogettazione e direzione operativa)"},
  {"voce":"Responsabile del procedimento","valore":"arch. Michela Francioni"},{"voce":"Impresa esecutrice","valore":"Scisciani & Frascarelli S.r.l., Tolentino"},
  {"voce":"Importo di aggiudicazione","valore":"1.759.588,09 € (di cui 63.597,06 € per la sicurezza)"},
  {"voce":"Finanziamento","valore":"PNRR, Missione 1 Componente 3, investimento 2.3 «Parchi e giardini storici», NextGenerationEU"},
  {"voce":"Tutela","valore":"Bene vincolato (D.Lgs. 42/2004); lavori autorizzati dalla Soprintendenza"}],
 "sezioni":sez,"cronologia":cron,"superfici":[],
 "disegni":[F("q-tav-planimetria","Planimetria generale, tavola di variante"),F("q-tav-gazebo","Il gazebo neogotico, tavola di variante"),F("q-tav-serra","La serra neogotica, tavola di variante")],
 "galleria":[F("q-orto-arco","Un arco in ferro corten nell'orto pomario"),F("q-atrio","L'atrio d'ingresso")]}
# la galleria non ripete foto gia' usate nelle sezioni
meta["galleria"]=[]
open(OUT+"index.md","w",encoding="utf-8").write("---\n"+yaml.safe_dump(meta,allow_unicode=True,sort_keys=False,width=100000)+"---\n")
print(sum(os.path.getsize(OUT+"img/"+f) for f in os.listdir(OUT+"img"))//1024,"KB immagini")
