
DISTILLERY.recipeBuilder()
        .fluidInputs(fluid('resin') * 100)
        .fluidOutputs(fluid('glue') * 75)
        .duration(15)
        .EUt(30)
        .buildAndRegister()

CENTRIFUGE.recipeBuilder()
        .inputs(metaitem('rubber_drop'))
        .fluidOutputs(fluid('resin') * 250)
        .duration(40)
        .EUt(8)
        .buildAndRegister()