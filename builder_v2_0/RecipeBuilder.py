import copy
from typing import List
from builder_v2_0.machines import Machine
from builder_v2_0.Globals import Globals

from data.dictionary import parseName

class recipeComponent(object):
    def __init__(self, name, amount: float, nc: bool = False, isFluid: bool = False):

        self.name = name
        self.amount = amount

        self.nc = nc

        if isFluid:
            self.unit = "L"
        else:
            self.unit = ""

        self.rate = None

        # process builder parameters

        self.waste = False
        self.input = False
        self.output = False

    def setRate(self, time_t):
        if not self.nc:
            self.rate = self.amount / (time_t / 20) # rate in units per second

    def getData(self):
        return f"name: {self.name} rate: {self.rate} nc: {self.nc} waste: {self.waste} input: {self.input} output: {self.output} unit: {self.unit}"

    def __str__(self):
        return self.getData()

class Recipe(object):
    def __init__(self, machine: Machine, inputs: List[recipeComponent], outputs: List[recipeComponent], eut: int, time_t, circuit: int = 0):

        globals_inst = Globals()

        self.inputs = inputs
        self.outputs = outputs

        if eut is None:
            self.eut = 0
        else:
            self.eut = eut

        self.time_t = int(time_t)

        self.machine = machine # done: type check for validation
        self.tier = globals_inst.get_tier(self.eut)
        self.circuit = circuit

        self.setIOrates()

    def setIOrates(self):
        for RC in (self.inputs + self.outputs):
            RC.setRate(self.time_t)

    def getData(self):
        data = f"inputs: {[x.getData() for x in self.inputs]} outputs: {[x.getData() for x in self.outputs]}"
        data += f"eut: {self.eut} time_t: {self.time_t} machine: {self.machine.name} tier: {self.tier} circuit: {self.circuit}"

        return data

    def getInputNameList(self):
        return [x.name for x in self.inputs]

    def getOutputNameList(self):
        return [x.name for x in self.outputs]

    def __str__(self):
        return self.getData()

    def __eq__(self, other):
        return self.getData() == other.getData()

    def isWaste(self):
        return set([x.waste for x in self.outputs]) == {True}

class RecipeBuilder(object):
    def __init__(self, recipes=None, colission_check=False):

        self.valid = True
        self.iteration = 0
        self.colission_check = colission_check

        if recipes is None:
            self.recipes = []
        else:
            self.recipes = recipes

    def append(self, recipe: Recipe):
        if self.colission_check:
            if recipe not in self.recipes:
                self.recipes.append(recipe)
        else:
            self.recipes.append(recipe)

    def merge(self, builder, verbose=False):

        if self.colission_check:
            colision_counter = 0
            colisions = []

            for recipe in builder.recipes:
                if recipe not in self.recipes:
                    self.append(recipe)
                else:
                    colision_counter += 1
                    colisions.append(recipe)

            if verbose:
                if colision_counter:
                    print(f"Recipe colisions found: {colision_counter}")
                    print("Colisions:")
                    for colision in colisions:
                        print(colision.getData())
        else:
            self.recipes += builder.recipes

    def CheckColisions(self):
        recipe_str = []
        new_recipes = []

        colision_counter = 0
        colisions = []

        for recipe in self.recipes:
            if str(recipe) not in recipe_str:
                recipe_str.append(str(recipe))
                new_recipes.append(recipe)
            else:
                colision_counter += 1
                colisions.append(str(recipe))

        if colision_counter:
            print(f"Recipe colisions found: {colision_counter}")
            print("Colisions:")
            for colision in colisions:
                print(colision)

        self.recipes = new_recipes

    def ParseAll(self):
        for recipe in self.recipes:
            for input_ in recipe.inputs:
                input_.name = parseName(input_.name)
            for output_ in recipe.outputs:
                output_.name = parseName(output_.name)

    def setOutput(self, output: str):
        for recipe in self.recipes:
            for output_ in recipe.outputs :
                if output_.name == output:
                    output_.output = True

    def filter_by_output(self, output: str, verbose: bool = False):

        if verbose:
            print(f"Filtering by output: {output}")

        to_remove = []

        for recipe in self.recipes:
            names = recipe.getOutputNameList()
            if output in names:
                for output_component in recipe.outputs:
                    if output == output_component.name:
                        output_component.waste = True # Set waste to true as it's an infinite system input

            if recipe.isWaste():
                to_remove.append(recipe)

        for recipe in to_remove:
            self.recipes.remove(recipe)

        if verbose and to_remove:
            print(f"Removed {len(to_remove)} recipes")


    def filter_by_voltage_tier(self, max_tier: str, spare_multiblocks: bool=True, verbose: bool = False):

        if verbose:
            print(f"Filtering by voltage tier: {max_tier}")

        voltage_tiers_dict = Globals().voltage_tiers
        to_remove = []

        for recipe in self.recipes:

            if recipe.machine.isMultiblock and spare_multiblocks:
                if voltage_tiers_dict[max_tier] + 1 < voltage_tiers_dict[recipe.tier]:
                    to_remove.append(recipe)
            else:
                if voltage_tiers_dict[max_tier] < voltage_tiers_dict[recipe.tier]:
                    to_remove.append(recipe)

        for recipe in to_remove:
            self.recipes.remove(recipe)

        if verbose and to_remove:
            print(f"Removed {len(to_remove)} recipes")

    def set_inputs(self, input_list: List):
        for recipe in self.recipes:
            for input_ in recipe.inputs:
                if input_.name in input_list:
                    input_.input = True

    def setWaste(self, waste):
        for recipe in self.recipes:
            for output in recipe.outputs:
                if output.name == waste:
                    output.waste = True

    def findByOutput(self, output: str):
        to_return = []

        for recipe in self.recipes:
            if output in recipe.getOutputNameList():
                to_return.append(recipe)

        return to_return

    def remove_recipe(self, recipeTarget: Recipe):
        self.recipes.remove(recipeTarget)