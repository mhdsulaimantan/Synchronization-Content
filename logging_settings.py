import logging
import sys
from validate_data import validate_path

LOG_PATH = validate_path(input("Enter log file path: "))
file_handler = logging.FileHandler(filename=LOG_PATH + '/sync.log')
stdout_handler = logging.StreamHandler(stream=sys.stdout)
handlers = [file_handler, stdout_handler]
logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.DEBUG,
                    handlers=handlers)
