from mpi4py import MPI
import numpy as np

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

neighbour_processes = [0, 0, 0, 0]

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

grid_rows = int(np.floor(np.sqrt(size)))
grid_columns = size // grid_rows

if grid_rows * grid_columns > size:
    grid_columns -= 1
if grid_rows * grid_columns > size:
    grid_rows -= 1

cartesian_communicator = comm.Create_cart((grid_rows, grid_columns), periods=(False, False), reorder=True)
my_mpi_row, my_mpi_col = cartesian_communicator.Get_coords(cartesian_communicator.rank)

neighbour_processes[UP], neighbour_processes[DOWN] = cartesian_communicator.Shift(0, 1)
neighbour_processes[LEFT], neighbour_processes[RIGHT] = cartesian_communicator.Shift(1, 1)

print("Process = %s\nrow = %s\ncolumn = %s\nUP = %s\nDOWN = %s\nLEFT = %s\nRIGHT = %s" % (
    rank, my_mpi_row, my_mpi_col, neighbour_processes[UP], neighbour_processes[DOWN], neighbour_processes[LEFT], neighbour_processes[RIGHT]
))
