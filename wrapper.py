import os
import time


def wrapper(watch_path, lock):

    files = os.listdir(watch_path)

    print files

    # Break if folder is locked
    if lock in files or len(files) == 0:
        return

    # Creating lock file
    open(watch_path + lock, 'w')

    # Do stuff...
    time.sleep(2)

    # Delete the file being used
    os.remove(watch_path + '/' + files[0])

    # Remove the lock
    os.remove(watch_path + lock)

    wrapper(watch_path, lock)
