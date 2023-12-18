
def ReplaceName(name: str):

    dictionary = {
        "Clay Ball" : "Clay",
        "Gtfo Apple Cider" : "Apple Cider",
        "Gtfo Heated Water" : "Heated Water",
        "Sponge.titanium.crude" : "Crude Titanium Sponge",
        "Sponge.titanium" : "Titanium Sponge",
        "Wheat seeds" : "Seeds",
        "Wood Dust" : "Wood Pulp",
    }

    try:
        return dictionary[name]
    except KeyError:
        return name

def ReplaceMachineName(machine : str):

    dictionary = {
        "assembly machine" : "assembler",
        "bcr" : "bubble_column_reactor",
        "br": "batch_reactor",
        "cutter": "cutting_machine",
        "cvd" : "cvd_unit",
        "dt" : "distillation_tower",
        "emseparator" : "electromagnetic_separator",
        "ebf_recipes" : "ebf",
        "fbr" : "fixed_bed_reactor",
        "ff": "froth_flotation_tank",
        "flotation" : "froth_flotation_tank",
        "high_pressure_distillation_tower" : "high_pressure_cryogenic_distillation_plant",
        "lcr" : "large_chemical_reactor",
        "low_pressure_distillation_tower": "high_pressure_cryogenic_distillation_plant",
        "modsgregtechassembler" : "assembler",
        "psa" : "pressure_swing_absorber",
        "primitiveblastfurnace" : "pbf",
        "polymerization" : "polymerization_tank",
        "rf": "reaction_furnace",
        "sifter" : "sifting_machine",
        "sintering_recipes" : "sintering_oven",
        "vacuumchamber" : "vacuum_chamber",
        "zonerefiner" : "zone_refiner"
    }

    try:
        return dictionary[machine]
    except KeyError:
        return machine

def parseName(name: str):

    name = parseUtil(name)

    if name.startswith("Dust"):
        name = name.split("Dust")[1] + " Dust"
        name = name[1:]

    if name.startswith("Small") and "Dust" in name:
        name = "Small Pile of" + name.split("Small")[1]

    if name.startswith("Tiny") and "Dust" in name:
        name = "Tiny Pile of" + name.split("Tiny")[1]

    if name.startswith("Minecraft"):
        name = name.split(":")[1].capitalize()

    if "Iii" in name: # Iron III for example
        splitted = name.split("Iii")
        name = f"{splitted[0]}III{splitted[1]}"

    if "Ii" in name: #Iron II for example:
        splitted = name.split("Ii")
        name = f"{splitted[0]}II{splitted[1]}"

    if name.startswith("Ingot"):
        name = name.split("Ingot")[1] + " Ingot"
        name = name[1:]

    if name.startswith("Ore"):
        name = name.split("Ore")[1] + " Ore"
        name = name[1:]

    if name.startswith("Plate"):
        name = name.split("Plate")[1] + " Plate"
        name = name[1:]

    return ReplaceName(name)

def parseUtil(name: str):
    name_parsed = []

    for char in name:
        if char.isupper():
            name_parsed.append(" ")
            name_parsed.append(char)
        elif char == "_":
            name_parsed.append(" ")
        else:
            name_parsed.append(char)

    final_name = "".join(name_parsed)

    capitalized_name = ""
    for piece in final_name.split(" "):
        capitalized_name += f"{piece.capitalize().strip()} "

    to_return = " ".join(capitalized_name[:-1].split())

    #print(to_return)

    return to_return