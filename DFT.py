from math import e, pi
from matplotlib import pyplot


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

	def plot(self):
		x_values = [int(x) for x in range(self.input_size)]
		y_values = [abs(x) for x in self.fourier_cofficients]
		pyplot.bar(x_values, y_values, width = 0.05)
		pyplot.axhline(0, color = 'grey')
		pyplot.title('Fourier Cofficients')
		pyplot.xlabel('n')
		pyplot.ylabel('modulus')
		pyplot.show()	

def main():
	dft = DFT()
	dft.set_input_function()
	dft.calculate()
	dft.print_fourier_cofficients()
	dft.plot()
	

if __name__ == '__main__':
	main()