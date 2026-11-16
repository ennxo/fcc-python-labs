# Build a Planet Class
# https://www.freecodecamp.org/learn/python-v9/lab-planet-class/build-a-planet-class

class Planet:
    def __init__(self, name, planet_type, star):
        try:
            if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
                raise TypeError('name, planet type, and star must be strings')
            elif '' in (name, planet_type, star):
                raise ValueError('name, planet_type, and star must be non-empty strings')
            else:
                self.name = name
                self.planet_type = planet_type
                self.star = star
        except (TypeError, ValueError):
            raise
    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'
    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

planet_1 = Planet('Earth', 'Terrestrial', '1')
planet_2 = Planet('Jupiter', 'Gas', '3')
planet_3 = Planet('Neptune', 'Ice', '5')

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())