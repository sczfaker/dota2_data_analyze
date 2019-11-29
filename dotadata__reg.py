from os import chdir,listdir,rename,walk,getcwd
from re import match,compile,search



#pattern=compile("(?=dotadata_dotadata_).*?") 
pattern=compile("(?P<id>dotadata_){1,2}.*?")
strings="dotadata_combi_final_generate5.py"
regobj=search(pattern,strings)
if regobj==None:
	print ("fail")
	assert 1>2,"f"
def delete_prefix():
	pattern=compile("(?P<id>dotadata_){2}.*?")
	for paths,folders,files in walk(getcwd()):
		for file in files:
			if search(pattern,file)!=None:
				rindex=file.rfind("dotadata_")
				new_name=file[rindex+8:]
				print (file,"->",new_name)
				rename(file,new_name)
# delete_prefix()
def add_prefix():
	for paths,folders,files in walk(getcwd()):
		for file in files:
			if file[-3:]==".py" and "dotadata_" not in file:
				tmp=file
				rename(file,"dotadata_"+tmp)
		break
add_prefix()

