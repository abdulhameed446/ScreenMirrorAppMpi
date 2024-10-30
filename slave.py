import cv2
import numpy as np
from mpi4py import MPI
import logging
import sys

def setup_logging():
    """Sets up logging configuration."""
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler(f"slave_{MPI.COMM_WORLD.Get_rank()}.log"),
                                  logging.StreamHandler(sys.stdout)])

def initialize_mpi():
    """Initializes the MPI environment and returns communicator and rank."""
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    return comm, rank

def receive_frames(comm, rank):
    """Receives frames from the master and displays them."""
    logging.info(f"Slave {rank} is ready to receive frames.")
    while True:
        frame = np.empty((480, 640, 3), dtype=np.uint8)  # Change according to your setup
        try:
            comm.Recv([frame, MPI.BYTE], source=0, tag=0)
            logging.info(f"Slave {rank} received a frame.")
            cv2.imshow(f'Slave {rank}', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except Exception as e:
            logging.error(f"Error receiving frame: {e}")
            break

def main():
    """Main function to run the slave process."""
    setup_logging()
    comm, rank = initialize_mpi()

    receive_frames(comm, rank)

if __name__ == "__main__":
    main()
