import numpy as np
import math
class logistic_regression:
    def __init__(self):
        pass
    def __initial(self,x):
        self.__w=np.random.uniform(-1,1,len(x[0]))
        self.__b=0
        self.__dw=np.zeros(len(x[0]))
        self.__db=0
    def __forward(self,x):
        net=0
        self.__netin=x
        net=np.dot(self.__w,x)
        net=net+self.__b
        fnet=self.__sigmoid(net)
        return fnet
    def __sigmoid(self,x):
        fnet=1/(1+math.exp(-x))
        return fnet
    def __derivative_sigmoid(self,x):
        d1=x*(1-x)
        return d1
    def __Sgd(self,t,y,alpha):
        dout=self.__derivative_cross_entrophy(t,y)
        for i in range(len(self.__w)):
            self.__w[i]=self.__w[i]-(alpha*self.__netin[i]*dout)
        self.__b=self.__b-(alpha*dout)
    def __cross_entrophy(self,t,y):
        epsilon = 1e-9
        error=-np.mean((t*np.log10(y+epsilon))+((1-t)*np.log10(1-y+epsilon)))
        return error
    def __derivative_cross_entrophy(self,t,y):
        error=(y-t)/(y*(1-y))
        return error
    def __shuffle(self,x,t):
        temp=np.random.normal(size=len(x))
        x=list(x)
        for i in range(len(temp)):
            for j in range(len(temp)-i-1):
                if(temp[j]>temp[j+1]):
                    temp[j],temp[j+1]=temp[j+1],temp[j]
                    x[j],x[j+1]=x[j+1],x[j]
                    t[j],t[j+1]=t[j+1],t[j]
        x=np.array(x)
        return x,t
    def __classify(self,x):
        y=self.__forward(x)
        if(y>0.5):
            y=1
        else:
            y=0
        return y
    def predict(self,x):
        y=np.zeros(len(x),dtype='float64')
        for i in range(len(x)):
            y[i]=self.__classify(x[i])
        return y
    def learn(self,x,t,alpha,epoch):
        self.__initial(x)
        y=np.zeros(len(t),dtype='float64')
        x=np.array(x,dtype='float64')
        t=np.array(t,dtype='float64')
        for i in range(epoch):
            x,t=self.__shuffle(x,t)
            for j in range(len(x)):
                y[j]=self.__forward(x[j])
                self.__Sgd(t[j],y[j],alpha)
            for j in range(len(x)):
                y[j]=self.__forward(x[j])
            los=self.__cross_entrophy(t,y)
            print('Iter : ',i+1,' Loss : ',los)
