# Python program to for Knight's tour problem using
# Warnsdorff's algorithm
import random

class Cell:
	def __init__(self, x, y):
		self.x = x
		self.y = y

N = 8

# Move pattern on basis of the change of
# x coordinates and y coordinates respectively
cx = [1, 1, 2, 2, -1, -1, -2, -2]
cy = [2, -2, 1, -1, 2, -2, 1, -1]

# function restricts the knight to remain within
# the 8x8 chessboard
def limits(x, y):
	return ((x >= 0 and y >= 0) and (x < N and y < N))

# Checks whether a square is valid and empty or not
def isempty(a, x, y):
	return (limits(x, y)) and (a[y * N + x] < 0)

# Returns the number of empty squares adjacent to (x, y)
def getDegree(a, x, y):
	count = 0
	for i in range(N):
		if isempty(a, (x + cx[i]), (y + cy[i])):
			count += 1
	return count

# Picks next point using Warnsdorff's heuristic.
# Returns false if it is not possible to pick
# next point.
def nextMove(a, cell):
	min_deg_idx = -1
	c = 0
	min_deg = (N + 1)
	nx = 0
	ny = 0

	# Try all N adjacent of (*x, *y) starting
	# from a random adjacent. Find the adjacent
	# with minimum degree.
	start = random.randint(0, 1000) % N
	for count in range(0, N):
		i = (start + count) % N
		nx = cell.x + cx[i]
		ny = cell.y + cy[i]
		c = getDegree(a, nx, ny)
		if ((isempty(a, nx, ny)) and c < min_deg):
			min_deg_idx = i
			min_deg = c

	# IF we could not find a next cell
	if (min_deg_idx == -1):
		return None

	# Store coordinates of next point
	nx = cell.x + cx[min_deg_idx]
	ny = cell.y + cy[min_deg_idx]

	# Mark next move
	a[ny * N + nx] = a[(cell.y) * N + (cell.x)] + 1

	# Update next point
	cell.x = nx
	cell.y = ny

	return cell

# displays the chessboard with all the legal knight's moves
def printA(a):
	for i in range(N):
		for j in range(N):
			print("%d\t" % a[j * N + i], end="")
		print()

# checks its neighbouring squares
# If the knight ends on a square that is one knight's move from the beginning square,then tour is closed
def neighbour(x, y, xx, yy):
	for i in range(N):
		if ((x + cx[i]) == xx) and ((y + cy[i]) == yy):
			return True
	return False

# Generates the legal moves using warnsdorff's heuristics. Returns false if not possible
def findClosedTour():
	# Filling up the chessboard matrix with -1's
	chessboard_matrix = [-1] * N * N

	# initial position
	sx = 0
	sy = 0

	# Current points are same as initial points
	cell = Cell(sx, sy)

	chessboard_matrix[cell.y * N + cell.x] = 1 # Mark first move.

	# Keep picking next points using Warnsdorff's heuristic
	ret = None
	for i in range(N * N - 1):
		ret = nextMove(chessboard_matrix, cell)
		if ret == None:
			return False

	# Check if tour is closed (Can end at starting point)
	if not neighbour(ret.x, ret.y, sx, sy):
		return False
	printA(chessboard_matrix)
	return True


# Driver Code
if __name__ == '__main__':
	# While we don't get a solution
	while not findClosedTour():
		pass

# This code is contributed by Tapesh(tapeshdua420)
