#!/usr/bin/env python
# -*- coding: utf-8 -*-
from behave import *

class bt_mission:

    # common member
    center = [480, 320]
    rec_center = [478, 315]
    isContinue = True
    x = 0
    y = 0
    z = 0.0
    
    # Now_color
    color = "blue"

    def __init__(self):
        self.tree = (
            self.BlueNotFinish >> (self.isNotCenter | self.PassAndSwitch) >> self.FixedPose
            |self.RedNotFinish >> (self.isNotCenter | self.PassAndLand) >> self.FixedPose
        )

    @condition
    def BlueNotFinish(self):
        print("condition: BlueNotFinish")
        return bt_mission.color == "blue"

    @condition
    def RedNotFinish(self):
        print("condition: RedNotFinish")
        return bt_mission.color == "red"

    @condition
    def isNotCenter(self):
        print("condition: isNotCenter")
        return abs(bt_mission.rec_center[0] - bt_mission.center[0]) > 30 or abs(bt_mission.rec_center[1] - bt_mission.center[1]) > 30

    @action
    def PassAndSwitch(self):
        print("action: PassAndSwitch")

    @action
    def PassAndLand(self):
      print("action: PassAndLand")

    @action
    def FixedPose(self):
      print("action: FixedPose")

    def run(self):
        while True:
            if bt_mission.isContinue == False:
                break
            bb = self.tree.blackboard(1)
            state = bb.tick()
            print("state = %s\n" % state)
            while state == RUNNING:
                state = bb.tick()
                print ("state = %s\n" % state)
            assert state == SUCCESS or state == FAILURE

def main():
    print("start...") 
    btCm_n = bt_mission()
    #time.sleep(3)
    try:
        btCm_n.run()
    except KeyboardInterrupt:
        print("Shutting down ROS Image feature detector module")

if __name__ == "__main__":
    main()
