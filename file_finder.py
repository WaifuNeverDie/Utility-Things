import os
import string
import ctypes
import time
import itertools
import threading

def search_file_with_keyword(keyword, search_path):
	"""
	Search for files that contain a specific keyword in all folders and subfolders.

	Parameters:
	- keyword: Keyword to search for in files.
	- search_path: Starting path to begin the search.

	Returns:
	- List of paths where the keyword is found.
	"""
	results = []
	cout = 1
	for root, dirs, files in os.walk(search_path):
		cout += 1
		print(f"Loading...{cout}")
		for file in files:
			file_path = os.path.join(root, file)
			try:
				with open(file_path, 'r', errors='ignore') as f:
					if keyword in f.read():
						results.append(file_path)
			except Exception as e:
				# Skip files that can't be opened (e.g., due to permission issues)
				continue
	return results

def get_available_drives():
	"""
	Get all available drive letters on the system.

	Returns:
	- List of available drives.
	"""
	drives = []
	bitmask = ctypes.windll.kernel32.GetLogicalDrives()
	for letter in string.ascii_uppercase:
		if bitmask & 1:
			drives.append(f"{letter}:\\")
		bitmask >>= 1
	return drives

def loading_animation(stop_event):
	"""
	Display a loading animation until the stop_event is set.
	"""
	for frame in itertools.cycle(['|', '/', '-', '\\']):
		if stop_event.is_set():
			break
		print(f"\rLoading {frame}", end="", flush=True)
		time.sleep(0.1)

def search_keyword_in_all_drives(keyword):
	"""
	Search for files containing the keyword in all available drives.

	Parameters:
	- keyword: Keyword to search for inside files.
	"""
	drives = get_available_drives()
	all_results = []
	
	stop_event = threading.Event()
	loading_thread = threading.Thread(target=loading_animation, args=(stop_event,))
	loading_thread.start()
	
	try:
		for drive in drives:
			print(f"\nSearching in drive {drive}...")
			results = search_file_with_keyword(keyword, drive)
			all_results.extend(results)
	finally:
		stop_event.set()
		loading_thread.join()
	
	print("\r", end="")  # Clear the loading line
	
	if all_results:
		print(f"Files containing the keyword '{keyword}' found at the following locations:")
		for result in all_results:
			print(result)
	else:
		print(f"No files containing the keyword '{keyword}' were found.")

if __name__ == "__main__":
	# Example usage
	keyword = "top111"
	search_keyword_in_all_drives(keyword)