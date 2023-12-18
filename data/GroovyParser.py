from builder_v2_0.Globals import Globals
from data.dictionary import ReplaceMachineName, parseName
def parseSusyDusts(filename):

    dusts = []

    with open(filename) as File:
        for line in File:
            if "=" in line:
                dusts.append(line.split(" ")[0])

    return dusts

def parseGTCEuDust(filename):

    dusts = []

    with open(filename) as File:

        temp_dust = None
        perhaps_dust = False

        for line in File:
            if "=" in line:
                temp_dust = line.split(" ")[0]
                perhaps_dust = True

            elif ("dust()" in line or "dust(1)" in line or "gem()" in line) and perhaps_dust:
                dusts.append(temp_dust)
                perhaps_dust = False

    return dusts

def parsePurified(filename):

    dusts = []

    with open(filename) as File:

        for line in File:
            if line.startswith("generate"):

                name = line.split("(")[1].split(" ")[0][:-1]
                dusts.append(name)

    return dusts

def ParseAllDusts():

    dusts_parsed = []
    dusts = []

    dusts += parseGTCEuDust("../data/parsed/dusts_data_gtceu.txt")
    dusts += parseGTCEuDust("../data/parsed/dusts_first_degree.txt")
    dusts += parsePurified("../data/parsed/dusts_first_degree_purified.txt")
    dusts += parseSusyDusts("../data/parsed/dusts_ore_materials.txt")
    dusts += parseGTCEuDust("../data/parsed/dusts_organic.txt")

    for dustName in dusts:
        dusts_parsed.append(parseName(dustName))

    return dusts_parsed

def RecipeParse(filename):

    global_data = Globals()

    class Data:
        def __init__(self):
            self.machine = None
            self.inputs = []
            self.outputs = []
            self.nc = []
            self.duration = None
            self.eut = None
            self.circuit = None

    recipes = []

    with open(filename) as file:

        data = Data()


        try:

            for line in file:
                if "recipeBuilder()" in line:

                    data.machine = ReplaceMachineName("".join(line.split(".")[0:-1]).lower())

                elif "nputs" in line: # inputs and fluidInputs

                    strings = line.split("'")
                    name = strings[1]
                    name = parseName(name)

                    if "*" in strings[2]:
                        quantity_split = strings[2].split("*")[1]
                        quantity = int(quantity_split[1:quantity_split.index(")")])
                    else:
                        quantity = 1

                    data.inputs.append([name, quantity])

                elif "utputs" in line: #fluidOutputs and outputs

                    strings = line.split("'")
                    name = strings[1]
                    name = parseName(name)

                    if "*" in strings[2]:
                        quantity_split = strings[2].split("*")[1]
                        quantity = int(quantity_split[1:quantity_split.index(")")])
                    else:
                        quantity = 1

                    data.outputs.append([name, quantity])

                elif "duration" in line:
                    data.duration = int(line[line.index("(") + 1:line.index(")")])

                elif "voltAmps" in line: #first energy format

                    eut_data = line.split("voltAmps[")[1]

                    eut = global_data.machineVoltageTiers[int(eut_data[:eut_data.index("]")]) - 1]

                    multiplier = 1
                    if "*" in line:
                        eut_split = eut_data.split("*")[1]
                        multiplier = float(eut_split[1:2])

                    data.eut = eut * multiplier

                elif "EUt" in line: #second energy format

                    temp_split = line.split("(")[1]

                    eut = temp_split[:temp_split.index(")")]
                    data.eut = int(eut)

                elif ".circuitMeta" in line:
                    temp_split = line.split("(")[1]

                    circuit = temp_split[:temp_split.index(")")]
                    data.circuit = int(circuit)

                elif ".notConsumable" in line:
                    strings = line.split("'")
                    name = strings[1]
                    name = parseName(name)

                    if "*" in strings[2]:
                        quantity_split = strings[2].split("*")[1]
                        quantity = int(quantity_split[1:quantity_split.index(")")])
                    else:
                        quantity = 1

                    data.nc.append([name, quantity])

                elif "buildAndRegister()" in line:
                    recipes.append(data)
                    data = Data()

        except IndexError:
            print("###### ERROR #####")
            print(data.__dict__)
            print("###### END ERROR #####")

    return recipes