from moviepy.editor import ImageSequenceClip
import os
import cv2

# Define the paths
input_image_path = "C:\\Users\\yeduk\\Downloads\\fresh_after_midsem-main\\fresh_after_midsem-main\\course-project-group-72-main\\zemp\\images"
output_video_path = "C:\\Users\\yeduk\\Downloads\\fresh_after_midsem-main\\fresh_after_midsem-main\\course-project-group-72-main\\zemp"
output_video_name = "out.mp4"
output_video_full_path = os.path.join(output_video_path, output_video_name)

# Read the input images and sort them
image_files = sorted(os.listdir(input_image_path))
if not image_files:
    print("No image files found in the input directory.")
    exit()

# Read the first image to get its dimensions
first_image = cv2.imread(os.path.join(input_image_path, image_files[0]))
if first_image is None:
    print("Failed to read the first image.")
    exit()
height, width, _ = first_image.shape

# Resize images to the same dimensions
for img_file in image_files:
    img_path = os.path.join(input_image_path, img_file)
    img = cv2.imread(img_path)
    if img is None:
        print(f"Failed to read image: {img_path}")
        continue
    img_resized = cv2.resize(img, (width, height))
    cv2.imwrite(img_path, img_resized)

# Calculate the number of frames per image to ensure at least 1 second per image
num_images = len(image_files)
fps = 25
duration_per_image = 8  # Set the duration per image to 2 seconds
num_frames_per_image = max(1, int(fps * duration_per_image / num_images))  # Ensure at least 2 seconds per image

# Create a list of image files where each image is repeated according to the calculated number of frames
image_files_expanded = [os.path.join(input_image_path, img_file) for img_file in image_files for _ in range(num_frames_per_image)]

# Create ImageSequenceClip from the images with the expanded list
clip = ImageSequenceClip(image_files_expanded, fps=fps)

# Write the video file
clip.write_videofile(output_video_full_path, codec='libx264')
