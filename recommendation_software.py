import node
import linked_list
import restaurantData

# Loading the food data to a linked list
def insert_food_type_to_linked_list():
    food_type_llist = linked_list.LinkedList()
    for type in restaurantData.types:
        food_type_llist.insert_beginning(type)
    return food_type_llist

insert_food_type_to_linked_list()

# Loading the restaurant data to a linked list
def insert_resto_data_to_linked_list():
    resto_llist = linked_list.LinkedList()
    for type in restaurantData.types:
        resto_type_llist = linked_list.LinkedList()
        for resto in restaurantData.restaurant_data:
            if resto[0] == type:
                resto_type_llist.insert_beginning(resto)
        resto_llist.insert_beginning(resto_type_llist)
        resto_type_llist.insert_beginning(resto)
    return resto_type_llist

insert_resto_data_to_linked_list()