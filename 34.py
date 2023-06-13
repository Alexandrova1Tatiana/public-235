def lyrics():
    if count > 1:
        print(f"{count} bottles of beer on the wall,")
        print("")
        print(f"{count} bottles of beer.")
        print("")
        print("Take one down, pass it around,")
        print("")
    else:
        print(f"{count} bottle of beer on the wall.")
        print("")
        print(f"{count} bottle of beer on the wall,")
        print("")
        print(f"{count} bottle of beer.")
        print("")
        print("Take it down, pass it around,")
        print("")
        print("No more bottles of beer on the wall.")


def bottles():
    global count
    while count > 1:
        lyrics()
        count = count - 1
        if count > 1:
            print(f"{count} bottles of beer on the wall.")
            print("")
        else:
            lyrics()


if __name__ == '__main__':
    count = 99
    bottles()