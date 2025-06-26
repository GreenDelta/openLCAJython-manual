# unit and unit group
kg = Unit.of("kg", 1.0)  # name: str, conversionFactor: float

units_of_mass = UnitGroup.of("Unit of mass", kg)  # name: str, referenceUnit: Unit
units_of_mass.units.add(kg)

# flow and flow property
flow = Flow()
flow.flowType = FlowType.PRODUCT_FLOW
flow.name = "Liquid aluminium"

mass = FlowProperty()
mass.flowPropertyType = FlowPropertyType.PHYSICAL
mass.unitGroup = units_of_mass

# the same operation can be done using the FlowProperty.of method as the
# default flow property type is PHYSICAL
mass = FlowProperty.of("Mass", units_of_mass)  # name: str, unitGroup: UnitGroup

flow.referenceFlowProperty = mass
massFactor = FlowPropertyFactor.of(mass, 1.0)  # prop: FlowProperty, factor: float
flow.flowPropertyFactors.add(massFactor)

# process
output = Flow.product("Molten aluminium", mass)  # name: str, flowProperty: FlowProperty
# create a process with `output` as quantitative reference with the default
# amount of 1.0
process = Process.of("Aluminium smelting", output)

waste = Flow.waste(
    "Spent Pot Lining (SPL)", mass
)  # name: str, flowProperty: FlowProperty
process.input(waste, 4.2)  # flow: Flow, amount: float

# product system
system = ProductSystem.of("Aluminium smelting", process)
# name: str, process: Process

db.insert(units_of_mass, mass, flow, output, waste, process, system)
