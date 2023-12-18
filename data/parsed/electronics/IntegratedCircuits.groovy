
mods.gregtech.assembler.recipeBuilder()
.inputs(ore('wireFineTin') * 6)
.inputs(metaitem('wafer.silicon'))
.fluidInputs(fluid('plastic') * 144)
.outputs(metaitem('component.transistor') * 8)
.duration(160)
.EUt(120)
.buildAndRegister()