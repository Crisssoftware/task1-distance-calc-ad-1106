import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
from turtlesim.msg import Pose
class Distance(Node):
    def __init__(self):
        super().__init__('Distance')
        self.subscription = self.create_subscription(Pose,'/turtle1/pose',self.listener_callback,10)
        self.publisher = self.create_publisher(Float32,'/turtle1/distance_from_origin',10)
        self.timer = self.create_timer(0.5,self.timer_callback)
        self.subscription  # prevent unused variable warning
        self.distance = 0.0
        self.x = 0
        self.y = 0
    def listener_callback(self, msg):
        self.x = msg.x
        self.y = msg.y
        self.distance = ((self.x)**2 +(self.y)**2) **0.5
    def timer_callback(self):
        message = Float32()
        message.data = self.distance
        self.publisher.publish(message)
        self.get_logger().info('Publishing: "%f"' % message.data)




def main(args=None):
    rclpy.init(args=args)

    Distance_calculator = Distance()

    rclpy.spin(Distance_calculator)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    Distance_calculator.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()