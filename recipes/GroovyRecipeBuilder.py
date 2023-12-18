
from builder_v2_0.RecipeBuilder import RecipeBuilder, Recipe
from builder_v2_0.RecipeBuilder import recipeComponent as RC
from builder_v2_0.machines import create_machine_dict

from data.GroovyParser import RecipeParse
import glob

machines = create_machine_dict()
recipeBuilder = RecipeBuilder()

def Parse(path):
    file_counter = 0

    for filename in glob.iglob(path + "**/**", recursive=True):
        if filename.endswith(".groovy"):

            file_counter +=1

            data = RecipeParse(filename)
            temp_builder = RecipeBuilder()

            len_data = len(data)

            print(f"    Parsing recipes from {filename} (0/{len_data})")

            for datapoint in data:

                #print(datapoint.__dict__)

                inputs = [RC(x[0], x[1]) for x in datapoint.inputs] + [RC(x[0], x[1], nc=True) for x in datapoint.nc]

                temp_builder.append(Recipe(
                    machines[datapoint.machine],
                    inputs,
                    [RC(x[0], x[1]) for x in datapoint.outputs],
                    datapoint.eut, datapoint.duration, circuit=datapoint.circuit
                ))

            recipeBuilder.merge(temp_builder)

            print(f"    Recipes parsed from {filename} ({len_data}/{len_data})")

    return file_counter

counter = Parse("../data/parsed")

if __name__ == '__main__':

    Parse("../data/parsed")