# print('hello world')
# userName = 'Kamran'
# print(userName)


# number_one = input("Enter First number : ")
# number_two = input("Enter Second number : ")


# def addition(first_num:int , second_num: int):
#     return (first_num + second_num)



    
# print(f"The addition is {addition(int(number_one),int(number_two))}")


# import re



#heyy_kamran

# table_number = input("Enter your table number to print : ")
# table_range = input("Enter your table Range : ")
# alphabet = re.compile(r'[a-zA-Z]+')

# def print_table(tableNumber:int,tableRange:int) :
#     if(alphabet.match(tableNumber) or alphabet.match(table_range)):
#      return print('Please Enter Int number to do calculation')
     
#     for n in range(1,int(tableRange)+1):
#      print(f"{int(tableNumber)} X {n} = {n*int(tableNumber)}")



# print_table(table_number,table_range)




# i :int = 0
# while i < 4:
#     print(i)
#     i+=1



# # value = 'd' in userInput
# print(len(userInput))




# jokeList = [1,2]


# i:int = 1

# while i <= 7:
#    # if i :
#     print(f"value of i is {i}")
#     i+=1
   #  break
# def tellJoke(userInput :str):

#     while i <= len(jokeList):
#       if "joke" in userInput:
#        i += 1 
#        return print('joke for you')
#     else:
       
#        print('no joke for you')






# # tellJoke("Tell me a joke about anything?")

# print(len(jokeList))



joke:str = """Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs"""
sorry:str ="Sorry I only tell jokes"
prompt:str = input("What do you want?\n")

def tellJoke(userPrompt):
  if('joke' in userPrompt):
    return joke

  return sorry


if __name__ == "__main__":
    output = tellJoke(prompt)
    print(output)