import networkx as nx
from config import EtatNoeud,TypeNoeud,EtatArc,SEUIL_BLOQUE,SEUIL_ENFUME


class Batiment:
    def __init__(self):
        self.batiment=nx.DiGraph()  #Graphe oriente vide
        
    def ajouter_noeud(self,nom,type_noeud,capacite):
        newNoeudAttribut={"type": type_noeud, "capacite":capacite,"etat": EtatNoeud.LIBRE , "niveau_fumee":0.0, "position":None}
        self.batiment.add_node(nom,**newNoeudAttribut)

    def ajouter_arc(self,depart,arrivee,capacite,cout,longueur):
        newArcAttribut={"capacite":capacite , "capacite_residuelle":capacite, "cout":cout,"etat":EtatArc.LIBRE,"longueur":longueur}
        self.batiment.add_edge(depart,arrivee,**newArcAttribut)
        # METHODES D'AJOUT
    def ajouter_salle(self,nom,capacite):
        self.ajouter_noeud(nom,TypeNoeud.SALLE,capacite)

    def ajouter_couloir(self,nom,capacite):
        self.ajouter_noeud(nom,TypeNoeud.COULOIR,capacite)

    def ajouter_sortie(self,nom,capacite):
        self.ajouter_noeud(nom,TypeNoeud.SORTIE,capacite)

    def ajouter_escalier(self,nom,capacite):
        self.ajouter_noeud(nom,TypeNoeud.ESCALIER,capacite)

        # METHODES DE MISE A JOUR

    def mettre_a_jour_fumee(self,nom,niveau):
        self.batiment.nodes[nom]["niveau_fumee"]=niveau
        if niveau ==0.0:
             self.batiment.nodes[nom]["etat"]=EtatNoeud.LIBRE
        elif niveau <= SEUIL_ENFUME:
            self.batiment.nodes[nom]["etat"]=EtatNoeud.ENFUME
        elif  niveau <= SEUIL_BLOQUE:
            self.batiment.nodes[nom]["etat"]=EtatNoeud.BLOQUE
        else:
             self.batiment.nodes[nom]["etat"]=EtatNoeud.EN_FEU

    def mettre_a_jour_cout(self,depart,arrivee,nouveau_cout):
        self.batiment.edges[depart,arrivee]["cout"]=nouveau_cout

    def bloquer_arc(self,depart,arrivee):
         self.batiment.edges[depart,arrivee]["capacite_residuelle"]=0
         self.batiment.edges[depart,arrivee]["cout"]=float('inf')
         self.batiment.edges[depart,arrivee]["etat"]=EtatArc.BLOQUE

    def mettre_a_jour_etat_noeud(self,nom,nouvel_etat):       #POur mettre automatiquement à jour l'etat sans forcement de fumee(trop de monde etc..)
        self.batiment.nodes[nom]["etat"]=nouvel_etat

        # Methode de consultation

    def get_sorties(self):
        noeuds=self.batiment.nodes(data=True)
        sorties=[]
        for nom,attributs in noeuds:
            if attributs["type"] == TypeNoeud.SORTIE:
                sorties.append(nom)
        return sorties
    
    def get_voisins(self,nom):
        return list( self.batiment.successors(nom))
    
    def est_arc_praticable(self,depart,arrivee):
       return (self.batiment.edges[depart,arrivee]["etat"]!= EtatArc.BLOQUE)
    
    def get_cout_arc(self, depart, arrivee):
       return self.batiment.edges[depart, arrivee]["cout"]
    
    def get_arcs(self):
       return self.batiment.edges(data=True)
    
    def get_noeuds(self):
       return self.batiment.nodes(data=True)



         
             
    