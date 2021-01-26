if __name__ == '__main__':
    s = input()
    # This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
    
    print(any(char.isalnum() for char in s))
    # This method checks if any of the characters of a string are alphabetical (a-z and A-Z)
    print(any(char.isalpha() for char in s))
   
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))
    
    
    
        
        
