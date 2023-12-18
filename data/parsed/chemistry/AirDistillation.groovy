
SIFTER.recipeBuilder()
.inputs(ore('dustTinyMolecularSieve'))
.fluidInputs(fluid('air') * 12000)
.fluidOutputs(fluid('decarburized_air') * 12000)
.outputs(metaitem('dustTinyDirtyMolecularSieve'))
.duration(4)
.EUt(Globals.voltAmps[3])
.buildAndRegister()

VACUUM_CHAMBER.recipeBuilder()
.inputs(ore('dustTinyDirtyMolecularSieve'))
.notConsumable(metaitem('springKanthal'))
.outputs(metaitem('dustTinyMolecularSieve'))
.fluidOutputs(fluid('carbon_dioxide') * 20)
.duration(4)
.EUt(Globals.voltAmps[1])
.buildAndRegister()

HEAT_EXCHANGER.recipeBuilder()
.fluidInputs(fluid('chilly_waste_gaseous_nitrogen') * 640)
.fluidInputs(fluid('hp_decarburized_air') * 1000)
.fluidOutputs(fluid('waste_gaseous_nitrogen') * 640)
.fluidOutputs(fluid('cold_hp_decarburized_air') * 1000)
.duration(1)
.buildAndRegister()

SMOKE_STACK.recipeBuilder()
.fluidInputs(fluid('waste_gaseous_nitrogen') * 640)
.duration(1)
.buildAndRegister()

SMOKE_STACK.recipeBuilder()
.fluidInputs(fluid('chilly_waste_gaseous_nitrogen') * 640)
.duration(1)
.buildAndRegister()

HIGH_PRESSURE_DISTILLATION_TOWER.recipeBuilder()
.circuitMeta(1)
.fluidInputs(fluid('liquid_decarburized_air') * 100)
.fluidInputs(fluid('cold_hp_decarburized_air') * 5600)
.fluidOutputs(fluid('oxygen_rich_liquid') * 50)
.fluidOutputs(fluid('oxygen_rich_gas') * 200)
.fluidOutputs(fluid('nitrogen_rich_gas') * 1400)
.duration(20)
.EUt(Globals.voltAmps[3])
.buildAndRegister()

BATH_CONDENSER.recipeBuilder()
.fluidInputs(fluid('nitrogen_rich_gas') * 200)
.fluidOutputs(fluid('untreated_liquid_nitrogen') * 25)
.duration(1)
.buildAndRegister()

HIGH_PRESSURE_DISTILLATION_TOWER.recipeBuilder()
.circuitMeta(2)
.fluidInputs(fluid('untreated_liquid_nitrogen') * 25)
.fluidInputs(fluid('liquid_decarburized_air') * 100)
.fluidInputs(fluid('cold_hp_decarburized_air') * 5600)
.fluidOutputs(fluid('oxygen_rich_liquid') * 50)
.fluidOutputs(fluid('oxygen_rich_gas') * 200)
.fluidOutputs(fluid('nitrogen_rich_gas') * 1600)
.duration(5)
.EUt(Globals.voltAmps[3])
.buildAndRegister()

LOW_PRESSURE_DISTILLATION_TOWER.recipeBuilder()
.circuitMeta(1)
.fluidInputs(fluid('oxygen_rich_liquid') * 50)
.fluidInputs(fluid('oxygen_rich_gas') * 800)
.fluidInputs(fluid('nitrogen_rich_gas') * 3200)
.fluidOutputs(fluid('untreated_liquid_oxygen') * 50)
.fluidOutputs(fluid('cold_waste_gaseous_nitrogen') * 5440)
.fluidOutputs(fluid('argon_rich_gas') * 200)
.duration(20)
.EUt(Globals.voltAmps[3])
.buildAndRegister()

HEAT_EXCHANGER.recipeBuilder()
.fluidInputs(fluid('cold_waste_gaseous_nitrogen') * 640)
.fluidInputs(fluid('untreated_liquid_nitrogen') * 50)
.fluidOutputs(fluid('chilly_waste_gaseous_nitrogen') * 640)
.fluidOutputs(fluid('subcooled_liquid_nitrogen') * 50)
.duration(5)
.buildAndRegister()

HEAT_EXCHANGER.recipeBuilder()
.circuitMeta(2)
.fluidInputs(fluid('untreated_liquid_nitrogen') * 25)
.fluidInputs(fluid('untreated_liquid_oxygen') * 50)
.fluidOutputs(fluid('subcooled_liquid_nitrogen') * 25)
.fluidOutputs(fluid('liquid_oxygen_product') * 50)
.duration(5)
.buildAndRegister()

