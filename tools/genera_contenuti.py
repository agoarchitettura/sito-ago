"""Una tantum: genera le schede di src/content/progetti/ dai dati della prova grafica."""
import json,os,shutil,yaml
S="/tmp/claude-1002/-mnt-ago-AGO-Engine-workspace/6beb8df7-e2e1-4c7d-bf13-5dd591449ee5/scratchpad/"
R="/mnt/ago/AGO Engine/workspace/reports/sito-prove/fase2/progetti/"
d=json.load(open("/home/agoclaude/sito-build/dati_multi.json"))["PD"]
b=json.load(open("/home/agoclaude/sito-build/dati160_files.json"))
def foto(pairs): return [{"img":"./img/%s.jpg"%n,"didascalia":c} for n,c in pairs]
def scrivi(slug,master,meta,usate):
    out="src/content/progetti/"+slug+"/"
    os.makedirs(out+"img",exist_ok=True)
    for n in sorted(usate):
        shutil.copy(R+master+"/immagini/"+n+".jpg",out+"img/"+n+".jpg")
    fm=yaml.safe_dump(meta,allow_unicode=True,sort_keys=False,width=100000,default_flow_style=False)
    open(out+"index.md","w",encoding="utf-8").write("---\n"+fm+"---\n")
    print(slug,len(usate),"immagini")
# ---- Palazzina B72
cr=[("Maggio 2022","Scavo e fondazioni","Il cantiere dopo lo scavo, con le fondazioni su pali e travi rovesce. La fotografia è a tutto schermo qui sopra.",None),
 ("13 maggio 2022","Gli isolatori","Isolatore sismico a scorrimento a doppia superficie curva sul pulvino di fondazione.","cantiere-20220513-isolatore"),
 ("20 maggio 2022","Le travi","Travi reticolari con profilo in acciaio, pronte per i solai.","cantiere-20220520-travi"),
 ("13 gennaio 2023","La struttura","La struttura in acciaio, circondata dai ponteggi.","cantiere-20230113-struttura"),
 ("5 febbraio 2023","I telai","Il telaio in acciaio con le travi reticolari in quota.","cantiere-20230205-telaio"),
 ("20 gennaio 2026","Gli impianti","La pompa di calore aria-acqua sulla copertura.","cantiere-20260120-pompa")]
cap="Schizzo di progetto e fotografia dell'edificio"
sez=[]
for t,par,sch,fig,fb in [(s[0],s[1],s[2],s[3],s[4]) for s in b["sezioni"]]:
    e={"titolo":t,"testo":par}
    if sch: e["schizzi"]=foto([(n,cap) for n in sch])
    ex=None
    if t=="La ricostruzione": ex="cronologia"; e["tuttoschermo"]=foto(fb)
    elif t=="Struttura e involucro": ex="struttura"
    elif t=="Energia e sostenibilità": ex="energia"; e["tuttoschermo"]=foto(fb)
    else:
        if fb: e["tuttoschermo"]=foto(fb)
    if ex: e["extra"]=ex
    sez.append(e)
dati=[{"voce":k,"valore":("ing. Gabriele Magrini (strutture) · ing. Franco Marini (impianti) · geol. Massimo Carnevali · ing. Chiara Antolini (collaudo)" if k=="Con" else v)} for k,v in b["dati"]]
usate=set(["hero-est001","hero-est091","hero-est0102"])
for e in sez:
    for k in ("schizzi","figure","tuttoschermo"):
        usate|={x["img"][6:-4] for x in e.get(k,[])}
usate|={n for n,_ in b["disegni"]}|{n for n,_ in b["gal"]}|{c[3] for c in cr if c[3]}
meta={"titolo":"Palazzina B72","sottotitolo":"Ricostruzione post-sisma di un condominio in via Bartolini 72, Macerata",
 "sintesi":"Ricostruzione post-sisma di un condominio a Macerata: un volume compatto in klinker chiaro, scavato da logge e frangisole.",
 "categoria":"Nuova edificazione","stato":"Realizzato","luogo":"Macerata","anni":"2016–2026","committente":"Condominio","in_evidenza":True,"ordine":1,
 "copertina":"./img/hero-est001.jpg","apertura":"./img/hero-est091.jpg","carosello":["./img/hero-est001.jpg","./img/hero-est091.jpg","./img/hero-est0102.jpg"],
 "dati":dati,"sezioni":sez,
 "cronologia":[dict({"data":a,"titolo":t,"testo":x},**({"img":"./img/%s.jpg"%i} if i else {})) for a,t,x,i in cr],
 "disegni":foto(b["disegni"]),"galleria":foto(b["gal"])}
scrivi("palazzina-b72","160-palazzina-b72",meta,usate)
# ---- Casa San Giuseppe
P=d["sg"]
sez=[]
for s in P["sezioni"]:
    e={"titolo":s[0],"testo":s[1]}
    if s[2]: e["schizzi"]=foto([tuple(x) for x in s[2]])
    if s[3]: e["figure"]=foto([tuple(x) for x in s[3]])
    if s[4]: e["tuttoschermo"]=foto([tuple(x) for x in s[4]])
    if s[5]: e["tabella"]=[{"voce":a,"valore":v} for a,v in s[5]]; e["nota_tabella"]="Dati dal progetto autorizzato; in cantiere possono essere variati."
    if s[6]: e["inglese"]=s[6]
    sez.append(e)
usate={P["hero"],"sg-hero-dsc","sg-fb-chiesetta"}
for e in sez:
    for k in ("schizzi","figure","tuttoschermo"): usate|={x["img"][6:-4] for x in e.get(k,[])}
usate|={n for n,_ in P["disegni"]}|{n for n,_ in P["gal"]}
meta={"titolo":"Casa San Giuseppe","sottotitolo":P["sottotitolo"],
 "sintesi":"Residenza e cappella per la Fraternità San Carlo Borromeo: tre volumi sotto un'unica copertura, tra le colline verso l'Adriatico.",
 "categoria":"New rural","stato":"Realizzato","luogo":"Corridonia","anni":"2013–2017","committente":"Fraternità San Carlo Borromeo","in_evidenza":True,"ordine":2,
 "copertina":"./img/sg-hero-dsc.jpg","apertura":"./img/sg-hero-0030.jpg","carosello":["./img/sg-hero-dsc.jpg","./img/sg-fb-chiesetta.jpg"],
 "dati":[{"voce":a,"valore":v} for a,v in P["dati"]],"sezioni":sez,"cronologia":[],"disegni":foto([tuple(x) for x in P["disegni"]]),"galleria":foto([tuple(x) for x in P["gal"]])}
scrivi("casa-san-giuseppe","123-casa-san-giuseppe",meta,usate)
