class Livre():
    def __init__(self, titre):
        self.titre = titre

    def __str__(self):
        return 'Le titre du livre est : ' + str(self.titre)

class Bibliothèque():
    def __init__(self, nom, catalogue = []):
        self. nom = nom
        self.catalogue = catalogue

    def acheterLivre(self, auteur, titre, qt):
        if type(auteur) == Auteur:
            if titre in [k.titre for k in auteur.oeuvres]:
                self.catalogue.append((Livre(titre), qt))
        else:
            print("REQ acheter :Auteur", auteur, "inconnu")

    def inventaire(self):
        print('\n--------------------------')
        print('Catalogue de la bibliothèque :', self.nom, "\n")
        for k in self.catalogue:
            print(k[0], "| Quantité :", k[1])
        print('--------------------------\n')

    def louer(self, client, titre):
        if type(client) == Client:
            if titre in [k[0].titre for k in self.catalogue]:
                index = [k[0].titre for k in self.catalogue].index(titre)
                if self.catalogue[index][1] > 0:
                    client.collection.append(self.catalogue[index][0])
                    self.catalogue[index] = (self.catalogue[index][0], self.catalogue[index][1]-1)
                else:
                    print("REQ louer :", titre, ": Stock épuisé")
            else:
                print("REQ louer :", titre, ": Pas en inventaire")
        else:
            print('REQ louer :', client, ': Client inconnu')

    def rendreLivres(self, client):
        if type(client) == Client:
            for livre in client.collection:
                titre = livre.titre
                index = [k[0].titre for k in self.catalogue].index(titre)
                self.catalogue[index] = (self.catalogue[index][0], self.catalogue[index][1] + 1)
            client.collection = []
        else:
            print('REQ rendre livres : ', client, 'Client inconnu')

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

class Client(Personne):
    def __init__(self, prenom, nom):
        super(Client, self).__init__(prenom, nom)
        self.collection = []

    def inventaire(self):
        print('\n--------------------------')
        print('Liste des livre empruntés par ', self.prenom, self.nom, " : \n")
        for k in self.collection:
            print(k)
        print('--------------------------\n')

class Auteur(Personne):
    def __init__(self, prenom, nom):
        super(Auteur, self).__init__(prenom, nom)
        self.oeuvres = []

    def listerOeuvre(self):
        print('\n--------------------------')
        print('Liste des oeuvres écrites par ', self.prenom, self.nom, " : \n")
        for k in self.oeuvres:
            print(k)
        print('--------------------------\n')


    def ecrireUnLivre(self, titre: str):
        nouveau_livre = Livre(titre)
        self.oeuvres.append(nouveau_livre)


a1 = Auteur('Jean', 'Mich')
a1.ecrireUnLivre('Le petit cheval')
a1.ecrireUnLivre('Le moyen cheval')
a1.ecrireUnLivre('Le grand cheval')
a1.ecrireUnLivre('Pack: La trilogie du cheval')
# a1.listerOeuvre()

a2 = Auteur('Albert', 'Deux')
a2.ecrireUnLivre('Révoltes')
a2.ecrireUnLivre('Révoltes 2')
# a2.listerOeuvre()


bibliotheque = Bibliothèque('Bibliothèque nationale')
bibliotheque.acheterLivre(a1, 'Le petit cheval', 3)
bibliotheque.acheterLivre(a1, 'Le moyen cheval', 1)
bibliotheque.acheterLivre(a1, 'Le grand cheval', 0)
bibliotheque.acheterLivre(a2, 'Révoltes', 3)
bibliotheque.acheterLivre(a1, 'Révoltes 2', 1)
bibliotheque.inventaire()

c1 = Client('Bernard', 'O')
c2 = 'Jean Paul'

bibliotheque.louer(c1, 'Le petit cheval')
bibliotheque.louer(c2, 'Le petit cheval')
bibliotheque.louer(c1, 'Le grand cheval')
bibliotheque.louer(c1, 'Le moyen cheval')
bibliotheque.louer(c1, 'Les merguez')

c1.inventaire()
bibliotheque.inventaire()
bibliotheque.rendreLivres(c1)
bibliotheque.rendreLivres(c2)

c1.inventaire()
bibliotheque.inventaire()
