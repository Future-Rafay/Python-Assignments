def main():
    anthon_age = 21
    beth_age = anthon_age + 6
    chen_age = beth_age + 20
    drew_age = chen_age + anthon_age
    ethan_age = chen_age

    print(f"""
          Anthon is : {anthon_age}
          Beth is : {beth_age}
          Chen is : {chen_age}
          Drew is : {drew_age}
          Ethan is : {ethan_age}
    """)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
