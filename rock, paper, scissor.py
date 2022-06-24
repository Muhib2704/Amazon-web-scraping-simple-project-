import random
import time
from timeit import repeat

user="user"
computer="computer"
rock="rock"
paper="paper"
scissor="scissor"

def main():
    user=input("Enter your choice:")
    computer=random.choice([rock,scissor,paper])

    if user==rock:
            if computer==rock:
                time.sleep(1)
                print("The computer has chosen rock, therefore it's a draw")
            elif computer==paper:
                time.sleep(1)
                print("The computer has chosen paper, therefore you have lost")
            elif computer==scissor:
                time.sleep(1)
                print("The computer has chosen scissor, therefore you have won")
                
    if user==paper:
            if computer==rock:
                time.sleep(1)
                print("The computer has chosen rock, therefore you have won")
            elif computer==paper:
                time.sleep(1)
                print("The computer has chosen paper, therefore it's a draw")
            elif computer==scissor:
                time.sleep(1)
                print("The computer has chosen scissor, therefore you have lost")

    if user==scissor:
            if computer==rock:
                time.sleep(1)
                print("The computer has chosen rock, therefore you have lost")
            elif computer==paper:
                time.sleep(1)
                print("The computer has chosen paper, therefore you have won")
            elif computer==scissor:
                time.sleep(1)
                print("The computer has chosen scissor, therefore it's a draw")
                
    restart=input(("Would you like to play again?"))
    if restart=="yes":
        main()
        
    else:
        print("Bye")
        exit()
        
main()  
    
        
    
        
        
   
         


   




          

            
            
            
  
            

                    
            
           
            



            


    

            
    

    


        
        
         
        
            
        
    

        
        
        
        
        
    

    

        
        
        
        
        
        
    
    
        


    

        





    
        


    
    
        

            
        
        
        
 


