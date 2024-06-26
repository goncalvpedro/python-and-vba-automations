from pathlib import Path
import os

root_dir = Path(r'Quick OS Automations\test_files')
files = root_dir.iterdir()

for file in files:
    
    new_name = f'python-{file.stem}{file.suffix}'
    new_filename = file.with_name(new_name)
    file.rename(new_filename)
