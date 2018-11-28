print("Python is very good for data analysis")
print("Important data analysis libraries in python are:")
#Enumerate allows us to loop over something and have an automatic counter.
Dict = {1:'Pandas', 2:'Numpy', 3:'Matplotlib'}
for i, item in enumerate(Dict):
    print("{}. {}".format(i, Dict[item]))
