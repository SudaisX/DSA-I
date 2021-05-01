#
# CS 102 (Data Structures & Algorithms)
#   Assignment 03 (Total points: 100)
#
# ---------------------------------------- #
# COVID-19 Patients' Contact Network       #
# ---------------------------------------- #
#
# Background
# ==========
# You and your friend have decided to start a  project to analyze COVID-19
# patients' contact network. Your friend will handle the website creation (they know
# what they are doing, having experience in Web development). However, it is
# up to you to create a data structure that manages the patients' contact network information
# and to implement several procedures that operate on the network.
#
# On a website, data is stored in a database. In your case, however, all
# information comes in a long string of text. Each pair of sentences in the text
# is formatted as follows: 
# 
# <user> is connected to <user1>, ..., <userM>.<user> traveled to <country1>, ..., <countryN>.
#
# Here, each sentence shows the user meetings to other users and his/her travel history
#
# For example:
# 
# Usama is connected to Saeed, Aaliya, Mohsin.Usama traveled to Italy, Japan, Korea.
# 
# Note that each sentence will be separated from the next by only a period (dot). There will
# not be a whitespace or new lines between sentences.
# 
# Your friend records the information in that string based on user activity on 
# the Website and passes it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the various data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g., lists of dictionaries). Choose one that
# will allow you to manage the data above and implement the procedures below. 
# 
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'Usama' in the network. Furthermore, connections are asymmetric
# - if 'Jawad' is connected to 'Babar', it does not necessarily mean that 'Babar' is
# connected to 'Jawad'.
#
# Assignment Description
# ====================---
# Your task is to complete the procedures according to the specifications below. You are encouraged 
# to define any additional helper function/procedure(s) that might assist you in accomplishing
# a task. You are encouraged to test your code using print statements with different
# data samples. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
example_input="Usama is connected to Saeed, Aaliya, Mohsin.Usama traveled to Italy, Japan, Korea.Saeed is connected to Sumaira, Zehra, Samar, Marium.Saeed traveled to China, Afghanistan.Marium is connected to Mohsin, Kashif, Saeed.Marium traveled to Japan, USA, Iran.Sumaira is connected to Usama, Zehra.Sumaira traveled to Japan, Saudi Arabia.Aaliya is connected to Mohsin, Bari, Sameera, Kashif.Aaliya traveled to India, USA, Malaysia.Mohsin is connected to Usama, Bari, Saeed.Mohsin traveled to Iran, Indonesia, Afghanistan.Bari is connected to Zehra, Usama, Mohsin.Bari traveled to Japan, India, China.Zehra is connected to Marium, Samar, Saeed.Zehra traveled to Russia, Malaysia, Italy.Sameera is connected to Bari, Usama, Samar, Kashif.Sameera traveled to Afghanistan, Korea, Russia.Kashif is connected to Zehra.Kashif traveled to Russia, Malaysia.Samar is connected to Sumaira, Usama, Aaliya.Samar traveled to Saudi Arabia, Indonesia, Iran."

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): [20 Points]
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the information on
#   connections and countries traveled for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A traveled to X, Y, Z.C is connected to A.C traveled to X."
#   as a test case for create_data_structure because the string does not 
#   lists B's connections or traveled countries.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return an empty data structure ('network').
# 
# Return:
#   The newly created network data structure
def create_data_structure(string_input):
    data = string_input.split('.')

    connections = [data[i] for i in range(0, len(data), 2)]
    traveled = [data[i] for i in range(1, len(data), 2)]

    connections = [connection.split(' is connected to ') for connection in connections]
    traveled = [country.split(' traveled to ') for country in traveled]

    network = {}
    for i in range(len(connections)):
        for j in range(1, len(connections[i])):
            network[connections[i][0]] = [connections[i][j].split(', '), traveled[i][j].split(', ')]
    return network

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is a 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from the 'network'.        #
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): [05 Points]
#   Returns a list of all the connections that the user has
#
# Arguments: 
#   network: the patients network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.
def get_connections(network, user):
    if user in network:
	    return network[user][0]
    return None

