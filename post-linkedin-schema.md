# Post LinkedIn à publier avec le visuel `schema-agents-ia-linkedin.png`

**Statut : brouillon, non publié.** Didier publie lui-même l'image et le texte.

Liens directs : visuel https://github.com/didier-lioniello/agents-ia-entreprise/blob/main/schema-agents-ia-linkedin.png · version 1200×1200 https://github.com/didier-lioniello/agents-ia-entreprise/blob/main/schema-agents-ia-linkedin-1200.png · détail du schéma https://github.com/didier-lioniello/agents-ia-entreprise/blob/main/schema-agents-ia.md

---

Chez Walmart, une IA négocie les contrats fournisseurs : 68 % de contrats conclus alors que l'objectif était de 20 %, et 75 % des fournisseurs préfèrent négocier avec elle, parce que c'est plus rapide.

C'est impressionnant. Mais je ne confierais pas tous les contrats au même agent.

Voici l'architecture que je propose :

→ 01 Recevoir, 02 Qualifier : un orchestrateur classe chaque dossier par niveau de risque.
→ 70 % faible risque : un agent négocie seul, dans des limites écrites. Un humain relit un échantillon chaque semaine.
→ 20 % complexe : des agents juridique, finance, logistique et conformité préparent une synthèse. L'acheteur senior valide avant l'envoi.
→ 10 % stratégique : l'IA prépare les scénarios, le comité décide.
→ Gros montants : validation humaine obligatoire, quelle que soit la zone.
→ Trois listes de règles : toujours faire, demander d'abord, ne jamais faire.
→ 04 Évaluer : un agent d'évaluation mesure et propose d'ajuster les seuils. Un humain valide.

Des objectifs, des limites et des règles, plutôt que le prompt parfait.

Précision honnête : ce schéma est une proposition de conception, pas l'architecture de Walmart, et je n'ai pas de résultats mesurés pour lui.

Et chez vous, quelle part des décisions pourrait passer en autonomie demain, avec quelles limites écrites ?

Détail du schéma : https://github.com/didier-lioniello/agents-ia-entreprise/blob/main/schema-agents-ia.md

Didier Lioniello · Applied AI Architect
