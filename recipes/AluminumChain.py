from builder_v2_0.RecipeBuilder import RecipeBuilder, Recipe
from builder_v2_0.RecipeBuilder import recipeComponent as RC
from builder_v2_0.machines import create_machine_dict

from builder_v2_0.Globals import combustibles

machines = create_machine_dict()
recipeBuilder = RecipeBuilder()

recipes = [
    Recipe(machines["roaster"],
           [RC("Bauxite Dust", 5), RC("Sodium Hydroxide Solution", 2000)],
           [RC("Impure Sodium Aluminate Solution", 3000)],
           16, 10*20),
    Recipe(machines["centrifuge"],
           [RC("Impure Sodium Aluminate Solution", 3000)],
           [RC("Sodium Aluminate Solution", 3000), RC("Red Mud", 500)],
           16, 10*20),
    Recipe(machines["crystallizer"],
           [RC("Sodium Aluminate Solution", 1500), RC("Water", 1500), RC("Aluminium Hydroxide Dust", 1, nc=True)],
           [RC("Aluminium Hydroxide Dust", 7), RC("Impure Sodium Hydroxide Solution", 1000)],
           16, 15*20),
    Recipe(machines["electrolyzer"],
           [RC("Impure Sodium Hydroxide Solution", 1000), RC("Steel Rod", 1, nc=True), RC("Graphite Electrode", 1, nc=True)],
           [RC("Sodium Hydroxide Solution", 1000), RC("Gallium Dust", 0.05)],
           30, 15*20),
    Recipe(machines["ebf"],
           [RC("Aluminium Hydroxide Dust", 14)],
           [RC("Alumina Dust", 5), RC("Steam", 3000)],
           40, 5*20),
    Recipe(machines["roaster"],
           [RC("Alumina Dust", 5), RC("Hydrofluoric Acid", 6000)],
           [RC("Aluminium Triflouride Dust", 8), RC("Steam", 9000)],
           16, 15*20),
    Recipe(machines["electrolytic_cell"],
           [RC("Alumina Dust", 10), RC("Aluminium Triflouride Dust", 1), RC("Carbon Dust", 3), RC("Cryolite", 2592, nc=True)],
           [RC("Aluminium Ingot", 4), RC("Cabon Dioxide", 3000), RC("Hydrogen Flouride", 750)],
           40, 5*20),
    Recipe(machines["bubble_column_reactor"],
           [RC("Hydrogen Flouride", 50), RC("Water", 50)],
           [RC("Hydrofluoric Acid", 50)],
           7, 0.05*20)
]

for combustible in combustibles:

    recipes.append(Recipe(
        machines["ebf"],
        [RC("dustAlumina", 10), RC(combustible.name, combustible.amount_required * 3)],
        [RC("Carbon Dioxide", 3000), RC("Aluminium Ingot", 4)],
        480*3, 60
    ))

for recipe in recipes:
    recipeBuilder.append(recipe)