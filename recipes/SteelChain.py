from builder_v2_0.RecipeBuilder import RecipeBuilder, Recipe
from builder_v2_0.RecipeBuilder import recipeComponent as RC
from builder_v2_0.machines import create_machine_dict

machines = create_machine_dict()
recipeBuilder = RecipeBuilder()

recipes = [
    Recipe(machines["ebf"],
           [RC("Banded Iron Dust", 2), RC("Carbon Dust", 3)],
           [RC("Pig Iron Ingot", 4), RC("Tiny Pile of Ashes", 3)],
           30, 8*20),
    Recipe(machines["electrolytic_cell"],
           [RC("Nickel Rod", 1, nc=True), RC("Iron Rod", 1, nc=True), RC("Water", 1000), RC("Sodium Hydroxide Solution", 50, nc=True)],
           [RC("Hydrogen", 2000), RC("Oxygen", 1000)],
           30, 20*20),
]

for recipe in recipes:
    recipeBuilder.append(recipe)