Activity Order:

I suggest students build up a set of tested functions in myfunctions.py they can then include

- Remote activity
`remote.py`

- Simple drive for time (introduce motor config, start, stop; expt with stop)
`driveForwards.py`

- Drive till button press on brick (introduce while guard)
`driveForwards_buttonstop.py`
*also multi-thread:* `threading_drive.py`

- Forwards, back, turn - create simple functions to turn motors on, off, drive, turn
`drive_forward_back_turn_function.py`

- Simple line stopper - introduce ColorSensor; reuse buttonstop while guard
`linestopper.py`
  - colour sensor - line activity can be done solely on the brick by inspecting sensor value there
  - extension activity to drive to a certain colour band? Change sensor mode (on brick?)
  - ?need to specify mode in code?


- Drive known number of motor ticks based on while monitoring of tick count
`drive_known_ticks.py`

- Calculate a mapping from ticks to distance
`drive_a_distance.py`

- Build up functions for driving a distance
`drive_a_distance_function.py`

- Reuse ticks drive function for turn_known_ticks
`turn_known_ticks_function.py`

- Reuse ideas and build on functions for turn_angle function
`turn_an_angle.py`

- Reuse distance and angle turn functions in for..in..range
`drive_square.py`

- simple bumper car - introduce touch sensor: forward, bump, reverse, turn, forward, while not buttonpress
`touchSensor.py`

- collision avoiding proximity detection: include random elements for turn direction and angle
`infra_red_proximity_bumper.py`

- homing beacon - use the infra-red sensor as a homing beacon and drive along the bearing to it
`homing_robot.py`

- gyro square corners - do the 90 degree turn based on the gyro
`gyro_square_corner.py`

- gyro square side heading - drive along a particular heading for each side-couldn't get this to work

- data logging as drive forward over stripes - data logger is too complicated for students to build from scratch
`data_logger_stripes.py`
