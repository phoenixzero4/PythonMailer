import re

def get_info(file):
	subject = input("Enter the subject:\n")
	recipient = input("Enter recipient email address:\n")
	attachment = input("Enter path of attachment (0):\n")

	with open(file, 'w') as f:
		f.write(f'Subject:{subject}')
		f.write("\n")
		f.write(f'To:{recipient}')
		f.write("\n")
		if attachment.lower() == 'n': 
			f.write(f'At:none')
			f.write("\n")
		elif re.search( ('jpg$|png$|pdf$'), attachment):
			f.write(f'At:{attachment}')
			f.write("\n")
		else:
			f.write(f'At:none')
			f.write("\n")

def print_file(file):
	with open(file) as f:
		data = f.readlines()
	print(data)