import fire


class Main:

	def hello(self, name: str):
		print(f"Hello, {name}!")

if __name__ == "__main__":
	fire.Fire(Main)
