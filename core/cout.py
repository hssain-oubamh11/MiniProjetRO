
from config import POIDS_FOULE,POIDS_FUMEE,SEUIL_COUT_BLOQUE

def calculer_cout(longueur,niveau_fumee,nb_personnes):
     cout=(longueur + (niveau_fumee * POIDS_FUMEE )+ (nb_personnes*POIDS_FOULE))
     if cout >  SEUIL_COUT_BLOQUE :
          return float('inf')
     return cout
def calculer_cout_arc(batiment,depart,arrivee):
      arc= batiment.getattributs_arc(depart,arrivee)
      noeud_arrivee=batiment.getattributs_noeud(arrivee)

      longueur=arc["longueur"]
      niveau_fumee=noeud_arrivee["niveau_fumee"]
      nb_personnes= noeud_arrivee["nb_personnes"]
      return calculer_cout(longueur,niveau_fumee,nb_personnes)

def recalculer_tous_les_couts(batiment):
     for  depart,arrivee  in  batiment.get_arcs():
          nouveau_cout=calculer_cout_arc(batiment,depart,arrivee)
          batiment.mettre_a_jour_cout(depart,arrivee,nouveau_cout)