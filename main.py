import logging
import logging_settings
from sync import Synchronization
from validate_data import validate_path, validate_period


def retrieve_path(folder, source_path=''):
    path = input("Enter the " + folder + " directory path: ")
    valid_path = validate_path(path)

    # make sure replica path is not source path
    if folder == "replica":
        while valid_path == source_path:
            logging.warning(
                "The source and replica paths should not be equal")
            path = input("Enter a new replica directory path: ")
            valid_path = validate_path(path)

    return valid_path


def retrieve_period():
    period = input("Enter synchronization period in seconds: ")
    valid_period = validate_period(period)
    return valid_period


if __name__ == "__main__":
    try:
        # execute log settings
        logging_settings

        # retrieve data
        SOURCE_PATH = retrieve_path('source')
        REPLICA_PATH = retrieve_path('replica', SOURCE_PATH)
        PERIOD = retrieve_period()

        # start sync process
        sync = Synchronization(SOURCE_PATH, REPLICA_PATH, PERIOD)
        sync.run()

    except Exception as e:
        logging.error(e)
    
    except KeyboardInterrupt:
        logging.error("KeyboardInterrupt")
