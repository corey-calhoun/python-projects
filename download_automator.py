# This app will automatically organise & move files from a download folder to a specified folder based on file type.

from os import scandir, rename
from os.path import exists, join, splitext
from shutil import move
import logging
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set up logging
logging.basicConfig(filename='download_automator.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# Define the file types to be moved
file_types = {
    'audio': ['.mp3', '.wav', '.flac', '.m4a', '.aac', '.ogg', '.wma', '.aiff', '.alac'],
    'video': ['.mp4', '.mov', '.avi', '.wmv', '.flv', '.mkv', '.webm', '.vob', '.ogv', '.m4v', '.3gp', '.3g2', '.mpeg', '.mpg', '.m2v', '.m4p', '.m4b', '.m4r', '.mxf', '.mts', '.m2ts', '.ts', '.qt', '.rm', '.rmvb', '.swf', '.vob', '.drc', '.gifv', '.mng', '.asf', '.amv', '.m4v', '.mp2', '.mpe', '.mpv', '.m2v', '.m4v', '.svi', '.3gp', '.3g2', '.mxf', '.roq', '.nsv', '.f4v', '.f4p', '.f4a', '.f4b'],
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.psd', '.ai', '.eps', '.indd', '.raw', '.cr2', '.nef', '.orf', '.sr2'],
    'documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.csv']
}

# Define the folders to move the files to
folders = {
    'src_dir': 'C:/Users/corey/Downloads',
    'audio': 'C:/Users/corey/Music',
    'video': 'C:/Users/corey/Videos',
    'images': 'C:/Users/corey/Pictures',
    'documents': 'C:/Users/corey/Documents'
}

# Set up file system event handler
class MyHandler(FileSystemEventHandler):

    def on_created(self, event):
        for file in scandir(folders['src_dir']):
            src = folders['src_dir'] + '/' + file
            new_destination = folders['src_dir'] + '/' + file
            if os.path.exists(src):
                ext = os.path.splitext(src)[1]
                if ext in file_types['audio']:
                    new_destination = folders['audio'] + '/' + file
                elif ext in file_types['video']:
                    new_destination = folders['video'] + '/' + file
                elif ext in file_types['images']:
                    new_destination = folders['images'] + '/' + file
                elif ext in file_types['documents']:
                    new_destination = folders['documents'] + '/' + file
                if src != new_destination:
                    try:
                        shutil.move(src, new_destination)
                        logging.info('Moved file: ' + file)
                    except shutil.Error:
                        logging.info('File already exists: ' + file)
                        os.remove(src)
                        logging.info('Removed file: ' + file)
                else:
                    logging.info('File not moved: ' + file)

# Set up watchdog observer
if __name__ == '__main__':
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=folders['src_dir'], recursive=False)
    observer.start()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
