from abc import ABC, abstractmethod
from .file_manager import *
from products.product import Product
from users.user import Customer, Cashier
import pandas as pd



class Converter(ABC):
	@abstractmethod
	def convert(self, dataFrame: pd.DataFrame, *args) -> list:
		pass  
	def print(self, objects):
		for item in objects:
			print(item.describe())

class CashierConverter(Converter):
	def convert(self, dataframe: pd.DataFrame):
		cashier = Cashier()
		cashiers = []
		for index, row in dataframe.iterrows():
			cashier.name = row['name']
			cashier.dni = row['dni']
			cashier.age = row['age']
			cashier.timeTable = row['timetable']
			cashier.salary = row['salary']
			cashiers.append(cashier)
		
		return cashiers

class CustomerConverter(Converter):
	#Write your code here
	pass

class ProductConverter(Converter):
	#Write your code here
	pass