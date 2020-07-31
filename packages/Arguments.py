from typing import List

class Arguments:
    def __init__(self, args: List[str]):
        supported_image_types = ['jpg', 'png', 'gif']
        supported_video_types = ['mkv', 'mp4']
        
        if len(args) < 2:
            print('Error: must receive 2 positional arguments: <video path> <image path>')
            return

        self.video_path, self.output_path = args

        video_filetype = self.video_path.split('.')[-1]
        image_filetype = self.output_path.split('.')[-1]

        try:
            supported_image_types.index(image_filetype)
        except:
            print('Error: Image output type is not supported. Open a Issue in our GitHub repo for more information')
            return

        try:
            supported_video_types.index(video_filetype)
        except:
            print('Error: Video type is not supported. Open a Issue in our GitHub repo for more information')
            return