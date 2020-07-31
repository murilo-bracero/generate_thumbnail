import sys
import cv2
from typing import Dict
from decorators import timestamp

THUMB_RESOLUTION = 640
FRAME_MOMENT_MULTIPLIER = 0.5

@timestamp
def generate_thumbnail(video_path: str, output_path: str):
    """
    Args:
        - video_path: str
          Video absolute path
        - output_path: str
          Thumbnail save path. For better performance, recommended .png format
    
    Returns:
        None
    
    Description:
        Extract a exact frame from provided video and transforms it into an image
    """

    print("Extract frame from video")

    frame = extract_frame(video_path)

    print ("Preparing thumbnail image")

    thumb = frame_to_image(frame)

    for _, buffer in thumb.items():
        print("Saving image")

        cv2.imwrite(output_path, buffer)

def extract_frame(video_filename: str):
    """
    Args:
        - video_filename: str
          Video absolute path
    
    Returns:
        OpenCV2 Frame
    
    Description:
        Extract a exact frame from provided video
    """

    video = cv2.VideoCapture(video_filename)
    video_length = int(video.get(cv2.CAP_PROP_FRAME_COUNT)) - 1

    if video.isOpened() and video_length > 0:
        frame_moment = round(video_length * FRAME_MOMENT_MULTIPLIER)
        count = 0

        success, frame = video.read()

        while success:
            if count == frame_moment:
                return frame
            success, frame = video.read()
            count += 1

def frame_to_image(frame) -> Dict[str, any]:
    """
    Args:
        - frame: any
          OpenCV2 Frame
    
    Returns:
        - dict[str, any]
          A dict with treated image of provided OpenCV2 video frame  
    
    Description:
        Transforms a OpenCV2 Frame from a OpenCV2 Video into a image file
    """

    height, width, _ = frame.shape
    thumb = {}
    size = THUMB_RESOLUTION

    if (width >= size):
        r = size / width
        max_size = (size, int(height * r))
        thumb[str(size)] = cv2.resize(frame, max_size, interpolation=cv2.INTER_AREA)

    return thumb

if __name__ == '__main__':
    _, video_path, thumb_path = sys.argv

    generate_thumbnail(video_path, thumb_path)