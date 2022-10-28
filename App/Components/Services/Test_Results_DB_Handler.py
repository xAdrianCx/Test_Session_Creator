from Components.Services import Config_Handler
from Components.Absts.Parse_Cantata import Parse_Cantata
from Components.Absts.Parse_VCast import Parse_VCast
from Components.Absts.Parse_Vtest import Parse_VTest


class Test_Results_DB_Excel_Handler:
   Test_Results_DB_Excel_Handler_Inst_lst = []
   Excel_Path = ''

   SW4_Fail_Comments = ''
   SW4_Pass_Comments = ''
   SW4_Skipped_Comments = ''

   SW5_Fail_Comments = ''
   SW5_Pass_Comments = ''
   SW5_Skipped_Comments = ''

   SW6_Fail_Comments = ''
   SW6_Pass_Comments = ''
   SW6_Skipped_Comments = ''


   def __init__(self, sw_lvl, comp_name, id, verdict, comment):
      self.sw_lvl = sw_lvl
      self.comp_name = comp_name
      self.id = id
      self.verdict = verdict
      self.comment = comment
      Test_Results_DB_Excel_Handler.Test_Results_DB_Excel_Handler_Inst_lst.append(self)


   @classmethod
   def Import_Cls_Config(cls,excel_path):
      # Import path to Excel file (used for import / export data)
      cls.Excel_Path = Config_Handler.Get_Excel_db_Path()

      # Import SW4 comments (Cantata &  VCast)
      cls.SW4_Pass_Comments = Config_Handler.Get_VCast_Pass_Comments()
      cls.SW4_Fail_Comments = Config_Handler.Get_VCast_Fail_Comments()
      cls.SW4_Skipped_Comments = Config_Handler.Get_VCast_Skipped_Comments()

      # Import SW5 comments (VTest)
      cls.SW5_Pass_Comments = Config_Handler.Get_VTest_SW5_Pass_Comments()
      cls.SW5_Fail_Comments = Config_Handler.Get_VTest_SW5_Fail_Comments()
      cls.SW5_Skipped_Comments = Config_Handler.Get_VTest_SW5_Skipped_Comments()

      # Import SW6 comments (VTest)
      cls.SW6_Pass_Comments = Config_Handler.Get_VTest_SW6_Pass_Comments()
      cls.SW6_Fail_Comments = Config_Handler.Get_VTest_SW6_Fail_Comments()
      cls.SW6_Skipped_Comments = Config_Handler.Get_VTest_SW6_Skipped_Comments()


   @classmethod
   def Import_Excel_Data(cls):
      pass


   @classmethod
   def Export_To_Excel (cls):
      pass


   # Hardcoded for Import Cantata_TCs and Import VCast_TCs only --> sw_lvl = SW4.
   # This method has to import test cases from Parse_Cantata
   @classmethod
   def Import_Cantata_Tcs(cls):
       sw_lvl = "SW4"
       for obj in Parse_Cantata.Parse_Cantata_Inst_lst:
           cls(sw_lvl, obj.CompName, obj.TC_ID, obj.TC_Result, obj.TC_Pars_Status)


   # This method has to import test cases from Parse_VCast.
   @classmethod
   def Import_VCast_Tcs(cls):
      sw_lvl = "SW4"
      for obj in Parse_VCast.Parse_VCast_Inst_lst:
         cls(sw_lvl, obj.CompName, obj.TC_ID, obj.TC_Result, obj.TC_Pars_Status)

   # This method has to import test cases from Parse_Vtest.
   @classmethod
   def Import_VTest_Tcs(cls):
      for obj in Parse_VTest.Parse_VTest_Inst_lst:
         cls(obj.SW_NR, obj.CompName, obj.TC_ID, obj.TC_Result, obj.TC_Pars_Status)

