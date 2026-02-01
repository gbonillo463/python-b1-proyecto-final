import pandas as pd

class CSVFileManager:
	def __init__(self, path: str):
		self.path = path

	def read(self):
		return pd.read_csv(self.path)
	
	def write(self, dataFrame: pd.DataFrame):
		dataFrame.to_csv(self.path, index=False)