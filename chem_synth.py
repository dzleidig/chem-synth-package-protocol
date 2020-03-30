################################################################################################
# This example protocol will create a new destination container and
# transfer `volume` amount of `source_aliquot` into each well.
#
# Test locally with some like the following, though will need to supply a valid project id.
# You must be in the same directory as the manifest and the protocol for the command to succeed.
#
#   transcriptic launch --local chem_synth -p SOME_PROJECT_ID
#
# For more information about autoprotocol-python check out the documentation.
#
#   http://autoprotocol-python.readthedocs.io/en/latest/
#
# For more information about editing the manifest.json check out the documentation.
#
#   https://developers.transcriptic.com/v1.0/docs/input-types
################################################################################################

def chem_synth(protocol, params):
    # These arguments and their types are specified in the manifest.json
    #   source_aliquot is of type Well
    #   volume is of type string and will be in the format similar to '100:microliter'
    #   dest_ctype is of type string and will be one of the options specified in the manifest.
    source_well = params["reagent_details"][0]["reagent_container"]
    protocol.spin(source_well, "5:g", "3:minutes")


if __name__ == '__main__':
    from autoprotocol.harness import run

    run(chem_synth, "chem_synth")
