import os
import subprocess


class Win_Sync_Process:
   Win_Sync_Process_Inst_lst = []

   # Needed for future development: Cmd, Status (new, on-going, done, error)
   def __init__(self):
      Win_Sync_Process.Win_Sync_Process_Inst_lst.append(self)

   # Needed for future development: Cmd, Status (new, on-going, done, error)
   def __del__(self):
      Win_Sync_Process.Win_Sync_Process_Inst_lst.remove(self)

   @staticmethod
   def Run_Win_Cmd(statement, param=None):
      if param is None:
         cmd = str(statement)
      else:

         cmd = str(statement) + ' ' + str(param)
      print("\nINFO: run_process {0}".format(cmd))
      try:
         p = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
         return False, str(p)
      except Exception as e:
         print('Error during process: '+str(e))
         return True, str(e)

   @staticmethod
   def Run_Win_Cmd2(statement, param=None):
      if param is None:
         cmd = str(statement)
      else:

         cmd = str(statement) + ' ' + str(param)
      print("\nINFO: run_process {0}".format(cmd))
      try:
         p = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
         return False, str(p)
      except Exception as e:
         print('Error during process: '+str(e))
         return True, str(e)

   @staticmethod
   def Run_Win_Cmd3(statement, param=None):
      cmd = 'cmd /c "'
      if param is None:
         cmd = cmd + str(statement)+'"'
      else:

         cmd = cmd + str(statement) + ' ' + str(param)+'"'
      print("\nINFO: run_process {0}".format(cmd))
      try:

         print(cmd)
         p = os.system(cmd)
         return False, str(p)
      except Exception as e:
         print('Error during process: '+str(e))
         return True, str(e)