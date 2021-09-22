def swapingreader() :
 data_input = input('Enter the filename you want to read')

 data_a = open('sample1.txt')
 data_b = open('sample2.txt')
 
 with open('sample1','r') as a:
   data_a = a.read()

 with open('sample2','w') as a:
   a.write()


swapingreader()