

class Customer_Repo_Handler:
   Customer_Repo_Handler_Inst_lst = []
   def __init__(self):
      Customer_Repo_Handler.Customer_Repo_Handler_Inst_lst.append(self)

   def __del__(self):
      Customer_Repo_Handler.Customer_Repo_Handler_Inst_lst.remove(self)