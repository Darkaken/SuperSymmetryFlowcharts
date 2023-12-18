
from builder_v2_0.ProcessBuilder import buildprocess
from builder_v2_0.create_flowchart import create_flowchart_simple

from recipes.BuildRecipes import buildRecipes

if __name__ == '__main__':

    # build recipe map

    expected_output = "Aluminium Ingot" #input("Please insert desired output: ")

    # validate output

    rate = 0 #float(input("Please insert desired output rate per second: "))

    builder = buildprocess(expected_output, 0, "mv")

    print(builder.recipes)

    if builder is None:
        print("Recipe map not found")

    else:
        create_flowchart_simple(builder, "test_flowchart", timeformat="seg")

    #recipeBuilderGlobal = buildRecipes(verbose=True)
    #recipeBuilderGlobal.CheckColisions()
    #recipeBuilderGlobal.ParseAll()

    #create_flowchart_simple(recipeBuilderGlobal, "ultimate_flowchart.gv", timeformat="seg")