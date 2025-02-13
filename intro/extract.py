import cv2
import os

# Function to extract frames
def extract_frames(video_path, output_folder, interval_seconds):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return
    
    # Get the frame rate of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * interval_seconds)
    
    frame_count = 0
    saved_frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Save the frame at the specified interval
        if frame_count % frame_interval == 0:
            output_filename = os.path.join(output_folder, f"frame_{saved_frame_count:04d}.jpg")
            cv2.imwrite(output_filename, frame)
            saved_frame_count += 1
            print(f"Saved: {output_filename}")

        frame_count += 1

    # Release the video capture object
    cap.release()
    print(f"Extraction complete. {saved_frame_count} frames saved.")

# Usage example
video_path = r"C:\Users\masho\Downloads\Telegram Desktop\kolla.mkv"  # Replace with your video path
output_folder = r"D:\projects\python\frames"        # Folder to save frames
interval_seconds = 30                  # Interval in seconds

extract_frames(video_path, output_folder, interval_seconds)
