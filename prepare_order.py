"""
Ejercicio 1: Sistema de comida rápida
 
Implementar un paquete llamado ‘products' que tiene dos módulos: ‘food_package.py' y ‘product.py', con la siguiente estructura:

products/
        __init__.py
        food_package.py
        product.py

El módulo food_package.py contendrá una clase abstracta denominada 'FoodPackage' con dos funciones abstractas: 'def pack(self)  -> str ' y 'def material(self) -> str '. Esta clase nos permite crear un tipo específico de paquete o envoltura dependiendo del tipo de alimento a empacar, por ejemplo:

Un vaso de soda puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Una hamburguesa puede ser empacada en un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las siguientes clases ‘Wrapping’, ‘Bottle’, ‘Glass’ y ‘Box’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Wrapping’ se puede definir como:

class Wrapping(FoodPackage):  
  def pack(self):
    return "Food Wrap Paper"
  def material(self):
    return "Aluminium" 

El módulo 'product.py’ contendrá una clase abstracta denominada 'Product' con dos funciones abstractas: 'def type(self) -> str' y 'def foodPackage(self)-> FoodPackage. Esta clase nos permita crear un producto específico y relacionarlo con su tipo de empaque por ejemplo:

Un producto con código de barras G1, es una soda Sprite cuyo precio es de 5 euros, pertenece al tipo Soda y puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Un producto con código de barras H1, es una hamburguesa Bacon  cuyo precio es de 15 euros, pertenece al tipo Hamburger y puede ser empacado en un paquete un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Hamburger’, ‘Soda’, ‘Drink’ y ‘HappyMeal’, es decir, de forma parecida al módulo anterior, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Hamburger’, se puede definir como:

class Hamburger(Product):
    def __init__(self, id:str, name:str, price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburger"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
Implementar un paquete llamado ‘users' que tiene un módulo ‘user.py', con la siguiente estructura:

users/
        __init__.py
        user.py

El módulo 'user.py' contendrá una clase abstracta denominada ‘User’ que tiene un constructor por defecto para los siguientes datos 'def __init__(self, dni:str, name:str, age:int) ', con una función abstracta: 'def describe(self) '.

Luego en el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Cashier’ y ‘Customer’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Adicionalmente, estas clases se diferencian por los parámetros que reciben sus constructores, por tanto, debemos hacer uso de herencia para inicializar el constructor de la clase padre y agregar características propias a cada clase.  

Implementar un paquete llamado 'util' que tiene dos módulos, denominados 'file_manager.py' y 'converter.py’, con la siguiente estructura:

util/
        __init__.py
        file_manager.py
        converter.py

El módulo ‘file_manager.py' contendrá una clase ‘CSVFileManager’ la cual es una implementaciòn libre y debe incluir las funciones:

La función 'def read(self)' lee un archivo en formato CSV y permite exportar su resultado como un Data Frame.
La función 'def write(self, dataFrame)' convierte un Data Frame en un archivo CSV. Esta es una función opcional, se deja al estudiante la implementación.

Los archivos en formato CSV se encuentran en la ruta “data/”, a continuación, se describe el contenido de cada archivo:

cashiers.csv: Información de los cajeros que harán uso del sistema.
customers.csv: Información de los clientes que harán uso del sistema.
drinks.csv: Información de los diferentes tipos de bebidas.
sodas.csv: Información de los diferentes tipos de gaseosas.
hamburgers.csv: Información de los diferentes tipos de hamburguesas.
happyMeal.csv: Información de los diferentes tipos de happy meals.

El módulo 'converter.py' contendrá una clase denominada ‘Converter’ con una función abstracta para convertir las filas de un Data Frame en instancias de objetos. La función sería ‘def convert(self, dataFrame, *args) -> list’. Adicionalmente esta clase debe incluir un método que permite imprimir la información de los objetos ‘def print(self, list)’. En el mismo módulo se deberán incluir las implementaciones específicas que permitan leer los archivos en formato CSV y convertir sus filas en objetos de cada clase utilizando los paquetes product y users.

Implementar un paquete llamado 'orders' que tiene un módulo 'order.py', con la siguiente estructura:

orders/
        __init__.py
        order.py

El módulo 'order.py' contendrá una clase denominada ‘Order’ con un constructor ‘def __init__(self, cashier:Cashier, customer:Customer):’, el cual permite inicializar la clase con los datos del cajero, del cliente y la lista de productos vacía por defecto. Además, debe incluir tres funciones para agregar productos, calcular el total de la orden solicitada y mostrar la información de la orden que está siendo procesada. Las funciones son ‘def add(self, product: Product)', ' def calculateTotal(self) -> float' y ‘def show(self)’, respectivamente.

Finalmente tendremos una clase principal que se llamará ‘PrepareOrder’ en la cual se deberá realizar una implementación que permita integrar los diferentes módulos empleados para leer los archivos en formato CSV y convertirlos en objetos. La implementación de esta clase es libre, es decir, no indicaremos las funciones que debe contener, pero la funcionalidad de la clase debe permitir crear una opción de menú que permita buscar los clientes, los cajeros y los productos para finalmente crear una orden. 

Se sugiere utilizar los métodos de entrada de teclado para leer los datos del dni cajero, cliente e id de los productos. 


A grandes rasgos, la aplicación seguiría los siguientes pasos:

1)	Leer archivos en formato csv: 
a.	Leer cada archivo en formato csv: Utilizar una instancia de la clase 'CSVFileManager' y llamar al método 'read()'.
2)	Convertir a listas de objetos:
a.	Convertir cajeros: Función creada por el alumno  
b.	Convertir clientes: Función creada por el alumno 
c.	Convertir productos: Función creada por el alumno 
3)	Preparar Orden:
a.	Buscar cajero por dni: Función creada por el alumno y debe devolver una instancia de tipo cajero.
b.	Buscar cliente por dni. Función creada por el alumno y debe devolver una instancia de tipo cliente.
c.	Inicializar Orden: Utilizar una instancia la clase 'Order', e inicializar con su constructor por defecto.
d.	Mostrar productos a vender: Función creada por el alumno.
e.	Escoger productos: Función creada por el alumno.
f.	Agregar productos: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'add()'.
4)	Mostrar Orden: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'show()'


"""
#Write your code here
from users import *
from util import *
from products import *
from orders import *


