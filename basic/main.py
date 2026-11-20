from dataclasses import dataclass


@dataclass
class Creature:
    name: str
    species: str
    level: int
    health: float


creature1 = Creature("Polyphemus", "Cyclopes", 15, 200.00)
creature2 = Creature("Alecto", "Furies", 11, 140.50)
creature3 = Creature("Silenus", "Satyrs", 9, 100.00)

print("Starting Stats of the Creatures")
print(creature1.name, creature1.species, creature1.level, creature1.health)
print(creature2.name, creature2.species, creature2.level, creature2.health)
print(creature3.name, creature3.species, creature3.level, creature3.health)

creature2.level = 12
creature2.health = 141.00

print("New Stats of the Creatures")
print(creature1.name, creature1.species, creature1.level, creature1.health)
print(creature2.name, creature2.species, creature2.level, creature2.health)
print(creature3.name, creature3.species, creature3.level, creature3.health)