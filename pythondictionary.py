#python dictionary  {key:value}

python_dictionary={"bug":"An error in a program.", 
"function":"Piece of code that you can easily call over and over again",

}

print(python_dictionary["bug"])

#adding new item to dictionary
python_dictionary["loop"]="The action of doing something over and over again"
print(python_dictionary)

#loop through the dictionary
for key in python_dictionary:
    print(key)
    print(python_dictionary[key])
    
   #nesting
capitals={"france":"paris","germany":"berlin",} 
#Nesting list in an dictionary
travel_log={
    "france":["paris","lille","Dijon"]
}

#Nesting dictionary in a dictionary

travel_log2={
    "france":{"cities_visited":["paris","lille","Dijon"],"Total_visits":12},
    "germany":{"cities_visited":["berlin","Hamburg"],"total_visits":33}
}
print(travel_log2)

#nesting dictionary in a list
travel_log3=[
    {"country":"france",
     "cities_visited":["paris","little","dijon"],
     "Total_visits":12},
    
    {"country":"germany",
     "cities_visited":["berlin","Hamburg","stuttgart"],
     "total_visits":4},
       
] 