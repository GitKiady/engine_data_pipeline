class Enregistrement:
    def __init__(self, data):
        self.data = data

    def nettoyer(self):
        raise NotImplementedError("Les sous-classes doivent implémenter nettoyer()")


class Utilisateur(Enregistrement):
    def __init__(self, data):
        super().__init__(data)
        self.nettoyer()

    def nettoyer(self):
        if self.data is not None:
            self.data["nom"] = self.data["nom"].strip().title()
            if self.data.get("age") is None:
                self.data["age"] = 0

    def __repr__(self):
        return str(self.data)


class Produit(Enregistrement):
    def __init__(self, data):
        super().__init__(data)
        self.nettoyer()

    def nettoyer(self):
        if self.data is not None:
            self.data["titre"] = self.data["titre"].strip().title()
            if self.data.get("prix") < 0:
                self.data["prix"] = 0

    def __repr__(self):
        return str(self.data)