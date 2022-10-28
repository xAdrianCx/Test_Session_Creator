import os
from configparser import ConfigParser


class Config_Handler:
   Class_Init_sts = False

   Cantata_Reports_Path = ''
   VCast_Reports_Path = ''
   VTest_SW5_Reports_Path = ''
   VTest_SW6_Reports_Path = ''
   Excel_db_Path = ''

   Parse_Cantata = False
   Parse_VCast = False
   Parse_VTest_SW5 = False
   Parse_VTest_SW6 = False

   Comp_Names_Cantata = []
   Comp_Names_VCast = []
   Comp_Names_VTest_SW5 = []
   Comp_Names_VTest_SW6 = []

   Cantata_Tcs_Doc_Ids = []
   VCast_Tcs_Doc_Ids = []
   VTest_SW5_Tcs_Doc_Ids = []
   VTest_SW6_Tcs_Doc_Ids = []

   Requirements_Acceptance_State = []

   VCast_Pass_Comments = ''
   VCast_Fail_Comments = ''
   VCast_Skipped_Comments = ''

   VTest_SW5_Pass_Comments = ''
   VTest_SW5_Fail_Comments = ''
   VTest_SW5_Skipped_Comments = ''

   VTest_SW6_Pass_Comments = ''
   VTest_SW6_Fail_Comments = ''
   VTest_SW6_Skipped_Comments = ''

   @classmethod
   def Get_Cantata_Reports_Path(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.Cantata_Reports_Path

   @classmethod
   def Get_VCast_Reports_Path(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.VCast_Reports_Path

   @classmethod
   def Get_VTest_SW5_Reports_Path(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.VTest_SW5_Reports_Path

   @classmethod
   def Get_VTest_SW6_Reports_Path(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.VTest_SW6_Reports_Path

   @classmethod
   def Get_Excel_db_Path(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.Excel_db_Path

   @classmethod
   def Get_Parse_Cantata(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.Parse_Cantata

   @classmethod
   def Get_Parse_VCast(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.Parse_VCast

   @classmethod
   def Get_Parse_VTest_SW5(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.Parse_VTest_SW5

   @classmethod
   def Get_Parse_VTest_SW6(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.Parse_VTest_SW6

   @classmethod
   def Get_Comp_Names_Cantata(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.Comp_Names_Cantata

   @classmethod
   def Get_Comp_Names_VCast(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.Comp_Names_VCast

   @classmethod
   def Get_Comp_Names_VTest_SW5(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.Comp_Names_VTest_SW5

   @classmethod
   def Get_Comp_Names_VTest_SW6(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.Comp_Names_VTest_SW6

   @classmethod
   def Get_Cantata_Tcs_Doc_Ids(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.Cantata_Tcs_Doc_Ids

   @classmethod
   def Get_VCast_Tcs_Doc_Ids(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.VCast_Tcs_Doc_Ids

   @classmethod
   def Get_VTest_SW5_Tcs_Doc_Ids(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.VTest_SW5_Tcs_Doc_Ids

   @classmethod
   def Get_VTest_SW6_Tcs_Doc_Ids(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.VTest_SW6_Tcs_Doc_Ids

   @classmethod
   def Get_Requirements_Acceptance_State(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.Requirements_Acceptance_State

   @classmethod
   def Get_VCast_Pass_Comments(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.VCast_Pass_Comments

   @classmethod
   def Get_VCast_Fail_Comments(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.VCast_Fail_Comments

   @classmethod
   def Get_VCast_Skipped_Comments(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.VCast_Skipped_Comments

   @classmethod
   def Get_VTest_SW5_Pass_Comments(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.VTest_SW5_Pass_Comments

   @classmethod
   def Get_VTest_SW5_Fail_Comments(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.VTest_SW5_Fail_Comments

   @classmethod
   def Get_VTest_SW5_Skipped_Comments(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.VTest_SW5_Skipped_Comments

   @classmethod
   def Get_VTest_SW6_Pass_Comments(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.VTest_SW6_Pass_Comments

   @classmethod
   def Get_VTest_SW6_Fail_Comments(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.VTest_SW6_Fail_Comments

   @classmethod
   def Get_VTest_SW6_Skipped_Comments(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.VTest_SW6_Skipped_Comments




   @classmethod
   def Import_Config(cls):
      #Creating path to project config file
      ROOT_DIR = os.path.dirname(os.path.abspath('App'))
      cfg_file_path = os.path.join(ROOT_DIR,"Config\\config.ini")

      #Create Inputs and Outputs Paths
      cls.Cantata_Reports_Path = os.path.join(ROOT_DIR,"Inputs\\Cantata")
      cls.VCast_Reports_Path = os.path.join(ROOT_DIR,"Inputs\\VectorCast")
      cls.VTest_SW5_Reports_Path = os.path.join(ROOT_DIR,"Inputs\\VTest\\SW5-SWIT")
      cls.VTest_SW6_Reports_Path = os.path.join(ROOT_DIR,"Inputs\\VTest\\SW6-SWQT")
      cls.Excel_db_Path = os.path.join(ROOT_DIR,"Output\\Output_template.xlsx")

      #Import and parse config file
      proj_config = ConfigParser()
      proj_config.read(cfg_file_path)

      #Import "Options" sections
      cls.Parse_Cantata = str(proj_config['Options']['Parse_Cantata'])
      cls.Parse_VCast = str(proj_config['Options']['Parse_VCast'])
      cls.Parse_VTest_SW5 = str(proj_config['Options']['Parse_VTest_SW5'])
      cls.Parse_VTest_SW6 = str(proj_config['Options']['Parse_VTest_SW6'])

      #Import "Inputs" sections
      cls.Comp_Names_Cantata = list(str(proj_config['Inputs']['Comp_Names_Cantata']).split(','))
      cls.Comp_Names_VCast = list(str(proj_config['Inputs']['Comp_Names_VCast']).split(','))
      cls.Comp_Names_VTest_SW5 = list(str(proj_config['Inputs']['Comp_Names_VTest_SW5']).split(','))
      cls.Comp_Names_VTest_SW6 = list(str(proj_config['Inputs']['Comp_Names_VTest_SW6']).split(','))

      cls.Cantata_Tcs_Doc_Ids = list(str(proj_config['Inputs']['Cantata_Tcs_Doc_Ids']).split(','))
      cls.VCast_Tcs_Doc_Ids = list(str(proj_config['Inputs']['VCast_Tcs_Doc_Ids']).split(','))
      cls.VTest_SW5_Tcs_Doc_Ids = list(str(proj_config['Inputs']['VTest_SW5_Tcs_Doc_Ids']).split(','))
      cls.VTest_SW6_Tcs_Doc_Ids = list(str(proj_config['Inputs']['VTest_SW6_Tcs_Doc_Ids']).split(','))

      #Import "Misk" sections

      cls.Requirements_Acceptance_State = list(str(proj_config['Misk']['Requirements_Acceptance_State']).split(','))

      cls.VCast_Pass_Comments = str(proj_config['Misk']['VCast_Pass_Comments'])
      cls.VCast_Fail_Comments = str(proj_config['Misk']['VCast_Fail_Comments'])
      cls.VCast_Skipped_Comments = str(proj_config['Misk']['VCast_Skipped_Comments'])

      cls.VTest_SW5_Pass_Comments = str(proj_config['Misk']['VTest_SW5_Pass_Comments'])
      cls.VTest_SW5_Fail_Comments = str(proj_config['Misk']['VTest_SW5_Fail_Comments'])
      cls.VTest_SW5_Skipped_Comments = str(proj_config['Misk']['VTest_SW5_Skipped_Comments'])

      cls.VTest_SW6_Pass_Comments = str(proj_config['Misk']['VTest_SW6_Pass_Comments'])
      cls.VTest_SW6_Fail_Comments = str(proj_config['Misk']['VTest_SW6_Fail_Comments'])
      cls.VTest_SW6_Skipped_Comments = str(proj_config['Misk']['VTest_SW6_Skipped_Comments'])

      cls.Class_Init_sts = True



