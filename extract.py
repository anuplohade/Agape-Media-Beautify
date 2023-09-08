import comfyui
import ffmpeg
import os

class FrameExtractorNode(comfyui.Node):
    def __init__(self):
        super().__init__()
        self.video_path = ''
        self.output_dir = ''

    def render(self):
        if not self.video_path:
            raise ValueError('Please specify the path to the video file.')
        if not self.output_dir:
            raise ValueError('Please specify the output directory.')

        # Extract the frames from the video file.
        frames = ffmpeg.input(self.video_path).frames()

        # Rename the frames incrementally.
        for i, frame in enumerate(frames):
            frame.filename = f'frame_{i:04d}.jpg'

        # Store the frames in the output directory.
        frames.output(os.path.join(self.output_dir, '*'))

    def cleanup(self):
        pass
