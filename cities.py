prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "


while True:
    city = input(prompt)

    if city .lower() == 'quit':
        break

    else:
        print(f"I would love to visit {city} one day!")

else:
    print("Thank you for sharing your travel experiences with me!")