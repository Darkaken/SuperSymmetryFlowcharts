EBF.recipeBuilder()
.inputs(ore('dustIron') * 6)
.inputs(ore('dustNickel'))
.inputs(ore('dustTinyManganese') * 2)
.fluidOutputs(fluid('carburized_stainless_steel') * 1440)
.blastFurnaceTemp(1400)
.duration(800)
.EUt(Globals.voltAmps[2] * 2)
.buildAndRegister()

EBF.recipeBuilder()
.inputs(ore('dustMagnetite') * 14)
.inputs(ore('dustNickel'))
.inputs(ore('dustTinyManganese') * 2)
.fluidOutputs(fluid('carburized_stainless_steel') * 1440)
.blastFurnaceTemp(1400)
.duration(800)
.EUt(Globals.voltAmps[2] * 2)
.buildAndRegister()

EBF.recipeBuilder()
.inputs(ore('dustBandedIron') * 15)
.inputs(ore('dustNickel'))
.inputs(ore('dustTinyManganese') * 2)
.fluidOutputs(fluid('carburized_stainless_steel') * 1440)
.blastFurnaceTemp(1400)
.duration(800)
.EUt(Globals.voltAmps[2] * 2)
.buildAndRegister()

EBF.recipeBuilder()
.inputs(ore('dustIronIiiOxide') * 15)
.inputs(ore('dustNickel'))
.inputs(ore('dustTinyManganese') * 2)
.fluidOutputs(fluid('carburized_stainless_steel') * 1440)
.blastFurnaceTemp(1400)
.duration(800)
.EUt(Globals.voltAmps[2] * 2)
.buildAndRegister()

EBF.recipeBuilder()
.inputs(ore('dustGraniticMineralSand') * 30)
.inputs(ore('dustNickel'))
.inputs(ore('dustTinyManganese') * 2)
.fluidOutputs(fluid('carburized_stainless_steel') * 1440)
.blastFurnaceTemp(1400)
.duration(800)
.EUt(Globals.voltAmps[2] * 2)
.buildAndRegister()

MIXER.recipeBuilder()
.circuitMeta(2)
.inputs(ore('dustIron'))
.inputs(ore('dustChrome') * 2)
.outputs(metaitem('dustFerrochromium') * 3)
.duration(100)
.EUt(Globals.voltAmps[1] * 2)
.buildAndRegister()

ADVANCED_ARC_FURNACE.recipeBuilder()
.fluidInputs(fluid('oxygen') * 2000)
.fluidInputs(fluid('argon') * 500)
.fluidInputs(fluid('carburized_stainless_steel') * 1440)
.inputs(ore('dustSmallFerrosilicon') * 2)
.inputs(ore('dustFerrochromium') * 3)
.inputs(ore('dustSmallQuicklime'))
.inputs(ore('dustSmallFluorite'))
.fluidOutputs(fluid('stainless_steel') * 1440)
.duration(400)
.EUt(Globals.voltAmps[2])
.buildAndRegister()

ADVANCED_ARC_FURNACE.recipeBuilder()
.fluidInputs(fluid('oxygen') * 2000)
.fluidInputs(fluid('nitrogen') * 1000)
.fluidInputs(fluid('carburized_stainless_steel') * 1440)
.inputs(ore('dustSmallFerrosilicon') * 2)
.inputs(ore('dustFerrochromium') * 3)
.inputs(ore('dustSmallQuicklime'))
.inputs(ore('dustSmallFluorite'))
.fluidOutputs(fluid('stainless_steel') * 1440)
.duration(600)
.EUt(Globals.voltAmps[2])
.buildAndRegister()


ADVANCED_ARC_FURNACE.recipeBuilder()
.fluidInputs(fluid('oxygen') * 2000)
.fluidInputs(fluid('argon') * 500)
.fluidInputs(fluid('carburized_stainless_steel') * 1440)
.inputs(ore('dustVanadium') * 2)
.inputs(ore('dustFerrochromium') * 3)
.inputs(ore('dustIron') * 6)
.inputs(ore('dustSmallQuicklime'))
.fluidOutputs(fluid('stainless_steel') * 2592)
.duration(600)
.EUt(Globals.voltAmps[2])
.buildAndRegister()