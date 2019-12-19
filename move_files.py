#!/usr/bin/python

import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import re
from pathlib import Path

global_path = "/home/renee/Downloads/"

def main():
    print("Hello World")
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = on_created
    my_event_handler.on_moved = on_moved
    #path = "/home/renee/Downloads/"
    path = global_path
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)
    my_observer.start()
    try:
         while True:
             time.sleep(1)
    except KeyboardInterrupt:
         my_observer.stop()
         my_observer.join()

def move_file(file):
    basefile = os.path.basename(file)
    rename_file = basefile.replace(" ", "_")
    rename_file2 = rename_file.replace("'","")
    if rename_file2 != basefile:
        os.rename(global_path + basefile, global_path + rename_file2)
    filename, file_extension = os.path.splitext(file)
    audio_regex_list = [".mp3", ".wav", "m3u"]
    text_regex_list = [".txt", ".doc", ".docx", ".odt", ".pdf", ".tex"]
    image_regex_list = [".gif", ".ico", ".jpg", ".jpeg", ".png", ".svg"]
    if re.match('(?:% s)' % '|'.join(audio_regex_list), file_extension):
        new_folder = Path(global_path + "Music/" + rename_file)
        if not os.path.exists(global_path + "Music"):
            os.makedirs(global_path + "Music")
        shutil.move(global_path + rename_file, new_folder)
    elif re.match('(?:% s)' % '|'.join(text_regex_list), file_extension):
        print("Text file")
        print(rename_file)
        new_folder = Path(global_path + "Text/" + rename_file)
        if not os.path.exists(global_path + "Text"):
            os.makedirs(global_path + "Text")
        shutil.move(global_path + rename_file, new_folder)
    elif  re.match('(?:% s)' % '|'.join(image_regex_list), file_extension):
        print("Image file")
        new_folder = Path(global_path + "Images/" + rename_file)
        if not os.path.exists(global_path + "Images"):
            os.makedirs(global_path + "Images")
        shutil.move(global_path + rename_file, new_folder)
    else:
        print("Other file")

def on_created(event):
    file = event.src_path
    print(f"{event.src_path} has been created")
    move_file(file)

def on_moved(event):
    print(f"{event.src_path} has been moved")

main()
