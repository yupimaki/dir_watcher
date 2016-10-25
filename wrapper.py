import os
import time


def hexparser(filename, watch_path, lock):

    # Debug
    print "Handling", filename

    # Do stuff...
    time.sleep(2)

    # Delete the file being used
    os.remove(watch_path + '/' + filename)

    # Get files without lock
    files = os.listdir(watch_path)
    files = [f for f in files if not f == lock]

    # Exist if dir is empty and return to wrapper
    if len(files) == 0:
        return

    # Recursive call to hexparser with lock in place
    hexparser(files[0], watch_path, lock)


def wrapper(filename, watch_path, lock):

    files = os.listdir(watch_path)

    print files

    # Break if folder is locked
    if lock in files or len(files) == 0:
        return

    # Creating lock file
    open(watch_path + lock, 'w')

    # Trigger hexparser
    hexparser(filename, watch_path, lock)

    # Remove the lock
    os.remove(watch_path + lock)
