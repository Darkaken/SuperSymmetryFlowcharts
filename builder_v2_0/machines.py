class Machine(object):
    def __init__(self, name: str, multiblock: bool = False):
        self.name = name
        self.isMultiblock = multiblock

def create_machine_dict():

    single_block_machines = [
        "Air Collector",
        "Alloy Furnace",
        "Amplifabricator",
        "Arc Furnace",
        "Assembler",
        "Autoclave",
        "Batch Reactor",
        "Bath Condenser",
        "Bending Machine",
        "Block Breaker",
        "Brewery",
        "Bubble Column Reactor",
        "Canning Machine",
        "Centrifuge",
        "Chemical Bath",
        "Chemical Reactor",
        "Compressor",
        "Cutting Machine",
        "Cutting Saw",
        "Cuisine Assembler",
        "Crystallizer",
        "CSTR",
        "CVD Unit",
        "Distillery",
        "Dryer",
        "Electric Furnace",
        "Electrolyzer",
        "Electromagnetic Separator",
        "Extractor",
        "Fermenter",
        "Fisher",
        "Fixed Bed Reactor",
        "Fluid Canner",
        "Fluid Extractor",
        "Fluid Heater",
        "Fluid Solidifier",
        "Forge Hammer",
        "Forming Press",
        "Item Collector",
        "Lathe",
        "Macerator",
        "Microwave",
        "Mixer",
        "Mob Extractor",
        "Ore Washer",
        "Packager",
        "Phase Separator",
        "Plasma Arc Furnace",
        "Polarizer",
        "Precision Laser Engraver",
        "Pump",
        "Roaster",
        "Sifting Machine",
        "Slicer",
        "Thermal Centrifuge",
        "Vacuum Chamber",
        "Wiremill",
        "Unpackager",
        "Zone Refiner"
    ]

    multi_block_machines = [
        "Advanced Arc Furnace",
        "Clarifier",
        "Distillation Tower",
        "Drone Pad",
        "EBF",
        "Electric Baking Oven",
        "Electrolytic Cell",
        "Heat Exchanger",
        "High Pressure Cryogenic Distillation Plant",
        "Fluidized Bed Reactor",
        "Froth Flotation Tank",
        "Large Chemical Reactor",
        "Low Pressure Cryogenic Distillation Plant",
        "Ore Sorter",
        "Polymerization Tank",
        "Pressure Swing Absorber",
        "PBF",
        "Pyrolyse Oven",
        "Reaction Furnace",
        "Rotary Kiln",
        "Single Column Cryogenic Distillation Plant",
        "Sintering Oven",
        "Smoke Stack",
        "Vacuum Freezer"
    ]

    machine_dict = {}

    for machine in single_block_machines:
        name = machine.lower().replace(" ", "_")
        machine_dict[name] = Machine(machine)

    for machine in multi_block_machines:
        name = machine.lower().replace(" ", "_")
        machine_dict[name] = Machine(machine, multiblock=True)

    return machine_dict
