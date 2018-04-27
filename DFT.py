from math import e, pi

class DFT(object):
	"""docstring for DFT"""
	def __init__(self):
		super(DFT, self).__init__()
		self.fourier_cofficients = []
		self.input_function = [] # Get this as parameter
		self.input_size = 0

	def set_input_function(self):
		self.input_size = int(input('Enter the size of input function\n'))
		print("Enter the {} values of input function in the form (X + iY)"
			.format(self.input_size))
		for i in range(self.input_size):
			x, y = (int(x) for x in input().split())
			self.input_function.append(complex(x, y))

	def print_input_function(self):
		for i in self.input_function:
			print(i)

	def get_unity_root(self):
		exp = complex(0, -(2*pi)/self.input_size)
		return e**exp

	def set_fourier_cofficients(self, unity_root):
		for i in range (self.input_size):
			coff = 0
			for j in range (self.input_size):
				coff += (unity_root ** (i*j)) * self.input_function[i] 

			self.fourier_cofficients.append(coff)

	def print_fourier_cofficients(self):
		for i in self.fourier_cofficients:
			print(complex(round(i.real, 4), round(i.imag, 4)))

	def calculate(self):
		unity_root = self.get_unity_root()
		self.set_fourier_cofficients(unity_root)		

def main():
	dft = DFT()
	dft.set_input_function()
	# dft.print_input_function()
	dft.calculate()
	dft.print_fourier_cofficients()

if __name__ == '__main__':
	main()