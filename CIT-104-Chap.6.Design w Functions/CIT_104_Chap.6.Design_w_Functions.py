"""

Kitsmiller, Jericho

This program is supposed to model the vertical motion of an object being
thrown up into the air and then falling back down. 
No hard coded numbers other than gravity. 

"""

# time_to_peak function will take the vertical speed function ('veritcal_speed')and the gravitational acceleration function ('gravity') : default value of -32 ft/s^2

#[ v = aT + V_0 ] : Velocity equation where v is the final velocity, a is the acceleration, T is the time, and V_0 is the initial velocity.

#[ 0 = aT + V_0 ] : At the highest point of the object's trajectory, the final velocity is 0.

# The maximum_height fuction will use the formula [ y = 1/2aT^2 + V_0T + Y_0 ] , using the time from the time_to_peak function to calculate the maximum height of the object.

#Upward motion will always be positive and downwards will always be negative.

def time_to_peak(initial_velocity, gravity=-32, min_time=0.5):
    """
    Calculate the time it takes for an object to reach its peak height when thrown vertically.
    Parameters:
    initial_velocity (float): The initial vertical velocity of the object in feet per second.
    gravity (float): The acceleration due to gravity in feet per second squared (default is -32 ft/s^2).
    Returns:
    float: The time in seconds it takes for the object to reach its peak height.
    """
    # Using the formula: 0 = aT + V_0 => T = -V_0 / a
    # Cannot be negative or less than zero, so we take the absolute value of gravity to ensure a positive time.

    time = initial_velocity / abs(gravity)
    return max(time, min_time)
print("Time taken to reach highest point:", time_to_peak(16))  # 16 as an example for initial velocity, the value can be changed 

#to any value greater than 16 to get a time greater than 0.5 seconds because there in no such thing as negative time.

def maximum_height(initial_velocity, initial_height=0, gravity=-32):
    """
    Calculate the maximum height reached by an object thrown vertically.
    Parameters:
    initial_velocity (float): The initial vertical velocity of the object in feet per second.
    initial_height (float): The initial height from which the object is thrown in feet (default is 0).
    gravity (float): The acceleration due to gravity in feet per second squared (default is -32 ft/s^2).
    Returns:
    float: The maximum height reached by the object in feet.
    """
    # Calculate time to peak using the time_to_peak function

    # The value Y should equal 0 unless another value is specified for the initial height. 

    #Cannot be negative or less than zero, so we take the absolute value of time to ensure a positive time.
    time = time_to_peak(initial_velocity, gravity=-32)
    
    # Using the formula: y = 1/2aT^2 + V_0T + Y_0
    max_height = 0.5 * gravity * time**2 + initial_velocity * time + initial_height
    return max_height
print("Maximum Height:", maximum_height(20)) # 20 as an example for initial velocity, 
# the value can be changed to any value greater than 16 to get a max height greater than 0.
