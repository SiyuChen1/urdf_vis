import pybullet as p
import time
import math
import os

p.connect(p.GUI)

p.setAdditionalSearchPath(os.getcwd())
p.loadURDF("birdbot_v01.urdf", useFixedBase = 1)

for i in range(10000):
    p.stepSimulation()
    time.sleep(.1)

p.disconnect()