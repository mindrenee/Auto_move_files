#!/usr/bin/python

import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import re
from pathlib import Path

track_dir = "/home/renee/Downloads/"

audio_regex_list = [".mp3", ".wav", ".m3u"]
text_regex_list = [".txt", ".doc", ".docx", ".odt", ".pdf", ".tex"]
image_regex_list = [".gif", ".ico", ".jpg", ".jpeg", ".png", ".svg"]
video_regex_list = [".flv", ".m4v", ".mkv", ".mov", ".mp4"]
internet_regex_list = [".html", ".css"]
compressed_regex_list = [".zip", ".rar", ".tar.gz"]
disc_regex_list = [".iso", ".dmg"]
data_regex_list = [".csv", ".sql", ".json"]
executables_regex_list = [".exe", ".apk", ".jar"]
programming_regex_list = [".sh", ".c", ".java", ".py"]

def main():
    print("Downloads folder organizer")
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = on_created
    my_event_handler.on_moved = on_moved
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, track_dir, recursive=go_recursively)
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
        os.rename(track_dir + basefile, track_dir + rename_file2)
    filename, file_extension = os.path.splitext(file)
    if re.match('(?:% s)' % '|'.join(audio_regex_list), file_extension):
        new_folder = Path(track_dir + "Music/" + rename_file2)
        if not os.path.exists(track_dir + "Music"):
            os.makedirs(track_dir + "Music")
        shutil.move(track_dir + rename_file2, new_folder)
    elif re.match('(?:% s)' % '|'.join(text_regex_list), file_extension):
        new_folder = Path(track_dir + "Text/" + rename_file2)
        if not os.path.exists(track_dir + "Text"):
            os.makedirs(track_dir + "Text")
        shutil.move(track_dir + rename_file2, new_folder)
    elif re.match('(?:% s)' % '|'.join(image_regex_list), file_extension):
        new_folder = Path(track_dir + "Images/" + rename_file2)
        if not os.path.exists(track_dir + "Images"):
            os.makedirs(track_dir + "Images")
        shutil.move(track_dir + rename_file2, new_folder)
    elif re.match('(?:% s)' % '|'.join(video_regex_list), file_extension):
        new_folder = Path(track_dir + "Video/" + rename_file2)
        if not os.path.exists(track_dir + "Video"):
            os.makedirs(track_dir + "Video")
        shutil.move(track_dir + rename_file2, new_folder)
    elif re.match('(?:% s)' % '|'.join(internet_regex_list), file_extension):
        new_folder = Path(track_dir + "Other/Internet/" + rename_file2)
        if not os.path.exists(track_dir + "Other/Internet/"):
            os.makedirs(track_dir + "Other/Internet")
        shutil.move(track_dir + rename_file2, new_folder)
    elif re.match('(?:% s)' % '|'.join(compressed_regex_list), file_extension):
        new_folder = Path(track_dir + "Other/Compressed/" + rename_file2)
        if not os.path.exists(track_dir + "Other/Compressed/"):
            os.makedirs(track_dir + "Other/Compressed")
        shutil.move(track_dir + rename_file2, new_folder)
    elif re.match('(?:% s)' % '|'.join(disc_regex_list), file_extension):
        new_folder = Path(track_dir + "Other/Disc/" + rename_file2)
        if not os.path.exists(track_dir + "Other/Disc/"):
            os.makedirs(track_dir + "Other/Disc")
        shutil.move(track_dir + rename_file2, new_folder)
    elif re.match('(?:% s)' % '|'.join(executables_regex_list), file_extension):
        new_folder = Path(track_dir + "Other/Executables/" + rename_file2)
        if not os.path.exists(track_dir + "Other/Executables/"):
            os.makedirs(track_dir + "Other/Executables")
        shutil.move(track_dir + rename_file2, new_folder)
    elif re.match('(?:% s)' % '|'.join(programming_regex_list), file_extension):
        new_folder = Path(track_dir + "Other/Programming/" + rename_file2)
        if not os.path.exists(track_dir + "Other/Programming/"):
            os.makedirs(track_dir + "Other/Programming")
        shutil.move(track_dir + rename_file2, new_folder)
    else:
        print("File not regonized")

def on_created(event):
    file = event.src_path
    print(f"{event.src_path} has been created")
    move_file(file)

def on_moved(event):
    print(f"{event.src_path} has been moved")

main()