# Creamos los bucles para encontrar a cajero y cliente
def find_cashier_by_dni(cashiers: list[Cashier], dni: str) -> Cashier | None:
    for cashier in cashiers:
        if str(cashier.dni) == dni:
            return cashier
    return None

def find_customer_by_dni(customers_list: list[Customer], dni: str) -> Customer | None:
    for customer in customers_list:
        if str(customer.dni) == dni:
            return customer
    return None

# Inicializamos la clase CSVFileManager de cada archivo
csv_file_cashiers = CSVFileManager('data/cashiers.csv')
csv_file_customers = CSVFileManager('data/customers.csv')
csv_file_drinks = CSVFileManager('data/drinks.csv')
csv_file_hamburguers = CSVFileManager('data/hamburgers.csv')
csv_file_happyMeal = CSVFileManager('data/happyMeal.csv')
csv_file_sodas = CSVFileManager('data/sodas.csv')

# Inicializamos la calse Converter de cada archivo
# De cada inicialización de la clase CVSFileManager, aplicamos
# el metodo read() para devolver un dataframe para cashier, costumer y 
# una tupla(dataframe, product_type) para los diferentes productos
cashier = CashierConverter()
cashiers_list = cashier.convert(csv_file_cashiers.read()[0])
customer = CustomerConverter()
customers_list = customer.convert(csv_file_customers.read()[0])
product_converter = ProductConverter()
drink_list = product_converter.convert(csv_file_drinks.read()[0], csv_file_drinks.read()[1])
hamburguers_list = product_converter.convert(csv_file_hamburguers.read()[0], csv_file_hamburguers.read()[1])
hapyyMeals_list = product_converter.convert(csv_file_happyMeal.read()[0], csv_file_happyMeal.read()[1])
sodas_list = product_converter.convert(csv_file_sodas.read()[0], csv_file_sodas.read()[1])

products = []

class PrepareOrder:
	def __init__(self, 
			cashiers_list: list[Cashier],
			customers_list: list[Customer], 
			drink_list: list[Product],
			hamburguers_list: list[Product],
			hapyyMeals_list: list[Product],
			sodas_list: list[Product]
		):
		self.cashiers_list = cashiers_list
		self.customers_list = customers_list
		self.drink_list = drink_list
		self.hamburguers_list = hamburguers_list
		self.hapyyMeals_list = hapyyMeals_list
		self.sodas_list = sodas_list
		
	# Usamos un bucle para asegurar que el cajero y cliente existen	
	def select_cashier(self) -> Cashier:
		cashier_find = None
		while cashier_find is None:
			dni_cashier = input('Introduce cashier DNI: ')
			cashier_find = find_cashier_by_dni(self.cashiers_list, dni_cashier)
			if cashier_find is None:
				print("Cajero no válido")
			else:
				print(cashier_find.describe())
		return cashier_find
	
	def select_customer(self) -> Customer:	
		customer_find = None
		while customer_find is None:
			dni_customer = input('Introduce costumer DNI: ')
			customer_find = find_customer_by_dni(self.customers_list, dni_customer)
			if customer_find is None:
				print("Cliente no válido")
			else:
				print(customer_find.describe())
		return customer_find
	
	# Creamos bucles para la selección de los productos
	def selecciona_opcion(self):
		customer_choice = None
		while customer_choice is None:
			customer_enter = input(
				'Selecciona tipo de producto: \n1-Drink\n2-Hamburgers\n3-Happy Meal\n4-Soda'
				)
			match customer_choice:
				case '1':
					
				case '2':
				case '3':
				case '4':

	# Inicializamos la order
	def create_order(self) -> Order:
		# Inicializamos objetos de cashier y customer
		cashier_find = self.select_cashier()
		customer_find = self.select_customer()
		return Order(cashier_find, customer_find)


prepare_order = PrepareOrder(
		cashiers_list, 
		customers_list, 
		drink_list,
		hamburguers_list,
		hapyyMeals_list,
		sodas_list		
		)

order = prepare_order.create_order()
order.show()