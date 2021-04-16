class Livre():
    def __init__(self, titre):
        self.titre = titre

    def __str__(self):
        return 'Le titre du livre est : ' + str(self.titre)

class Personne(object):
    def __init__(self, prenom, nom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("Je m'appelle", self.prenom, self.nom)

    def get_prenom(self):
        return self.prenom

    def get_nom(self):
        return self.nom

    def set_prenom(self, prenom):
        self.prenom = prenom

    def set_nom(self, nom):
        self.nom = nom


class Auteur(Personne):
    def __init__(self, prenom, nom):
        super(Auteur, self).__init__(prenom, nom)
        self.oeuvres = []

    def listerOeuvre(self):
        print('\nListe des oeuvres écrites par ', self.prenom, self.nom, " : \n")
        for k in self.oeuvres:
            print(k)

    def ecrireUnLivre(self, titre: str):
        nouveau_livre = Livre(titre)
        self.oeuvres.append(nouveau_livre)


auteur = Auteur('Jean', 'Mich')
auteur.ecrireUnLivre('Le petit cheval')
auteur.ecrireUnLivre('Le moyen cheval')
auteur.ecrireUnLivre('Le grand cheval')

auteur.listerOeuvre()