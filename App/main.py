import os
from Components.Drivers import Text_Read_Write
from Components.Absts import Parse_Cantata
from Components.Absts import Parse_VCast
from Components.Absts import Parse_VTest
from Components.Absts.Excel_Handler import Excel_Handler
from Components.Services.Test_Results_DB_Handler import Test_Results_DB_Excel_Handler




### This file is just for testing purposes.

if __name__ == '__main__':
   # ___________________________________________________________________________________________________________________
   # ___________________________________________________________________________________________________________________
   # Run Test_Results_DB_Handler class with Parse_Vtest.

   # Run Pars_File_Return_Status method.

   vtest_file = "Report_SW5_DataThrouput_1.html"
   VTest_File_Path = os.path.dirname(os.path.abspath(("App")))
   VTest_File_Path = os.path.join(VTest_File_Path, f"Inputs\\VTest\\SW6-SWQT\\{str(vtest_file)}")
   if "_SW5_" in str(vtest_file) and "SW6-SWQT" in str(VTest_File_Path):
      VTest_File_Path = str(VTest_File_Path).replace("SW6-SWQT", "SW5-SWIT")
   elif "_SW6_" in str(vtest_file) and "SW5-SWIT" in str(VTest_File_Path):
      VTest_File_Path = str(VTest_File_Path).replace("SW5-SWIT", "SW6-SWQT")
   status = Parse_VTest.Pars_File_Return_Status(VTest_File_Path)
   Test_Results_DB_Excel_Handler.Import_VTest_Tcs()
   for index in Test_Results_DB_Excel_Handler.Test_Results_DB_Excel_Handler_Inst_lst:
      print(index.sw_lvl)
   # ___________________________________________________________________________________________________________________
   # ___________________________________________________________________________________________________________________


   # ___________________________________________________________________________________________________________________
   # ___________________________________________________________________________________________________________________
   # Run Test_Results_DB_Handler class with Parse_VCast.

   # Run Parse_File_Return_Status method.
   # vcast_file = "L2H0090_MFK5_SWCT_TestReport_DIAG_Image_Upload_DetailedDesign_test_copy.html"
   # VCast_Test_File_Path = os.path.dirname(os.path.abspath('App'))
   # VCast_Test_File_Path = os.path.join(VCast_Test_File_Path, f"Inputs\\VectorCast\\{str(vcast_file)}")
   # status = Parse_VCast.Pars_File_Return_Status(VCast_Test_File_Path, '')
   #
   # Test_Results_DB_Excel_Handler.Import_VCast_Tcs()
   # for index in Test_Results_DB_Excel_Handler.Test_Results_DB_Excel_Handler_Inst_lst:
   #    print(index.sw_lvl)
   # ___________________________________________________________________________________________________________________
   # ___________________________________________________________________________________________________________________


   # ___________________________________________________________________________________________________________________
   # ___________________________________________________________________________________________________________________
   # Run Test_Results_DB_Handler class with Parse_Cantata.

   # Run Pars_File_Return_Status method.
   # cantata_file = 'test_SignalMonitoringQM_test.ctr'
   # Cantata_Test_File_Path = os.path.dirname(os.path.abspath('App'))
   # Cantata_Test_File_Path = os.path.join(Cantata_Test_File_Path,f"Inputs\\Cantata\\{str(cantata_file)}")
   # status = Parse_Cantata.Pars_File_Return_Status(Cantata_Test_File_Path,'SigMon')
   #
   # Test_Results_DB_Excel_Handler.Import_Cantata_Tcs()
   # for index in Test_Results_DB_Excel_Handler.Test_Results_DB_Excel_Handler_Inst_lst:
   #    print(index.id)
   # ___________________________________________________________________________________________________________________
   # ___________________________________________________________________________________________________________________


   # ___________________________________________________________________________________________________________________
   # ___________________________________________________________________________________________________________________
   # Run Parse_VTest Class using Excel_Handler class

   # Run Pars_File_Return_Status method.
   # vtest_file = "Report_SW6_LogTrace_Field_Mode_2.html"
   # VTest_File_Path = os.path.dirname(os.path.abspath(("App")))
   # VTest_File_Path = os.path.join(VTest_File_Path, f"Inputs\\VTest\\SW6-SWQT\\{str(vtest_file)}")
   # if "_SW5_" in str(vtest_file) and "SW6-SWQT" in str(VTest_File_Path):
   #    VTest_File_Path = str(VTest_File_Path).replace("SW6-SWQT", "SW5-SWIT")
   # elif "_SW6_" in str(vtest_file) and "SW5-SWIT" in str(VTest_File_Path):
   #    VTest_File_Path = str(VTest_File_Path).replace("SW5-SWIT", "SW6-SWQT")
   # status = Parse_VTest.Pars_File_Return_Status(VTest_File_Path)

   # for obj in Parse_VTest.Parse_VTest_Inst_lst:
   #    Excel_Handler.Add_Data(obj.TC_ID, obj.CompName, obj.TC_Result, obj.TC_Pars_Status, obj.SW_NR)
   # excel_file = "Output_template.xlsx"
   # excel_file_path = os.path.dirname(os.path.abspath(("App")))
   # excel_file_path = os.path.join(excel_file_path, f"Output\\{str(excel_file)}")
   # Excel_Handler.Import_Sheet(excel_file_path, "SW6")
   # for obj in Excel_Handler.Excel_Handler_Inst_lst:
   #    print(obj.el1)
   # Excel_Handler.Write_Sheet(excel_file_path, "SW6", filter_el=7, filter_val=9859717)

   # print(f"Before remove: {len(excel_handler.Excel_Handler_Inst_lst)}")
   # for index in Excel_Handler.Excel_Handler_Inst_lst:
   #    print(f"el1: {index.el1}")
   #    print(f"el2: {index.el2}")
   #    print(f"el3: {index.el3}")
   #    print(f"el4: {index.el4}")
   #    print(f"el5: {index.el5}")
   #    print(f"el6: {index.el6}")
   #    print(f"el7: {index.el7}")
   # excel_handler.Remove_Data(2)
   # print(f"After Remove_Data(): {len(excel_handler.Excel_Handler_Inst_lst)}")
   # excel_handler.Remove_All_Data()
   # print(f"After Remove_All_Data(): {len(excel_handler.Excel_Handler_Inst_lst)}")

   # for index in Excel_Handler.Excel_Handler_Inst_lst:
   #    print(f"el1: {index.el1}")
   #    print(f"el2: {index.el2}")
   #    print(f"el3: {index.el3}")
   #    print(f"el4: {index.el4}")
   #    print(f"el5: {index.el5}")
   #    print(f"el6: {index.el6}")
   #    print(f"el7: {index.el7}")
      # print("____________________________________________")
      # print (f'Comp Name: {str((index.CompName))}')
      # print (f'SW_NR: {str((index.SW_NR))}')
      # print (f'ID: {str((index.TC_ID))}')
      # print (f'Test Result: {str((index.TC_Result))}')
      # print (f'Status: {str((index.TC_Pars_Status))}')
      # print("____________________________________________")

   # Run Get_Test_lst method(must be run togheter with a function that parses results to class(e.g.,
   # Parse_File_Return_Status or Read_File_Line_by_Line with the class's Pars_Line_Clbk method as parameter.).
   # getter = Parse_VTest.Get_Tests_lst()
   # pprint(getter)

   # Run Read_File_Line_by_Line method so we check if Pars_Line_Clbk method works
   # vtest_file = "Report_SW6_LogTrace_Eng_Mode_Lock_Active.html"
   # VTest_File_Path = os.path.dirname(os.path.abspath(("App")))
   # VTest_File_Path = os.path.join(VTest_File_Path, f"Inputs\\VTest\\SW6-SWQT\\{str(vtest_file)}")
   # if "_SW5_" in str(vtest_file) and "SW6-SWQT" in str(VTest_File_Path):
   #    VTest_File_Path = str(VTest_File_Path).replace("SW6-SWQT", "SW5-SWIT")
   # elif "_SW6_" in str(vtest_file) and "SW5-SWIT" in str(VTest_File_Path):
   #    VTest_File_Path = str(VTest_File_Path).replace("SW5-SWIT", "SW6-SWQT")
   # read = Text_Read_Write.Read_File_Line_by_Line(VTest_File_Path, Parse_VTest.Pars_Line_Clbk)
   # for index in Parse_VTest.Parse_VTest_Inst_lst:
   #    index.CompName = str(vtest_file).split(".")[0]
   #    print("____________________________________________")
   #    print (f'Comp Name: {str((index.CompName))}')
   #    print (f'SW_NR: {str((index.SW_NR))}')
   #    print (f'ID: {str((index.TC_ID))}')
   #    print (f'Test Result: {str((index.TC_Result))}')
   #    print (f'Status: {str((index.TC_Pars_Status))}')
   #    print("____________________________________________")
   # ___________________________________________________________________________________________________________________
   # ___________________________________________________________________________________________________________________


   # ___________________________________________________________________________________________________________________
   # ___________________________________________________________________________________________________________________
   # Run Parse_VCast class.

   # Run Parse_File_Return_Status method.
   # vcast_file = "L2H0090_MFK5_SWCT_TestReport_DIAG_Image_Upload_DetailedDesign_test_copy.html"
   # VCast_Test_File_Path = os.path.dirname(os.path.abspath('App'))
   # VCast_Test_File_Path = os.path.join(VCast_Test_File_Path, f"Inputs\\VectorCast\\{str(vcast_file)}")
   # status = Parse_VCast.Pars_File_Return_Status(VCast_Test_File_Path, '')
   # print(f"Status: {str(status)}")
   # for index in Parse_VCast.Parse_VCast_Inst_lst:
   #    print("____________________________________________")
   #    print (f'Comp Name: {str((index.CompName))}')
   #    print (f'ID: {str((index.TC_ID))}')
   #    print (f'Test Result: {str((index.TC_Result))}')
   #    print (f'Status: {str((index.TC_Pars_Status))}')
   #    print("____________________________________________")

   # Run Get_Tests_lst method.
   # vcast_file = "L2H0090_MFK5_SWCT_TestReport_SAF_EyeQ_Fault_Handler_DetailedDesign_test_copy.html"
   # VCast_Test_File_Path = os.path.dirname(os.path.abspath('App'))
   # VCast_Test_File_Path = os.path.join(VCast_Test_File_Path,f"Inputs\\VectorCast\\{str(vcast_file)}")
   # getter = Parse_VCast.Get_Tests_lst()
   # pprint(getter)

   # Run Read_File_Line_by_Line method so we check if Pars_Line_Clbk method works.
   # vcast_file = "L2H0090_MFK5_SWCT_TestReport_DIAG_Image_Upload_DetailedDesign_test_copy.html"
   # VCast_Test_File_Path = os.path.dirname((os.path.abspath("App")))
   # VCast_Test_File_Path = os.path.join(VCast_Test_File_Path, f"Inputs\\VectorCast\\{str(vcast_file)}")
   # read = Text_Read_Write.Read_File_Line_by_Line(VCast_Test_File_Path, Parse_VCast.Pars_Line_Clbk)
   # print(f"Reading from the source: {read}")
   # for index in Parse_VCast.Parse_VCast_Inst_lst:
   #    print("____________________________________________")
   #    print (f'ID: {str((index.TC_ID))}')
   #    print (f'Test Result: {str((index.TC_Result))}')
   #    print (f'Status: {str((index.TC_Pars_Status))}')
   #    print("____________________________________________")
   # ___________________________________________________________________________________________________________________
   # ___________________________________________________________________________________________________________________



   # ___________________________________________________________________________________________________________________
   # ___________________________________________________________________________________________________________________
   # Run Parse_Cantata class.

   # Run Pars_File_Return_Status method.
   # print ('start')
   # cantata_file = 'test_SignalMonitoringQM_test.ctr'
   # Cantata_Test_File_Path = os.path.dirname(os.path.abspath('App'))
   # Cantata_Test_File_Path = os.path.join(Cantata_Test_File_Path,f"Inputs\\Cantata\\{str(cantata_file)}")
   # status = Parse_Cantata.Pars_File_Return_Status(Cantata_Test_File_Path,'SigMon')
   # print('status:'+str(status))
   # for index in Parse_Cantata.Parse_Cantata_Inst_lst:
   #    print("____________________________________________")
   #    print (f'Comp Name: {str((index.CompName))}')
   #    print (f'ID: {str((index.TC_ID))}')
   #    print (f'Test Result: {str((index.TC_Result))}')
   #    print (f'Status: {str((index.TC_Pars_Status))}')
   #    print("____________________________________________")

   # Run Get_Tests_lst method.
   # print("start")
   # cantata_file = 'test_SignalMonitoringQM_test.ctr'
   # Cantata_Test_File_Path = os.path.dirname(os.path.abspath('App'))
   # Cantata_Test_File_Path = os.path.join(Cantata_Test_File_Path,f"Inputs\\Cantata\\{str(cantata_file)}")
   # getter = Parse_Cantata.Get_Tests_lst()
   # pprint(getter)

   # Run Read_File_Line_by_Line method so we check if Pars_Line_Clbk method works.
   # print ('start')
   # cantata_file = 'test_SignalMonitoringQM_test.ctr'
   # Cantata_Test_File_Path = os.path.dirname(os.path.abspath('App'))
   # Cantata_Test_File_Path = os.path.join(Cantata_Test_File_Path,f"Inputs\\Cantata\\{str(cantata_file)}")
   # read = Text_Read_Write.Read_File_Line_by_Line(Cantata_Test_File_Path, Parse_Cantata.Pars_Line_Clbk)
   # ___________________________________________________________________________________________________________________
   # ___________________________________________________________________________________________________________________
