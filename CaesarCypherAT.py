def CaesarCypher():
    #Define a list with alphabets.Each alphabet here will have their corresponding index from 0-25
    l1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    result="" #variable to store result
    print("Enter the method you want to employ on text: Encrypt/Decrypt")
    Method=str(input().capitalize())# to store the Method Entered as input by user
    if Method not in ["Encrypt","Decrypt"]:
        result="The Method entered is not correct"
    else:
        print("Enter the key value in range 1 to 25")
        key=int(input()) # to store the shift key Entered as input by user
        if (key<1 or key>25):
            result="The entered Key value is not correct."
        else:  
            if Method=="Encrypt": #logic for Encryption
                print("Please Enter the clear Text/ plaintext")
                Msg=str(input()) #to store the text by user as input
                for i in range(len(Msg)): #iterate over length of message (Msg)
                    currentLetter=Msg[i]  #store the current fetched Value from Msg
                    if (currentLetter.isupper()): 
                        #if the currentLetter is UpperCase, then fetch its index from list l1 and store at pos_CL
                        pos_CL=l1.index(currentLetter) 
                        #add key value to index and modular divide it by 26, and append to result
                        result += l1[(pos_CL+key)%26]  
                    elif currentLetter.islower():
                        pos_CL=l1.index(currentLetter.upper()) #if the currentLetter is lowerCase,use upper() method and fetch its index from list l1
                        result += l1[(pos_CL+key)%26].lower() # get the position of shifted letter and use lower() method to append it to result
                    else:
                        result+=currentLetter #if currentLetter is a symbol or space,append it to result as it is
            else:  #logic for Decryption
                print("Please Enter the encrypted text")
                Msg=str(input())  #to store the text by user as input
                for i in range(len(Msg)): #iterate over length of message (Msg)
                    currentLetter=Msg[i]
                    if (currentLetter.isupper()):
                        pos_CL=l1.index(currentLetter) #if the currentLetter is UpperCase, then fetch its index from list l1
                        result += l1[pos_CL-key] #subtract key value from index, to get the position of letter it is shifted to and append to result
                    elif currentLetter.islower():
                        pos_CL=l1.index(currentLetter.upper()) #if the currentLetter is lowerCase,use upper() method and fetch its index from list l1
                        result += l1[pos_CL-key].lower() # get the position of shifted letter and use lower() method to append it to result
                    else:
                        result+=currentLetter #if currentLetter is a symbol or space,append it to result as it is 
    if len(result)==0:
        return "There is no input text given to Encrypt or Decrypt"
    else:    
        return "Output: "+result

print(CaesarCypher())
