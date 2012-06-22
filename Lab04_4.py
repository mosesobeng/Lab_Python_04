##The Dictionary of stocked items with the item name as its key, and another dictionary of
##prices with the respective store and the corresponding price at the store.

def binary_insert(new_float,some_list_of_floats):
    
    low = 0
    high = len (some_list_of_floats) - 1
    while low <= high:
        mid = (low+high) / 2
	
  	  
        item = some_list_of_floats[mid]
        if new_float < item: 
            high = mid -1
        elif new_float > item:
            low = mid + 1
         
        else:
            break
    
        some_list_of_floats.insert(mid, new_float)
    
        return some_list_of_floats


def min_cost(grocery_list,item_to_price_list_dict):

    min_cost = 0
    for item in grocery_list:
        min_cost += min(item_to_price_list_dict[item])
    return min_cost
    

