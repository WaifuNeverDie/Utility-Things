import os
import shutil


def organize_downloads():
	# Define paths for downloads and media folder
	downloads_path = os.path.expanduser("~/Downloads")
	media_path = os.path.join(downloads_path, "Media")
	
	# Create Media folder if it doesn't exist
	if not os.path.exists(media_path):
		os.makedirs(media_path)
	
	# Define subfolders for different types of media within Media folder
	pictures_path = os.path.join(media_path, "Pictures")
	music_path = os.path.join(media_path, "Music")
	movies_path = os.path.join(media_path, "Movies")
	
	# Create subfolders if they don't exist
	for folder_path in [pictures_path, music_path, movies_path]:
		if not os.path.exists(folder_path):
			os.makedirs(folder_path)
	
	# File extensions for different types of media
	media_extensions = {
			"Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
			"Music": [".mp3", ".wav", ".aac", ".flac", ".m4a"],
			"Movies": [".mp4", ".mkv", ".avi", ".mov", ".wmv"]
			}
	
	# Get a list of all files in the Downloads folder
	files_in_downloads = os.listdir(downloads_path)
	
	# Loop through the files and move media files to the appropriate subfolder in the Media folder
	for file_name in files_in_downloads:
		file_path = os.path.join(downloads_path, file_name)
		
		# Skip folders and non-media files
		if os.path.isfile(file_path):
			file_extension = os.path.splitext(file_name)[-1].lower()
			
			# Check if the file extension matches any media type
			if file_extension in media_extensions["Pictures"]:
				shutil.move(file_path, os.path.join(pictures_path, file_name))
				print(f"Moved to Pictures: {file_name}")
			elif file_extension in media_extensions["Music"]:
				shutil.move(file_path, os.path.join(music_path, file_name))
				print(f"Moved to Music: {file_name}")
			elif file_extension in media_extensions["Movies"]:
				shutil.move(file_path, os.path.join(movies_path, file_name))
				print(f"Moved to Movies: {file_name}")


if __name__ == "__main__":
	organize_downloads()