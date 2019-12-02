from math import log as ln
import numpy as np
from matplotlib import pyplot as plt
import random
dimention=2
percent_training_data=0.75
maximum_number_of_weight_update=100
learning_rate=0.1
number_of_class=3

def read_training_dataset(filename):
    file_object=open(filename,'r')
    file_data=file_object.readlines()
    data_vectors=[]#list of list
    for line in file_data:
        data_vectors.append([float(x) for x in line.split()])
    return data_vectors

def weight_training(training_data,class1,class2):

     weight = [0 for v in range(dimention)]
     bias=0
     convergence_x=[]
     convergence_y=[]
     # i think we should this number of input as all willl upadte the weght one time
     # print(len(training_data))
     for item in training_data:
         if item[2]==class1:
             item[2]=0
         elif item[2]==class2:
             item[2]=1
     number_of_wrongly_classified_point=len(training_data)
     itr=0
     convergence_x.append(itr)
     convergence_y.append(number_of_wrongly_classified_point)
     while number_of_wrongly_classified_point!=0:
     # for i2 in range(1000):
         itr+=1

     # for i2 in range(50):
         print("=== wronlgy classified ",number_of_wrongly_classified_point)
         # print(weight[0],weight[1],bias)
         number_of_wrongly_classified_point=0
         for i in range(len(training_data)):

             val=0
             val+=(training_data[i][0]*weight[0])
             val+=(training_data[i][1]*weight[1])
             val+=bias
             # print("val == ",val)
             output=0
             #activation
             if val>=0:
                 output=1
             else :
                 output=0

             number_of_wrongly_classified_point+=abs(output-training_data[i][2])
             #weight update
             # if condition:
             #     pass
             weight[0]=weight[0]+(learning_rate*(training_data[i][2]-output)*training_data[i][0])
             weight[1]=weight[1]+(learning_rate*(training_data[i][2]-output)*training_data[i][1])
             bias=bias+(learning_rate*(training_data[i][2]-output)*1)#bias can be assumed as input value 1
         convergence_x.append(itr)
         convergence_y.append(number_of_wrongly_classified_point)
     above_zero=class2
     # val=0
     # val+=(training_data[0][0]*weight[0])
     # val+=(training_data[0][1]*weight[1])
     # val+=bias
     # if val>=0:
     #     output=1
     # else:
     #     output=0
     # print(val,above_zero,training_data[0][2])
     return weight,bias,above_zero,[convergence_x,convergence_y]

def pridict_class(weight,bias,above_zero,i,j):
    # print(" ********************************************* ")
    predicted_class=-1
    x=0
    # print("x == =",x)
    val=0
    val+=(i*weight[x][0])
    val+=(j*weight[x][1])
    val+=bias[x]
    if val>=0:
        x=above_zero[x]

    if x==0:
        pass
        val+=(i*weight[2][0])
        val+=(j*weight[2][1])
        val+=bias[2]
        if val>=0:
            x=above_zero[2]
    else:
        val+=(i*weight[1][0])
        val+=(j*weight[1][1])
        val+=bias[1]
        if val>=0:
            x=above_zero[1]
    return x
    # for k in range(2):
    #
    #     val=0
    #     val+=(i*weight[x][0])
    #     val+=(j*weight[x][1])
    #     val+=bias[x]
    #     # output=0
    #     #activation
    #     print("val == =",val)
    #     if val>=0:
    #         # output=1
    #         predicted_class=above_zero[x]
    #     else :
    #         # output=0
    #         print(x," ^^^ ",above_zero[x])
    #         if above_zero[x]!=2:
    #             predicted_class=above_zero[x]+1
    #         else:
    #             predicted_class=0
    #
    #     x=predicted_class
    #     print("x == =",x)
        # predicted_class=above_zero[x][]
    return predicted_class

