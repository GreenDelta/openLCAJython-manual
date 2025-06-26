# create the boiling water flow
volume = db.getForName(FlowProperty, "Volume")
boiling_water = Flow.product("Boiling water", volume)


# create the boiling water process
boiling_water_kettle = Process.of(
    "Boiling water with an electric kettle", boiling_water
)

# add the inputs
water = db.getForName(Flow, "Water")
boiling_water_kettle.input(water, 0.001)  # m3

energy = db.getForName(FlowProperty, "Energy")
electricity = Flow.product("Electricity", energy)
boiling_water_kettle.input(electricity, 0.35)  # MJ

# create the electricity production process
electricity_production = Process.of("Electricity production", electricity)
coal = db.getForName(Flow, "Coal, hard, unspecified")
electricity_production.input(coal, 0.05)  # kg

# insert the datasets needed to create the product system into the database
db.insert(boiling_water, electricity, boiling_water_kettle, electricity_production)

# create the product system
system = ProductSystem.of("Boiling water with an electric kettle", boiling_water_kettle)
system.link(electricity_production, boiling_water_kettle)
db.insert(system)

# run the calculation with the Ecological Scarcity 2013 method
method = db.getForName(ImpactMethod, "EPD 2018")
setup = CalculationSetup.of(system).withImpactMethod(method)
result = SystemCalculator(db).calculate(setup)

categories = list(method.impactCategories)
impact = next(i for i in categories if i.name == "Abiotic depletion, fossil fuels")
value = result.getTotalImpactValueOf(Descriptor.of(impact))

print(
    "The total impact on %s for %s is %.4f %s."
    % (impact.name, system.name, value, impact.referenceUnit)
)
