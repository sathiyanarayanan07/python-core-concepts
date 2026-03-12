items = [ "Wallet", "phone", "Water Bottle", "","Keys"]

for item in items:
    if item == "Water Bottle":
        print("Skipping water bottle..")
        continue

    if item == "Bomb":
        print("Danger! stopping scan!")
        break

    print(f"Scanning {items}")

