import os
import shutil


def organize_downloads(source_dir, skip_folder, extensions_to_collect):
	# Define paths for source and result folder
	result_path = os.path.join(source_dir, "Result")
	
	# Create Result folder if it doesn't exist
	if not os.path.exists(result_path):
		os.makedirs(result_path)
	
	# Define subfolders for different types of media within Result folder
	subfolders = {ext: os.path.join(result_path, ext.capitalize()) for ext in extensions_to_collect}
	
	# Create subfolders if they don't exist
	for folder_path in subfolders.values():
		if not os.path.exists(folder_path):
			os.makedirs(folder_path)
	
	# Get a list of all files in the source directory
	files_in_source = os.listdir(source_dir)
	
	# Loop through the files and move files with specified extensions to the appropriate subfolder in the Result folder
	for file_name in files_in_source:
		file_path = os.path.join(source_dir, file_name)
		
		# Skip the specified folder
		if skip_folder in file_path:
			continue
		
		# Skip folders and non-media files
		if os.path.isfile(file_path):
			file_extension = os.path.splitext(file_name)[-1].lower()
			
			# Check if the file extension matches any specified type
			for ext, folder_path in subfolders.items():
				if file_extension == ext:
					shutil.move(file_path, os.path.join(folder_path, file_name))
					print(f"Moved to {folder_path}: {file_name}")
					break

if __name__ == '__main__':
	# Usage example:
	source_directory = "C:\\Users\\Admin\\Downloads"
	skip_directory = "C:\\Users\\Admin\\Downloads\\FEM_ISO_Q4"  # Folder name to skip checking
	extensions = [".m"]
	
	organize_downloads(source_directory, skip_directory, extensions)