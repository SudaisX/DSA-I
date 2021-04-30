from pprint import pprint

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

def get_connections(network, user):
    if user in network:
	    return network[user][0]
    return None

def get_countries_traveled(network, user):
    if user in network:
        return network[user][1]
    return None

def add_connection(network, user_A, user_B):
    if user_B not in network or user_A not in network:
        return None
    elif user_B not in network[user_A][0]: 
        network[user_A][0].append(user_B)
        return network
    elif user_B in network[user_A][0]:
        return network

def add_new_user(network, user, countries):
    if user not in network:
        network[user] = [[], countries]
        return network
    return network

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

def count_common_connections(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False

    common = []
    for connA in network[user_A][0]:
        for connB in network[user_B][0]:
            if connA == connB and connA not in common and connB not in common:
                common.append(connA)
    return len(common)


def find_path_to_patient(network, user_A, user_B):
	# your RECURSIVE solution here!
	return None



data = "Usama is connected to Saeed, Aaliya, Mohsin.Usama traveled to Italy, Japan, Korea.Saeed is connected to Sumaira, Zehra, Samar, Marium.Saeed traveled to China, Afghanistan.Marium is connected to Mohsin, Kashif, Saeed.Marium traveled to Japan, USA, Iran.Sumaira is connected to Usama, Zehra.Sumaira traveled to Japan, Saudi Arabia.Aaliya is connected to Mohsin, Bari, Sameera, Kashif.Aaliya traveled to India, USA, Malaysia.Mohsin is connected to Usama, Bari, Saeed.Mohsin traveled to Iran, Indonesia, Afghanistan.Bari is connected to Zehra, Usama, Mohsin.Bari traveled to Japan, India, China.Zehra is connected to Marium, Samar, Saeed.Zehra traveled to Russia, Malaysia, Italy.Sameera is connected to Bari, Usama, Samar, Kashif.Sameera traveled to Afghanistan, Korea, Russia.Kashif is connected to Zehra.Kashif traveled to Russia, Malaysia.Samar is connected to Sumaira, Usama, Aaliya.Samar traveled to Saudi Arabia, Indonesia, Iran."
network = create_data_structure(data)

pprint(network)
print()
# pprint(get_connections(network, 'Mohsin'))
# print()
# pprint(get_countries_traveled(network, 'Mohsin'))
# print()

pprint(count_common_connections(network, 'Mohsin', 'Usama'))