


class Test_Results_Appl:
   Test_Results_Appl_Inst_lst = []
   def __init__(self):
      Test_Results_Appl.Test_Results_Appl_Inst_lst.append(self)

   def __del__(self):
      Test_Results_Appl.Test_Results_Appl_Inst_lst.remove(self)

   @classmethod
   def Import_TCs_SW4(cls):
      pass

   @classmethod
   def Import_TCs_SW5(cls):
      pass

   @classmethod
   def Import_TCs_SW6(cls):
      pass