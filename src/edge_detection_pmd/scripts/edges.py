#!/usr/bin/env python
from __future__ import print_function
import numpy as np
import roslib
roslib.load_manifest('edge_detection_pmd')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("image_topic_2",Image)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/royale_camera_driver/depth_image", Image, self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "32FC1")
    except CvBridgeError as e:
      print(e)

   
    #show resized image stream from pmd
    cv2.namedWindow("Image window", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Image window", cv_image.shape[1] * 3, cv_image.shape[0] * 3)
    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)
    #blur image with median blurring with a 5x5 pixel median
    median = cv2.medianBlur(cv_image,5)
    cv2.namedWindow("Blurred image window", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Blurred image window", cv_image.shape[1] * 3, cv_image.shape[0] * 3)
    cv2.imshow("Blurred image window", median)
    cv2.waitKey(3)
    #morphological transformation Opening transformation with ellipsoid kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    image_after_opening = cv2.morphologyEx(median, cv2.MORPH_OPEN, kernel)
    cv2.namedWindow("After Opening", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("After Opening", cv_image.shape[1] * 3, cv_image.shape[0] * 3)
    cv2.imshow("After Opening", image_after_opening)
    cv2.waitKey(3)
    #morphological transformation Closing transformation with ellipsoid kernel
    image_after_closing = cv2.morphologyEx(median, cv2.MORPH_CLOSE, kernel)
    cv2.namedWindow("After Closing", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("After Closing", cv_image.shape[1] * 3, cv_image.shape[0] * 3)
    cv2.imshow("After Closing", image_after_closing)
    cv2.waitKey(3)
    #Canny Edge detection
    #before canny edge detection can be applied image must be converted

    edges = auto_canny(np.uint8(image_after_closing))
    cv2.namedWindow("Edges", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Edges", cv_image.shape[1] * 3, cv_image.shape[0] * 3)
    cv2.imshow("Edges", edges)
    cv2.waitKey(3)
    



    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "32FC1"))
    except CvBridgeError as e:
     print(e)

def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
 
	# return the edged image
	return edged

def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
