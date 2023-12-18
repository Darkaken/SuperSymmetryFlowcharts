ROASTER.recipeBuilder()
.inputs(ore('dustRhodochrosite'))
.outputs(metaitem('dustManganeseIiOxide') * 2)
.fluidOutputs(fluid('carbon_dioxide') * 1000)
.duration(120)
.EUt(Globals.voltAmps[1])
.buildAndRegister()

BATCH_REACTOR.recipeBuilder()
.inputs(ore('dustManganeseIiOxide'))
.fluidInputs(fluid('sulfuric_acid') * 1000)
.fluidOutputs(fluid('crude_manganese_ii_sulfate_solution') * 1000)
.duration(120)
.EUt(Globals.voltAmps[2])
.buildAndRegister()

BATCH_REACTOR.recipeBuilder()
.inputs(ore('dustSodiumHydroxide') * 3)
.fluidInputs(fluid('crude_manganese_ii_sulfate_solution') * 4000)
.chancedOutput(metaitem('dustIronIiiHydroxide') * 0.35)
.fluidOutputs(fluid('manganese_ii_sulfate_solution') * 4000)
.duration(200)
.EUt(Globals.voltAmps[2])
.buildAndRegister()

ELECTROLYTIC_CELL.recipeBuilder()
.fluidInputs(fluid('manganese_ii_sulfate_solution') * 1000)
.notConsumable(metaitem('stickManganese'))
.notConsumable(metaitem('graphite_electrode'))
.outputs(metaitem('dustManganese'))
.fluidOutputs(fluid('sulfuric_acid') * 1000)
.duration(480)
.EUt(Globals.voltAmps[2])
.buildAndRegister()






    
    