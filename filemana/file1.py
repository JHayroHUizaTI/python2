"""
from io import open

def write_file():
    file1 = open('texto.txt','w')
    file1.write('Hello world\nhow are you')
    file1.close()


write_file()
"""
"""
with open('data3.txt','w+') as file1:
    file1.write("Oscar\nAlejandro\ncarlos\ngustavo")
    print(file1)
    read1 = file1.read()
    print(read1)
    file1.close()

"""

"""
fichero = open('./filemana/demo1.txt','w+')
fichero.write("Oscar\nAlejandro\ncarlos\ngustavo")
fichero.close()
"""

fichero = open('./filemana/demo1.txt','a')
fichero.write("\nComo es gente vamos a culear")
fichero.close()
