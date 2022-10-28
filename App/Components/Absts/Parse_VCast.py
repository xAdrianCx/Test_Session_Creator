
from Components.Drivers.Text_Read_Write import Text_Read_Write


class Parse_VCast:
   Parse_VCast_Inst_lst = []
   Parsing_Component = []


   def __init__(self, CompName, TC_ID, TC_Result, TC_Pars_Status = 'ERROR: Unexpected Value!'):
      self.CompName = str(CompName)
      self.TC_ID = str(TC_ID)
      self.TC_Result = str(TC_Result)
      self.TC_Pars_Status = str(TC_Pars_Status)
      Parse_VCast.Parse_VCast_Inst_lst.append(self)


   # Parses a cantata file at the given Path and reference the found TCs, IDs and results to CompName parameter
   # Returns error status: 0 = No Error. Erorrs tbd
   @classmethod
   # def Pars_File_Return_Status(cls, Path, CompName)
   def Pars_File_Return_Status(cls, Path, CompName=""):
      content, status = Text_Read_Write.Read_File_Ret_Content(Path)
      results_lst = []
      # Step 2: Check for errors
      if CompName == "":
         CompName = str(Path)
      if status != "Successful!":
         return status
      # Process content.
      else:
         for i in content:
            results = {}
            if "passed" in i and "title=" in i:
               test_id = i.partition(("title="))
               try:
                  only_id = test_id[2].split("_")[0].split('"')[1]
                  only_id = int(only_id)
               except ValueError:
                  only_id = test_id[2].split(".")[1].split('"')[0]
               only_id = str(only_id)
               if only_id.isdigit() and len(only_id) > 5:
                  results["Test ID"] = only_id
                  test_result = i.partition("passed")[1]
                  results["Test Result"] = test_result[:4].upper()
                  results_lst.append(results)
               else:
                  results["Test ID"] = test_id[2].split('"')[1]
                  test_result = i.partition("passed")[1]
                  results["Test Result"] = test_result[:4].upper()
                  results_lst.append(results)
            if "failed" in i and "title=" in i:
               test_id = i.partition(("title="))
               try:
                  only_id = test_id[2].split("_")[0].split('"')[1]
                  only_id = int(only_id)
               except ValueError:
                  only_id = test_id[2].split(".")[1].split('"')[0]
               only_id = str(only_id)
               if only_id.isdigit() and len(only_id) > 5:
                  results["Test ID"] = only_id
                  test_result = i.partition("failed")[1]
                  results["Test Result"] = test_result[:4].upper()
                  results_lst.append(results)
               else:
                  results["Test ID"] = test_id[2].split('"')[1]
                  test_result = i.partition("failed")[1]
                  results["Test Result"] = test_result[:4].upper()
                  results_lst.append(results)
      for i in results_lst:
         if i["Test ID"].isdigit() and len(i["Test ID"]) > 5:
            TC_Pars_Status = "OK"
            TC_ID = i["Test ID"]
            TC_Result = i["Test Result"]
            cls(CompName, TC_ID, TC_Result, TC_Pars_Status)
         else:
            TC_Pars_Status = "Error: No ID Found!"
            TC_ID = i["Test ID"]
            TC_Result = i["Test Result"]
            cls(CompName, TC_ID, TC_Result, TC_Pars_Status)
      cls.Parsing_Component = ''


   # Returns error status: 0 = No Error. 1 = Search has found no elements and
   # A list containing the TCs stored in the calss:
   # ['CompName,TC_ID,TC_Result,TC_Pars_Status','...']
   # If CompName is not '', The retuned list will be fliterd by 'CompName'.
   # If Error_Filter is not False, The returnd list will only return cls elements which have TC_Pars_Status = 'OK'
   @classmethod
   # def Get_Tests_lst(cls,CompName='',Error_Filter=False):
   def Get_Tests_lst(cls, Error_Filter=""):
      """
      :param Error_Filter: if this is set to True
      :return: "Displaying only errors!"
      :param Error_Filter: if this is set to False
      :return: "Not displaying the errors!"
      :param Error_Filter: if this is set to ""
      :return: "Displaying everything!"
      """
      error = ""
      if Error_Filter == True:
         error = "Displaying only errors!"
      elif Error_Filter == False:
         error = "Not displaying the errors!"
      elif Error_Filter == "":
         error = "Displaying everything!"
      results_lst = []
      for i in Parse_VCast.Parse_VCast_Inst_lst:
         results = {}
         results["Comp Name"] = i.CompName
         results["Test ID"] = i.TC_ID
         results["Test Result"] = i.TC_Result
         results["Status"] = i.TC_Pars_Status
         if Error_Filter == True:
            if results["Status"] == "Error: No ID Found!":
               results_lst.append(results)
         elif Error_Filter == False:
            if results["Status"] == "OK":
               results_lst.append(results)
         elif Error_Filter == "":
            results_lst.append(results)
      return error, results_lst


   # Callback function (called by Text_Read_Write) containing a line of the VCast file to be parsed.
   # In case sufficant data was callected, TCs information will be added to the Class
   @classmethod
   def Pars_Line_Clbk(cls, Line):
      if "passed" in Line and "title=" in Line:
         test_id = Line.partition(("title="))
         try:
            only_id = test_id[2].split("_")[0].split('"')[1]
            only_id = int(only_id)
         except ValueError:
            only_id = test_id[2].split(".")[1].split('"')[0]
         only_id = str(only_id)
         if only_id.isdigit() and len(only_id) > 5:
            test_result = Line.partition("passed")[1]
            TC_ID = only_id
            TC_Result = test_result[:4].upper()
            TC_Pars_Status = "OK"
            Parse_VCast(cls.Parsing_Component, TC_ID, TC_Result, TC_Pars_Status)
         else:
            test_result = Line.partition("passed")[1]
            TC_ID = test_id[2].split('"')[1]
            TC_Result = test_result[:4].upper()
            TC_Pars_Status = "Error: No ID Found!"
            Parse_VCast(cls.Parsing_Component, TC_ID, TC_Result, TC_Pars_Status)

      if "failed" in Line and "title=" in Line:
         test_id = Line.partition(("title="))
         try:
            only_id = test_id[2].split("_")[0].split('"')[1]
            only_id = int(only_id)
         except ValueError:
            only_id = test_id[2].split(".")[1].split('"')[0]
         only_id = str(only_id)
         if only_id.isdigit() and len(only_id) > 5:
            test_result = Line.partition("failed")[1]
            TC_ID = only_id
            TC_Result = test_result[:4].upper()
            TC_Pars_Status = "OK"
            Parse_VCast(cls.Parsing_Component, TC_ID, TC_Result, TC_Pars_Status)
         else:
            test_result = Line.partition("failed")[1]
            TC_ID = test_id[2].split('"')[1]
            TC_Result = test_result[:4].upper()
            TC_Pars_Status = "Error: No ID Found!"
            Parse_VCast(cls.Parsing_Component, TC_ID, TC_Result, TC_Pars_Status)
