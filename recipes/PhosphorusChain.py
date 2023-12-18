from builder_v2_0.RecipeBuilder import RecipeBuilder, Recipe
from builder_v2_0.RecipeBuilder import recipeComponent as RC
from builder_v2_0.machines import create_machine_dict

machines = create_machine_dict()
recipeBuilder = RecipeBuilder()

recipes = []

apatites = [
    'dustChlorapatite',
    'dustHydroxyapatite',
    'dustFluorapatite'
]

for apatite in apatites:

    recipes.append(Recipe(
        machines["mixer"],
        [RC(apatite, 2), RC("Clay", 1), RC("dustStone", 1)],
        [RC("Bone China Clay", 4)],
        eut=8, time_t=40
    ))

for recipe in recipes:
    recipeBuilder.append(recipe)