import rclpy
import rclpy.node

class MinimalParam(rclpy.node.Node):
    def __init__(self):
        super().__init__('minimal_param_node')

        self.declare_parameter('parameter1', 'cat')

        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        my_param = self.get_parameter('parameter1').get_parameter_value().string_value

        self.get_logger().info('Pretty %s!' % my_param)

        my_new_param = rclpy.parameter.Parameter(
            'parameter1',
            rclpy.Parameter.Type.STRING,
            'cat'
        )
        all_new_parameters = [my_new_param]
        self.set_parameters(all_new_parameters)

def main():
    rclpy.init()
    node = MinimalParam()
    rclpy.spin(node)

if __name__ == '__main__':
    main()