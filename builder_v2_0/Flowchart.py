from builder_v2_0.Globals import Globals
import graphviz

def create_flowchart_simple(recipeBuilder, diagram_name, timeformat="ticks"):

    counter = 1
    styles = Globals().get_styles()
    diagram = graphviz.Digraph(name=diagram_name, strict=True)

    if timeformat == "seg":
        multiplier = 0.05
    else:
        multiplier = 1

    used_ids = []

    for recipe in recipeBuilder.recipes:

        machine_id = str(counter)
        diagram.node(f"{counter}", f"{recipe.machine.name}\n{recipe.eut} Eu/t ({recipe.tier.upper()})\n{recipe.time_t * multiplier} {timeformat}", styles["machine_style"])
        counter += 1

        for component in recipe.inputs:

            if component.nc is True:

                diagram.node(f"{component.name} {counter}]", f"{component.name} (NC)", styles["nc_style"])
                diagram.edge(f"{component.name} {counter}]", machine_id)
                counter+=1

            else:

                text = f"{component.name}"

                if component.input is True:
                    diagram.node(f"{component.name} {counter}", text, styles["input_style"])
                    diagram.edge(f"{component.name} {counter}", machine_id)
                    counter+=1

                else:
                    diagram.node(f"{component.name}", text, styles["regular_style"])
                    diagram.edge(f"{component.name}", machine_id)

            used_ids.append(component.name)

        for component in recipe.outputs:

            if component.name not in used_ids:

                text = f"{component.name}"

                if component.waste is True:
                    diagram.node(f"{component.name} {counter}", text, styles["waste_style"])
                    diagram.edge(machine_id, f"{component.name} {counter}")
                    counter += 1
                    continue

                elif component.output is True:
                    diagram.node(f"{component.name}", text, styles["output_style"])
                else:
                    diagram.node(f"{component.name}", text, styles["regular_style"])

            else:
                pass

            diagram.edge(machine_id, f"{component.name}")



    diagram.save(f"../diagrams/{diagram_name}")