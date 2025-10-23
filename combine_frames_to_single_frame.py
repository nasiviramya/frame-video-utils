import cv2
import numpy as np
import os
import glob
import math

# --- Step 1: Input folder and parameters ---
frames_folder = "input/thathamanavadu_mask_merged"   # folder with source frames
output_folder = "output/thathamanavadu_mask_merged"
os.makedirs(output_folder, exist_ok=True)

images_per_row = 2                # how many per row
total_images_per_combined = 6     # total images per combined image

# --- Step 2: Collect and sort frames ---
image_paths = sorted(glob.glob(os.path.join(frames_folder, "*.jpg")))
if not image_paths:
    raise ValueError("❌ No frames found in input folder!")

# --- Step 3: Base image dimensions ---
sample = cv2.imread(image_paths[0])
base_h, base_w = sample.shape[:2]

# --- Step 4: Calculate grid dimensions ---
rows = math.ceil(total_images_per_combined / images_per_row)
new_w = base_w // images_per_row
new_h = base_h // rows

# --- Step 5: Combine frames ---
for i in range(0, len(image_paths), total_images_per_combined):
    batch = image_paths[i:i + total_images_per_combined]
    resized_imgs = [cv2.resize(cv2.imread(p), (new_w, new_h)) for p in batch]

    # Black padding if needed
    while len(resized_imgs) < total_images_per_combined:
        resized_imgs.append(np.zeros((new_h, new_w, 3), dtype=np.uint8))

    # Stack into grid
    grid_rows = []
    for r in range(rows):
        start = r * images_per_row
        end = start + images_per_row
        row_imgs = resized_imgs[start:end]
        grid_rows.append(np.hstack(row_imgs))

    combined = np.vstack(grid_rows)

    # --- Step 6: Save output ---
    out_name = f"combined_{i//total_images_per_combined:04d}.jpg"
    out_path = os.path.join(output_folder, out_name)
    cv2.imwrite(out_path, combined)
    print(f"✅ Saved {out_path} ({len(batch)} frames)")

print("🎉 All combined images created successfully.")




