import math

def main():
    print(""" 
          
        A    
        |\\
   perp | \\ Hyp
        |  \ 
        |   \\
        |____\ 
        B     C
          Base

            """)

    AB: float = float(input("Enter the length of AB (Perp) :"))
    BC: float = float(input("Enter the length of BC (Base ) :"))
    AC: float = math.sqrt(AB ** 2 + BC ** 2)
    print("")
    print(f"The Lenght of AC (Hyp) = {AC:.2f}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
