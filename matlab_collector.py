import os
import shutil


def move_matlab_files(source_dir, target_dir, skip_folder):
	# Create the target directory if it doesn't exist
	os.makedirs(target_dir, exist_ok=True)
	
	# Track duplicate file counts
	file_counts = {}
	
	# Walk through the source directory
	for root, dirs, files in os.walk(source_dir):
		# Skip the specified folder
		if skip_folder in root:
			continue
		
		for file in files:
			# Process only .m files
			if file.endswith(".m"):
				file_path = os.path.join(root, file)
				
				# Rename file if a duplicate exists
				if file in file_counts:
					file_counts[file] += 1
					base, ext = os.path.splitext(file)
					new_file_name = f"{base}_{file_counts[file]}{ext}"
				else:
					file_counts[file] = 0
					new_file_name = file
				
				# Move file to the target directory
				target_file_path = os.path.join(target_dir, new_file_name)
				shutil.move(file_path, target_file_path)
				print(f"Moved {file_path} to {target_file_path}")


# Usage example:
source_directory = "C:\\Users\\Admin\\Downloads"
target_directory = "C:\\Users\\Admin\\Downloads\\MatlabCollector"
skip_directory = "C:\\Users\\Admin\\Downloads\\FEM_ISO_Q4"  # Folder name to skip checking

move_matlab_files(source_directory, target_directory, skip_directory)
