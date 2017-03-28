"""
The main program Python file
"""

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
    #   - Inputing inventory
    #   - Adding Recipes
    #   - Finding recipes from inventory

def run():
    """The main function of the program
    """
    userinput = input("HUH?: ")
    while userinput != "exit":
        handleinput(userinput)

if __name__ == "__main__":
    run()
