class Car():
	"""Clase tipo coche""" 
	def __init__(self, make, model, year): 
		"""Inicializacion de los atributos""" 
		self.make = make
		self.model = model 
		self.year = year 
		self.odometer_reading = 0
	def get_descriptive_name(self):
		""" Imprime las caracteristicas en la pantalla"""
		long_name = str(self.year)+ ' '+self.make +' '+self.model 
		return long_name.title()
	def read_odometer(self): #Error conregido sefl
		"""Imprime los kilometros recorrido por el auto""" 
		print("This car has " + str(self.odometer_reading) + " miles on it")#eror sefl
my_new_car = Car('audi','a4',2020) 
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
#my_new_car.odometer_reading = 25 'borre self.odometer_reading del constructor y trate de denirlo dentro de read_odometer(self)'

#Nota: observe que aunque estava Sefl se ejecutaba pero mandaba el siguiente error 
#	"Method 'read_odometer' should have 'self' as first argument."
# Tambien al quitar	self.odometer_reading = 0 dice que el atributo no se encuentra en el objeto