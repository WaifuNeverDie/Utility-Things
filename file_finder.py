import os


def search_file(filename, search_path):
	"""
	Search for a file by name in all folders and subfolders.

	Parameters:
	- filename: Name of the file to search for.
	- search_path: Starting path to begin the search.

	Returns:
	- List of paths where the file is found.
	"""
	results = []
	cout =  1
	for root, dirs, files in os.walk(search_path):
		cout +=1
		print(f"Loading...{cout}")
		if filename in files:
			results.append(os.path.join(root, filename))
	
	if results:
		print(f"File '{filename}' found at the following locations:")
		for result in results:
			print(result)
	else:
		print(f"File '{filename}' not found.")

if __name__ == "__main__":
	# Example usage
	filename = input("Enter the filename you want to search for: ")
	search_path = "C:\\"  # Set to the root directory or any specific starting directory
	search_file(filename, search_path)