LOW_PRESSURE_DISTILLATION_TOWER.recipeBuilder()
.circuitMeta(2)
.fluidInputs(fluid('oxygen_rich_liquid') * 50)
.fluidInputs(fluid('oxygen_rich_gas') * 800)
.fluidInputs(fluid('nitrogen_rich_gas') * 3200)
.fluidInputs(fluid('subcooled_liquid_nitrogen') * 50)
.fluidOutputs(fluid('untreated_liquid_oxygen') * 50)
.fluidOutputs(fluid('cold_waste_gaseous_nitrogen') * 640)
.fluidOutputs(fluid('liquid_nitrogen') * 150)
.fluidOutputs(fluid('argon_rich_gas') * 200)
.duration(5)
.EUt(Globals.voltAmps[3])
.buildAndRegister()

SMOKE_STACK.recipeBuilder()
.fluidInputs(fluid('argon_rich_gas') * 200)
.duration(5)
.buildAndRegister()

CENTRIFUGE.recipeBuilder()
.fluidInputs(fluid('liquid_nitrogen_product') * 100)
.fluidOutputs(fluid('liquid_nitrogen') * 75)
.duration(1)
.EUt(Globals.voltAmps[0])
.buildAndRegister()

CENTRIFUGE.recipeBuilder()
.fluidInputs(fluid('liquid_oxygen_product') * 100)
.fluidOutputs(fluid('liquid_oxygen') * 75)
.duration(1)
.EUt(Globals.voltAmps[0])
.buildAndRegister()

HIGH_PRESSURE_DISTILLATION_TOWER.recipeBuilder()
.circuitMeta(3)
.fluidInputs(fluid('untreated_liquid_nitrogen') * 25)
.fluidInputs(fluid('liquid_decarburized_air') * 100)
.fluidInputs(fluid('cold_hp_decarburized_air') * 5600)
.fluidOutputs(fluid('oxygen_rich_liquid') * 75)
.fluidOutputs(fluid('nitrogen_rich_gas') * 1600)
.duration(5)
.EUt(Globals.voltAmps[3])
.buildAndRegister()

SINGLE_COLUMN_CRYOGENIC_DISTILLATION_PLANT.recipeBuilder()
.circuitMeta(1)
.fluidInputs(fluid('argon_rich_gas') * 800)
.fluidOutputs(fluid('crude_argon_vapor') * 80)
.fluidOutputs(fluid('oxygen_rich_liquid') * 90)
.duration(20)
.EUt(Globals.voltAmps[3])
.buildAndRegister()

SINGLE_COLUMN_CRYOGENIC_DISTILLATION_PLANT.recipeBuilder()
.circuitMeta(2)
.fluidInputs(fluid('liquid_crude_argon') * 5)
.fluidInputs(fluid('argon_rich_gas') * 400)
.fluidOutputs(fluid('crude_argon_vapor') * 120)
.fluidOutputs(fluid('oxygen_rich_liquid') * 90)
.duration(10)
.EUt(Globals.voltAmps[3])
.buildAndRegister()

BATH_CONDENSER.recipeBuilder()
.fluidInputs(fluid('subcooled_oxygen_rich_liquid') * 150)
.fluidInputs(fluid('crude_argon_vapor') * 60)
.fluidOutputs(fluid('liquid_crude_argon') * 15)
.fluidOutputs(fluid('oxygen_rich_liquid') * 100)
.fluidOutputs(fluid('oxygen_rich_gas') * 400)
.duration(1)
.buildAndRegister()

MIXER.recipeBuilder()
.inputs(ore('dustAmmoniumHexachloroplatinate') * 17)
.fluidInputs(fluid('phosphoric_acid') * 1000)
.fluidOutputs(fluid('deoxygenation_catalyst_precursor_solution') * 1000)
.duration(100)
.EUt(Globals.voltAmps[3])
.buildAndRegister()

SINTERING_OVEN.recipeBuilder()
.inputs(ore('dustAlumina') * 5)
.fluidInputs(fluid('deoxygenation_catalyst_precursor_solution') * 1000)
.outputs(metaitem('dustDeoxygenationCatalyst'))
.fluidOutputs(fluid('phosphoric_acid') * 1000)
.duration(100)
.EUt(Globals.voltAmps[3])
.buildAndRegister()

FBR.recipeBuilder()
.fluidInputs(fluid('liquid_crude_argon') * 50)
.fluidInputs(fluid('hydrogen') * 24)
.notConsumable(metaitem('catalystBedDeoxygenationCatalyst'))
.chancedOutput(metaitem('dustIce'), 120, 0)
.fluidOutputs(fluid('liquid_deoxygenated_argon') * 50)
.duration(20)
.EUt(Globals.voltAmps[3])
.buildAndRegister()

