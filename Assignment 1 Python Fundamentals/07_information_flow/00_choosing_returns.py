ADULT_AGE : int = 18 # Pakistan. age 

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    
    return False

def main():
    age : str = int(input("How old is this person?: "))
    if is_adult(age):
        print("The Person is Adult")
    else:
        print("The Person is not Adult")
    

if __name__ == "__main__":
    main()