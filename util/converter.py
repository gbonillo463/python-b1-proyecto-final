from abc import ABC, abstractmethod
from .file_manager import *
from products.product import Product, Hamburger, Soda, Drink, HappyMeal
from users.user import Customer, Cashier
import pandas as pd



class Converter(ABC):
	@abstractmethod
	def convert(self, dataFrame: pd.DataFrame, *args) -> list:
		pass  
	def print(self, objects):
		for item in objects:
			print(item.describe())

# Converter de cajeros, donde usamos el inicializador de la clase Cashier
# y devolvemos una lista de todos los cajeros del archivo
class CashierConverter(Converter):
	def convert(self, dataframe: pd.DataFrame):
		cashiers = []
		for index, row in dataframe.iterrows():
			cashier = Cashier(
					row['dni'],
					row['name'],
					row['age'],
					row['timetable'],
					row['salary']
					)
			cashiers.append(cashier)
		
		return cashiers

# Converter de clientes, donde usamos el inicializador de la clase Costumer
# y devolvemos una lista de todos los clientes del archivo
class CustomerConverter(Converter):
	def convert(self, dataframe: pd.DataFrame):
		customers = []
		for index, row in dataframe.iterrows():
			customer = Customer(
					row['dni'], 
					row['name'], 
					row['age'], 
					row['email'],
					row['postalcode'])
			customers.append(customer)
		
		return customers

# Product map para definir el tipo de producto
PRODUCT_MAP = {
	'hamburgers': Hamburger,
	'sodas': Soda,
	'drinks': Drink,
	'happyMeal': HappyMeal
}

# Conerter de productos, usando el dataframe y product_type para definir
# que clase de procuto iniciamos y devolvemos una lista de todos los 
# productos del archivo
class ProductConverter(Converter):
	def convert(self, dataFrame: pd.DataFrame, product_type: str):
		product_class = PRODUCT_MAP[product_type]
		products = []
		for index, row in dataFrame.iterrows():
			product = product_class(
					row['id'], 
					row['name'], 
					row['price']
					)
			products.append(product)
		return products