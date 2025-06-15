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



# joke:str = """Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs"""
# sorry:str ="Sorry I only tell jokes"
# prompt:str = input("What do you want?\n")

# def tellJoke(userPrompt):
#   if('joke' in userPrompt):
#     return joke

#   return sorry


# if __name__ == "__main__":
#     output = tellJoke(prompt)
#     print(output)


from graphics import Canvas
import time
    
CANVAS_WIDTH : int = 400
CANVAS_HEIGHT : int = 400

CELL_SIZE : int = 40
ERASER_SIZE : int = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""
    # Get mouse info to help us know which cells to delete
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()
    
    # Calculate where our eraser is
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    # Find things that overlap with our eraser
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    # For everything that overlaps with our eraser (that isn't our eraser), change
    # its color to white
    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:
            canvas.set_color(overlapping_object, 'white')

# There is no need to edit code beyond this point

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    num_rows = CANVAS_HEIGHT // CELL_SIZE  # Figure out how many rows of cells we need
    num_cols = CANVAS_WIDTH // CELL_SIZE   # Figure out how many columns of cells we need
    
    # Make a grid of squares based on the number of rows and columns.
    # The rows and columns along with our cell size help determine where
    # each individual cell belongs in our grid!
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE   # The right coordinate of the cell is CELL_SIZE pixels away from the left
            bottom_y = top_y + CELL_SIZE   # The bottom coordinate of the cell is CELL_SIZE pixels away from the top
            
            # Create a single cell in the grid
            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')
            
            
    canvas.wait_for_click()  # Wait for the user to click before creating the eraser
    
    last_click_x, last_click_y = canvas.get_last_click()  # Get the starting location for the eraser
    
    # Create our eraser
    eraser = canvas.create_rectangle(
        last_click_x, 
        last_click_y, 
        last_click_x + ERASER_SIZE, 
        last_click_y + ERASER_SIZE, 
        'pink'
    )
    
    # Move the eraser, and erase what it's touching
    while True:
        # Get where our mouse is and move the eraser to there
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        
        # Erase anything touching the eraser
        erase_objects(canvas, eraser) 
        
        time.sleep(0.05)


if __name__ == '__main__':
    main()