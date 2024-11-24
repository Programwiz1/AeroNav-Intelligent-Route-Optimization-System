import random
import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt 
from itertools import combinations


#list of twenty cities 
def merge_sort(lst, n):
    if n > 1:
        mid = n // 2  # Find the middle of the list
        left_half = lst[:mid]  # Divide the list elements into two halves
        right_half = lst[mid:]

        # Recursively sort both halves
        merge_sort(left_half, len(left_half))
        merge_sort(right_half, len(right_half))

        i = j = k = 0

        # Copy data to temp lists left_half and right_half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left in left_half
        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1

        # Check if any element was left in right_half
        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1
    
    return lst



def main():
    locations = {1: "Abha", 2: "Acre", 3: "Aden", 4: "Agra", 5: "Baku", 6: "Cali", 7: "Dili", 8: "Erie", 9: "Faro", 
             10: "Giza", 11: "Hama", 12: "Iona", 13: "Java", 14: "Kiev", 15: "Lima", 16: "Myra", 17: "Nara", 
             18: "Oran", 19: "Pula", 20: "Riva"}

    totalcites = int(input("Please enter the number of random cities to be displayed. Number should be between 2 and 20: "))
    randomnums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    randomcities = []
    
    #populating randomcities with cites from location 
    for i in range(0,totalcites):
        select_randomnum = random.choice(randomnums)
        k = 0
        while (randomnums[k] != select_randomnum):
            k+=1
        randomcities.append(locations[select_randomnum])
        randomnums.pop(k)
    print("Here is the list of random cites: ", randomcities)
    
    
    starting_city = input("Please input the name of the starting city: ")
    
    while starting_city not in randomcities:
        starting_city = input("Please input the name of the starting city again: ")

    ending_city = input("Please input the name of the second city from the list: ")
    
    while ending_city not in randomcities:
        ending_city = input("Please input the name of the second city from the list again: ")
    

    #creates G as object of type nx.Graph
    G = nx.Graph()
    for names in range(0,totalcites): #to populate the nodes 
        G.add_node(randomcities[names])
    
    #Randomly connecting cities through creating an undirected graph 
    connected_nodes = set()
    remaining_nodes = set(randomcities)
    
    random_node = remaining_nodes.pop()
    connected_nodes.add(random_node)
    
    while remaining_nodes:
        random_node = remaining_nodes.pop()
        connection_node = random.choice(list(connected_nodes))
        G.add_edge(random_node,connection_node, cost = random.randint(1,100))
        connected_nodes.add(random_node)
    
    additional_edge_probability = 0.2
    
    possible_edges = list(combinations(randomcities,2))
        
    for connection1,connection2 in possible_edges:
        exisiting_edges = list(G.edges())
        if (connection1, connection2) and (connection2,connection1) not in exisiting_edges:
            if random.random() < additional_edge_probability:
                G.add_edge(connection1,connection2, cost = random.randint(1,100))
    
    
    plt.figure(figsize=(15, 10))
    
    pos = nx.circular_layout(G) #circular arragement of nodes minimzes cluttering 
    node_colors = []
    for node in G.nodes():
        if node == starting_city or node == ending_city:
            node_colors.append('green')
        else:
            node_colors.append('orange')
    
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1500)
        
    #MINIMUM path
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1500)
    path1 = nx.shortest_path(G, source=starting_city, target=ending_city, weight='cost') #implements dijkstra's algorithm to get the shorted path
    # Extracting the edge labels (weights)
    connecting_costs = nx.get_edge_attributes(G, 'cost')
    edge_colors1 = []
    for u, v in G.edges():
        if (u, v) in zip(path1, path1[1:]) or (v, u) in zip(path1, path1[1:]):
            edge_colors1.append('red')
        else:
            edge_colors1.append('black')

    nx.draw_networkx_edges(G, pos, edgelist=list(G.edges()), edge_color=edge_colors1, width=2)
    # Drawing the edge labels on the graph
    nx.draw_networkx_edge_labels(G, pos, edge_labels=connecting_costs, label_pos=0.5, font_size=9, font_color='purple')    
    plt.margins(0.1)
    plt.axis('off')  # Turn off the axis for a cleaner look
    plt.show()    
        
        
    # MAXIMUM COST Brute-force find the path with maximum total cost
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1500)
    all_paths = list(nx.all_simple_paths(G, source=starting_city, target=ending_city))
    max_cost = -1
    best_path = None
        
    for path in all_paths:
        total_cost = sum(G[u][v]['cost'] for u, v in zip(path, path[1:]))
        if total_cost > max_cost:
            max_cost = total_cost
            best_path = path
        
    path = best_path
     
    connecting_costs = nx.get_edge_attributes(G, 'cost')
    edge_colors = []
    for u, v in G.edges():
        if (u, v) in zip(path, path[1:]) or (v, u) in zip(path, path[1:]):
            edge_colors.append('red')
        else:
            edge_colors.append('black')
    
    nx.draw_networkx_edges(G, pos, edgelist=list(G.edges()), edge_color=edge_colors, width=2)

    # Drawing the edge labels on the graph
    nx.draw_networkx_edge_labels(G, pos, edge_labels=connecting_costs, label_pos=0.5, font_size=9, font_color='purple')
    plt.margins(0.1)
    plt.axis('off')  # Turn off the axis for a cleaner look
    plt.show()    

    
    possible_destinations = randomcities
    possible_destinations.remove(starting_city)
    
    # Printing the Cheapest prices
    cheap_prices = {}
    cheap_prices_lst = []
    for city in possible_destinations:
        calc_path = nx.shortest_path(G, source=starting_city, target=city, weight='cost')
        total_cost_path = sum(G[u][v]['cost'] for u, v in zip(calc_path, calc_path[1:]))
        cheap_prices[city] = total_cost_path
        cheap_prices_lst.append(total_cost_path)

    sorted_cheap_prices_lst = merge_sort(cheap_prices_lst, len(cheap_prices_lst))
    print("Cost Efficient: ")
    printed_cities = set()  # Track cities that have already been printed
    for cost in sorted_cheap_prices_lst:
        for city, price in cheap_prices.items():
            if price == cost and city not in printed_cities:
                print(f"{city}: {cost}")
                printed_cities.add(city)  # Mark the city as printed

    # Printing the Luxurious Prices
    luxurious_prices = {}
    luxurious_prices_lst = []

    for city in possible_destinations:
        all_paths = list(nx.all_simple_paths(G, source=starting_city, target=city))
        max_cost = -1
        best_path = None
    
        for path in all_paths:
            total_cost_path = sum(G[u][v]['cost'] for u, v in zip(path, path[1:]))
            if total_cost_path > max_cost:
                max_cost = total_cost_path
                best_path = path
    
        luxurious_prices[city] = max_cost
        luxurious_prices_lst.append(max_cost)

    sorted_luxurious_prices_lst = merge_sort(luxurious_prices_lst, len(luxurious_prices_lst))
    sorted_luxurious_prices_lst.reverse()  # For descending order

    print("Luxury: ")
    printed_cities = set()  # Track cities that have already been printed
    for cost in sorted_luxurious_prices_lst:
        for city, price in luxurious_prices.items():
            if price == cost and city not in printed_cities:
                print(f"{city}: {cost}")
                printed_cities.add(city)  # Mark the city as printed
    

        
main()

