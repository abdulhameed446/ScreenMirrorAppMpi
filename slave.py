import logging
from mpi4py import MPI
import cv2
import numpy as np
import pickle

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank != 0:
        try:
            while True:
                # Receive the frame from the master
                data = comm.recv(source=0, tag=0)
                frame = pickle.loads(data)

                # Display the frame
                cv2.imshow(f"Slave {rank}", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except Exception as e:
            logging.error(f"Error in slave process {rank}: {e}")

if __name__ == "__main__":
    main()
