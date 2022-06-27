beverages = ["beer", "wine", "vodka", "lemonade", "milk", "pilk", "juice", "oil", "coffee"]
beverage_name = 1

print("Hello, here's our menu. What would you like to drink?")
while True:
    for (i, item) in enumerate(beverages, start=1):
        print(str(i) + ". " + item)
    print("0. nothing for me today, thanks.")

    choice = int(input())
    if choice != 0:
        if choice <= int(len(beverages)):
            print("Alright, {} coming right up.\nAnything else?".format(beverages[choice-1]))
        else:
            print("Sorry, I don't think we have that.\nAnything else?")

    else:
        print("Okay then, good bye!")
        break