"""
The main program Python file
"""

from JSONparser import JSONParser

def handleinput(inp):
    """Handles the input passed from the user
    Args:
        inp(Str): The line input by the user
    """
    # General structure of each case of user input
    if inp == "something":
        pass
    # Needs a case for:
    #   - Listing drinks
    elif inp == "drinks" or inp == 'all drinks':
        #lists every drink available

    #   - Inputing inventory
    elif inp == "add":
        #add an ingredient
        #see if the user defined ingredient matches one of our database ingredients (aka one needed for a recipe)
        #if so, ask if the user means that, otherwise, add it as a new ingredient
        
        #update the list of makeable drinks by the user based on their current inventory
        
        pass
        
    #   - Adding Recipes
    elif inp == 'recipe':
        #adds a recipe
        #ask user for the name, ask for the first ingredient, as how much
        #if the ingredient is not one already that the code knows about (aka one needed or a recipe)
        #ask if there are extra ingredients due to the above block and suggest if the user means that, otherwise, add it as a new ingredient
        
        #continue asking for ingredients and for how much until the user exits
        #ask if there are any special mixing or serving instructions 
        
        pass
    #   - Finding recipes from inventory
    elif inp == "list":
        # go through the JSON file and make a global dictionary for the inventory?
        # Keep a list of the recipes we can make so we don't have to search the entire inventory every time
        pass
    else:
        #nonsense
        print("Wtf? I don't understand you.")
        pass

def run():
    """The main function of the program
    """
    userinput = input("HUH?: ").strip().lower()
    while userinput != "exit":
        handleinput(userinput)

if __name__ == "__main__":
    test = JSONParser("JSON/recipies.JSON")
    if 'recipies' in test.getdata():
        print(test.getdata()['recipies'])
    run()