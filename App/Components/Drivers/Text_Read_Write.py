import os


class Text_Read_Write:
	Text_Read_Write_Inst_lst = []

	# Needed for future development - nothing to do
	def __init__(self):
		Text_Read_Write.Text_Read_Write_Inst_lst.append(self)

	# Needed for future development - nothing to do
	def __del__(self):
		Text_Read_Write.Text_Read_Write_Inst_lst.remove(self)

	# Starts the reading process of a file and calls
	# a callback function of the upper layers which will process it
	# and returns the status
	@staticmethod
	# def Read_File_Line_by_Line(path):
	def Read_File_Line_by_Line(path, callback):
		if path.split(".")[1] == "ctr":
			try:
				with open(path, "r", encoding="UTF-8") as file:
					if len(file.readlines()) < 1:
						return "Unsuccessful! File is empty."
			except FileNotFoundError:
				return "Unsuccessful! File Not Found!"
			else:
				with open(path, "r", encoding="UTF-8") as file:
					lines = file.read()
					lines = lines.splitlines()
					for line in lines:
						callback(line.rstrip())
				return "Successful!"
		if path.split(".")[1] == "html":
			try:
				with open(path, "r") as html_file:
					if len(html_file.readlines()) < 1:
						return "Unsuccessful! File is empty."
			except FileNotFoundError:
				return "Unsuccessful! File Not Found!"
			else:
				with open(path, "r") as html_file:
					lines = html_file.read()
					lines = lines.splitlines()
					for line in lines:
						callback(line.rstrip())
				return "Successful!"


	# Reads a file and returns its entire content as a list (element = line) and returns the status
	@staticmethod
	def Read_File_Ret_Content(path):
		# defined the content variable to prevent py error: variable used before declaration
		content = []
		try:
			if path.split(".")[1] == "ctr":
				with open(path, "r") as file:
					content = file.readlines()
			if path.split(".")[1] == "html":
				with open(path, "r") as html_file:
					content = [i for i in html_file]
		except FileNotFoundError:
			# before changes: return "Unsuccessfull! File Not Found."
			return content, "Unsuccessful! File Not Found!"
		if len(content) == 0:
			# before changes: return "Unsuccessfull! File is empty."
			return content, "Unsuccessful! File is empty!"
		else:
			return content, "Successful!"


	# Writes the full content of a file and returns the status
	@staticmethod
	# def Write_File_Full_Ret_Status(path):
	def Write_File_Full_Ret_Status(path, content):
		# Function need to be reworked.
		# The scope of this function is to write the "content", provided by content parameter,
		# to a file provided by the "path" parmeter
		# The "path" parmeter contains the full path to the file.
		# The "path" parameters is a string.
		# The "content" parameter contains the data to be written.
		# The "content" paramater is a list. Each element of the list shall be considerd a line in the written file.
		try:
			with open(path, "w") as file:
				if isinstance(content, str):
					if len(content) > 0:
						file.write(content)
					else:
						return "Unsuccessful! You need to pass something to the string."
				elif isinstance(content, list):
					if len(content) > 0:
						for line in content:
							file.writelines(line)
					else:
						return "Unsuccessful! You need to pass something to the list."
				elif os.path.getsize(path) == 0:
					return "Unsuccessful! File is empty."
		except:
			return "Unsuccessful! An exception has occured."
		else:
			return "Successful!"
	# old code ---------------------------------------------------
	# content, error = Text_Read_Write.Read_File_Ret_Content(path)
	# if error != "Unsuccessfull!":
	# 	with open(new_file_path, "w") as file:
	# 		# Changed from content[0] to content -> we need the full
	# 		for elem in content[0]:
	# 			file.write(elem.strip() + "\n")
	# else:
	# 	return "Unsuccessfull!"


	# Injects content into a file at given line and returns the status
	# The function needs to be updated. Consider text as a list, where each element is a line to be added.
	@staticmethod
	# def Write_File_Full_Ret_Status(path,line):
	def Inject_Into_File_Ret_Status(path, line, text):
		"""
		If the file has less lines as 'line' parameter,
		it will insert everything at the end of the file.
		"""
		global content
		try:
			with open(path, "r") as file:
				content = file.readlines()
			with open(path, "w") as file:
				if isinstance(text, str):
					content.insert(line, f"{text}\n")
					file.writelines(content)
				elif isinstance(text, list):
					new_content = ""
					for i in text:
						new_content += str(f"{i}\n")
					content.insert(line, new_content)
					file.writelines(content)
		except FileNotFoundError:
			return "Unsuccessful! File not found!"
		else:
			return "Successful!"
