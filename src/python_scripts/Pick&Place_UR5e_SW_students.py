import time
from math import radians, degrees, pi
from robodk.robolink import Robolink
from robodk.robomath import *

# Robot setup
RDK = Robolink()
robot = RDK.Item("UR5e")
base = RDK.Item("UR5e Base")
tool = RDK.Item('2FG7')
Init_target = RDK.Item('Init')
Pick_target = RDK.Item('Pick')
table = RDK.Item("Table")
cube = RDK.Item('cube')
cube.setVisible(False)
cube_POSE=Pick_target.Pose()
cube.setPose(cube_POSE)
cube.setParent(table)# Do not maintain the actual absolute POSE

robot.setPoseFrame(base)
robot.setPoseTool(tool)
robot.setSpeed(20)

def Init():
    print("Init")
    robot.MoveL(Init_target, True)
    print("Init_target REACHED")
    cube.setVisible(True)

def Pick():
    print("Pick")
    robot.MoveL(Pick_target, True)
    cube.setParentStatic(tool)#Maintain the actual absolute POSE
    print("Pick FINISHED")

# Main function
def main():
    Init()
    Pick()
    Init()
     
if __name__ == "__main__":
    main()