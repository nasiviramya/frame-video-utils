import cv2
import os
import glob

# --- Step 1: Folder containing frames ---
frames_folder = r"C:\Users\admin\Desktop\frames pipeline\input\t2"
 # example path 
# --- Step 2: Get only the base folder name ---
base_name = os.path.basename(frames_folder.rstrip("/\\"))  # e.g. "thathamanavadu_mask_merged"

# --- Step 3: Output video path ---
os.makedirs("output", exist_ok=True)  # ensure output folder exists
video_name = f"output/{base_name}.mp4"

# --- Step 4: FPS (customizable) ---
fps = 30  # change as needed

# --- Step 5: Collect and sort frames ---
image_files = sorted(
    glob.glob(os.path.join(frames_folder, "*.jpg")) +
    glob.glob(os.path.join(frames_folder, "*.png"))
)


if not image_files:
    raise ValueError("❌ No frame images found in the folder!")

# --- Step 6: Get dimensions from first frame ---
first_frame = cv2.imread(image_files[0])
height, width, _ = first_frame.shape

# --- Step 7: Create video writer ---
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

# --- Step 8: Write frames ---
for idx, img_path in enumerate(image_files):
    frame = cv2.imread(img_path)
    if frame is None:
        print(f"⚠️ Skipping unreadable frame: {img_path}")
        continue
    out.write(frame)

out.release()
print(f"✅ Video '{video_name}' created successfully at {fps} FPS.")
