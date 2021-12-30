import node
import linked_list
import restaurantData

# Loading the food data to a linked list
def insert_food_type_to_linked_list():
    food_type_llist = linked_list.LinkedList()
    for type in restaurantData.types:
        food_type_llist.insert_beginning(type)
    return food_type_llist

food_type_linked_list = insert_food_type_to_linked_list()

# Loading the restaurant data to a linked list
def insert_resto_data_to_linked_list():
    resto_llist = linked_list.LinkedList()
    for type in restaurantData.types:
        resto_type_llist = linked_list.LinkedList()
        for resto in restaurantData.restaurant_data:
            if resto[0] == type:
                resto_type_llist.insert_beginning(resto)
        resto_llist.insert_beginning(resto_type_llist)
    return resto_llist


resto_data_linked_list = insert_resto_data_to_linked_list()
finish_status = False
# Asking for user input and listing all the types if requested
while not finish_status:
    user_input = input("Which cuisine do you want to eat. Just type your choice, or beginning letters of your preference. If you wish to see the whole list to help you decide, type in 'list': ").lower()
    while not user_input.isalpha():
        user_input = input("Uh oh! Looks like you typed in an invalid search request. Please try searching for something else.").lower()
    if user_input == "list":
        current_type_node = food_type_linked_list.get_head_node()
        while current_type_node:
            print(current_type_node.get_value())
            if current_type_node.get_next_node().get_value() is not None:
                current_type_node = current_type_node.get_next_node()
            else:
                user_input = input("Which cuisine do you want to choose? You can also enter initials: ").lower()
                break
    selection_made = False
    while not selection_made:
        selected_type = ""
        matching_types = []
        while not matching_types:
            current_type_node = food_type_linked_list.get_head_node()
            type_list_head_node = food_type_linked_list.get_head_node()
            while type_list_head_node is not None:
                if str(type_list_head_node.get_value()).startswith(user_input):
                    matching_types.append(type_list_head_node.get_value())
                type_list_head_node = type_list_head_node.get_next_node()

            for food in matching_types:
                print(food)

            if len(matching_types) == 0:
                user_input= input("Sorry there's been no match, please search a different keyword.")
            elif len(matching_types) == 1:
                confirmation_user_input= input(f"Are you sure you want to choose {matching_types[0]}, type in y for yes and n for no.").lower()
                while confirmation_user_input != "y" and confirmation_user_input != "n":
                    confirmation_user_input= input(f"Please type in y for yes and n for no.").lower()
                if confirmation_user_input == "y":
                    selected_type += matching_types[0]
                    selection_made = True
                else:
                    user_input = input("Which cuisine do you want to choose? You can also enter initials: ").lower()
            else:
                user_input = input(f"You have {len(matching_types)} matches. Please type in the name of the cuisine you want to eat.").lower()

    restaurant_head_node = resto_data_linked_list.get_head_node()
    while restaurant_head_node.get_next_node() is not None:
        resto_type_head = restaurant_head_node.get_value().get_head_node()
        if resto_type_head.get_value()[0] == selected_type:
            while resto_type_head.get_next_node() is not None:
                print(f"Name: {resto_type_head.get_value()[1]}")
                print(f"Price: {resto_type_head.get_value()[2]} / 5")
                print(f"Rating: {resto_type_head.get_value()[3]} / 5")
                print(f"Address: {resto_type_head.get_value()[4]}")
                print("")
                resto_type_head = resto_type_head.get_next_node()
        restaurant_head_node = restaurant_head_node.get_next_node()

    finish_confirmation = input("If you want to search again type in 'a', otherwise press enter to exit: ").lower()
    if finish_confirmation != "a":
        finish_status = True