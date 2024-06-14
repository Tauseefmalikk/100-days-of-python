#functions with input
def greet(name1,name2):  #paramater is the name of the data and we use the paramater inside the function to refer to it and to do things
    print(f"Hello {name1}")
    print(f"how do you do {name2}")
    print("isn't the weather nice today")
    
    
greet("tauseef", "malik") #arguement is the actual value of data that is going to be passed to the function here positional arguement
greet(name2="malik",name1="tausseef") #here used keyword arguement


