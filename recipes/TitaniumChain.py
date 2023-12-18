from builder_v2_0.RecipeBuilder import RecipeBuilder, Recipe
from builder_v2_0.RecipeBuilder import recipeComponent as RC
from builder_v2_0.machines import create_machine_dict

from builder_v2_0.Globals import highPurityCombustibles, inertGases

machines = create_machine_dict()
recipeBuilder = RecipeBuilder()

recipes = []

for combustible in highPurityCombustibles:

        recipes.append(Recipe(
                machines["fluidized_bed_reactor"],
                [RC("Chlorine", 3000), RC("dustIlmenite", 1), RC(combustible.name, 1)],
                [RC(combustible.byproduct, 0.1), RC("gaseous_iron_iii_chloride", 120), RC("Carbon Monoxide", 1000), RC("dustRutile", 3)],
                eut=30, time_t=100*combustible.duration
        ))

        recipes.append(Recipe(
                machines["fluidized_bed_reactor"],
                [RC("Chlorine", 2000), RC("dustPerovskite", 1), RC(combustible.name, 1)],
                [RC(combustible.byproduct, 0.1), RC("calcium_chloride", 432), RC("carbon_monoxide", 1000), RC("dustRutile", 3)],
                eut=30, time_t=100*combustible.duration
        ))

        recipes.append(Recipe(
                machines["fluidized_bed_reactor"],
                [RC("dustRutile", 3), RC(combustible.name, 2), RC("Chlorine", 4000)],
                [RC(combustible.byproduct, 0.1), RC("gaseous_titanium_tetrachloride", 1000), RC("carbon_monoxide", 2000)],
                eut=120, time_t=50*combustible.duration
        ))

for gas in inertGases:

        recipes.append(Recipe(
                machines["ebf"],
                [RC("titanium_tetrachloride", 900), RC(gas.name, gas.amount_required), RC("dustMagnesium", 2)],
                [RC("Crude Titanium Sponge", 1), RC("magnesium_chloride", 756), RC("dustMagnesium", 0.125)],
                eut=480*2, time_t=100*gas.duration, circuit=2
        ))

for recipe in recipes:
    recipeBuilder.append(recipe)