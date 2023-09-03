elements_list=[1,2,9,143,"irfan","SK","Python","Anaconda",4.45,-20.90]#bool also will get printed due to promotion(doubt)
num_list_lambda=lambda x:isinstance(x,(int,float))
number_list=filter(num_list_lambda,elements_list)
print(list(number_list))
