class Article():
    def __init__(self, titre, contenu):
        self.titre = titre
        self.contenu = contenu
        self.date_publication = None

    def modifier(self, titre, contenu):
        self.titre = titre
        self.contenu = contenu

    def afficher(self):
        print("Titre:", self.titre)
        print("Contenu:", self.contenu)