def main():
     # training_data=[[] for i in range(3)]

     # xmin=ymin=100;xmax=ymax=-100
     upper_limit=-100
     lower_limit=100
     data_vectors=[[]for v in range(number_of_class)]
     testing_data=[[] for i in range(3)]
     for i in range(1,4):#because it is two class perceptron
         filename='data_ls/Class'+str(i)+'.txt'
         data_vectors[i-1]=read_training_dataset(filename)
         lower_limit=min(lower_limit, np.amin(data_vectors[i-1]));
         upper_limit=max(upper_limit, np.amax(data_vectors[i-1]));
         for j in range((int(len(data_vectors[i-1])*percent_training_data)),int(len(data_vectors[i-1]))):
         # for j in range((int(len(data_vectors[i-1])*percent_training_data))):
             item=data_vectors[i-1][j]
             # print(item)
             testing_data.append([item[0],item[1],i-1])
             # print(testing_data)
     # print(testing_data)
     weight=[[] for v in range(number_of_class)]
     bias=[[] for v in range(number_of_class)]
     above_zero=[[] for v in range(number_of_class)]
     convergence_graph=[]
     for i in range(number_of_class):
         training_data=[]
         if i!=(number_of_class-1):
             # pass
             for item in data_vectors[i][:int(len(data_vectors[i])*percent_training_data)]:
                 training_data.append([item[0],item[1],i])
             for item in data_vectors[i+1][:int(len(data_vectors[i+1])*percent_training_data)]:
                 training_data.append([item[0],item[1],i+1])
             training_data = [x for x in training_data if x != []]
             # random.shuffle(training_data)
             # print("============trainging data========================")
             # print(training_data)
             weight[i],bias[i],above_zero[i],tempo=weight_training(training_data,i,i+1)
             convergence_graph.append(tempo)

         else:
             for item in data_vectors[i][:int(len(data_vectors[i])*percent_training_data)]:
                 training_data.append([item[0],item[1],i])
             for item in data_vectors[0][:int(len(data_vectors[0])*percent_training_data)]:
                 training_data.append([item[0],item[1],0])
             training_data = [x for x in training_data if x != []]
             random.shuffle(training_data)
             # print("============trainging data========================")
             # print(training_data)
             weight[i],bias[i],above_zero[i],tempo=weight_training(training_data,i,0)
             convergence_graph.append(tempo)

         # for item in data_vectors[int(len(data_vectors)*percent_training_data):]:
         #     testing_data.append([item[0],item[1],i-1])
     # print(1,pridict_class(weight,bias,above_zero,int(data_vectors[1][1][0]),int(data_vectors[1][1][1])))

     # print(above_zero)
     # print("F")
     X=[[] for v in range(number_of_class)]
     Y=[[] for v in range(number_of_class)]

     for i in np.arange(lower_limit,upper_limit,0.1):
         for j in np.arange(lower_limit,upper_limit,0.1):
             output=pridict_class(weight,bias,above_zero,i,j)
             # print i,j,' belongs to class ',C
             X[output].append(i)
             Y[output].append(j)
     #
     print ('drawing graph...\n')
     # print X,Y
     #naming the x axis
     plt.xlabel('x - axis')
     # naming the y axis
     plt.ylabel('y - axis')
     plt.plot(X[0],Y[0],color='pink',label='class 1')
     plt.plot(X[1],Y[1],color='lightgreen',label='class 2')
     plt.plot(X[2],Y[2],color='lightblue',label='class 3')
     testing_data = [x for x in testing_data if x != []]
     # random.shuffle(testing_data)
     check2=False
     check1=False
     check0=False
     total_error=0
     for i in range(len(testing_data)):
         # print(testing_data[0])
         output=pridict_class(weight,bias,above_zero,testing_data[i][0],testing_data[i][1])
         # print(output," = p *** real =",testing_data[i][2])
         if output!=testing_data[i][2]:
             total_error+=abs(output)
         if output==0:
             if check0==False:
                 plt.plot(testing_data[i][0], testing_data[i][1],marker='o', markersize=1, color="red",label="class1")
                 check0=True
             else:
                 plt.plot(testing_data[i][0], testing_data[i][1],marker='o', markersize=1, color="red")
         elif output==1:
             if check1==False:
                 plt.plot(testing_data[i][0], testing_data[i][1],marker='o', markersize=1, color="green",label="class2")
                 check1=True
             else:
                 plt.plot(testing_data[i][0], testing_data[i][1],marker='o', markersize=1, color="green")
         elif output==2:
             if check2==False:
                 plt.plot(testing_data[i][0], testing_data[i][1],marker='o', markersize=1, color="blue",label="class3")
                 check2=True
             else:
                 plt.plot(testing_data[i][0], testing_data[i][1],marker='o', markersize=1, color="blue")
     #
     # plt.plot(marker='o', markersize=1, color="green",label="redkw")
     plt.legend()
     plt.savefig('result.png')
     # plt.savefig('result.pdf')
     plt.show()
     plt.close()
     print ('## drawing convergence graph...\n')
     # print X,Y
     #naming the x axis
     plt.xlabel('x - axis')
     # naming the y axis
     plt.ylabel('y - axis')
     plt.plot(convergence_graph[0][0],convergence_graph[0][1],color='red',label='class 1')
     plt.plot(convergence_graph[1][0],convergence_graph[1][1],color='green',label='class 2')
     plt.plot(convergence_graph[2][0],convergence_graph[2][1],color='blue',label='class 3')
     plt.legend()
     plt.savefig('convergence.png')
     plt.show()
     print("model Accuracy is ",float(((len(testing_data)-total_error)/len(testing_data))*100))

if __name__ == '__main__':
    main()
    # print("frist")
