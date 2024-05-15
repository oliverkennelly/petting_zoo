class Sheep: 
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
    
    def __str__(self):
        return f"{self.name} is a {self.species} added at {self.date_added}"
    