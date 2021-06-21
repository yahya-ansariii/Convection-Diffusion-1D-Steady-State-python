'''
      Copyright 2021 MOHAMMED YAHYA ANSARI

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''
print("\n \t\t UPWIND Solver\n")
n = int(input("\nEnter the no. of grid points: "))

l = float(input("Enter length of plate in m: "))

u = float(input("Enter velocity in m/s: "))

rho = float(input("Enter density in kg/m3: "))

ta = float(input("Enter left boundary condition: "))

tb = float(input("Enter right boundary condition: "))

g = float(input("Enter Gamma in kg/ms: "))


#create list of size n
D = [0]*n
beta = [0]*n
alpha = [0]*n
c =[0]*n
A = [0]*n
C = [0]*n
temp = [0]*n


dx = l/n
x=g/dx
y=rho*u

D[0]=(3*x)+y
D[1]=(2*x)+y
D[n-1]=(3*x)+y

beta[1]=x+y
alpha[1]=x

c[0]=((2*x)+y)*ta

for i in range(1 , n-1):
	c[i]=0
#setup tdma
c[n-1]=0
beta[0] = 0
beta[n-1] = beta[1]
alpha[0] = alpha[1]
alpha[n-1] = 0
#copy common values in tdma
for i in range(2 , n-1):
    D[i] = D[1]
    beta[i]=beta[1]
    alpha[i]=alpha[1]

print("\n")

for i in range(0 , n):
    print("\t D%d is %f \t Beta %d is %f \t Alpha%d is %f \t C%d is %f " % (i+1,D[i],i+1,beta[i],i+1,alpha[i],i+1,c[i]))
    print("\n")

#solve tdma
a = alpha[0]
A[0] = a/D[0]
C[0] = c[0]/D[0]
for i in range(1 , n):
    A[i] = alpha[i]/(D[i] - beta[i]*A[i-1])
    C[i] = (beta[i]*C[i-1] + c[i])/(D[i] - beta[i]*A[i-1])

for i in range(0 , n):
    print("\tA%d = %f \t\t C'%d = %f"% (i+1, A[i], i+1,C[i]))
    print("\n")

print("\n")


temp[n-1] = C[n-1]

j = n-2
while j>=0:
    temp[j] = A[j] * temp[j+1] + C[j]
    j = j-1


#print result
print("Temperature values are:\n")

for i in range(0 , n):
    print("\t\t T%d = %f C \n" % (i+1, temp[i]))



input("Press enter to exit")