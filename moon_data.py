# The purpose for this is to make a much easier way for future updating.
# Having a spreadsheet like this makes for easy updating of values.
# It also makes it much more possible to add in v49 where many high quota runs still take place.


import pandas as pd

# locations of information for each moon in Excel files + the possible scrap amounts
experimentation_rows = [2, 25]
experimentation_scrapamounts = [8, 11]

assurance_rows = [27, 61]
assurance_scrapamounts = [13, 15]

vow_rows = [63, 96]
vow_scrapamounts = [12, 14]

offense_rows = [98, 122]
offense_scrapamounts = [14, 17]

march_rows = [124, 148]
march_scrapamounts = [13, 16]

adamance_rows = [150, 183]
adamance_scrapamounts = [16, 18]

rend_rows = [185, 220]
rend_scrapamounts = [18, 25]

dine_rows = [222, 259]
dine_scrapamounts = [22, 25]

titan_rows = [261, 295]
titan_scrapamounts = [28, 31]

embrion_rows = [297, 319]
embrion_scrapamounts = [11, 15]

artifice_rows = [321, 358]
artifice_scrapamounts = [31, 37]


# creates list to actually be used
def create_moon_lists(start_row, end_row, moon_scrapamounts, version):

    # lists to store info
    moon_items = []
    moon_chances = []
    moon_values = {}

    # reads Excel file for each column of information
    moon_items_names = pd.read_excel('lethalcompany_scrap_table.xlsx', sheet_name=version, usecols='A')
    moon_items_chances = pd.read_excel('lethalcompany_scrap_table.xlsx', sheet_name=version, usecols='B')
    total_items_names = pd.read_excel('lethalcompany_scrap_table.xlsx', sheet_name=version, usecols='F')
    total_items_value = pd.read_excel('lethalcompany_scrap_table.xlsx', sheet_name=version, usecols='I')

    #  gives the names of items on moons
    for i in range(start_row, end_row):
        x = moon_items_names.values[i]
        moon_items.append(x[0])

    # gives the chances for each item
    for i in range(start_row, end_row):
        x = moon_items_chances.values[i]
        moon_chances.append(x[0])

    # gives the values for every possible item across all moons
    for i in range(1, 55):
        x = total_items_names.values[i]
        y = total_items_value.values[i]
        moon_values[x[0]] = y[0]

    # sends all information back to get_moon function
    return [moon_items, moon_chances, moon_scrapamounts, moon_values]


# function called in calculate_scrap_average.py
def get_moon(moon, version):

    # if statements send the location of data in Excel file sheet + scrap amounts and the version
    # future versions may be possible, but the data is not nearly as available. Would also require reworking
    if moon == "exp":
        return create_moon_lists(experimentation_rows[0], experimentation_rows[1], experimentation_scrapamounts, version)
    elif moon == "ass":
        return create_moon_lists(assurance_rows[0], assurance_rows[1], assurance_scrapamounts, version)
    elif moon == "vow":
        return create_moon_lists(vow_rows[0], vow_rows[1], vow_scrapamounts, version)
    elif moon == "off":
        return create_moon_lists(offense_rows[0], offense_rows[1], offense_scrapamounts, version)
    elif moon == "mar":
        return create_moon_lists(march_rows[0], march_rows[1], march_scrapamounts, version)
    elif moon == "ada":
        return create_moon_lists(adamance_rows[0], adamance_rows[1], adamance_scrapamounts, version)
    elif moon == "ren":
        return create_moon_lists(rend_rows[0], rend_rows[1], rend_scrapamounts, version)
    elif moon == "din":
        return create_moon_lists(dine_rows[0], dine_rows[1], dine_scrapamounts, version)
    elif moon == "tit":
        return create_moon_lists(titan_rows[0], titan_rows[1], titan_scrapamounts, version)
    elif moon == "emb":
        return create_moon_lists(embrion_rows[0], embrion_rows[1], embrion_scrapamounts, version)
    elif moon == "art":
        return create_moon_lists(artifice_rows[0], artifice_rows[1], artifice_scrapamounts, version)






