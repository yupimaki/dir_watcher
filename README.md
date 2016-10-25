# dir_watcher
Use the python inotify library to run a process over a folder.

 - The process starts when a file is dropped into a watched folder
 - As the process is running, the folder is locked from firing another process
 - The file is handled and removed, the lock is removed
 - The process calls itself to finish
  - If there exists another file, we process that too
  - If not, we wait for another file to be dropped into the folder

## Usage
 - cd to repo
 - Run `python runner.py` in the command line
 - Drop a file into `dir` to start processing files
 
Wrapper can probably just be used as a decorator
