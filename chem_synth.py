def chem_synth(protocol, params):
    source_well = params["reagent_details"][0]["container"]
    protocol.spin(source_well, "500:g", "3:minutes")


if __name__ == '__main__':
    from autoprotocol.harness import run

    run(chem_synth, "ChemicalSynthesis")
