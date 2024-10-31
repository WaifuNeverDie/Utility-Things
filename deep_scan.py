import pytsk3
import sys

def deep_scan_filesystem(drive_letter):
	# Open a drive for deep scan
	drive_path = f'\\\\.\\{drive_letter}:'
	img = pytsk3.Img_Info(drive_path)
	fs = pytsk3.FS_Info(img)
	
	def scan_directory(directory):
		for entry in directory:
			if entry.info.name.name in [b'.', b'..']:
				continue
			
			# Deleted files have certain flags, let's filter for them
			if entry.info.meta and entry.info.meta.flags == pytsk3.TSK_FS_META_FLAG_UNALLOC:
				print(f"Deleted file found: {entry.info.name.name.decode('utf-8')}")
			
			# Recursively scan subdirectories
			if entry.info.meta and entry.info.meta.type == pytsk3.TSK_FS_META_TYPE_DIR:
				scan_directory(entry.as_directory())
	
	root = fs.open_dir('/')
	scan_directory(root)
if __name__ == '__main__':
	# Example usage
	deep_scan_filesystem('C')
