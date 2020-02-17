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
        long_name = str(self.year)+' '+self.make + ' '+self.model 
        return long_name.title()
    def read_odometer(self):
        """Imprime los kilometros recorrido por el auto""" 
        print("This car has " + str(self.odometer_reading) + " miles on it")
    def update_odometer(self, mileage):
        """Modifica el valor del metodo desde la funcion""" 
        self.odometer_reading = mileage
    def change_make(self,new_make):
        self.make=new_make
    def change_model(self,new_model):
        self.model=new_model
    def change_year(self,new_year):
        self.year=new_year	

my_new_car = Car('Koenigsegg','ccx',2012) 
print(my_new_car.get_descriptive_name()) 
my_new_car.change_make('Koenigsegg')
my_new_car.change_model('Agera R')
my_new_car.change_year(2015)
my_new_car.update_odometer(23) 
my_new_car.read_odometer()