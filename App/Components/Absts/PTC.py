
#from Components import Win_Sync_Process

class PTC:
   PTC_Handler_Inst_lst = []
   def __init__(self):
      PTC.PTC_Handler_Inst_lst.append(self)

   def __del__(self):
      PTC.PTC_Handler_Inst_lst.remove(self)
