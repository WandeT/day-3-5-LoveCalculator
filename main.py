# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_name = name1 + name2


lowercase_name=combined_name.lower()


t=lowercase_name.count("t")
r=lowercase_name.count("r")
u=lowercase_name.count("u")
e=lowercase_name.count("e")

true= t+r+u+e
l=lowercase_name.count("o")
o=lowercase_name.count("o")
v=lowercase_name.count("v")
e=lowercase_name.count("e")

love= l+o+v+e

love_score = int(str(true) + str(love))

print(love_score)

if (love_score < 10) or (love_score > 90):
  print(f"Your score is{love_score} , you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is{love_score} , you are alright together.")
else:
  print(f"Your score is{love_score} ")






# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")







