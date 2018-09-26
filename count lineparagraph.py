def make gen(reader):
      b=reader(1024*1024)
while b:
yield b
      b=reader(1024*1024)
 def rawpy count(file name):
      f=open(file name):
f gen=make gen(f.raw,read)
     return sum(but.count(b'\n')for buf in f gen)
   
