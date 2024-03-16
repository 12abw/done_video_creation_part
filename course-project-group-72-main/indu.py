import os
from moviepy.editor import ImageSequenceClip
import cv2

def resize_image(image_path, target_width, target_height):
   image = cv2.imread(image_path)
   resized_image = cv2.resize(image, (target_width, target_height))
   return resized_image

def create_video_from_folder(folder_path, output_path, fps, total_duration):
   # Get a list of image files in the folder
   image_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(('.png', '.jpg', '.jpeg'))]

   if not image_files:
      print("No image files found in the folder. Exiting.")
      return

   # Get dimensions of the first image
   first_image = cv2.imread(image_files[0])
   target_width, target_height = first_image.shape[1], first_image.shape[0]

   # Resize all images to match dimensions of the first image
   resized_images = [resize_image(image_file, target_width, target_height) for image_file in image_files]

   # Calculate duration per image
   num_frames = len(resized_images)
   duration_per_image = total_duration / num_frames

   # Initialize VideoClip with the resized images and durations
   video_clip = ImageSequenceClip(resized_images, fps=fps)
   
   # Set durations for each frame
   frame_durations = [duration_per_image] * (num_frames - 1)  # Leave out last image
   frame_durations.append(total_duration - sum(frame_durations))  # Adjust duration for the last image
   video_clip = video_clip.set_duration(total_duration)

   # Write the video to a file
   video_clip.write_videofile(output_path, fps=fps)

   print("Video created successfully!")

# Example usage
folder_path = input("Enter the name of the folder containing the images (within the present working directory): ").strip()
output_path = input("Enter the output video file path: ").strip()
fps = int(input("Enter the frames per second (FPS) for the video: "))
total_duration = float(input("Enter the total duration (in seconds) for the video: "))

create_video_from_folder(folder_path, output_path, fps, total_duration)