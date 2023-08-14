from robot_control_class import RobotControl
rc = RobotControl() 
class Robot:
    def lab(self, motion, speed, time):
        self.rc = RobotControl()
        self.motion = motion
        self.clockwise = clockwise
        self.speed = speed
        self.time = time

    def lab1(self):
        self.rc = RobotControl()
        i = rc.get_laser(360)
        while (i > 1):
            i = self.rc.get_laser(360)
            self.rc.move_straight()
            print ("i = ", i)
        self.rc.stop_robot()

    def lab2(self):
        self.rc = RobotControl()
        self.rc.rotate(80)
        self.rc.move_straight()

    def lab3(self):
        self.rc = RobotControl()
        self.rc.rotate(-100)
        self.rc.move_straight()

    
l1 = Robot()
l1.lab1()
l2 = Robot()
l2.lab2()
l1 = Robot()
l1.lab1()
l2 = Robot()
l2.lab2()
l1 = Robot()
l1.lab1()
l3 = Robot()
l3.lab3()

