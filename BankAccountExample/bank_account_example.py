import json
import os

class FileManagement:
    def __init__(self):
        pass


    def save_data(self,file_name,data_to_save):
       try:
          ## if file exist so read file
          if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
             with open(file_name, 'r') as f:
               data = json.load(f)
          else:
             ## intialize empty list to append distionary
             data =[]
          if isinstance(data_to_save,list):
            data.extend(data_to_save)
          else:
             data.append(data_to_save)
          with open(file_name, 'w') as f:
                json.dump(data, f, indent=4)

                print(f"Data saved successfully to {file_name}")
          
               
       except Exception as e :
          print(f"Error In saving data in file {e}")
       


 
class Bank:
    def __init__(self):
     self.file_manager = FileManagement()

# autheinticate user
    def user_auth(self):
     _saved_email = 'admin@gmail.com'
     _saved_password = "admin2211"
     email = input("Enter your orginzation Email: ")
     password = input("Enter your orginzation password: ")
     if(email == _saved_email and password == _saved_password):
         print("\n=== Banker MENU ===")
         options = ['Account Opening', 'Reset Password', 'Exit Menu']
         for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

         choice = input("Enter your choice: ")

         if choice == "1":
            print("👉 You selected: Account Openning")
            self.account_opening()
            

         elif choice == "2":
            print("👉 You selected: reset Paasword")
            self.resetPassword()
            # call account holder menu here
         else:
          print('invalid choice')
          return

        
        
         

     else:
       print('Invalid email or password')
       return



# function for open account
    def account_opening(self):
        name = input("Enter user name: ")
        email = input("Enter user email: ")
        initial_deposit = input("Enter user initial Deposit: ")
        pin = input("Enter user pin: ")
        file_name='user_records.json'
        try:
            data_to_save = {"name":name,"email":email,"initial_deposit":initial_deposit,"pin":pin}
            self.file_manager.save_data(file_name=file_name,data_to_save=data_to_save)
            print("Data saved successfully.")
        except Exception as e:
            print(f"error in opening Accouunt {e}")
    
    
    # reset password for specific user
    def resetPassword(self):
       user_email = input("Enter user Email: ")
       new_pin = input("Enter user new pin: ")
       file_name='user_records.json'
       try:
           # open and found file
           if os.path.exists(file_name) and os.path.getsize(file_name) > 0 :
               with open(file_name, 'r') as f:
                data = json.load(f)
               for x in data:  
                 if x.get('email') == user_email:
                  x['pin'] = new_pin
                  os.remove(file_name)
                  self.file_manager.save_data(file_name=file_name,data_to_save=data)
                  print(f"{x['name']} pin updated new pin is {new_pin}")
                  break
               else:
                 print(f"No user is found with email {user_email}")
           else:
              print(f"file not found with name {file_name}")
              return

       except Exception as e:
          print(f"Error in file {e}")        



class Account:
   def __init__(self):
    self.file_manager = FileManagement()

   def get_balance():
    pass




def main():
   bank = Bank()
   # bank.resetPassword()

   options = ['Login as banker', 'Login as Account Holder', 'Exit Menu']

   while True: 
        print("\n=== MAIN MENU ===")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("👉 You selected: Login as banker")
            bank.user_auth()

        elif choice == "2":
            print("👉 You selected: Login as Account Holder")
            # call account holder menu here

        elif choice == "3":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice, please try again.")
            pass







main()
