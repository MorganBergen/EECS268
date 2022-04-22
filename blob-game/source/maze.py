

class Maze:
	
	def __init__(self):
		self.file = ""
		self.total_rows = 0
		self.total_cols = 0
		self.start_row = 0
		self.start_col = 0
		self.total_eaten = 0
		self.total_ppl = 0
		self.grid = []
		self.track = 0
		
	def print_grid(self):
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				print(f"{self.grid[i][j]}", end="")
			print()

	def build_grid(self):
		x = False
		while x == False:
			# self.file = input("enter file: ")
			self.file = "1-input.txt"
			# self.file = "2-input.txt"
			x = self.fileio()
		self.total_ppl = self.count_ppl()

	def fileio(self):
		try:
			f = open(self.file, 'r')
		except FileNotFoundError as e:
			print(e)
			return False
		else:
			total = f.readline().split()
			start = f.readline().split()
			self.grid = list(f.read().splitlines())
			self.total_rows = int(total[0])
			self.total_cols = int(total[1])
			self.start_row = int(start[0])
			self.start_col = int(start[1])
			
			if self.valid_dimensions() == False:
				return False
			else:
				for i in range(len(self.grid)):
					self.grid[i] = list(self.grid[i])
		f.close()
		return True

	def valid_dimensions(self):
		if self.total_rows < 1:
			print(f"error: invalid dimensions provided, total rows cannot be less than 1")
			return False
		elif self.total_cols < 1:
			print(f"error: invalid dimensions provided, total cols cannot be less than 1")
			return False
		elif self.start_row > self.total_rows:
			print(f"error: invalid dimensions provided, starting position is not within range.")
			return False
		elif self.start_col > self.total_cols:
			print(f"error: invalid dimensions provided, starting position is not within range.")
			return False
		elif self.start_col < 0:
			print(f"error: invalid dimensions provided, starting position is not within range.")
			return False
		elif self.start_row < 0:
			print(f"error: invalid dimensions provided, starting position is not within range.")
			return False
		else:
			return True
	
	def reset_grid(self):
		self.fileio()

	def count_ppl(self):
		ppl = 0
		for i in range(len(self.grid)):
			ppl = self.grid[i].count('P') + ppl
		return (ppl)

	def start(self):
		self.walk(self.start_row, self.start_col)

	'''
	def find_path(self, row, col):
		
		self.mark(row, col)
		self.track = self.track + 1

		if self.valid_move(row - 1, col): #up
			self.print_grid()
			# print(f"____{self.grid[row][col]}__at__{row}{col}__up__")
			print(f"________") 
			return (self.find_path(row - 1, col))

		elif self.valid_move(row, col + 1): #right
			self.print_grid()
			# print(f"____{self.grid[row][col]}__at__{row}{col}__right__")
			print(f"________") 
			return (self.find_path(row, col + 1))

		elif self.valid_move(row + 1, col): #down
			self.print_grid()
			# print(f"____{self.grid[row][col]}__at__{row}{col}__down__")
			print(f"________") 
			return (self.find_path(row + 1, col))

		elif self.valid_move(row, col - 1): #left
			self.print_grid()
			# print(f"____{self.grid[row][col]}__at__{row}{col}__left__")
			print(f"________") 
			return (self.find_path(row, col - 1))

		elif self.grid[row][col] == 'X':
			self.unmark(row, col)
			self.print_grid()
			# {self.grid[row][col]}__at__{row}{col}
			print(f"________") 
			return (self.find_path(row, col))
		else:
			return False
	'''

	def walk(self, row, col):
		
		self.mark(row, col)
		self.print_grid()

		self.track = self.track + 1
		
		if self.valid_spot(row - 1, col): #check up
			self.walk(row - 1, col)
		
		if self.valid_spot(row, col + 1): #check right
			self.walk(row, col + 1)

		if self.valid_spot(row + 1, col): #check down
			self.walk(row + 1, col)
		
		if self.valid_spot(row, col - 1): #check left last check
			self.walk(row, col - 1)
			
		self.grid[row][col] = 'B'

	def mark(self, row, col):
		if self.grid[row][col] == 'P':
			self.total_eaten = self.total_eaten + 1
			self.grid[row][col] = self.track
		elif self.grid[row][col] == 'S':
			self.grid[row][col] = self.track
		else:
			return False

	def valid_spot(self, row, col):
		if row >= 0 and row < self.total_rows and col >= 0 and col < self.total_cols:
			if self.grid[row][col] == 'P':
				return True
			elif self.grid[row][col] == 'S':
				return True
			else:
				return False
		else:
			return False
