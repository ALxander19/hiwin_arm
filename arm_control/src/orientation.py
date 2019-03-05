# tf.transformations alternative is not yet available in tf2
from tf.transformations import quaternion_from_euler
from tf.transformations import euler_from_quaternion
  
if __name__ == '__main__':

  # RPY to convert: 0, 0, -1.5708 look down
  # RPY to convert: -3.1416, 0, 1.5708 or -0.707,-0.707,0,0 look up
  q = quaternion_from_euler( 0, 0, 1.5708)

  print "The quaternion representation is %s %s %s %s." % (q[0], q[1], q[2], q[3])

  x = (0.0,0.0,-0.0,1)
  e = euler_from_quaternion(x)

  print "The euler representation is %s %s %s" % (e[0], e[1], e[2])

  # RPY to convert: 0, 0, -1.5708 look up
  # RPY to convert: 0, 0, 0 look horizontal
