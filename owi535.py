import sys
import usb
import time
from owi535state import Owi535State


class Owi535:
    def __init__(self):
        self.state = Owi535State()
        self.arm = usb.core.find(idVendor=0x1267, idProduct=0x0001)  # owi535's hardware id
        if self.arm is None:
            raise ValueError("Arm not found")
        else:
            sys.stdout.write("Arm Connection established." + '\n')

    def SendMove(self):
        """
        Send a motion command to the robot.
        WARNING: This method does not contain a stop command. The robot will keep moving until \
        another stop command (implemented by other methods) is sent.
        """
        ArmCmd = self.state.render()
        self.arm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,3)

    def StopMove(self):
        """
        Send a stop command to pause the robot motion.
        This method does not change the motion state values.
        """
        ArmCmd = [0,0,0]
        self.arm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,3)

    def MoveTime(self, t):
        """
        Make the robot move for a certain time.

        :param t: duration time of the motion, in seconds.
        """
        self.SendMove()
        time.sleep(t)
        self.StopMove()

    def RotateBase(self, value=0):
        """
        Rotate the base motor (M5).

        :param value: motion state flag, if smaller than 0, rotate anticlockwise; \
        if larger than 0, rotate clockwise; if equals 0, cancel the rotation.
        """
        if value < 0:  # anti-clock wise
            self.state.startACW('base')
        elif value > 0:  # clock wise
            self.state.startCW('base')
        else:
            self.state.stopCW('base')
            self.state.stopACW('base')

    def RotateShoulder(self, value=0):
        """
        Rotate the shoulder motor (M4).

        :param value: motion state flag, if smaller than 0, the arm goes down; \
        if larger than 0, the arm goes up; if equals 0, cancel the motion.
        """
        if value < 0:  # down
            self.state.startACW('shoulder')
        elif value > 0:  # up
            self.state.startCW('shoulder')
        else:
            self.state.stopCW('shoulder')
            self.state.stopACW('shoulder')

    def RotateElbow(self, value=0):
        """
        Rotate the elbow motor (M3).

        :param value: motion state flag, if smaller than 0, the arm goes down; \
        if larger than 0, the arm goes up; if equals 0, cancel the motion.
        """
        if value < 0:  # down
            self.state.startACW('elbow')
        elif value > 0:  # up
            self.state.startCW('elbow')
        else:
            self.state.stopCW('elbow')
            self.state.stopACW('elbow')

    def RotateWrist(self, value=0):
        """
        Rotate the wrist motor (M2).

        :param value: motion state flag, if smaller than 0, the arm goes down; \
        if larger than 0, the arm goes up; if equals 0, cancel the motion.
        """
        if value < 0:  # down
            self.state.startACW('wrist')
        elif value > 0:  # up
            self.state.startCW('wrist')
        else:
            self.state.stopCW('wrist')
            self.state.stopACW('wrist')
    
    def RotateGripper(self, value=0):
        """
        Rotate the gripper motor (M1).

        :param value: motion state flag, if smaller than 0, open the gripper; \
        if larger than 0, close the gripper; if equals 0, cancel the motion.
        """
        if value < 0:
            self.state.startACW('gripper')  # open
        elif value > 0:
            self.state.startCW('gripper')  # close
        else:
            self.state.stopCW('gripper')
            self.state.stopACW('gripper')

    def SwitchLight(self, value=0):
        """
        Switch the light.

        :param value: light state flag, if larger than 0, turn on the light, \
        else turn off the light.
        """
        if value > 0:
            self.state.startCW('light')
        else:
            self.state.stopCW('light')
