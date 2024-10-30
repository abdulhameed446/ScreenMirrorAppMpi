import cv2
import numpy as np
from mpi4py import MPI
import logging
import sys

def setup_logging():
    """Sets up logging configuration."""
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler("master.log"),
                                  logging.StreamHandler(sys.stdout)])

def initialize_mpi():
    """Initializes the MPI environment and returns communicator and rank."""
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    return comm, rank, size

def capture_screen(comm, size):
    """Captures the screen and sends frames to all slave devices."""
    # Use your desired method for capturing the screen
    cap = cv2.VideoCapture(0)  # Change this to the appropriate screen capture method
    
    if not cap.isOpened():
        logging.error("Failed to open video capture.")
        return

    logging.info("Starting screen capture.")
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                logging.error("Failed to capture frame.")
                break
            
            # Resize the frame to fit slave devices
            frame = cv2.resize(frame, (640, 480))  # Adjust resolution as needed
            
            # Send the frame to each slave device
            for i in range(1, size):
                try:
                    comm.Send([frame, MPI.BYTE], dest=i, tag=0)
                    logging.info(f"Sent frame to slave {i}.")
                except Exception as e:
                    logging.error(f"Failed to send frame to slave {i}: {e}")

    finally:
        cap.release()
        logging.info("Screen capture stopped.")

def main():
    """Main function to run the master process."""
    setup_logging()
    comm, rank, size = initialize_mpi()

    if rank == 0:  # Only master executes this
        capture_screen(comm, size)

if __name__ == "__main__":
    main()
