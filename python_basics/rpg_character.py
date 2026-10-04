# Build an RPG Character
# http://freecodecamp.org/learn/python-v9/lab-rpg-character/build-an-rpg-character

full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    elif name == "":
        return 'The character should have a name'
    elif len(name) > 10:
        return 'The character name is too long'
    elif " " in name:
        return 'The character name should not contain spaces'
    elif not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    elif not (strength + intelligence + charisma) == 7:
        return 'The character should start with 7 points'
    else:
        str_points = compute_points(strength)
        int_points = compute_points(intelligence)
        cha_points = compute_points(charisma)
        return f'{name}\nSTR {str_points}\nINT {int_points}\nCHA {cha_points}'
        
def compute_points(points):
    base_points = empty_dot * 10
    return full_dot * points + base_points[points:]
