import pandas as pd
from pathlib import Path

class CSVFileManager:
	def __init__(self, path: str):
		self.path = path

	def read(self):
		dataframe = pd.read_csv(self.path)
		change_path = Path(self.path)
		product_type = change_path.stem

	# 	La función read() devuelve el dataframe y además 
	#	product_type sacado del nombre del archivo.
		return dataframe, product_type

	def write(self, dataFrame: pd.DataFrame):
		dataFrame.to_csv(self.path, index=False)