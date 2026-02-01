from abc import ABC, abstractmethod

class FoodPackage (ABC): 
    @abstractmethod
    def pack(self)  -> str:
        pass
    @abstractmethod
    def material(self) -> str:
        pass
    def describe(self):
        return f"Empaque: {self.pack()} , Material: {self.material()}"    
    
class Wrapping(FoodPackage):  
	def pack(self):
		return 'Food Wrap Paper'
	def material(self):
		return 'Aluminium'

class Bottle(FoodPackage):  
#Write your code here
	def pack(self):
		return 'Liquid Bottle'
	def material(self):
		return 'Plastic'

class Glass(FoodPackage):  
#Write your code here
	def pack(self):
		return 'Food Glass Plate'
	def material(self):
		return 'Glass'

class Box(FoodPackage):  
#Write your code here
	def pack(self):
		return 'Hamburguer Carton Box'
	def material(self):
		return 'Carton'