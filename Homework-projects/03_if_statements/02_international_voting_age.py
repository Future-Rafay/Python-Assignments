PETURKSBOUIPO = 16
STANLAU = 25
MAYENGUA = 48


def main():
    user_age: int = int(input("Enter your age: "))


    if user_age >= PETURKSBOUIPO:
        print("You can vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO) + ".") 
    else:
        print("You are not eligible to vote in Peturksbouipo where. the voting age is " + str(PETURKSBOUIPO) + ".")

    
    if user_age >= STANLAU:
        print("You can vote in STANLAU where the voting age is " + str(STANLAU) + ".")
    else:
        print("You are not eligible to vote in STANLAU where. the voting age is " + str(STANLAU) + ".")
    
    
    if user_age >= MAYENGUA:
        print(f"You can vote in MAYENGUA where the voting age is {MAYENGUA}")
    else:
        print("You are not eligible to vote in MAYENGUA where. voting age is " + str(MAYENGUA) + ".")



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
