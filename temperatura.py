def celsius_farenheit(temp):
	return (temp * 9/5) + 32

def celsius_kelvin(temp):
	return temp + 273.15


if __name__ == "__main__":
	temperatura = 30
	print(f"{temperatura} grados celsius son {celsius_farenheit(temperatura)} grados farenheit")