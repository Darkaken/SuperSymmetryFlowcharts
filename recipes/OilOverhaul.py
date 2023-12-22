from builder_v2_0.RecipeBuilder import RecipeBuilder, Recipe
from builder_v2_0.RecipeBuilder import recipeComponent as RC
from builder_v2_0.machines import create_machine_dict

from builder_v2_0.Globals import sintering_fuels, sintering_comburents

machines = create_machine_dict()
recipeBuilder = RecipeBuilder()

recipes = []

class Oil:
    def __init__(self, name):
        self.name = name

    def getDiluted(self):
        return 'diluted_' + self.name

    def getDesalted(self):
        return 'desalted_' + self.name

    def get(self):
        return self.name

class OilFraction:
    def __init__(self, name, upgrade_name = None):
        self.name = name
        self.upgrade_name = upgrade_name

    def getTreatedSulfuric(self):
        return 'treated_sulfuric_' + self.name

    def getSulfuric(self):
        return 'sulfuric_' + self.name


    def getUpgraded(self):
        return self.upgrade_name


    def getUpgradedMix(self):
        return 'upgraded_' + self.name + '_mix'

    def get(self):
        return self.name

class OilFractionCrackable(OilFraction):
    def __init__(self, name, upgrade_name = None):
        super().__init__(name, upgrade_name)

    def getLightlyHydro(self):
        return 'lightly_hydrocracked_' + self.name

    def getSeverelyHydro(self):
        return 'severely_hydrocracked_' + self.name

    def getLightlySteam(self):
        return 'lightly_steamcracked_' + self.name

    def getSeverelySteam(self):
        return 'severely_steamcracked_' + self.name

    def getLightlyHydroMix(self):
        return 'lightly_hydrocracked_' + self.name + '_mix'

    def getSeverelyHydroMix(self):
        return 'severely_hydrocracked_' + self.name + '_mix'

    def getLightlySteamMix(self):
        return 'lightly_steamcracked_' + self.name + '_mix'

    def getSeverelySteamMix(self):
        return 'severely_steamcracked_' + self.name + '_mix'

fractions = {
    "fuel_oil" : OilFraction('fuel_oil', 'diesel'),
    "diesel" : OilFraction('diesel', 'kerosene'),
    "kerosene" : OilFractionCrackable('kerosene', 'naphtha'),
    "naphtha" : OilFractionCrackable('naphtha', 'gasoline'),
    "gasoline" : OilFractionCrackable('gasoline'),
    "refinery_gas" : OilFraction('refinery_gas'),
    "natural_gas" : OilFraction('natural_gas')
}

oils = {
    "oil": Oil('oil'),
    "oil_light": Oil('oil_light'),
    "oil_heavy": Oil('oil_heavy')
}

for _, oil in oils.items():
    recipes.append(Recipe(
        machines["mixer"],
        [RC("Water", 100), RC(oil.get(), 1000)],
        [RC(oil.getDiluted(), 1000)],
        30, 200
    ))

for _, fraction in fractions.items():
    recipes.append(Recipe(
        machines["fixed_bed_reactor"],
        [RC(fraction.getSulfuric(), 180), RC("Hydrogen", 45), RC("Alumina Catalyst Bed", 1, nc=True)],
        [RC(fraction.getTreatedSulfuric(), 180)],
        30, time_t=30
    ))

    recipes.append(Recipe(
        machines["distillation_tower"],
        [RC(fraction.getTreatedSulfuric(), 1000)],
        [RC(fraction.get(), 1000), RC("Sour Gas", 250)],
        30, 100
    ))

    if fraction.upgrade_name is not None:

        recipes.append(Recipe(
            machines["oil_cracking_unit"],
            [RC(fraction.get(), 1000), RC("Cracking Catalyst", 1)],
            [RC(fraction.getUpgradedMix(), 1000)],
            60, 260
        ))

        recipes.append(Recipe(
            machines["centrifuge"],
            [RC(fraction.getUpgradedMix(), 1000)],
            [RC(fraction.getUpgraded(), 1000), RC("Spent Cracking Catalyst", 1)],
            30, 160
        ))

    if isinstance(fraction, OilFractionCrackable):

        recipes.append(Recipe(
            machines["oil_cracking_unit"],
            [RC(fraction.get(), 1000), RC("Hydrogen", 1000)],
            [RC(fraction.getLightlyHydro(), 1000)],
            60, 260
        ))

        recipes.append(Recipe(
            machines["oil_cracking_unit"],
            [RC(fraction.get(), 1000), RC("Hot High-Pressure Hydrogen", 1000)],
            [RC(fraction.getSeverelyHydro(), 1000)],
            60, 260
        ))

        recipes.append(Recipe(
            machines["oil_cracking_unit"],
            [RC(fraction.get(), 1000), RC("Steam", 1000)],
            [RC(fraction.getLightlySteam(), 1000)],
            60, 260
        ))

        recipes.append(Recipe(
            machines["oil_cracking_unit"],
            [RC(fraction.get(), 1000), RC("Hot High-Pressure Steam", 1000)],
            [RC(fraction.getSeverelySteam(), 1000)],
            60, 260
        ))

