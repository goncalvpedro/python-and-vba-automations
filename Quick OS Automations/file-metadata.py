from pathlib import Path
from datetime import datetime

path = Path(r'Quick OS Automations\test_files')

files = path.iterdir()
for file in files:
    print(file)
    stats = file.stat()
    raw_creation_date = stats.st_ctime

    created_date = datetime.fromtimestamp(raw_creation_date).strftime('%d.%m.%Y_%H_%M_%S').replace('.','-').replace('_','-')
    new_name = f'{created_date}{file.suffix}'
    new_filename = file.with_name(new_name)
    file.rename(new_filename)

# Make unique file names based on their creation date