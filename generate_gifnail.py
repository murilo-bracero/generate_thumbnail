import sys
import cv2
import imageio
from typing import Any, List
from packages.Arguments import Arguments
from decorators import timestamp

GIF_RESOLUTION = 640
GIF_FRAMES = 240

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

    frames = extract_frame(video_path)

    print ("Preparing thumbnail image")

    buffers = frames_to_buffers(frames)

    print(f'Saving image')

    imageio.mimsave(output_path, buffers, fps=60)

def extract_frame(video_filename: str) -> List[Any]:
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
        frames = []
        count = 0

        success, frame = video.read()

        while success:
            if count <= GIF_FRAMES:
                print(f'computing frame {count}', end='\r', flush=True)

                # color correction
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

                frames.append(frame)
            else:
                return frames
            success, frame = video.read()
            count += 1

def frames_to_buffers(frames: List[Any]) -> List[Any]:
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
    size = GIF_RESOLUTION
    buffers = []

    for frame in frames:
        y, x, _ = frame.shape
        max_size = (x // 5, y // 6)
        buffers.append(cv2.resize(frame, max_size, interpolation=cv2.INTER_AREA))

    return buffers

if __name__ == '__main__':
    args = Arguments(sys.argv[1:])

    generate_thumbnail(args.video_path, args.output_path)