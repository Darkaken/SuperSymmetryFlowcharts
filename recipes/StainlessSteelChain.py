from builder_v2_0.RecipeBuilder import RecipeBuilder, Recipe
from builder_v2_0.RecipeBuilder import recipeComponent as RC
from builder_v2_0.machines import create_machine_dict

from builder_v2_0.Globals import highPurityCombustibles

machines = create_machine_dict()
recipeBuilder = RecipeBuilder()

recipes = []

for combustible in highPurityCombustibles:

    recipes.append(Recipe(
        machines["ebf"],
        [RC("dustSiliconDioxide", 3), RC("dustIron", 3), RC(combustible.name, 2)],
        [RC("dustFerrosilicon", 4), RC("Carbon Monoxide", 2000)],
        30*2, 200*combustible.duration
    ))

for recipe in recipes:
    recipeBuilder.append(recipe)