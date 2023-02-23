import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

"""
Features from accelerated segment test (FAST) Corner Detector
https://en.wikipedia.org/wiki/Features_from_accelerated_segment_test
"""

def fast_detector(img):
  fast = cv.FastFeatureDetector_create()
  """
  Drawing keypoints
  """
  kp = fast.detect(img,None)
  img2 = cv.drawKeypoints(img, kp, None, color=(255,0,0))
  # Print all default params
  print( "Threshold: {}".format(fast.getThreshold()) )
  print( "nonmaxSuppression:{}".format(fast.getNonmaxSuppression()) )
  print( "neighborhood: {}".format(fast.getType()) )
  print( "Total Keypoints with nonmaxSuppression: {}".format(len(kp)) )
  cv.imwrite('fast_true.png', img2)
  """
  NON_MAX(NMS) Supression Disabled
  """
  fast.setNonmaxSuppression(0)
  kp = fast.detect(img, None)
  detected_img = cv.drawKeypoints(img, kp, None, color=(255,0,0))
  return detected_img

if __name__ == "__main__":
  input_img = cv.imread("path_to_image", cv.IMREAD_GRAYSCALE)
  corner_detect = fast_detector(input_img)
  cv.imwrite("detected.png", corner_detect)
    
   
