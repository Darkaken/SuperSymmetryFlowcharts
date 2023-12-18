from builder_v2_0.RecipeBuilder import RecipeBuilder, Recipe
from builder_v2_0.RecipeBuilder import recipeComponent as RC

from builder_v2_0.machines import create_machine_dict
from data.GroovyParser import ParseAllDusts

machines = create_machine_dict()
recipeBuilder = RecipeBuilder()

dusts = set(ParseAllDusts()) #removes duplicates, if any

for dustName in dusts:

    dustName = dustName[1:] #has an extra space

    recipeBuilder.append(
        Recipe(machines["packager"],
               [RC(dustName, 1)],
               [RC(f"Tiny Pile of {dustName} Dust", 9)],
               12, 0.5*20, circuit=1)
    )
    recipeBuilder.append(
        Recipe(machines["packager"],
               [RC(dustName, 1)],
               [RC(f"Small Pile of {dustName} Dust", 4)],
               12, 0.5*20, circuit=2)
    )
    recipeBuilder.append(
        Recipe(machines["packager"],
               [RC(f"Small Pile of {dustName} Dust", 4)],
               [RC(dustName, 1)],
               12, 0.5*20, circuit=1)
    )
    recipeBuilder.append(
        Recipe(machines["packager"],
               [RC(f"Tiny Pile of {dustName} Dust", 9)],
               [RC(dustName, 1)],
               12, 0.5*20, circuit=1)
    )