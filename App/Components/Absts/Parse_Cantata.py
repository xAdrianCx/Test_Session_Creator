import re
from Components.Drivers import Text_Read_Write


class Parse_Cantata:
   Parse_Cantata_Inst_lst = []
   Parsing_Component = ''

   def __init__(self, CompName, TC_ID, TC_Result, TC_Pars_Status = 'ERROR: Unexpected Value!'):
      self.CompName = str(CompName)
      self.TC_ID = str(TC_ID)
      self.TC_Result = str(TC_Result)
      self.TC_Pars_Status = str(TC_Pars_Status)
      Parse_Cantata.Parse_Cantata_Inst_lst.append(self)


   # Parses a cantata file at the given Path and reference the found TCs, IDs and results to CompName parameter
   # Returns error status: 0 = No Error. Erorrs tbd
   @classmethod
   # def Pars_File_Return_Status(cls, Path, CompName):
   def Pars_File_Return_Status(cls, Path, CompName=""):
      # Step 1: Call  content, status = Text_Read_Write.Read_File_Ret_Content(Path)
      content, status = Text_Read_Write.Read_File_Ret_Content(Path)
      # Step 2: Check for errors
      if CompName == "":
         CompName = str(Path.split("_")[1])
      cls.Parsing_Component = str(CompName)
      if status != "Successful!":
         return status
      else:
         # Process content.
         temp_ids = []
         lines = []
         test_results = []
         for i in content:
            id_pattern = re.findall(r"[_]\d{5,}[_]", i, re.MULTILINE)
            test_result_pattern = re.findall(r"\s\s{5,}[=]$", i, re.MULTILINE)
            test_result_pattern_pass_fail = re.findall(r"\s[A-Z]{4}\s[=]$", i, re.MULTILINE)
            for j in id_pattern:
               if j != []:
                  temp_ids.append(j)
                  break
            for k in test_result_pattern:
               if k != []:
                  test_results.append(k)
                  break
            for l in test_result_pattern_pass_fail:
               if l != []:
                  test_results.append(l)
                  break
         for i in content:
            for j in temp_ids:
               for k in test_results:
                  if j in i and k in i:
                     lines.append(i)
                     break
         ids = []
         # Format the ids list.
         for i in temp_ids:
            ids.append(i.split("_"))
         ids = [j for i in ids for j in i]
         ids = [i for i in ids if i != ""]
         ids = set(ids)
         ids = list(ids)
         ids.sort()
         # Get rid of duplicates in lines.
         lines = set(lines)
         lines = list(lines)
         lines.sort()
         parsed = {}
         not_parsed = {}
         # Find all IDs with a PASS or FAIL status.
         for i in lines:
            one_id = re.findall(r"\d{5,}", i)
            test_res = re.findall(r"[A-Z]{4}", i)
            for j in one_id:
               for k in test_res:
                  if k == "PASS" or k == "FAIL":
                     parsed[j] = k
                  else:
                     not_parsed[j] = k
         # Find all IDs with no status.
         for i in lines:
            one_id = re.findall(r"\d{5,}", i)
            test_res = re.findall(r"\s{3,}[=]$", i)
            for j in one_id:
               for k in test_res:
                  not_parsed[j] = k
         if not_parsed != {}:
            TC_Pars_Status = 'ERROR: Unexpected Value!'
            for i in not_parsed.keys():
               TC_ID = i
               TC_Result = not_parsed[i]
               cls(CompName, TC_ID, TC_Result, TC_Pars_Status)
         if parsed != {}:
            TC_Pars_Status = 'OK'
            for i in parsed.keys():
               TC_ID = i
               TC_Result = parsed[i]
               cls(CompName, TC_ID, TC_Result, TC_Pars_Status)
         cls.Parsing_Component = ''


   # Returns error status: 0 = No Error. 1 = Search has found no elements and
   # A list containing the TCs stored in the class:
   # ['CompName,TC_ID,TC_Result,TC_Pars_Status','...']
   # If CompName is not '', The retuned list will be fliterd by 'CompName'.
   # If Error_Filter is not False, The returnd list will only return cls elements which have TC_Pars_Status = 'OK'
   @classmethod
   # def Get_Tests_lst(cls, CompName='', Error_Filter=False):
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
      for i in Parse_Cantata.Parse_Cantata_Inst_lst:
         results = {}
         results["Comp Name"] = i.CompName
         results["Test ID"] = i.TC_ID
         results["Test Result"] = i.TC_Result
         results["Status"] = i.TC_Pars_Status
         if Error_Filter == True:
            if results["Status"] == 'ERROR: Unexpected Value!':
               results_lst.append(results)
         elif Error_Filter == False:
            if results["Status"] == "OK":
               results_lst.append(results)
         elif Error_Filter == "":
               results_lst.append(results)
      return error, results_lst


   # Callback function (called by Text_Read_Write) containing a line of the Cantata file to be parsed.
   # In case sufficient data was callected, TCs information will be added to the Class.
   @classmethod
   def Pars_Line_Clbk(cls, Line):
      id_regex = r"[_]\d{5,}[_]"
      id_match = re.search(id_regex, Line)
      test_result_regex = r"\s\s{5,}[=]$"
      test_result_match = re.search(test_result_regex, Line)
      test_result_pass_or_fail_regex = r"\s[A-Z]{4}\s[=]$"
      test_result_pass_or_fail_match = re.search(test_result_pass_or_fail_regex, Line)
      if id_match != None:
         if test_result_pass_or_fail_match != None:
            if "PASS" in test_result_pass_or_fail_match.group().split()[0]:
               TC_ID = str(id_match.group().split('_')[1])
               TC_Result = str(test_result_pass_or_fail_match.group().split()[0])
               TC_Pars_Status = "OK"
               Parse_Cantata(cls.Parsing_Component, TC_ID, TC_Result, TC_Pars_Status)
            elif "FAIL" in test_result_pass_or_fail_match.group().split()[0]:
               TC_ID = str(id_match.group().split('_')[1])
               TC_Result = str(test_result_pass_or_fail_match.group().split()[0])
               TC_Pars_Status = "OK"
               Parse_Cantata(cls.Parsing_Component, TC_ID, TC_Result, TC_Pars_Status)
            else:
               TC_ID = str(id_match.group().split('_')[1])
               TC_Result = str(test_result_pass_or_fail_match.group().split()[0])
               TC_Pars_Status = "ERROR: Unexpected Value!"
               Parse_Cantata(cls.Parsing_Component, TC_ID, TC_Result, TC_Pars_Status)
         elif test_result_match != None:
            TC_ID = str(id_match.group().split('_')[1])
            TC_Result = str(test_result_match.group())
            TC_Pars_Status = "ERROR: Unexpected Value!"
            Parse_Cantata(cls.Parsing_Component, TC_ID, TC_Result, TC_Pars_Status)
