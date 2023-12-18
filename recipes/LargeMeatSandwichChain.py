from builder_v2_0.RecipeBuilder import RecipeBuilder, Recipe
from builder_v2_0.RecipeBuilder import recipeComponent as RC
from builder_v2_0.machines import create_machine_dict

machines = create_machine_dict()
recipeBuilder = RecipeBuilder()

recipe_cusine_assembler = [Recipe(machines["cuisine_assembler"],
    [RC("Pre-Sliced Baguette", 3), RC("Cheddar Slice", 3), RC("Cooked Meat Ingot", 3)],
    [RC("Large Meat Sandwich", 3)],
    75, 9*15)]

meat_ingot_recipes = [
    Recipe(machines["electric_baking_oven"],
        [RC("Toughened Meat", 1)],
        [RC("Cooked Meat Ingot", 1)],
        21, 2.5*20),
    Recipe(machines["mixer"],
        [RC("Flour", 1), RC("Mince Meat", 1), RC("Water", 500)],
        [RC("Toughened Meat", 2)],
        16, 4.5*20),
    Recipe(machines["macerator"],
        [RC("Wheat", 1)],
        [RC("Flour", 1)],
        2, 4.9*20),

    Recipe(machines["macerator"],
        [RC("Raw Beef", 8)],
        [RC("Mince Meat", 13), RC("Small Pile of Bone Meal", 8), RC("Animal Fat", 10)],
        20, 20*20),

    Recipe(machines["macerator"],
       [RC("Raw Porkchop", 8)],
       [RC("Mince Meat", 13), RC("Small Pile of Bone Meal", 8), RC("Animal Fat", 10)],
       20, 20 * 20),

    Recipe(machines["macerator"],
       [RC("Raw Chicken", 8)],
       [RC("Mince Meat", 13), RC("Small Pile of Bone Meal", 8), RC("Animal Fat", 10)],
       20, 20 * 20),
]

cheddar_slice_recipes = [
    Recipe(machines["slicer"],
        [RC("Cheddar Block", 1), RC("Slicer Blade (Flat)", 1, nc=True)],
        [RC("Cheddar Slice", 9)],
        16, 4*20),
    Recipe(machines["canning_machine"],
        [RC("Aged Cheddar Mold", 1)],
        [RC("Cheddar Block", 1), RC("Mold (Block)", 1)],
        8, 2*20),
    Recipe(machines["compressor"],
        [RC("Cheddar Curd Mold", 1)],
        [RC("Aged Cheddar Mold", 1)],
        16, 300*20),
    Recipe(machines["canning_machine"],
        [RC("Cut Curd", 64), RC("Mold (Block)", 1)],
        [RC("Cheddar Curd Mold", 1)],
        4, 10*20),
    Recipe(machines["slicer"],
        [RC("Coagulated Milk Curd", 1), RC("Slicer Blade (Stripes)", 1, nc=True)],
        [RC("Cut Curd", 64)],
        16, 2*20),
    Recipe(machines["centrifuge"],
        [RC("Milk", 3000), RC("Crude Rennet Solution", 1)],
        [RC("Whey", 600), RC("Coagulated Milk Curd", 1)],
        30, 10*20),
    Recipe(machines["mob_extractor"],
        [RC("Cow", 1)],
        [RC("Milk", 10)],
        16, 1*20, circuit=3),
]

baguette_recipes = [
    Recipe(machines["cutting_saw"],
        [RC("Water", 4), RC("Baguette", 1)],
        [RC("Pre-Sliced Baguette", 1)],
        18, 3*20),
    Recipe(machines["electric_baking_oven"],
        [RC("Unbaked Baguette", 1)],
        [RC("Baguette", 1)],
        51, 1.85*20),
    Recipe(machines["forming_press"],
        [RC("Dough", 2), RC("Baguette Wooden Form", 1, nc=True)],
        [RC("Unbaked Baguette", 1)],
        20, 5*20),
    Recipe(machines["mixer"],
        [RC("Flour", 4), RC("Tiny Pile of Salt", 1), RC("Water", 1000)],
        [RC("Dough", 8)],
        8, 7.5*20, circuit=2)
]

recipes = recipe_cusine_assembler + cheddar_slice_recipes + meat_ingot_recipes + baguette_recipes

for recipe in recipes:
    recipeBuilder.append(recipe)