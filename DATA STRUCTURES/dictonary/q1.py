dict = {"india" : "delhi","usa":"new York","england" : "london"}
def check(country):
    if country in dict:
        print(f"capital is : {dict[country]}")
    else:
        print("country not found")

c = input("Enter a country : ");
check(c)

