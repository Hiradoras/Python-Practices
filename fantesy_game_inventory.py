import string


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory : dict) -> string:
    print("Inventory:")
    for k,v in inventory.items():
        print('%i : %s\n' % (v, k))

print('Original Inventory: ')
displayInventory(inventory)



def addToInventory(inventory : dict, added_items : list):
    set_added_items = set(added_items)
    items = list(inventory.keys())
    for i in set_added_items:
        if i not in items:
            inventory[i] = added_items.count(i)
        else:
            inventory[i]+= added_items.count(i)
            


dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(inventory, dragon_loot)

print("New inventory")
displayInventory(inventory)