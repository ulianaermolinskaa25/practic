from robot_control_class import RobotControl

class Robot:
    def __init__(self, motion,clockwise,speed,time,) -> None:
        self.rc = RobotControl(robot_name="summit")
        self.motion = motion
        self.clockwise = clockwise
        self.speed = speed
        self.time = time
        self.time_turn = 7

    def circle(self):
        x = 0

        while (x < 4):
            self.move_straight()
            self.turn()
            x +=1
    
    def move_straight(self):
        self.rc.move_straight_time(self.motion, self.speed, self.time)

    def turn(self):  
        self.rc.turn(self.clockwise, self.speed, self.time)  

l1 = Robot('forward','clockwise', 0.5, 5)
l1.circle()

l2 = Robot('forward', 'clockwise', 0.5, 5)
l2.circle()
