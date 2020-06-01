
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


with open('gbk.txt', 'a+', encoding='utf-8') as f:
	f.seek(0)
	print (f.readlines())
	f.write("\n我是谁?我去哪?我会怎么样?")