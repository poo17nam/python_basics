file_name = "my_tasks.txt"

f=open(file_name,'a')
f.write("abc")
f.write("def")
f.close()

print("File written successfully")