for fuel in sintering_fuels:
    if not fuel.isPlasma:
        for comburent in sintering_comburents:

            recipes.append(Recipe(
                machines["rotary_kiln"],
                [RC("Green Coke Dust", 1), RC(fuel.name, fuel.amount_required), RC(comburent.name, comburent.amountRequired)],
                [RC("Coke Dust", 1), RC(fuel.byproduct, fuel.byproduct_amount)],
                eut=120, time_t=fuel.duration * comburent.duration
            ))

            recipes.append(Recipe(
                machines["rotary_kiln"],
                [RC("bituminous_residue", 1), RC(fuel.name, fuel.amount_required), RC(comburent.name, comburent.amountRequired)],
                [RC("bitumen", 1), RC(fuel.byproduct, fuel.byproduct_amount)],
                eut=120, time_t=fuel.duration * comburent.duration
            ))

OxygenateMap = {
        'ethanol': 500,
        'methanol': 500,
        'n_butanol': 100,
        'tert_butyl_alcohol': 100,
        'isopropyl_alcohol': 200,
        'ethyl_tertbutyl_ether': 150
}

AntioxidantMap = {
        'butylated_hydroxytoluene': 300,
        'dimethyl_tert_butylphenol': 300,
        'di_tert_butylphenol': 300,
        'ethylenediamine': 300
}

AntiknockMap = {
        'toluene': 500,
        'isooctane': 300,
        'tetraethyl_lead': 100
}

GeneralAdditiveMap = {
        'acetone': 500,
        'diethyl_ether': 500,
        'nitromethane': 500
}

AdditivesMap = [
        'gasoline_general_additives',
        'gasoline_antioxidants',
        'gasoline_oxygenates',
        'gasoline_antiknock'
]

def getUniquePairs(item_list):

    to_return = []

    for item1 in item_list:
        for item2 in item_list:
            if item1 != item2:
                if ([item1, item2] in to_return) or ([item2, item1] in to_return):
                    pass
                else:
                    to_return.append([item1, item2])
    return to_return

for mapping in getUniquePairs(GeneralAdditiveMap.keys()):
    fluid1, fluid2 = mapping

    recipes.append(Recipe(
        machines["mixer"],
        [RC(fluid1, GeneralAdditiveMap[fluid1]), RC(fluid2, GeneralAdditiveMap[fluid2])],
        [RC("gasoline_general_additives", 1000)],
        eut=120, time_t=200
    ))

for mapping in getUniquePairs(OxygenateMap.keys()):
    fluid1, fluid2 = mapping

    recipes.append(Recipe(
        machines["mixer"],
        [RC(fluid1, OxygenateMap[fluid1]), RC(fluid2, OxygenateMap[fluid2])],
        [RC("gasoline_oxygenates", 1000)],
        eut=120, time_t=200
    ))

for mapping in getUniquePairs(AntioxidantMap.keys()):
    fluid1, fluid2 = mapping

    recipes.append(Recipe(
        machines["mixer"],
        [RC(fluid1, AntioxidantMap[fluid1]), RC(fluid2, AntioxidantMap[fluid2])],
        [RC("gasoline_antioxidants", 1000)],
        eut=120, time_t=200
    ))

for mapping in getUniquePairs(AntiknockMap.keys()):
    fluid1, fluid2 = mapping

    recipes.append(Recipe(
        machines["mixer"],
        [RC(fluid1, AntiknockMap[fluid1]), RC(fluid2, AntiknockMap[fluid2])],
        [RC("gasoline_antiknock", 1000)],
        eut=120, time_t=200
    ))

for name, amount in AntiknockMap.items():

    recipes.append(Recipe(
        machines["mixer"],
        [RC("dustFerrocene", 1), RC(name, amount)],
        [RC("gasoline_antiknock", 2000)],
        eut=120, time_t=200
    ))

for recipe in recipes:
    recipeBuilder.append(recipe)