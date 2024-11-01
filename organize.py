import os
import shutil

def organize_downloads_folder(target_folder):
	# Define paths for target and media folder
	target_folder = os.path.expanduser(target_folder)
	media_folder = os.path.join(target_folder, "Media")
	
	# Create Media folder if it doesn't exist
	if not os.path.exists(media_folder):
		os.makedirs(media_folder)
	
	# File extensions for different types of media
	picture_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"]
	music_extensions = [".mp3", ".wav", ".aac", ".flac", ".m4a"]
	movie_extensions = [".mp4", ".mkv", ".avi", ".mov", ".wmv"]
	
	# Get a list of all files in the target folder
	files = os.listdir(target_folder)
	
	# Loop through the files and move media files to the Media folder
	for file in files:
		file_path = os.path.join(target_folder, file)
		
		# Skip folders and non-media files
		if os.path.isfile(file_path):
			file_extension = os.path.splitext(file)[-1].lower()
			
			if (file_extension in picture_extensions or
					file_extension in music_extensions or
					file_extension in movie_extensions):
				
				# Move file to Media folder
				shutil.move(file_path, os.path.join(media_folder, file))
				print(f"Moved: {file}")

if __name__ == "__main__":
	target_folder = os.path.expanduser("~/Downloads")
	organize_downloads_folder(target_folder)

