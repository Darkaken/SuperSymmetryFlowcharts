from builder_v2_0.RecipeBuilder import RecipeBuilder, Recipe
from builder_v2_0.RecipeBuilder import recipeComponent as RC
from builder_v2_0.machines import create_machine_dict

from builder_v2_0.Globals import combustibles

machines = create_machine_dict()
recipeBuilder = RecipeBuilder()

recipes = []

for combustible in combustibles:

    recipes.append(Recipe(
        machines["pbf"],
        [RC("Nickel Dust", 1), RC(combustible.name, combustible.amount_required)],
        [RC("Nickel Ingot", 1), RC(combustible.byproduct, combustible.amount_required)],
        0, 250
    ))

    recipes.append(Recipe(
        machines["pbf"],
        [RC("Garnierite Dust", 1), RC(combustible.name, combustible.amount_required)],
        [RC("Nickel Ingot", 1), RC(combustible.byproduct, combustible.amount_required)],
        0, 250
    ))

    recipes.append(Recipe(
        machines["pbf"],
        [RC("Pentlandite Dust", 1), RC(combustible.name, combustible.amount_required * 4)],
        [RC("Nickel Ingot", 1), RC(combustible.byproduct, combustible.amount_required * 4)],
        0, 250
    ))

    recipes.append(Recipe(
        machines["ebf"],
        [RC("Garnierite Dust", 1), RC(combustible.name, combustible.amount_required)],
        [RC("Nickel Ingot", 1), RC("Carbon Monoxide", 1000)],
        30, 40
    ))

for recipe in recipes:
    recipeBuilder.append(recipe)