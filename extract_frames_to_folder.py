import cv2
import os

# --- Step 1: Input video path ---
video_path = "input/customplot_and_plot_combained_side_by_side.mp4"  # change to your file name

# --- Step 2: Create output folder with same name as input (no extension) ---
video_name = os.path.splitext(os.path.basename(video_path))[0]
output_folder = f"output/{video_name}"
os.makedirs(output_folder, exist_ok=True)

# --- Step 3: Read video ---
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    raise ValueError("❌ Could not open the video file. Check the path!")

# --- Step 4: Auto-detect total frames → decide padding digits ---
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
digits = len(str(total_frames))

# --- Step 5: Extract frames and save ---
frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    filename = os.path.join(output_folder, f"frame_{frame_count:0{digits}d}.jpg")
    cv2.imwrite(filename, frame)
    frame_count += 1

cap.release()
print(f"✅ Extracted {frame_count} frames to '{output_folder}' with {digits}-digit padding.")