SINGLE_COLUMN_CRYOGENIC_DISTILLATION_PLANT.recipeBuilder()
.fluidInputs(fluid('liquid_deoxygenated_argon') * 200)
.fluidOutputs(fluid('cold_waste_gaseous_nitrogen') * 16)
.fluidOutputs(fluid('liquid_argon_product') * 200)
.duration(200)
.EUt(Globals.voltAmps[3])
.buildAndRegister()

//REFLUXED DISTILLATION
BATH_CONDENSER.recipeBuilder()
.fluidInputs(fluid('cold_waste_gaseous_nitrogen') * 8)
.fluidOutputs(fluid('liquid_waste_nitrogen') * 1)
.duration(1)
.buildAndRegister()

SINGLE_COLUMN_CRYOGENIC_DISTILLATION_PLANT.recipeBuilder()
.fluidInputs(fluid('liquid_deoxygenated_argon') * 200)
.fluidInputs(fluid('argon') * 400)
.fluidInputs(fluid('liquid_waste_nitrogen'))
.fluidOutputs(fluid('cold_waste_gaseous_nitrogen') * 24)
.fluidOutputs(fluid('liquid_argon_product') * 200)
.duration(83)
.EUt(Globals.voltAmps[3])
.buildAndRegister()

HEAT_EXCHANGER.recipeBuilder()
.fluidInputs(fluid('oxygen_rich_liquid') * 75)
.fluidInputs(fluid('liquid_nitrogen') * 150)
.fluidOutputs(fluid('subcooled_oxygen_rich_liquid') * 75)
.fluidOutputs(fluid('nitrogen') * 9600)
.duration(5)
.buildAndRegister()

HEAT_EXCHANGER.recipeBuilder()
.fluidInputs(fluid('oxygen_rich_liquid') * 75)
.fluidInputs(fluid('liquid_argon_product') * 5)
.fluidOutputs(fluid('subcooled_oxygen_rich_liquid') * 75)
.fluidOutputs(fluid('partially_liquefied_argon') * 18)
.duration(5)
.buildAndRegister()

PHASE_SEPARATOR.recipeBuilder()
.fluidInputs(fluid('partially_liquefied_argon') * 450)
.fluidOutputs(fluid('argon') * 400)
.fluidOutputs(fluid('liquid_argon_product') * 50)
.duration(29)
.EUt(Globals.voltAmps[3])
.buildAndRegister()

LOW_PRESSURE_DISTILLATION_TOWER.recipeBuilder()
.circuitMeta(3)
.fluidInputs(fluid('oxygen_rich_liquid') * 100)
.fluidInputs(fluid('oxygen_rich_gas') * 1600)
.fluidInputs(fluid('nitrogen_rich_gas') * 6400)
.fluidInputs(fluid('subcooled_liquid_nitrogen') * 100)
.fluidOutputs(fluid('untreated_liquid_oxygen') * 105)
.fluidOutputs(fluid('cold_waste_gaseous_nitrogen') * 1280)
.fluidOutputs(fluid('liquid_nitrogen_product') * 300)
.fluidOutputs(fluid('argon_rich_gas') * 400)
.duration(5)
.EUt(Globals.voltAmps[3])
.buildAndRegister()

HEAT_EXCHANGER.recipeBuilder()
.fluidInputs(fluid('cold_waste_gaseous_nitrogen') * 1280)
.fluidInputs(fluid('untreated_liquid_nitrogen') * 100)
.fluidOutputs(fluid('chilly_waste_gaseous_nitrogen') * 1280)
.fluidOutputs(fluid('subcooled_liquid_nitrogen') * 100)
.duration(5)
.buildAndRegister()

HEAT_EXCHANGER.recipeBuilder()
.circuitMeta(1)
.fluidInputs(fluid('untreated_liquid_nitrogen') * 100)
.fluidInputs(fluid('untreated_liquid_oxygen') * 55)
.fluidOutputs(fluid('subcooled_liquid_nitrogen') * 100)
.fluidOutputs(fluid('liquid_oxygen_product') * 55)
.duration(5)
.buildAndRegister()

FLUID_HEATER.recipeBuilder()
.circuitMeta(2)
.fluidInputs(fluid('liquid_nitrogen') * 100)
.fluidOutputs(fluid('nitrogen') * 6400)
.duration(2)
.EUt(Globals.voltAmps[3])
.buildAndRegister()

FLUID_HEATER.recipeBuilder()
.circuitMeta(2)
.fluidInputs(fluid('liquid_oxygen') * 100)
.fluidOutputs(fluid('oxygen') * 6400)
.duration(2)
.EUt(Globals.voltAmps[3])
.buildAndRegister()

FLUID_HEATER.recipeBuilder()
.fluidInputs(fluid('liquid_argon') * 100)
.fluidOutputs(fluid('argon') * 6400)
.duration(2)
.EUt(Globals.voltAmps[3])
.buildAndRegister()