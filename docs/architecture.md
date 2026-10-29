# Architecture du système

Proposition de conception de Didier Lioniello (Applied AI Architect). Ce n'est pas l'architecture réelle de Walmart.

## Composants

| Composant | Rôle | Contrôle humain |
|---|---|---|
| Agent orchestrateur | Reçoit contrats, historique de prix, objectifs et limites ; classe chaque dossier par niveau de risque | Seuils et répartition validés par un humain |
| Zone 70 % faible risque | Agent de négociation autonome, dans des limites écrites | Échantillon relu chaque semaine, alerte de seuil |
| Zone 20 % complexe | Agents juridique, finance, logistique, conformité + agent de synthèse | L'acheteur senior valide avant l'envoi |
| Zone 10 % stratégique | Agent de préparation : scénarios et simulations | Le comité décide |
| Gros montants | Règle transverse | Validation humaine obligatoire, toutes zones |
| Agent d'évaluation | Mesure conclusion, délais, écarts de prix, avis fournisseurs ; propose des ajustements | Chaque ajustement est validé par un humain |

Règles des agents : voir [regles-agents.md](regles-agents.md).

## Diagramme

```mermaid
flowchart TD
    A[Entrées : contrats, historique de prix, objectifs et limites] --> O[Agent orchestrateur : classe chaque dossier par niveau de risque]
    R[Protocoles d'agent : toujours faire / demander d'abord / ne jamais faire] --> O
    O -->|70 % faible risque| L1[Agent de négociation autonome]
    O -->|20 % complexe inter-services| L2[Agents juridique, finance, chaîne d'approvisionnement, conformité + agent de synthèse]
    O -->|10 % stratégique| L3[Agent de préparation : scénarios et simulations]
    L1 --> H1{{Contrôle humain : échantillon hebdomadaire et alerte de seuil}}
    L2 --> H2{{Contrôle humain : validation de l'acheteur senior avant envoi}}
    L3 --> H3{{Contrôle humain : le comité décide}}
    G{{Gros montants : validation humaine obligatoire, quelle que soit la zone}} -.-> H1 & H2 & H3
    H1 --> E[Agent d'évaluation : taux de conclusion, délais, écarts de prix, avis fournisseurs]
    H2 --> E
    H3 --> E
    E -->|ajuste seuils et répartition, validé par un humain| O
```
