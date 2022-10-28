

class Test_Results_Upload_PTC:
   Test_Results_Upload_PTC_Inst_lst = []
   def __init__(self):
      Test_Results_Upload_PTC.Test_Results_Upload_PTC_Inst_lst.append(self)

   def __del__(self):
      Test_Results_Upload_PTC.Test_Results_Upload_PTC_Inst_lst.remove(self)