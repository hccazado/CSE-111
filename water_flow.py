

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
    
    pressure = 998.2 * 9.80665 * height / 1000
    
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
    p = 998.2
    v = fluid_velocity
    d = pipe_diameter
    
    pressure_loss = (-f * L * p * v **2 ) / (2000 * d)
    
    return pressure_loss

    