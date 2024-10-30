# ScreenMirrorApp

**ScreenMirrorApp** is a distributed screen mirroring application that allows a master device to capture its screen and send the video stream to multiple slave devices using MPI (Message Passing Interface). This project is designed to work in a Windows environment.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Logging](#logging)
- [Error Handling](#error-handling)
- [Contribution](#contribution)
- [License](#license)

## Features

- Captures the screen of the master device.
- Streams the captured video to multiple slave devices in real-time.
- Runs on Windows using MPI.
- Error handling and logging for better maintenance and debugging.
- Configuration file to manage dependencies.

## Requirements

Before running the application, ensure you have the following installed:

- Python 3.x
- MPI for Windows (e.g., Microsoft MPI)
- Required Python packages (listed in `requirements.txt`)

## Installation

1. Clone this repository or download the source code.
2. Open a command prompt and navigate to the `ScreenMirrorApp` directory.
3. Run the following command to install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Build the executables by running the `build_exe.bat` script:

   ```bash
   build_exe.bat
   ```

   This will create a `dist` folder containing the `master.exe` and `slave.exe` executables.

## Usage

1. **Run the Master Application**:
   - Double-click the `start_master.vbs` file to launch the master application. This will start the master process, which captures the screen.

2. **Run the Slave Application**:
   - On each slave device, double-click the `start_slave.vbs` file to launch the slave application. Each slave will display the screen captured by the master device.

3. **Stopping the Applications**:
   - Press `q` in the slave window to stop the video feed. Close the master application by terminating it manually.

## How It Works

- The master application captures the screen using the `pyautogui` library.
- It serializes the captured frames using `pickle` and sends them to all slave devices using MPI.
- The slave applications receive the frames, deserialize them, and display them in separate windows.

## Logging

The application uses Python's built-in logging library to record important events and errors. Logs are printed to the console for easy debugging.

## Error Handling

Error handling is implemented throughout the application to ensure that issues are logged and do not cause the program to crash unexpectedly.

## Contribution

Contributions to the project are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.



