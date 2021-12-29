import node
import linked_list
import restaurantData

# Loading the restaurant and food data to a linked list
def insert_food_type_to_linked_list():
    food_type_llist = linked_list.LinkedList()
    for type in restaurantData.types:
        food_type_llist.insert_beginning(type)
    return food_type_llist

insert_food_type_to_linked_list()