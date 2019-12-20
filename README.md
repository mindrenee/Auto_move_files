# Auto move files
Reorganize automatically the files in your Downloads folder.

When downloading files to your computer in the Downloads folder, you get a lot of different 
files in there. To keep track of what kind of files you have downloaded this script organizes 
the files directly after downloading. 

| Extension | Folder |
|---|---|
| .mp3 | Music | 
| .wav | Music |  
| .m3u | Music | 
| .gif | Images |
| .ico | Images |
| .jpg | Images |
| .jpeg | Images |
| .png | Images |
| .svg | Images |
| .txt | Text |
| .doc | Text |
| .docx | Text |
| .odt | Text |
| .pdf | Text |
| .tex | Text |
| .flv | Video |
| .m4v | Video |
| .mkv | Video |
| .mov | Video |
| .mp4 | Video |
| .html | Other/Internet |
| .css | Other/Internet |
| .zip | Other/Compressed |
| .rar | Other/Compressed |
| .tar.gz | Other/Compressed |
| .iso | Other/Disc |
| .dmg | Other/Disc |
| .csv | Other/Data |
| .sql | Other/Data |
| .json | Other/Data |
| .exe | Other/Executables |
| .apk | Other/Executables |
| .jar | Other/Executables |
| .sh | Other/Programming |
| .c | Other/Programming |
| .java | Other/Programming |
| .py | Other/Programming |

## Dependencies
Script is tested on Ubuntu 18.04, with Python3 and watchdog.

## Build and run as a service 
In the /lib/systemd/system folder you create your custom .service file as follows:

```
sudo nano auto-move-files.service

[Unit]
Description=Auto move files

[Service]
WorkingDirectory=/home/renee/CodeProjects/Auto_move_files
User=renee
ExecStart=/usr/bin/python3 /home/renee/CodeProjects/Auto_move_files/move_files.py

[Install]
WantedBy=multi-user.target

sudo systemctl daemon-reload
sudo systemctl enable auto-move-files.service
sudo systemctl start auto-move-files.service 
sudo systemctl status auto-move-files.service 
```

Check if the service is running:

```
● auto-move-files.service - Auto move files
   Loaded: loaded (/lib/systemd/system/auto-move-files.service; enabled; vendor preset: enabled)
   Active: active (running) since Thu 2019-12-19 21:07:49 CET; 2s ago
 Main PID: 3453 (python3)
    Tasks: 4 (limit: 4915)
   CGroup: /system.slice/auto-move-files.service
           └─3453 /usr/bin/python3 /home/renee/CodeProjects/Auto_move_files/move_files.py
```

Replace file locations with your own.
