import logging
from mpi4py import MPI
import cv2
import numpy as np
import pyautogui
import pickle

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        logging.info("Master running, capturing screen...")
        try:
            while True:
                # Capture the screen
                screen = pyautogui.screenshot()
                frame = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
                data = pickle.dumps(frame)

                # Send the frame to all slaves
                for i in range(1, size):
                    comm.send(data, dest=i, tag=0)
        except Exception as e:
            logging.error(f"Error in master process: {e}")
    else:
        while True:
            try:
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
