print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
name = name1 + name2

T_num = name.lower().count("t") 
R_num = name.lower().count("r") 
U_num = name.lower().count("u") 
E_num = name.lower().count("e") 
L_num = name.lower().count("l") 
O_num = name.lower().count("o") 
V_num = name.lower().count("v") 

total = str(T_num + R_num + U_num + E_num) + str(L_num + O_num + V_num + E_num)
score = int(total)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {socre}, you are alright together.")
else:
    print(f"Your score is {score}")
