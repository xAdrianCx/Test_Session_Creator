import re
from Components.Drivers.Text_Read_Write import Text_Read_Write

class Parse_VTest:
   Parse_VTest_Inst_lst = []
   Parsing_Component = ''
   SW_NR = ''
   Pars_line_clbk_state = 'Get TC Name'
   Pars_line_clbk_tmp_TC_ID = ''
   Pars_line_clbk_tmp_TC_Result = ''
   all_ids = []

   def __init__(self, SW_NR, CompName, TC_ID, TC_Result, TC_Pars_Status = 'Error: Item Not Parsed!'):
      self.SW_NR = str(SW_NR)
      self.CompName = str(CompName)
      self.TC_ID = str(TC_ID)
      self.TC_Result = str(TC_Result)
      self.TC_Pars_Status = str(TC_Pars_Status)
      Parse_VTest.Parse_VTest_Inst_lst.append(self)


   # Parses a cantata file at the given Path and reference the found TCs, IDs and results to CompName and SW_NR parameters
   # Returns error status: 0 = No Error. Erorrs tbd
   @classmethod
   # def Pars_File_Return_Status(cls, Path, CompName, SW_NR):
   def Pars_File_Return_Status(cls, Path, CompName="", SW_NR=""):
      content, status = Text_Read_Write.Read_File_Ret_Content(Path)
      cls.SW_NR = str(SW_NR)
      if CompName == "":
         CompName = str(Path)
      cls.Parsing_Component = str(CompName)
      if status != "Successful!":
         return status
      else:
         ids = []
         for i in range(len(content)):
            id_pattern = r"[A-Z]{2,}\d[_]\d{5,}"
            id_string = content[i]
            id_result = re.findall(id_pattern, id_string)
            for j in id_result:
               if j != []:
                  ids.append(j)
         ids = set(ids)
         ids = list(ids)
         results_lst = []
         # When id is found, search 3 rows further for a test result.
         flag = 1
         while flag <= 3:
            for i in range(len(content)):
               for j in ids:
                  if j in content[i]:
                     results_dict = {}
                     try:
                        i += flag
                        test_result_pattern = r'(?<=>)[\s\S]+?(?=<)'
                        test_result_string = content[i]
                        test_result = re.search(test_result_pattern, test_result_string).group()
                        results_dict["Test ID"] = j
                        results_dict["Test Result"] = test_result.upper()
                        results_lst.append(results_dict)
                     except AttributeError:
                        pass
            flag += 1
      for i in results_lst:
         for j in i:
            if i["Test Result"] == "PASS" or i["Test Result"] == "FAIL":
               TC_Pars_Status = "OK"
               SW_NR = str(i["Test ID"])[0:3]
               CompName = CompName
               TC_ID = str(i["Test ID"])[4:]
               TC_Result = i["Test Result"]
               cls(SW_NR, CompName, TC_ID, TC_Result, TC_Pars_Status)
            else:
               TC_Pars_Status = "Error: Item Not Parsed!"
               SW_NR = str(i["Test ID"])[0:3]
               CompName = CompName
               TC_ID = str(i["Test ID"])[4:]
               TC_Result = i["Test Result"]
               cls(SW_NR, CompName, TC_ID, TC_Result, TC_Pars_Status )
            break
      cls.Parsing_Component = ''
      cls.SW_NR = ''


   # Returns error status: 0 = No Error. 1 = Search has found no elements and
   # A list containing the TCs stored in the calss:
   # ['SW_NR,CompName,TC_ID,TC_Result,TC_Pars_Status','...']
   # If SW_NR is not '', The retuned list will be fliterd by 'SW_NR'.
   # If CompName is not '', The retuned list will be fliterd by 'CompName'.
   # If Error_Filter is not False, The returnd list will only return cls elements which have TC_Pars_Status = 'OK'
   @classmethod
   # def Get_Tests_lst(cls, SW_NR ="", Comp_Name="", Error_Filter=""):
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
      for i in Parse_VTest.Parse_VTest_Inst_lst:
         results = {}
         results["Comp Name"] = i.CompName
         results["SW_NR"] = i.SW_NR
         results["Test ID"] = i.TC_ID
         results["Test Result"] = i.TC_Result
         results["Status"] = i.TC_Pars_Status
         if Error_Filter == True:
            if results["Status"] == 'Error: Item Not Parsed!':
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
      id_regex = r"[A-Z]{2,}\d[_]\d{5,}"
      test_result_regex = r"(?<=>)[\s\S]+?(?=<)"
      # Try to find an ID.
      if cls.Pars_line_clbk_state == 'Get TC Name':
         id_match = re.search(id_regex, Line)
         if id_match:
            # If ID is found, add it to class attribute cls.Pars_line_clbk_tmp_TC_ID then set the state to "Get ID".
            cls.Pars_line_clbk_tmp_TC_ID = str(id_match.group())
            cls.SW_NR = id_match.group()[2]
            cls.Pars_line_clbk_state = 'Get ID'
      # After state is set to "Get ID" we know we have found an ID. Now we need the test result.
      elif cls.Pars_line_clbk_state == 'Get ID':
         test_result_match = re.search(test_result_regex, Line)
         idmach_flg = 'No'
         if test_result_match:
            # If test result is found and if the ID hasn't been found yet, store both(ID and test result) into the class
            # then set the state to "Get TC Name" so we can start looking for another ID.
            if test_result_match.group() == "pass" or test_result_match.group() == "fail" or test_result_match.group() == "not executed":
               for index in cls.Parse_VTest_Inst_lst:
                  if cls.Pars_line_clbk_tmp_TC_ID == index.TC_ID:
                     idmach_flg = 'Yes'
                     break

               if idmach_flg == 'No':
                  #cls.all_ids.append(cls.Pars_line_clbk_tmp_TC_ID)
                  Parse_VTest(cls.SW_NR, cls.Parsing_Component, cls.Pars_line_clbk_tmp_TC_ID, test_result_match.group().upper(), 'OK')
                  cls.Pars_line_clbk_state = 'Get TC Name'
            else:
               # If ID is found, but no test result, store the ID and the result into the class only if the ID
               # hasn't been found yet.
               for index in cls.Parse_VTest_Inst_lst:
                  if cls.Pars_line_clbk_tmp_TC_ID == index.TC_ID:
                     idmach_flg = 'Yes'
                     break

               if idmach_flg == 'No':
                  Parse_VTest(cls.SW_NR, cls.Parsing_Component, cls.Pars_line_clbk_tmp_TC_ID, 'No test result found!',' Error: Item Not Parsed!')
                  cls.Pars_line_clbk_state = 'Get TC Name'
