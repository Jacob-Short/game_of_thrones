
class Dragon():

    def __init__(self, name, special_power) -> None:
        self.name = name
        self.special_power = special_power

    def __str__(self) -> str:
        return self.name

dragon = Dragon('jacob', 'fire')

print(dragon)