@echo off
REM Check if Python is installed
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python is not installed. Please install Python first.
    exit /b
)

REM Install requirements if not already installed
pip install -r requirements.txt

REM Install PyInstaller if not already installed
pip install pyinstaller

REM Build master executable
echo Building master executable...
pyinstaller --onefile --hidden-import=mpi4py.master master.py
IF ERRORLEVEL 1 (
    echo Failed to build master executable.
    exit /b
)

REM Build slave executable
echo Building slave executable...
pyinstaller --onefile --hidden-import=mpi4py.slave slave.py
IF ERRORLEVEL 1 (
    echo Failed to build slave executable.
    exit /b
)

echo "Build complete! Find executables in the 'dist' folder."
pause
