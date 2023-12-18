from builder_v2_0.RecipeBuilder import RecipeBuilder, Recipe
from builder_v2_0.RecipeBuilder import recipeComponent as RC
from builder_v2_0.machines import create_machine_dict

from builder_v2_0.Globals import sintering_fuels, sintering_comburents

machines = create_machine_dict()
recipeBuilder = RecipeBuilder()

recipes = []

for fuel in sintering_fuels:
    if fuel.isPlasma:

        recipes.append(Recipe(
            machines["sintering_oven"],
            [RC("dustSiliconCarbide", 1), RC("Mold (Plate)", 1, nc=True), RC(fuel.name, fuel.amount_required)],
            [RC("plateSiliconCarbide", 1), RC(fuel.byproduct, fuel.byproduct_amount)],
            480, fuel.duration
        ))

    else:

        for comburent in sintering_comburents:

            recipes.append(Recipe(
                machines["sintering_oven"],
                [RC("dustSiliconCarbide", 1), RC("Mold (Plate)", 1, nc=True), RC(fuel.name, fuel.amount_required), RC(comburent.name, comburent.amountRequired)],
                [RC("plateSiliconCarbide", 1), RC(fuel.byproduct, fuel.byproduct_amount)],
                30, fuel.duration + comburent.duration
            ))

for recipe in recipes:
    recipeBuilder.append(recipe)