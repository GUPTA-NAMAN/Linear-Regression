import csv
import math

def predict(vector,parameter) :
    ans= parameter[0]
    for i in range(1,len(parameter)) :
        ans = ans + vector[i-1]*parameter[i]
    return ans

file=open("train_data.csv","r")
datasheet=csv.reader(file)

variable=[]
output=[]
first=0

for row in datasheet :
    if  first==1 :
        temp=[]
        for i in range(4) :
            temp.append(float(row[i]))
        variable.append(temp)
        output.append(float(row[4]))
    first=1


for i in range(4) :
    sum=0
    for j in range(len(output)) :
        sum=sum+variable[j][i]
    av=sum/float(len(output))
    sum=0
    for j in range(len(output)) :
        sum = sum + (variable[j][i]-av)**2
    deviation = math.sqrt(sum/(len(output)-1 ))
    for j in range(len(output)) :
        variable[j][i]=(variable[j][i]-av)/deviation

sum=0
for j in range(len(output)) :
    sum=sum+output[j]
av=sum/float(len(output))
sum=0
for j in range(len(output)) :
    sum=sum+(output[j]-av)**2
deviation=math.sqrt(sum/len(output)-1)
for j in range(len(output)) :
    output[j]=(output[j]-av)/deviation


no_example = len(output)
learing_rate=0.0001
decay_rate=0.0001
iteration=1000
temp=[0,0,0,0,0]
parameter=[0,0,0,0,0]


for i in range(iteration) :
    print(parameter)
    j_theta=[]
    loss=0
   
    
    for j in range(no_example) :
        j_theta.append( predict(variable[j],parameter) - output[j] )
    for j in range(5) :
        sum=0
        if (j!=0) :
            for k in range(no_example) :
                sum  = sum + j_theta[k]*variable[k][j-1]*learing_rate
        else :
            for k in range(no_example) :
                sum = sum + j_theta[k]*learing_rate
        temp[j]=temp[j] - sum - decay_rate*parameter[j]

    for j in range(5) :
        parameter[j] = temp[j]



print(parameter)
