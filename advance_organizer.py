import os
import shutil


def organize_downloads():
	# Define paths for downloads and media folder
	downloads_path = os.path.expanduser("~/Downloads")
	media_path = os.path.join(downloads_path, "Media")
	
	# Create Media folder if it doesn't exist
	if not os.path.exists(media_path):
		os.makedirs(media_path)
	
	# File extensions for different types of media
	media_extensions = {
			"Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
			"Music"   : [".mp3", ".wav", ".aac", ".flac", ".m4a"],
			"Movies"  : [".mp4", ".mkv", ".avi", ".mov", ".wmv"]
			}
	
	# Get a list of all files in the Downloads folder
	files_in_downloads = os.listdir(downloads_path)
	
	# Loop through the files and move media files to the Media folder
	for file_name in files_in_downloads:
		file_path = os.path.join(downloads_path, file_name)
		
		# Skip folders and non-media files
		if os.path.isfile(file_path):
			file_extension = os.path.splitext(file_name)[-1].lower()
			
			# Check if the file extension matches any media type
			for media_type, extensions in media_extensions.items():
				if file_extension in extensions:
					# Move file to Media folder
					shutil.move(file_path, os.path.join(media_path, file_name))
					print(f"Moved: {file_name}")
					break


if __name__ == "__main__":
	organize_downloads()
