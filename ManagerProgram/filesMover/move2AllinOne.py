from pathlib import Path 
from utils.FileProcessor import FileProcessor

if __name__ == '__main__':
    watch_path = [Path.home() / 'Downloads' , Path.home() / 'Desktop']
    destination_root = Path.home() / 'Desktop/AllinOne'
    
    for path in watch_path:
        file_processor = FileProcessor(watch_path=path, destination_root=destination_root)
        file_processor.moveFiles()