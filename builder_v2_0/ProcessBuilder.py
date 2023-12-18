
from recipes.BuildRecipes import buildRecipes
from builder_v2_0.config import Config
from builder_v2_0.RecipeBuilder import RecipeBuilder
import copy
import random

class Solution(object):
    def __init__(self):
        self.inputs = Config.automated

        self.to_remove = None
        self.waste = []

    def add_input(self, input_):
        self.inputs.append(input_)

    def check_input(self, input_):
        return input_ in self.inputs

    def add_waste(self, waste):
        if waste not in self.waste:
            self.waste.append(waste)

    def check_input_recipe(self, recipe): # if every input of a recipe is automated or is in inputs, you stop searching
        return set([x in self.inputs for x in recipe.inputs]) == {True}

def buildprocess(output: str, rate: float, max_tier: str):

    """
    :param output: Output Item/Fluid name, ex: "Aluminum Ingot"
    :param rate: item/fluid output rate (units/sec), ex: 2.5
    :param max_tier: max circuit tier available, ex: "lv"
    :return: recipeBuiler object that satisfies available inputs and desired output, False in other case

    Note: just pass the recipeBuilder object to the flowchart creator to create a .dot file from graphviz

    """

    recipeBuilderGlobal = buildRecipes(verbose=True)
    recipeBuilderGlobal.CheckColisions()
    recipeBuilderGlobal.ParseAll()

    recipeBuilderGlobal.setOutput(output)
    recipeBuilderGlobal.filter_by_voltage_tier(max_tier, spare_multiblocks=True, verbose=True) # spare multiblocks disable deletion of recipes that can be accessed with 4A of a lower tier voltage (ex: MV recipes in an EBF with 2 LV energy hatches)

    for component in Config.force_waste: # sets recipe outputs to waste
        recipeBuilderGlobal.setWaste(component)

    for component in Config.automated: # removes recipes that have already automated outputs and removes all-waste output recipes
        recipeBuilderGlobal.filter_by_output(component, verbose=True)

    recipeBuilderGlobal.set_inputs(Config.automated) # mark global inputs as inputs

    solution = find_one(recipeBuilderGlobal, output)

    return solution

def iteration(recipeBuilderGlobal: RecipeBuilder, output: str, base: RecipeBuilder, solution: Solution):

    possible_recipes = recipeBuilderGlobal.findByOutput(output)
    if not possible_recipes: # if you cant find a recipe for this

        print(f"Cant find recipe for: {output}") # this is correct
        base.valid = False

    if len(possible_recipes) > 1:
        next_recipe = random.choice(possible_recipes)  # selects one recipe from available at random
        solution.to_remove = next_recipe
    else:
        next_recipe = possible_recipes[0]  # if only one recipe, select that one

    print(f"Next Recipe: {next_recipe}")

    len_recipe_set = len(base.recipes)
    base.append(next_recipe)

    if (len(base.recipes) == len_recipe_set) or (solution.check_input_recipe(next_recipe)): # (adding a "new" recipe doesn't change anything) or (every input in the recipe is either automated or marked as input) -> return recipeBuilder
        print(f"Repeated recipe: {str(next_recipe)}")
        for output_ in next_recipe.getOutputNameList():
            if output_ != output:
                solution.add_waste(output_)  # every output that is not the expected output is treated as waste (checked later)

    else:  # if it's a new addition
        for input_ in next_recipe.inputs:

            if input_.name in solution.waste: # if it's incorrectly flagged as waste, then you unmark it
                solution.waste.remove(input_.name)

            if (input_.name not in solution.inputs) and (input_.nc != True):
                solution.add_input(input_.name)
                iteration(recipeBuilderGlobal, input_.name, base, solution)

def find_one(recipeBuilderGlobal: RecipeBuilder, output: str):

    recipeBuilderGlobal.iteration += 1
    print(f"Iteration: {recipeBuilderGlobal.iteration}")

    base = RecipeBuilder(colission_check=True)
    solution = Solution()

    iteration(recipeBuilderGlobal, output, base, solution)

    if base.valid is True:

        print("hey")

        for recipe in base.recipes:
            for output_ in recipe.outputs:
                if output_.name in solution.waste:
                    print(output_.name)
                    output_.waste = True
        return base

    else:

        if solution.to_remove is not None:
            print("Removed")
            print(solution.to_remove)
            print("End Removed")
            recipeBuilderGlobal.remove_recipe(solution.to_remove)
            return find_one(recipeBuilderGlobal, output=output)
        else:
            return None