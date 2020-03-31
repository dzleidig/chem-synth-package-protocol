import pprint
from dataclasses import dataclass
from typing import Any

from transcriptic import Connection, Run

# instantiate your api
api = Connection.from_file("~/.transcriptic")  # this will only work if you've run `transcriptic login` in your venv
# get a run from an ID
r = Run("r1e9pkqdq4c8nx")  # this is a fake run
# get info needed to get it's launch request
protocol_id = r.attributes["protocol_id"]
launch_request_id = r.attributes["launch_request_id"]
# launch request
launch_request = api.get_launch_request(protocol_id, launch_request_id)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(launch_request['inputs']['parameters'])


@dataclass
class Order:
    step_id: Any = ""
    ms_order_id: Any = ""
    module_id: Any = ""
    reagent_name: Any = ""
    reagent_id: Any = ""
    weight: Any = ""
    volume: Any = ""
    molarity: Any = ""
    density: Any = ""
    mol_weight: Any = ""
    cas: Any = ""
    phase: Any = ""
    workflow: Any = ""
    type: Any = ""
    role: Any = ""
    dispense_strategy: Any = ""
    source_container: Any = ""
    source_location: Any = ""
    source_sub_location: Any = ""
    dispense_type: Any = ""
    reactor_type: Any = ""
    time: Any = ""
    temperature: Any = ""
    pressure: Any = ""
    stir_speed: Any = ""
    destination_location: Any = ""
    destination_sub_location: Any = ""
    destination_container: Any = ""
    destination_type: Any = ""
    comment: Any = ""

    def get_dict(self):
        return {
            "StepId": self.step_id,
            "MSOrderId": self.ms_order_id,
            "ModuleId": self.module_id,
            "ReagentName": self.reagent_name,
            "ReagentId": self.reagent_id,
            "Weight": self.weight,
            "Volume": self.volume,
            "Molarity": self.molarity,
            "Density": self.density,
            "MolWeight": self.mol_weight,
            "CAS": self.cas,
            "Phase": self.phase,
            "Workflow": self.workflow,
            "Type": self.type,
            "Role": self.role,
            "DispenseStrategy": self.dispense_strategy,
            "SourceContainer": self.source_container,
            "SourceLocation": self.source_location,
            "SourceSubLocation": self.source_sub_location,
            "DispenseType": self.dispense_type,
            "ReactorType": self.reactor_type,
            "Time": self.time,
            "Temperature": self.temperature,
            "Pressure": self.pressure,
            "StirSpeed": self.stir_speed,
            "DestinationLocation": self.destination_location,
            "DestinationSubLocation": self.destination_sub_location,
            "DestinationContainer": self.destination_container,
            "DestinationType": self.destination_type,
            "Comment": self.comment
        }


@dataclass
class Plate:
    ms_order_id: int
    module_id: str
    plate_id: str
    well_id: str
    plate_type: str
    plate_role: str
    plate_size: str
    substance_id: str
    substance_name: str
    phase: str
    container_type: str
    container_size: str
    cap_type: str
    comment: str

    def get_dict(self):
        return {
            "MSOrderId": self.ms_order_id,
            "ModuleId": self.module_id,
            "PlateId": self.plate_id,
            "WellId": self.well_id,
            "PlateType": self.plate_type,
            "PlateRole": self.plate_role,
            "PlateSize": self.plate_size,
            "SubstanceId": self.substance_id,
            "SubstanceName": self.substance_name,
            "Phase": self.phase,
            "ContainerType": self.container_type,
            "ContainerSize": self.container_size,
            "CapType": self.cap_type,
            "Comment": self.comment
        }


@dataclass
class Reagent:
    ms_order_id: int
    module_id: str
    substance_id: str
    substance_name: str
    phase: str
    container_type: str
    comment: str

    def get_dict(self):
        return {
            "MSOrderId": self.ms_order_id,
            "ModuleId": self.module_id,
            "SubstanceId": self.substance_id,
            "SubstanceName": self.substance_name,
            "Phase": self.phase,
            "ContainerType": self.container_type,
            "Comment": self.comment}


@dataclass
class ReagentOrder(Order):
    ms_order_id: int = ""
    module_id: str = ""
    reagent_name: str = ""
    reagent_id: str = ""
    weight: float = ""
    volume: float = ""
    molarity: float = ""
    density: float = ""
    mol_weight: float = ""
    cas: str = ""
    phase: str = ""
    workflow: str = ""
    type: str = ""
    role: str = ""
    dispense_strategy: str = ""
    source_container: str = ""
    source_location: str = ""
    source_sub_location: str = ""
    dispense_type: str = ""
    destination_location: str = ""
    destination_sub_location: str = ""
    destination_container: str = ""
    destination_type: str = ""


@dataclass
class ReactorOrder(Order):
    step_id: int = ""
    ms_order_id: str = ""
    module_id: str = ""
    reagent_name: str = ""
    reagent_id: str = ""
    weight: float = ""
    mol_weight: float = ""
    cas: str = ""
    phase: str = ""
    workflow: str = ""
    type: str = ""
    role: str = ""
    dispense_strategy: str = ""
    source_container: str = ""
    source_location: str = ""
    source_sub_location: str = ""
    reactor_type: str = ""
    time: float = ""
    temperature: float = ""
    destination_location: str = ""
    destination_sub_location: str = ""
    destination_container: str = ""
    destination_type: str = ""

# class ReagentCsv:
#     def __init__(self, step_id, reagent_name):
#         self.step_id = step_id
#         self.reagent_name = reagent_name
#
#
# class ReactCsv:
#     def __init__(self, step_id, reactor_type):
#         self.step_id = step_id
#         self.reactor_type = reactor_type
#
# reagent_a = ReagentCsv(1,'a')
# reagent_b = ReagentCsv(2,'b')
# react = ReactCsv(2,'mw')
#
# order_list = [reagent_a,reagent_b,react]
# order_list.extend((reagent_a,reagent_b,react))
# pd.DataFrame.from_records(tuple(map(lambda x: vars(x), order_list)), index='step_id')
