#used to store grouped piece of data having similar relationship eg states of india
states_of_india=["karnataka","uttarpradesh","Jammu&kashmir","Delhi","Hyderabad","Goa","rajasthan"]
print(states_of_india[0])
print(states_of_india[-1])

states_of_india[0]="Uttrakhand"  #edditing a list
print(states_of_india[0])

states_of_india.append("tauseef") #adding new single item at the end of the list
print(states_of_india)

states_of_india.extend(["malik","ahmad"]) # adding multiple items at the end of the list
print(states_of_india)

north=["Jammu&kashmir","Delhi"]
south=["karnataka","Hyderabad"]
states_of_india=[north,south]  #nestedlists
print(states_of_india)