from config import TypeEvenement

class Evenement:
    def __init__(self,tick,type_evenement,localisation,intensite=0):
        self.tick=tick
        self.type_evenement=type_evenement
        self.localisation=localisation
        self.intensite=intensite


def creer_scenario_defaut():
    evenement0= Evenement(1,TypeEvenement.FUMEE,"Couloir_1",0.2)
    evenement1=Evenement(2,TypeEvenement.FUMEE,"Couloir_1",0.4)
    evenement2=Evenement(3,TypeEvenement.ALERTE_PMR,"Salle_A",1)
    evenement3=Evenement(4,TypeEvenement.INCENDIE,"Couloir_1",0.5)
    evenement4=Evenement(5,TypeEvenement.INCENDIE,"Couloir_1",0.8)
    evenement5=Evenement(6,TypeEvenement.OBSTRUCTION,("Escalier","Couloir_1"),0)
    evenements=[evenement0,evenement1,evenement2,evenement3,evenement4,evenement5]
    return evenements
def get_evenement_tick(evenements,tick_actuel):
    return [evenement for evenement in evenements if evenement.tick==tick_actuel]

