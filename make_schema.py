from PIL import Image, ImageDraw, ImageFont
W,H=2000,1560
img=Image.new("RGB",(W,H),"#F7F8FA"); d=ImageDraw.Draw(img)
R="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"; B="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def f(s,b=False): return ImageFont.truetype(B if b else R,s)
def wrap(t,font,maxw):
    out=[]
    for para in t.split("\n"):
        words=para.split(); line=""
        for w in words:
            tr=(line+" "+w).strip()
            if d.textlength(tr,font=font)<=maxw: line=tr
            else: out.append(line); line=w
        out.append(line)
    return out
def box(x,y,w,h,title,body,fill,edge,tcol="#111",bs=21):
    d.rounded_rectangle((x,y,x+w,y+h),radius=18,fill=fill,outline=edge,width=4)
    ty=y+14
    for l in wrap(title,f(25,True),w-30):
        d.text((x+16,ty),l,font=f(25,True),fill=tcol); ty+=34
    ty+=4
    for l in wrap(body,f(bs),w-32):
        d.text((x+16,ty),l,font=f(bs),fill="#222"); ty+=bs+8
def arrow(x1,y1,x2,y2,col="#444"):
    d.line((x1,y1,x2,y2),fill=col,width=5)
    import math
    a=math.atan2(y2-y1,x2-x1); L=18
    for s in (-0.5,0.5):
        d.line((x2,y2,x2-L*math.cos(a+s),y2-L*math.sin(a+s)),fill=col,width=5)
d.text((50,28),"Négociation fournisseurs avec des agents IA : version supervisée par niveau de risque",font=f(38,True),fill="#0B2545")
d.text((50,80),"Proposition de Didier Lioniello à partir du cas Walmart : 68 % de contrats conclus par l'IA, contre 20 % visés.",font=f(23),fill="#444")
# input
box(50,130,560,150,"1. Entrées","Contrats fournisseurs, historique de prix, objectifs métier et limites (marge, délais, clauses).","#E8F0FE","#3B6FD4")
box(720,130,560,150,"2. Agent orchestrateur","Lit l'objectif, classe chaque dossier par niveau de risque, attribue l'agent et fixe le point de contrôle.","#FFF4D6","#D9A400")
box(1390,130,560,150,"Règles d'agent (3 listes)","Chargées avant chaque action. Voir le bandeau en bas : toujours faire, demander d'abord, ne jamais faire.","#F1E8FF","#7A47D1")
arrow(610,205,720,205); arrow(1390,205,1280,205)
# lanes
lanes=[
 (50,"70 % : faible risque","Contrats standard, petits montants, clauses types.","Agent de négociation autonome : propose, contre-propose, conclut dans les limites fixées.","Contrôle humain : échantillon aléatoire relu chaque semaine, alerte si un seuil est dépassé.","#E3F6E8","#2E9B54"),
 (700,"20 % : complexe, inter-services","Remises croisées, délais de paiement, clauses juridiques ou logistiques.","Agents spécialisés (juridique, finance, chaîne d'approvisionnement, conformité) puis un agent de synthèse.","Contrôle humain : l'acheteur senior valide avant tout envoi au fournisseur.","#FFEFD9","#E08A1E"),
 (1350,"10 % : stratégique","Accords-cadres, changement de fournisseur, impact sur l'organisation.","L'IA prépare les scénarios et simule les issues. Elle ne négocie ni ne décide.","Contrôle humain : comité de direction décide, l'IA documente et trace.","#FFE3E3","#D43B3B"),
]
for x,t,scope,agent,ctrl,fill,edge in lanes:
    d.rounded_rectangle((x,330,x+600,1080),radius=20,fill=fill,outline=edge,width=5)
    d.text((x+18,342),t,font=f(29,True),fill=edge)
    box(x+18,395,564,170,"Cas traités",scope,"#FFFFFF",edge)
    box(x+18,590,564,210,"Agents",agent,"#FFFFFF",edge)
    box(x+18,825,564,235,"Point de contrôle humain",ctrl,"#FFFFFF",edge)
    arrow(x+300,565,x+300,590,edge); arrow(x+300,800,x+300,825,edge)
    arrow(1000 if x==700 else (x+300),282 if x==700 else 282,x+300,330,"#444") if x!=700 else None
arrow(1000,280,350,330); arrow(1000,280,1000,330); arrow(1000,280,1650,330)
# rules band
d.rounded_rectangle((50,1110,1950,1330),radius=20,fill="#FFFFFF",outline="#7A47D1",width=5)
d.text((70,1122),"Protocoles d'agent",font=f(29,True),fill="#7A47D1")
cols=[("Toujours faire","Journaliser chaque décision et sa justification. Rester dans le mandat et les plafonds. Citer la clause source. Escalader si la confiance est basse.","#2E9B54"),
      ("Demander d'abord","Toute concession hors grille. Tout nouveau type de clause. Tout montant au-dessus du seuil. Tout fournisseur sensible ou en litige.","#E08A1E"),
      ("Ne jamais faire","Signer seul un accord stratégique. Modifier un contrat existant sans trace. Partager des données d'un fournisseur avec un autre. Contourner une limite.","#D43B3B")]
for i,(t,b,c) in enumerate(cols):
    x=70+i*620
    d.text((x,1165),t,font=f(26,True),fill=c)
    ty=1203
    for l in wrap(b,f(20),590): d.text((x,ty),l,font=f(20),fill="#222"); ty+=28
# bottom loop
box(50,1360,900,160,"3. Agent d'évaluation (boucle d'amélioration)","Mesure le taux de contrats conclus, les délais, les écarts de prix et l'avis des fournisseurs. Propose d'ajuster les seuils et la répartition 70 / 20 / 10, toujours validé par un humain.","#E8F0FE","#3B6FD4",bs=20)
box(1000,1360,950,160,"Ce qui s'améliore par rapport au cas Walmart","Les décisions à fort enjeu restent humaines, tout est tracé, les seuils sont revus par des mesures, et chaque agent a un mandat écrit plutôt qu'une consigne parfaite.","#E3F6E8","#2E9B54",bs=20)
arrow(1000,1330,500,1360,"#444"); 
d.text((50,1530),"Schéma de proposition, pas l'architecture réelle de Walmart. Proposition de conception de Didier Lioniello (Applied AI Architect).",font=f(18),fill="#666")
img.save("schema-agents-ia.png")
