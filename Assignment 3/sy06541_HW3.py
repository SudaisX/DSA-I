from pprint import pprint

data = "Usama is connected to Saeed, Aaliya, Mohsin.Usama traveled to Italy, Japan, Korea.Saeed is connected to Sumaira, Zehra, Samar, Marium.Saeed traveled to China, Afghanistan.Marium is connected to Mohsin, Kashif, Saeed.Marium traveled to Japan, USA, Iran.Sumaira is connected to Usama, Zehra.Sumaira traveled to Japan, Saudi Arabia.Aaliya is connected to Mohsin, Bari, Sameera, Kashif.Aaliya traveled to India, USA, Malaysia.Mohsin is connected to Usama, Bari, Saeed.Mohsin traveled to Iran, Indonesia, Afghanistan.Bari is connected to Zehra, Usama, Mohsin.Bari traveled to Japan, India, China.Zehra is connected to Marium, Samar, Saeed.Zehra traveled to Russia, Malaysia, Italy.Sameera is connected to Bari, Usama, Samar, Kashif.Sameera traveled to Afghanistan, Korea, Russia.Kashif is connected to Zehra.Kashif traveled to Russia, Malaysia.Samar is connected to Sumaira, Usama, Aaliya.Samar traveled to Saudi Arabia, Indonesia, Iran."

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

pprint(create_data_structure(''))
