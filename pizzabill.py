
   
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L") # What size pizza do you want? S, M, or L
add_pepperoni = input("do you want perparoni") # Do you want pepperoni? Y or N
extra_cheese = input("do you want extra cheese") # Do you want extra cheese? Y or N
small=15
Medium=20
Large=25
if size == "S":
  if add_pepperoni == "Y":
     small +=2
  if extra_cheese == "Y":
     small +=1
  print(f"Thank you for choosing Python Pizza Deliveries!Your final bill is: ${small}.")
elif size == "M":
  if add_pepperoni == "Y":
    Medium +=3
  if extra_cheese == "Y":
    Medium +=1
  print(f"Thank you for choosing Python Pizza Deliveries!Your final bill is: ${Medium}.")
elif size == "L":
  if add_pepperoni == "Y":
    Large +=3
  if extra_cheese == "Y":
     Large +=1
  print(f"Thank you for choosing Python Pizza Deliveries!Your final bill is: ${Large}.")
  
    