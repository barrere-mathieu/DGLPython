class Personne():
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


P1 = Personne('jean', 'pierre')
P2 = Personne('john', 'moustache')

P1.SePresenter()
P2.SePresenter()
