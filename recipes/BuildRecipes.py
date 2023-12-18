import os
from builder_v2_0.RecipeBuilder import RecipeBuilder

import importlib.util
import sys

def buildRecipes(verbose: bool = False):
    recipeBuilder = RecipeBuilder()
    rel_path = "../recipes/"
    counter = 0

    if verbose:

        print("########################")
        print("Loading Recipes")
        print("######################## \n")

    for filename in os.listdir(rel_path):
        if filename != "BuildRecipes.py" and filename.endswith(".py"):

            path = rel_path + filename
            module = load_module(path)

            len_module_recipes = len(module.recipeBuilder.recipes)

            if verbose:
                print(f"Loading recipes from: {filename} (0/{len_module_recipes})")

            recipeBuilder.merge(module.recipeBuilder, verbose=verbose)
            counter += 1

            if verbose:
                print(f"Recipes loaded from: {filename} ({len_module_recipes}/{len_module_recipes})")

    if verbose:
        print("\n########################")
        print(f"Finished loading recipes from {counter} files")
        print(f"Total recipes loaded: {len(recipeBuilder.recipes)}")
        print("######################## \n")

    return recipeBuilder

def load_module(path, module_name="temp_module"):

    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    return module