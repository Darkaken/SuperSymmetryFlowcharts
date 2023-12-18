from builder_v2_0.RecipeBuilder import RecipeBuilder, Recipe
from builder_v2_0.RecipeBuilder import recipeComponent as RC
from builder_v2_0.machines import create_machine_dict

from builder_v2_0.Globals import combustibles, highPurityCombustibles, Reductant

machines = create_machine_dict()
recipeBuilder = RecipeBuilder()

recipes = []

for combustible in combustibles:

    recipes.append(Recipe(
        machines["ebf"],
        [RC("dustPyrolusite", 1), RC(combustible.name, combustible.amount_required * 2), RC("Tiny Calcite Dust", 1)],
        [RC("dustManganese", 0.75), RC("Carbon Dioxide", 1000)],
        eut=120, time_t=120
    ))

for combustible in highPurityCombustibles:

    recipes.append(Recipe(
        machines["roaster"],
        [RC("dustManganeseIiOxide", 2), RC(combustible.name, 1)],
        [RC("dustManganese", 0.85), RC(combustible.byproduct, 0.1), RC("Carbon Monoxide", 1000)],
        eut=30, time_t=120*combustible.duration
    ))


hydrocarbonReductants = [
        Reductant('fuel_oil', 'carbon_dioxide', 67, 288, multiplier=1),
        Reductant('natural_gas', 'carbon_dioxide', 167, 234, multiplier=1)
]

reductants = [
        Reductant('carbon_monoxide', 'carbon_dioxide', 1000, 1000, multiplier=1),
        Reductant('hydrogen', 'steam', 2000, 1000, multiplier=1)
]

for reductant in hydrocarbonReductants:

    recipes.append(Recipe(
        machines["reaction_furnace"],
        [RC("dustPyrolusite", 1), RC(reductant.name, reductant.amount_required)],
        [RC("dustManganeseIiOxide", 2), RC(reductant.byproduct, reductant.byproduct_amount), RC("steam", 1000 - reductant.byproduct_amount)],
        eut=480, time_t=120
    ))

for reductant in reductants:

    recipes.append(Recipe(
        machines["reaction_furnace"],
        [RC("dustPyrolusite", 1), RC(reductant.name, reductant.amount_required)],
        [RC("dustManganeseIiOxide", 2), RC(reductant.byproduct, reductant.byproduct_amount)],
        eut=480, time_t=120
    ))

for recipe in recipes:
    recipeBuilder.append(recipe)