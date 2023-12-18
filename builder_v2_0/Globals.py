from data.dictionary import parseName

class Globals(object):
    def __init__(self):

        self.voltage_tiers = {"lv": 1,
                              "mv": 2,
                              "hv": 3,
                              "ev": 4,
                              "iv": 5,
                              "luv": 6,
                              "zpm": 7,
                              "uv": 8,
                              "uhv": 9,
                              "uev": 10,
                              "uiv": 11,
                              "uxv": 12,
                              "opv": 13,
                              "max": 14}

        self.voltage_list = [x for x in self.voltage_tiers.keys()]

        self.voltageTiersInt = [32, 128, 512, 2048, 8192, 32768, 131072, 524288, 2097152, 8388608, 33554432, 134217728, 536870912, 2147483647]
        self.machineVoltageTiers = [30, 120, 480, 1920, 7680, 30720, 122880]


    def get_tier(self, eut: int):
        for i in range(len(self.voltageTiersInt)):
            if eut <= self.voltageTiersInt[i]:
                return self.voltage_list[i]

    @staticmethod
    def get_styles():
        return {
            "input_style": {
                "color": "green",
                "style": "filled"
            },
            "machine_style": {
                "color": "lightsalmon",
                "style": "filled",
                "shape": "hexagon"
            },
            "waste_style": {
                "color": "red",
                "style": "filled"
            },
            "output_style": {
                "color": "orange",
                "shape": "box",
                "style": "filled"
            },
            "regular_style": {
                "color": "lightgray",
                "style": "filled"
            },
            "nc_style": {
                "color": "yellow",
                "style": "filled"
            }
        }

class Blastable:
    def __init__(self, name, amount_required, amount_produced, reductant_required, duration):

        self.name = parseName(name)
        self.amount_required = amount_required
        self.amount_produced = amount_produced
        self.reductant_required = reductant_required
        self.duration = duration
class Reductant:
    def __init__(self, name, byproduct, amount_required, byproduct_amount, multiplier=1000):

        self.name = parseName(name)
        self.byproduct = byproduct
        self.amount_required = multiplier * amount_required
        self.byproduct_amount = multiplier * byproduct_amount

class Combustible:
    def __init__(self, name, amount_required, duration, byproduct, byproduct_amount=None, isPlama=None):

        self.name = parseName(name)
        self.amount_required = amount_required
        self.duration = duration
        self.byproduct = byproduct
        self.byproduct_amount = byproduct_amount
        self.isPlasma = isPlama

class Comburent:
    def __init__(self, name, amountRequired, duration):
        self.name = name
        self.amountRequired = amountRequired
        self.duration = duration

class InertGas:
    def __init__(self, name, amount_required, duration):

        self.name = name
        self.amount_required = amount_required
        self.duration = duration


inertGases = [
        InertGas('nitrogen', 8000, 4),
        InertGas('helium', 4000, 2),
        InertGas('argon', 1000, 1)
]


combustibles = [
        Combustible('Coke', 1, 3, 'dustTinyAsh'),
        Combustible('dustCoke', 1, 3, 'dustTinyAsh'),
        Combustible('gemAnthracite', 1, 2, 'dustTinyAsh'),
        Combustible('dustAnthracite', 1, 2, 'dustTinyAsh'),
        Combustible('Coal', 2, 4, 'dustTinyDarkAsh'),
        Combustible('dustCoal', 2, 4, 'dustTinyDarkAsh'),
        Combustible('Charcoal', 2, 4, 'dustTinyDarkAsh'),
        Combustible('dustCharcoal', 2, 4, 'dustTinyDarkAsh'),
        Combustible('dustCarbon', 1, 1, 'dustTinyAsh')
]

highPurityCombustibles = [
        Combustible('dustCoke', 1, 2, 'dustTinyAsh'),
        Combustible('dustCarbon', 1, 1, 'dustTinyAsh')
    ]

sintering_fuels = [
        Combustible('methane', 10, 50, 'carbon_dioxide', 5, isPlama=False),
        Combustible('syngas', 10, 50, 'carbon_dioxide', 5, isPlama=False),
        Combustible('natural_gas', 10, 50, 'carbon_dioxide', 5, isPlama=False),
        Combustible('refinery_gas', 10, 50, 'carbon_dioxide', 5, isPlama=False),
        Combustible('plasma.helium', 10, 5, 'helium', 10, isPlama=True)
]

sintering_comburents = [
        Comburent('air', 10, 50),
        Comburent('oxygen', 8, 30)
]