from builder_v2_0.RecipeBuilder import RecipeBuilder, Recipe
from builder_v2_0.RecipeBuilder import recipeComponent as RC
from builder_v2_0.machines import create_machine_dict

from builder_v2_0.Globals import Blastable, Reductant, combustibles

machines = create_machine_dict()
recipeBuilder = RecipeBuilder()

recipes = []


blastables = [
    Blastable('dustMagnetite', 2, 6, 4, 80),
    Blastable('dustBandedIron', 2, 4, 3, 80),
    Blastable('dustHematite', 2, 4, 3, 80),
    Blastable('dustIronIiiOxide', 5, 2, 3, 20),
    Blastable('dustIronIiOxide', 2, 1, 1, 20),
    Blastable('dustGraniticMineralSand', 2, 6, 4, 80),
    Blastable('oreIron', 2, 2, 2, 60),
    Blastable('oreMagnetite', 1, 3, 4, 60),
    Blastable('oreBandedIron', 1, 2, 3, 60),
]

reductants = [
    Reductant('carbon_monoxide', 'carbon_dioxide', 1, 1),
    Reductant('hydrogen', 'steam', 2, 1)
]

for blastable in blastables:
    for combustible in combustibles:

        recipes.append(Recipe(
            machines["pbf"],
            [RC(blastable.name, blastable.amount_required), RC(combustible.name, combustible.amount_required * blastable.reductant_required)],
            [RC("ingotPigIron", blastable.amount_produced), RC(combustible.byproduct, combustible.amount_required * blastable.reductant_required)],
            0, combustible.duration * blastable.amount_produced * blastable.duration
        ))

        recipes.append(Recipe(
            machines["ebf"],
            [RC(blastable.name, blastable.amount_required), RC(combustible.name, combustible.amount_required * blastable.reductant_required)],
            [RC("ingotPigIron", blastable.amount_produced), RC(combustible.byproduct, combustible.amount_required * blastable.reductant_required)],
            30, (combustible.duration * blastable.amount_produced * blastable.duration) / 2
        ))

    for reductant in reductants:

        recipes.append(Recipe(
            machines["ebf"],
            [RC(blastable.name, blastable.amount_required), RC(reductant.name, blastable.reductant_required * reductant.amount_required)],
            [RC("ingotIron", blastable.amount_produced), RC("dustSiliconDioxide", 0.5), RC(reductant.byproduct, blastable.reductant_required * reductant.byproduct_amount)],
            480, (blastable.amount_produced * blastable.duration) / 4, circuit=1
        ))

        recipes.append(Recipe(
            machines["ebf"],
            [RC(blastable.name, blastable.amount_required), RC(reductant.name, blastable.reductant_required * reductant.amount_required)],
            [RC("ingotPigIron", blastable.amount_produced), RC(reductant.byproduct, blastable.reductant_required * reductant.byproduct_amount)],
            480, (blastable.amount_produced * blastable.duration) / 4, circuit=2
        ))

for combustible in combustibles:

    recipes.append(Recipe(
        machines["pbf"],
        [RC("Iron Ingot", 1), RC(combustible.name, combustible.amount_required)],
        [RC("Steel Ingot", 1), RC(combustible.byproduct, combustible.amount_required)],
        0, combustible.duration * 120
    ))

    recipes.append(Recipe(
        machines["pbf"],
        [RC("Wrought Iron Ingot", 1), RC(combustible.name, combustible.amount_required)],
        [RC("Steel Ingot", 1), RC(combustible.byproduct, combustible.amount_required)],
        0, combustible.duration * 60
    ))

for recipe in recipes:
    recipeBuilder.append(recipe)