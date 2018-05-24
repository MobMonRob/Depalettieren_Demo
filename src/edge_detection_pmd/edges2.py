#!/usr/bin/env python
import numpy as np
import time

import cv2
import roslib
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

from JsonManager import JsonManager
from ObjectManager import ObjectManager

roslib.load_manifest('edge_detection_pmd')

class image_converter:

  def __init__(self):
    #self.image_pub = rospy.Publisher("image_topic_2",Image)


    self.image_sub = rospy.Subscriber("/royale_camera_driver/depth_image", Image, self.callback)
    self.cv_bridge = CvBridge()
    self.settings =JsonManager("../parameters/settings.json").load_json()
    self.timestamp_last_call = time.time()
    self.state = None
    self.pressed_key = -1
    self.colors = {"blue": (255, 0, 0), "green": (0, 255, 0), "red": (0, 0, 255), "yellow": (0, 255, 255),
                       "pink": (255, 0, 255)}

    self.image_bw = None
    self.image_rgb = None
    self.image_prepared = None
    self.contours = None
    rospy.loginfo("to enable/disable debugging images, press D")
    self.debugging = self.settings["debugging"]

  def callback(self,img_msg):
    if time.time() > self.timestamp_last_call + 1:
       self.timestamp_last_call = time.time()
       self.convert_img_msg(img_msg)
       #cv2.namedWindow("BW", cv2.WINDOW_NORMAL)

       #cv2.imshow("BW", self.image_bw)
       #cv2.waitKey(3)
       #cv2.namedWindow("RGB", cv2.WINDOW_NORMAL)

       #cv2.imshow("RGB", self.image_rgb)
       #cv2.waitKey(3)
       #self.prepare_image()

       
       self.get_contours()
       
       self.state
       if self.pressed_key ==27:
          rospy.signal_shutdown("User Shutdown")
       if self.pressed_key == ord('d'):
          self.debugging = not self.debugging
          rospy.loginfo("Debugging: " + str(self.debugging))
  def convert_img_msg(self, img_msg):
    float_image = self.cv_bridge.imgmsg_to_cv2(img_msg, "32FC1")
    float_image[float_image <0.01] = self.settings["camera_thresh"]
    float_image = (float_image - self.settings["camera_min"]) / \
                      (self.settings["camera_max"] - self.settings["camera_min"])
    float_image[float_image > 1] = 1
    float_image[float_image < 0] = 0

        # Convert 32fc1 to 8uc1
    self.image_bw = (float_image * 255).astype('u1')
    self.image_rgb = cv2.cvtColor(self.image_bw, cv2.COLOR_GRAY2RGB)
  def prepare_image(self):
    thresh = (self.settings["camera_thresh"] - self.settings["camera_min"]) * 255 / \
             (self.settings["camera_max"] - self.settings["camera_min"])

    ret, prepared_image = cv2.threshold(self.image_bw, thresh, 0, cv2.THRESH_TOZERO_INV)
    # Remove noise
    prepared_image = cv2.morphologyEx(prepared_image, cv2.MORPH_OPEN,
                                          cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
    self.image_prepared = prepared_image

  def debug_image(self, image, window_name):
        if self.debugging:
            show_image(image, window_name)
       
  
  def get_contours(self):
# Delete areas further away than ...
        thresh = (self.settings["camera_thresh"] - self.settings["camera_min"]) * 255 / \
                 (self.settings["camera_max"] - self.settings["camera_min"])

        ret, prepared_image = cv2.threshold(self.image_bw, thresh, 0, cv2.THRESH_TOZERO_INV)
        # Remove noise

        prepared_image = cv2.morphologyEx(prepared_image, cv2.MORPH_OPEN,
                                          cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))

        self.debug_image(prepared_image, "Prepared Image")

        # Find Contours
        image, contours, hierarchy = cv2.findContours(prepared_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Filter useful contours
        self.contours = []
        image_y, image_x = self.image_bw.shape
        corners = [(2, 2), (2, image_y - 3), (image_x - 3, 2), (image_x - 3, image_y - 3)]
        for contour in contours:
            # Only select contours with more than 40 points
            if len(contour) > self.settings["minimal_contour_length"]:
                in_corner = False
                # Test if Contour is in one of the corners
                for point in corners:
                    if cv2.pointPolygonTest(contour, point, False) == 1:
                        in_corner = True
                if not in_corner:
                    self.contours.append(contour)

        # Sort useful contours by their number of points
        self.contours.sort(key=len, reverse=True)

        # Show useful contours
        image_show = np.copy(self.image_rgb)
        # drawContours(image, contours, contourIdx, color, thickness)
        cv2.drawContours(image_show, self.contours, -1, (0, 255, 255), 1)
        for corner in corners:
            cv2.circle(image_show, corner, 1, color=self.colors["blue"], thickness=1)
        self.debug_image(image_show, "Useful Contours")

def show_image(image, window_name):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, image.shape[1] * 4, image.shape[0] * 4)
    cv2.imshow(window_name, image)  # Show image

def main():
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
