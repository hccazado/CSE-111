

def water_column_height(tower_height, tank_height):
    """Returns the height of a column of water from a tower height
    and a tank wall height. Based on formula: h = t + 3w/4
    
    Parameter
    tower_height: a float number
    tank_height: a float number"""
    
    height = tower_height + 3*tank_height/4
    
    return height


def pressure_gain_from_water_height(height):
    """returns the pressure caused by Earth's gravity pulling on the 
    water stored in an elevated tank. Based on formula: P = pgh/1000
    
    Parameter
    height: a float number"""
    
    pressure = WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height / 1000
    
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """returns the water pressure lost because of the friction between 
    the water and the walls of a pipe that it flows through. 
    Based on formula: P = -f L p vˆ2 / 2000 d
    
    Parameter
    pipe_diameter: a float number 
    pipe_length: a float number 
    fricction_factor: a float number 
    fluid_velocity: a float number
    """
    
    f = friction_factor
    L = pipe_length
    v = fluid_velocity
    d = pipe_diameter
    
    pressure_loss = (-f * L * WATER_DENSITY * v **2 ) / (2000 * d)
    
    return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """returns the water pressure lost because of fittings such as 45 and 90
    degrees bends that are in a pipeline.
    
    Parameter
    P: lost pressure in Kilopascals
    p: density of water 998.2 kg/m³
    v: velocity of the water flowing through the pipe in meters/second
    n: quantity of fittings"""

    v = fluid_velocity
    n = quantity_fittings

    P = (-0.04 * WATER_DENSITY * v**2 * n) / 2000

    return P
    
def reynolds_number(hydraulic_diameter, fluid_velocity):
    """returns the Reynolds number for a pipe with water flowing through it.
    Parameter
    
    R: Reynolds number
    d: hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter 
    is the same as the pipe's inner diameter.
    v: velocity of the water flowing through the pipe in meters / second
    u: dynamic viscosity of water (0.0010016 Pascal seconds)"""

    d = hydraulic_diameter
    v = fluid_velocity

    R = (WATER_DENSITY * d * v) / WATER_DYNAMIC_VISCOSITY

    return R

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """returns water pressure lost because of water moving from a pipe with a large diameter into a pipe with 
    a smaller diameter.
    
    Parameter
    k: constant computed by the first formula and used in the second formula
    R: Reynolds number that corresponds to the pipe with the larger diameter
    D: diameter of the larger pipe in meters
    d: diameter of the smaller pipe in meters
    P: lost pressure kilopascals
    v: velocity of the water flowing through the larger diameter pipe in meters / second
    """

    R = reynolds_number
    D = larger_diameter
    d = smaller_diameter
    v = fluid_velocity


    k = (0.1 + 50/R) * ((D/d)**4 - 1)

    P = (-k * WATER_DENSITY * v ** 2) / 2000

    return P

def convert_kpa_psi(kpa):
    """returns the conversion between kilopascals to psi (pounds per square inch)
    
    Parameter
    kpa: kilospacal pressure to be converted
    psi: converted pressure from kpa
    """

    psi = kpa * 0.14504

    return psi

EARTH_ACCELERATION_OF_GRAVITY = 9.80665
WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    psi = convert_kpa_psi(pressure)

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {psi:.1f} psi")


if __name__ == "__main__":
    main()