import cv2
import numpy as np
import os
import glob
import math

# --- Step 1: Input/output paths ---
combined_folder = "output/thathamanavadu_mask_merged"
split_output = "output/thathamanavadu_mask_merged_frames"
os.makedirs(split_output, exist_ok=True)

images_per_row = 2                # must match combine script
total_images_per_combined = 6     # must match combine script

# --- Step 2: Define original size to restore ---
original_width = 1280
original_height = 720

# --- Step 3: Read combined images ---
combined_paths = sorted(glob.glob(os.path.join(combined_folder, "*.jpg")))
if not combined_paths:
    raise ValueError("❌ No combined images found!")

for img_idx, path in enumerate(combined_paths):
    combined = cv2.imread(path)
    if combined is None:
        print(f"⚠️ Skipping unreadable image: {path}")
        continue

    h, w, _ = combined.shape
    rows = math.ceil(total_images_per_combined / images_per_row)
    sub_w = w // images_per_row
    sub_h = h // rows

    frame_count = 0
    for r in range(rows):
        for c in range(images_per_row):
            y1, y2 = r * sub_h, (r + 1) * sub_h
            x1, x2 = c * sub_w, (c + 1) * sub_w

            sub_img = combined[y1:y2, x1:x2]

            # Resize back to original frame size
            restored = cv2.resize(sub_img, (original_width, original_height))

            out_name = f"restored_{img_idx:02d}_{frame_count:02d}.jpg"
            out_path = os.path.join(split_output, out_name)
            cv2.imwrite(out_path, restored)
            frame_count += 1

    print(f"✅ Split {path} into {frame_count} restored frames.")

print("🎉 All combined images successfully split and resized.")