# ----------------------------------------------------------------------------- 
# get_countries_traveled(network, user): [05 Points]
#   Returns a list of all the countries a user traveled.
#
# Arguments: 
#   network: the patients' network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all countries the user traveled.
#   - If the user traveled no countries, return an empty list.
#   - If the user is not in network, return None.
def get_countries_traveled(network, user):
    if user in network:
        return network[user][1]
    return None

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): [05 Points]
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the patients network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, the network remains unchanged.
#   - If user_A or user_B is not in network, return None.
def add_connection(network, user_A, user_B):
    if user_B not in network or user_A not in network:
        return None
    elif user_B not in network[user_A][0]: 
        network[user_A][0].append(user_B)
        return network
    elif user_B in network[user_A][0]:
        return network

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, countries): [05 Points]
#   Creates a new user profile and adds that user to the network, along with
#   any country traveled specified in countries. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the patients network data structure
#   user:    a string containing the name of the user to be added to the network
#   countries:   a list of strings containing the user's traveled countries, e.g.,
#		     ['Indonesia', 'Afghanistan', 'Korea']
#
# Return: 
#   The updated network with the new user and countries traveled added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's traveled countries)

def add_new_user(network, user, countries):
    if user not in network:
        network[user] = [[], countries]
        return network
    return network
		
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): [15 Points]
#   Finds all the secondary connections (i.e., connections of connections) of a
#   given user.
# 
# Arguments: 
#   network: the patients network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# Note: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.

def get_secondary_connections(network, user):
    if user not in network:
        return None
    if network[user][0] == []:
        return []

    secondary_connections = []
    for connection in network[user][0]:
        if connection not in secondary_connections:
            secondary_connections.append(connection)
    return secondary_connections

# ----------------------------------------------------------------------------- 	
# count_common_connections(network, user_A, user_B): [10 Points]
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the patients network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return:
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.

def count_common_connections(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False

    common = []
    for connA in network[user_A][0]:
        for connB in network[user_B][0]:
            if connA == connB and connA not in common and connB not in common:
                common.append(connA)
    return len(common)

# ----------------------------------------------------------------------------- 
# find_path_to_patient(network, user_A, user_B): [15 Points]
#   Finds a path  from user_A to user_B. It has to be an existing
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print find_path_to_patient(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# N OTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.

def find_path_to_patient(network, user_A, user_B):
    def dfs_patient(network, user, visited=[]):
        if user not in visited:
            visited.append(user)
            for i in network[user][0]:
                visited = dfs_patient(network, i, visited)
        return visited

    path = dfs_patient(network, user_A)
    path_to_patient = []
    for user in path:
        path_to_patient.append(user)
        if user == user_B: break

    return path_to_patient

# ----------------------------------------------------------------------------- 
# find_all_possible_paths_to_user(network, user_A, user_B):  [20 points]
#   Finds all possible path from user_A to user_B.
#  
# Arguments:
#   network: The network you created with create_data_structure.
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
#
# Return:
#   A nested list which contains sublist of possible paths from user_A to user_B.
#   - If there exists no path in between the two users, the function will return an empty list.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> find_all_possible_paths_to_user(network, "Abe", "Zed")
#   >>> [['Abe', 'Zed'], ['Abe', 'Tom', 'Zed'], ['Abe', 'Gel', 'Sam', 'Zed']]
#

def find_all_possible_paths_to_user(network, user_A, user_B, path=[]):
    if user_A not in network:
        return []

    path = path + [user_A]
    if user_A == user_B:
        return [path]

    paths = []
    for user in network[user_A][0]:
        if user not in path:
            newpaths = find_all_possible_paths_to_user(network, user, user_B, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths  

from pprint import pprint

net = create_data_structure(example_input)
print(net)
print(get_connections(net, "Aaliya"))
print(get_connections(net, "Marium"))
print(get_countries_traveled(net, "Usama"))
print(add_connection(net, "Usama", "Samar"))
print(add_new_user(net, "Aaliya", []))
print(add_new_user(net, "Nick", ["India", "Italy"])) # True
print(get_secondary_connections(net, "Marium"))
print(count_common_connections(net, "Marium", "Usama"))
print(find_path_to_patient(net, "Usama", "Zehra"))
print(find_all_possible_paths_to_user(net, "Usama", "Zehra"))