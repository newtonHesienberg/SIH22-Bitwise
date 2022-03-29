pip install katna

from Katna.video import Video
from Katna.writer import KeyFrameDiskWriter
import os
import ntpath
import cv2

# For windows, the below if condition is must.
if __name__ == "__main__":

  #instantiate the video class
  vd = Video()

  #number of key-frame images to be extracted
  no_of_frames_to_return = 3

  #Input Video directory path
  #All .mp4 and .mov files inside this directory will be used for keyframe extraction)
  videos_dir_path = "/content/ISRO1.mp4"

  diskwriter = KeyFrameDiskWriter(location="selectedframes")

  vd.extract_keyframes_from_videos_dir(
       no_of_frames=no_of_frames_to_return, dir_path=videos_dir_path,
       writer=diskwriter
  )