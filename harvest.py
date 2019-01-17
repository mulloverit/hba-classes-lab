############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, is_bestseller 
                 ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code 
        self.first_harvest = first_harvest
        self.color  = color 
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 'Muskmelon', 1998, 'green',
                     True, True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    casaba = MelonType('cas', 'Casaba', 2003, 'orange', True, False)
    casaba.add_pairing(['strawberries', 'mint'])
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 'Crenshaw', 1996, 'green', True, False)
    crenshaw.add_pairing(['proscuitto'])
    all_melon_types.append(crenshaw)

    yellow = MelonType('yw', 'Yellow Watermelon', 2013, 'yellow', True, True)
    yellow.add_pairing(['ice cream'])
    all_melon_types.append(yellow)    

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for self.name in MelonTypes:
        print(f"{self.name} pairs wtih {self.pairings}")

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



