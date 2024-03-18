from pathlib import Path
from datetime import datetime

omit_folders = {'ActiveProjects','Archive','AllinOne'}

def get_file_creation_time(file: Path):
    c_timestamp = file.stat().st_ctime
    ctime = datetime.fromtimestamp(c_timestamp)
    return ctime

def get_file_modification_time(file: Path):
    m_timestamp = file.stat().st_mtime
    mtime = datetime.fromtimestamp(m_timestamp)
    return mtime

def add_date_folder(path: Path, ctime):
    year = ctime.year
    month = ctime.strftime("%B")
    day = ctime.day
    date_folder = path / f'{year}' / f'{month}' / f'{year}{month}{day}'
    date_folder.mkdir(parents=True, exist_ok=True)
    return date_folder

def rename_file(source: Path, destination: Path):
    if Path(destination / source.name).exists():
        version = 1

        while True:
            version += 1
            version_updated_path = destination / f'{source.stem}_{version}{source.suffix}'
            if not version_updated_path.exists():
                return version_updated_path

    return destination / source.name


class FileProcessor:
    def __init__(self, watch_path: Path, destination_root: Path):
        self.watch_path = watch_path.resolve()
        self.destination_root = destination_root.resolve()

    def moveFiles(self):
        for item in self.watch_path.iterdir():
            if item.is_file() and not item.name.startswith('~') and not item in omit_folders:
                ctime = get_file_creation_time(item)
                destination_path = add_date_folder(self.destination_root, ctime)
                destination_path = rename_file(item, destination_path)
                item.rename(destination_path)


    