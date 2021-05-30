import numpy as np
import matplotlib.pyplot as plt

pontos=np.array([[1.00, 1.51],[2.29,4.13],[3.57,6.28],[4.86,10.02],[6.14,11.46],[7.43,14.63],[8.71,17.99],[10.00,19.77]])

def p_lagrange(x,pontos):

  p = 0    

  n=pontos.shape[0]
  
  for i in range(n):   
    l_i = 1    
    for j in range(n):   
      if i!=j:           
        l_i = l_i*(x-pontos[j,0])/(pontos[i,0]-pontos[j,0])  
    p = p+l_i*pontos[i,1]    
    
  return p

x_range = np.linspace(0.5,10,100)


y=[]


for x in x_range:
  y.append(p_lagrange(x,pontos))
y=np.array(y)


plt.plot(x_range,y, 'k', label= 'P(x)')  
plt.scatter(pontos[:,0],pontos[:,1], label='dados') 
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
