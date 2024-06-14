#functions with output

def format_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return "empty"
    
    a=f_name.title()
    b=l_name.title()
    return f"result: {a} {b}"
    
    
print(format_name(input("what is your first name"),input("What is your last name")))

#function with multiple outputs
