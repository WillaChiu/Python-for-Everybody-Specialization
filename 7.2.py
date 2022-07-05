#7.2 Write a program that prompts for a file name, 
#then opens that file and reads through the file,
#looking for lines of the form:
 #       X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values 
#from each of the lines and compute the average
#of those values and produce an output as shown below.
#You can download the sample data at http://www.py
#thonlearn.com/code/mbox-short.txt when 
#you are testing below enter mbox-short.txt as the file name.


# Use the file name mbox-short.txt as the file name
fname=input('enter file name:')
try:
    f=open(fname)
except:
    print('fail')
    quit()
count=0
sum=0
for line in f:
    if not line.startswith('X-DSPAM-Confidence'):
        continue
    count=count+1

    a=line.find(':')
    num=float(line[a+2:])
    
    sum=sum+num
print(count,sum/count)
