from math import e, pi
from matplotlib import pyplot

class IDFT(object):
	"""docstring for IDFT"""

	def __init__(self):
		super(IDFT, self).__init__()
		self.time_domain = []
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
		exp = complex(0, (2*pi)/self.input_size)
		return e**exp

	def set_time_domain(self, unity_root):
		for i in range (self.input_size):
			coff = 0
			for j in range (self.input_size):
				coff += (unity_root ** (i*j)) * self.input_function[j] 

			self.time_domain.append(coff)

	def print_time_domain(self):
		for i in range(len(self.time_domain)):
			print('X[{}] : '.format(i), self.time_domain[i])

	def calculate(self):
		unity_root = self.get_unity_root()
		self.set_time_domain(unity_root)

	def get_IDFT(self):
		return self.time_domain

	def plot(self):
		x_values = [int(x) for x in range(self.input_size)]
		y_values = [abs(x) for x in self.time_domain]
		pyplot.bar(x_values, y_values, width = 0.05)
		pyplot.axhline(0, color = 'grey')
		pyplot.title('Fourier Cofficients')
		pyplot.xlabel('n')
		pyplot.ylabel('modulus')
		pyplot.show()	

def main():
	idft = IDFT()
	idft.set_input_function()
	idft.calculate()
	idft.print_time_domain()
	idft.plot()
	

if __name__ == '__main__':
	main()