// Required headers for the node
#include "ros/ros.h"
#include "geometry_msgs/Twist.h" // turtle's cmd_vel
#include "turtlesim/Pose.h" // reading turtle's position
#include "turtlesim/SetPen.h"
#include "turtlesim/TeleportAbsolute.h"

class TurtleLawnmower
{
    ros::NodeHandle nh_;
    ros::Subscriber sub_;
    ros::Publisher pub_;
    bool turtleInitialized = false;
    bool leftEdge = true;
    bool changeLeftEdge=false;
    int turnCounter=0;
    public:
        TurtleLawnmower(); // Class constructor
        ~TurtleLawnmower(); // Class destructor

    void turtleCallback(const turtlesim::Pose::ConstPtr& msg);
    void initializeTurtle();
};

TurtleLawnmower::TurtleLawnmower()
{
    sub_ = nh_.subscribe("turtle1/pose", 1, &TurtleLawnmower::turtleCallback, this);
    pub_ = nh_.advertise<geometry_msgs::Twist>("turtle1/cmd_vel", 1);
}

TurtleLawnmower::~TurtleLawnmower()
{}

int main(int argc, char **argv)
{
    // Initialize the node and an object that will process data
    ros::init(argc, argv, "turtle_lawnmower_node");
    TurtleLawnmower TtMower;
    ros::spin();
    return 0;
}

void TurtleLawnmower::turtleCallback(const turtlesim::Pose::ConstPtr& msg)
{    
    if (!turtleInitialized)
        initializeTurtle();


    geometry_msgs::Twist turtle_cmd_vel;

    if(msg->y < 10.5)
    {
        if(msg->x > 0.5 && msg->x < 10.6 || msg->x <= 0.5 && turnCounter == 0)
        {
            turtle_cmd_vel.linear.x = 1.08009;
            if(msg->theta<-0.01)
                turtle_cmd_vel.angular.z = -0.11;
            else if(msg->theta>0.01)
                turtle_cmd_vel.angular.z = 0.11;
            if(turnCounter>0 && leftEdge && turnCounter!=1)
                leftEdge = false;
            else if(changeLeftEdge)
            {
                leftEdge = true;
                changeLeftEdge = false;
                turnCounter=1;
            }
        }

        else if(msg->theta<5 && leftEdge) 
        {
            //turning left
            
            turtle_cmd_vel.angular.z = 4.065;
            turtle_cmd_vel.linear.x = 1.57;
          
            turnCounter=turnCounter+1;
        }

        else if (leftEdge == false)
        {
            turtle_cmd_vel.linear.x = 1.7;
            turtle_cmd_vel.angular.z = -4.008;
            changeLeftEdge = true;
        }
    }

    

    pub_.publish(turtle_cmd_vel);
    ROS_INFO("Turtle lawnmower@[%f, %f, %f]", msg->x, msg->y, msg->theta); 
}

void TurtleLawnmower::initializeTurtle()
{
    turtleInitialized = true;
    ros::ServiceClient pen_client = nh_.serviceClient<turtlesim::SetPen>("/turtle1/set_pen");
    turtlesim::SetPen turnThePenOff;
    turnThePenOff.request.off = 1;
    pen_client.call(turnThePenOff);

    ros::ServiceClient pose_client = nh_.serviceClient<turtlesim::TeleportAbsolute>("/turtle1/teleport_absolute");
    turtlesim::TeleportAbsolute initialPose;
    initialPose.request.x = 0.7;
    initialPose.request.y = 0.3;
    pose_client.call(initialPose);

    turtlesim::SetPen turnThePenOn;
    turnThePenOn.request.off = 0;
    turnThePenOn.request.r = 255;
    turnThePenOn.request.g = 255;
    turnThePenOn.request.b = 255;
    turnThePenOn.request.width = 3;
    pen_client.call(turnThePenOn);
}


