import pandas as pd
import numpy as np

class Excel:
   Excel_Inst_lst = []
   # Needed for future development - nothing to do
   def __init__(self):
      Excel.Excel_Inst_lst.append(self)
   # Needed for future development - nothing to do
   def __del__(self):
      Excel.Excel_Inst_lst.remove(self)


   # Reads the excel file at the given path and returns the content of the sheet in list format
   # Returns also an error status
   @staticmethod
   def Read_Excel_Sheet_Ret_List(path, sheet):
      # 'sheet' parameter can be eighter index or sheet's name.
      # replaces NaN with empy string.
      content = []
      try:
         xl = pd.ExcelFile(path)
         df = xl.parse(sheet)
         df1 = df.replace(np.nan, "", regex=True)
         content = pd.DataFrame(df1).values.tolist()
      except FileNotFoundError:
         return content, "Unsuccessful! File Not Found!"
      except ValueError:
         xl = pd.ExcelFile(path)
         return content, f"Unssuccessful! File has only {len(xl.sheet_names)} sheets."
      else:
         return content, "Successful!"


   # Overwrites the content of an excel file at the given path and sheet
   # Returns also an error status
   @staticmethod
   def Write_Excel_Sheet_Ret_Sts(path, sheet_name, sheet_content):
      """ In order to properly write to excel file,
		  'sheet_content' parameter has to be a dict of form:
			  sheet_content = {
				  'Name': ['Tom', 'nick', 'krish', 'jack'],
				  'Age': [20, 21, 19, 18]
				  }
		  'sheet' parameter can be eighter index or actual sheet's name.
	  """
      with pd.ExcelWriter(path, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
         try:
            xl = pd.ExcelFile(path)
            sheets = xl.sheet_names
            if isinstance(sheet_name, str):
               df = pd.DataFrame(sheet_content)
               df.to_excel(writer, sheet_name, index=False)
            elif isinstance(sheet_name, int):
               sheet_name = sheets[sheet_name]
               df = pd.DataFrame(sheet_content)
               df.to_excel(writer, sheet_name, index=False)
         except ValueError:
            return "Unsuccessful! 'sheet_content' parameter is not properly called!"
         else:
            return "Successful!"


   # Adds provided content to an excel file at the given sheet. The content is added at the end of the existing content.
   # Returns also an error status
   @staticmethod
   def Update_Excel_Sheet_Ret_Sts(path, sheet_name, sheet_content):
      """ In order to properly append to excel file,
      		  'sheet_content' parameter has to be a dict of form:
      			  sheet_content = {
      				  'Name': ['Tom', 'nick', 'krish', 'jack'],
      				  'Age': [20, 21, 19, 18]
      				  }
      		  'sheet' parameter can be eighter index or actual sheet's name.
      	  """
      with pd.ExcelWriter(path, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
         try:
            xl = pd.ExcelFile(path)
            sheets = xl.sheet_names
            if isinstance(sheet_name, str):
               df = pd.DataFrame(sheet_content)
               df.to_excel(writer, sheet_name=sheet_name, startrow=writer.sheets[sheet_name].max_row, index=False,
                           header=True)
            elif isinstance(sheet_name, int):
               sheet_name = sheets[sheet_name]
               df = pd.DataFrame(sheet_content)
               df.to_excel(writer, sheet_name=sheet_name, startrow=writer.sheets[sheet_name].max_row, index=False,
                           header=True)
         except ValueError:
            return "Unsuccessful! 'sheet_content' parameter is not properly called!"
         else:
            return "Successful!"
