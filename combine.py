import comfyui
import ffmpeg
import os

class FrameCombinerNode(comfyui.Node):
    def __init__(self):
        super().__init__()
        self.input_dir = ''
        self.output_path = ''

    def render(self):
        if not self.input_dir:
            raise ValueError('Please specify the input directory.')
        if not self.output_path:
            raise ValueError('Please specify the output path.')

        # Get the list of frames in the input directory.
        frames = os.listdir(self.input_dir)
        frames.sort()

        # Create a video writer.
        writer = ffmpeg.output('frame_%04d.jpg' % i for i in range(len(frames)), self.output_path, vcodec='libx264', preset='veryslow')

        # Write the frames to the video writer.
        for frame in frames:
            writer.input(os.path.join(self.input_dir, frame))

        # Close the video writer.
        writer.close()

    def cleanup(self):
        pass
