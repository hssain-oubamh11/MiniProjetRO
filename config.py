# CE fichier contient toutes les constantes du projet
from enum import Enum
class EtatNoeud(Enum):
    LIBRE = "libre" 
    ENFUME = "enfume"
    BLOQUE = "bloque"
    EN_FEU = "en_feu"
   
class TypeNoeud(Enum):
     SALLE = "salle"
     COULOIR = "couloir"
     ESCALIER = "escalier"
     SORTIE = "sortie"

class EtatArc(Enum):
    LIBRE = "libre"
    RALENTI ="ralenti"
    BLOQUE = "bloque"

class TypeEvenement(Enum):
    INCENDIE="incendie"
    FUMEE="fumee"
    OBSTRUCTION="obstruction"
    ALERTE_PMR="alerte_pmr"
    
SEUIL_ENFUME=0.4
SEUIL_BLOQUE=0.8

POIDS_FUMEE=100
POIDS_FOULE=5
SEUIL_COUT_BLOQUE=150