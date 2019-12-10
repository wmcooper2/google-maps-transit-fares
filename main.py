# load graph and tree
    # graph: collection of nodes with fare information
    # tree:  a fast way to check for fare existence

# get station names through user input
    # a list of names
    # check if they already exist
        # if in the tree, check the graph, else get from gui
        # if checking the graph, return the price


# manipulate the gui to get the directions 
    # pyautogui
    # googlemaps

# extract the fare from the image
    # pytesseract

# insert the fare into the gui
# add the station names to the tree if not there.

if __name__ == "__main__":
    from scrape import get_fares_from_google_maps as get_fares
    get_fares()
