

class Main:

	def __init__(self, name: str):
		self.name = name

	def greet(self):
		print(f"Hello, {self.name}!")

if __name__ == "__main__":
	main = Main(name="World")
	main.greet()
