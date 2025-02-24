@echo off
echo Building executable...
pyinstaller --onefile --windowed deviceappscanner.py
echo Build complete!
pause
