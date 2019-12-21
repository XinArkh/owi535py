import time
from owi535 import Owi535


# NOTE: insufficient power may cause all the motors cannot work simultaneously

# connect with the robot
arm = Owi535()
# set up motion configureations
arm.RotateBase(1)
arm.RotateShoulder(1)
arm.RotateElbow(-1)
arm.RotateWrist(-1)
# arm.RotateGripper(1)
arm.SwitchLight(1)
# keep motion for 3 seconds
arm.MoveTime(3)

time.sleep(1)

# set up motion configureations
arm.RotateBase(-1)
arm.RotateShoulder(-1)
arm.RotateElbow(1)
arm.RotateWrist(1)
# arm.RotateGripper(-1)
arm.SwitchLight(1)
# keep motion for 3 seconds
arm.MoveTime(3)
