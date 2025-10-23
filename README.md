# 🎬 Frame & Video Processing Utilities

A collection of Python scripts for handling video frame operations using **OpenCV**.  
You can extract frames from a video, combine multiple frames into a single image grid, split that grid back into frames, and recreate a video from frames.



---

## ⚙️ Requirements

- Python 3.8 or higher  
- [OpenCV]
- [NumPy]

Install dependencies:
pip install opencv-python numpy



1️⃣ extract_frames_to_folder.py

Concept:
A video is made up of many individual frames (images) shown quickly in sequence.
This script extracts each of those frames and saves them as separate image files.

Use Case:
Ideal for analyzing, editing, or processing each frame individually — for example, to train AI models, apply filters, or inspect motion between frames.

2️⃣ combine_frames_to_single_frame.py

Concept:
Multiple frames can be arranged into a single large “grid” image — similar to a collage or film strip — making it easier to visualize sequences or comparisons at a glance.

Use Case:
Helpful for summarizing video sequences, creating preview thumbnails, or compressing many images into one for easier sharing or archiving.

3️⃣ single_frame_to_multiple_frames.py

Concept:
This script reverses the grid-combining process. It splits a combined grid image back into individual frame images and restores their original resolution.

Use Case:
Useful when you need to recover or reprocess individual frames that were previously merged into a grid — for example, during dataset reconstruction or video restoration tasks.


4️⃣ frames_to_video.py

Concept:
A video can be reconstructed from a sequence of images (frames) displayed rapidly one after another at a fixed frame rate (FPS).
This script reads ordered frames from a folder and compiles them into a playable video file.

Use Case:
Ideal for generating a video after frame-based processing — such as after image filtering, animation rendering, AI-generated frame interpolation, or reconstruction from extracted frames.
