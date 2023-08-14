#include "rosbot_control/rosbot_class.h"
#include <ros/ros.h>
#include <math.h>
#include <string>

using namespace std;

class Rosbot {
public:
    RosbotClass rosbot;
    void Run();
    float dist(float x1, float x2, float y1, float y2);
};

void Rosbot::Run() {
    rosbot.move_forward(1);
        while (rosbot.get_laser(0) > 1.75) {
        ROS_INFO_STREAM(rosbot.get_laser(0));
        rosbot.move_forward(1);
        }

    rosbot.turn("clockwise", 3.0);
    rosbot.move_forward(2);
    rosbot.turn("counterclockwise",3);


    float x1 = rosbot.get_position(1);
    float y1 = rosbot.get_position(2);
    float x2 = x1;
    float y2 = y1;
    float distance = dist(x1, y1, x2, y2);
        while (distance < 8.0) {
        x1 = rosbot.get_position(1);
        y1 = rosbot.get_position(2);
        ROS_INFO_STREAM(distance);
        rosbot.move_forward(1);
        }

    rosbot.turn("clockwise", 3.0);
    rosbot.move_forward(5);
    ROS_INFO_STREAM("!!!!");
    }
float Rosbot::dist(float x1, float y1, float x2, float y2){
return sqrt(pow(x2-x1,2)+ pow(y2-y1,2));
}

int main(int argc,char **argv) {
ros::init(argc, argv,"Rosbot_move_node");
Rosbot rosbot_moves;
rosbot_moves.Run();
}




