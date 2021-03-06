import sys
from math import e, pi
try:
	from matplotlib import pyplot
except Exception as e:
	print('Module matplotlib not present! Graph will not be plotted')

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
				coff += (unity_root ** (i*j)) * self.input_function[j] 

			self.fourier_cofficients.append(coff)

	def print_fourier_cofficients(self):
		for i in range(len(self.fourier_cofficients)):
			print('X[{}] : '.format(i), self.fourier_cofficients[i])

	def calculate(self):
		unity_root = self.get_unity_root()
		self.set_fourier_cofficients(unity_root)

	def get_DFT(self):
		return self.fourier_cofficients()

	def plot(self):
		x_values = [int(x) for x in range(self.input_size + 1)]
		y_values = [abs(x) for x in self.fourier_cofficients]
		y_values.append(0)

		pyplot.bar(x_values, y_values, width = 0.05)
		pyplot.axhline(0, color = 'red')
		pyplot.title('Fourier Cofficients')
		pyplot.xlabel('n')
		pyplot.ylabel('| X[n] |')
		pyplot.show()	

def main():
	dft = DFT()
	dft.set_input_function()
	dft.calculate()
	dft.print_fourier_cofficients()
	if 'matplotlib' in sys.modules:
		dft.plot()
	

if __name__ == '__main__':
	main()