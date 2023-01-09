item_list = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
}


def cat():
    try:
        item_name = input('item: ').lower().title().strip()
        if item_name in item_list:
            total = item_list[item_name]
            print('Total: ', "$","%.2f"% round(total, 2), sep='')
            return total
    except KeyError:
        pass
    except EOFError:
                print('\u2028')
                exit()
    

def main():
        x = cat()
        while True:
            try:
                item_name = input('item: ').lower().title().strip()
                if item_name in item_list:
                    total2 = item_list[item_name] + x
                    x = total2
                    print('Total: ', "$","%.2f"% round(x, 2), sep='')
            except KeyError:
                pass
            except EOFError:
                print('\u2028')
                exit()
            

main()