class Pokemon:
  def __init__(self, name: str, max_armour: int, max_hit: int):
    self.name = name
    self.armour = max_armour
    self.hit_points = max_hit
    self._is_charging = False

  def attack(self):
    print(f"{self.name} attacks")

  def defend(self):
    print(f"{self.name} defends itself")

  def _charge_attack(self):
      print(f"{self.name} is charging attack type")

# inheritance
class ElectricPokemon(Pokemon):
  def wild_chareg(self):
    print(f"{self.name} is attacking wild")

  def attack(self):
    print(f"{self.name} attacked by itself")

pikachu = Pokemon("Pikachu", 100, 1000)
vaporeon = ElectricPokemon("Vaporeon", 155, 140 )

# polymorphism
pokemons = (pikachu, vaporeon)

for pokemon in pokemons:
  pokemon.attack()