import cv2
import os
import random
import numpy as np
from io import BytesIO
from PIL import Image


def capture_random_frames(video_path, output_folder, num_captures):
    """
    Captures a fixed number of random screenshots from a video.

    Args:
        video_path (str): The path to the MP4 video file.
        output_folder (str): The folder to save the screenshots.
        num_captures (int): The total number of screenshots to capture.
    """

    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video file.")
        return  # Exit if video can't be opened

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Generate random frame indices to capture
    if num_captures >= total_frames:
        # Capture all frames if num_captures is greater than or equal to the total frames
        frame_indices = list(range(total_frames)) 
    else:
        frame_indices = random.sample(range(total_frames), num_captures)

    # Capture frames at the selected indices
    for i, frame_index in enumerate(frame_indices):
        # Set the frame position
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

        # Read the frame
        ret, frame = cap.read()
        if not ret:
            print(f"Error reading frame {frame_index}")
            continue  # Skip to the next frame if there's an error

        screenshot_path = os.path.join(output_folder, f"{i}.jpg")
        cv2.imwrite(screenshot_path, frame)
        print(f"Screenshot saved to: {screenshot_path}")

    # Release the video capture object
    cap.release()

def delete_files_in_directory(directory_path):
  """Deletes all files within a specified directory.

  Args:
    directory_path: The path to the directory containing the files to delete.
  """

  if not os.path.exists(directory_path):
    print(f"Error: Directory not found: {directory_path}")

  for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    try:
      if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"Deleted file: {file_path}")
    except Exception as e:
      print(f"Error deleting {file_path}: {e}")

def count_files_in_directory(directory_path):
  """Counts the number of files (not directories) in a directory.

  Args:
    directory_path: The path to the directory to count files in.

  Returns:
    The number of files in the directory, or -1 if an error occurs.
  """

  try:
    file_count = 0
    for item in os.listdir(directory_path):
      item_path = os.path.join(directory_path, item)
      if os.path.isfile(item_path):
        file_count += 1
    return file_count

  except FileNotFoundError:
    print(f"Error: Directory not found: {directory_path}")
    return -1
  except Exception as e:
    print(f"Error counting files in {directory_path}: {e}")
    return -1
  

def read_file_as_img(data)-> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))

    return image