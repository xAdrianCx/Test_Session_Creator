
import distutils.dir_util
import os
import shutil

class Win_File_Sys:

   Win_File_Sys_Inst_lst = []
   # Needed for future development - nothing to do
   def __init__(self):
      Win_File_Sys.Win_File_Sys_Inst_lst.append(self)
   # Needed for future development - nothing to do
   def __del__(self):
      Win_File_Sys.Win_File_Sys_Inst_lst.remove(self)


   # Returns a list of paths to files found at the given path.
   # If parameters 'Name_filter' is not '', the results will be filterd by parameter.
   # The filtering shall work as fallows: if the parameter 'Name_filter' content is found in the file name, the result shall not be discarded.
   # If parameters 'Ext_Filter' is not '', the reulets will be filterd by parameter
   # The filtering shall work as fallows: if the parameter 'Ext_Filter' content is found in the file name, the result shall not be discarded.
   @staticmethod
   def Search_Files_Ret_List(Path, Name_filter='', Ext_Filter=''):
      result = []
      for root, dirs, files in os.walk(Path):
         for file in files:
            result.append(os.path.join(root, file))
      if Name_filter != '' and Ext_Filter == '':
         n_filter = []
         for i in result:
            if Name_filter in i:
               n_filter.append(i)
         return n_filter
      if Name_filter != '' and Ext_Filter != '':
         all_filter = []
         for i in result:
            if Name_filter in i and Ext_Filter in i:
               all_filter.append(i)
         return all_filter
      if Name_filter == '' and Ext_Filter != '':
         e_filter = []
         for i in result:
            if Ext_Filter in i:
               e_filter.append(i)
         return e_filter
      else:
         return result


   # Copyes source content in destination folder and replaces existing items.
   # If you need to delete de content of the destination folder before copy, use ReplaceFolder API.
   @staticmethod
   def CopyFolder(Source, Destination):
      error = False
      print ("Copy From: " + Source)
      print ("To  : " + Destination)

      if not os.path.exists(Destination):
         try:
            os.mkdir(Destination)
            print("Directory " , Destination ,  " Created ")
         except:
            print('Error in creating directory: '+Destination)
            error = True
      try:
         pass
         #distutils.dir_util.remove_tree(Destination)
      except:
         print('Error in deleting containt from: '+Destination)
         error = True
      try:
         distutils.dir_util.copy_tree(Source, Destination)
      except:
         print('Error in copying containt from: ' + Source + ' to ' + Destination)
         error = True
      return error


   # Deletes containt of destination folder
   # Copyes sorce containt in destination folder
   @staticmethod
   def ReplaceFolder(Source, Destination):
      error = False
      print ("Copy From: " + Source)
      print ("To  : " + Destination)

      if not os.path.exists(Destination):
         try:
            os.mkdir(Destination)
            print("Directory " , Destination ,  " Created ")
         except:
            print('Error in creating directory: '+Destination)
            error = True
      try:

         distutils.dir_util.remove_tree(Destination)
      except:
         print('Error in deleting containt from: '+Destination)
         error = True
      try:
         distutils.dir_util.copy_tree(Source, Destination)
      except:
         print('Error in copying containt from: ' + Source + ' to ' + Destination)
         error = True
      return error


   # Checks if the given path egzists on the machines file system
   # Returns True if OK, False if invalid path
   @staticmethod
   def Check_Folder_Exists(path):
      if os.path.exists(path):
         return True
      else:
         return False


   #Copyes a file from "Source" path to "Destination"
   #Returns Ture of the operation has failed.
   #Returns False if the opperation has scuceeded.
   @staticmethod
   def copyfile(Source,Destination):
      error = False
      print ("Copy From: " + Source)
      print ("To  : " + Destination)
      try:
         shutil.copy(Source, Destination)
      except:
         print('Error in copying content from: '+Source+' to '+Destination)
         error = True
      return error

      #shutil.copy(src,dest)
