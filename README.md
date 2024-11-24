# AeroNav Pro: Intelligent Route Optimization System

## Overview
**AeroNav Pro** is a Python-based intelligent navigation system designed to optimize travel routes between randomly selected cities. It uses graph theory, advanced algorithms like Dijkstra’s, and interactive data visualization to provide users with the shortest and most luxurious travel paths. This system is a robust prototype for real-world applications in smart transportation, travel planning, and urban mobility solutions.

---

## Features
- **Dynamic City Selection**: Randomly generates city nodes from a predefined list, creating a unique navigation scenario every time.
- **Graph Representation**: Uses NetworkX to model city connections as a graph with nodes (cities) and weighted edges (travel costs).
- **Route Optimization**:
  - **Shortest Path Calculation**: Employs Dijkstra’s algorithm to find the most cost-efficient travel route.
  - **Most Luxurious Path**: Brute-force analysis to determine the path with the highest travel cost.
- **Interactive Visualization**: Uses Matplotlib to visually represent the city network, with color-coded nodes, edges, and labels for clarity.
- **Customizable and Scalable**: The system allows for expansion to include more cities, advanced cost metrics, and real-time data integration.
- **Sorting Algorithms**: Implements Merge Sort to rank cities by cost-efficiency and luxury, ensuring quick and accurate results.

---

## Technologies Used
1. **Python**: Core programming language for system logic, algorithms, and user interaction.
2. **NetworkX**: Graph processing library for creating, analyzing, and managing the city network.
3. **Matplotlib**: Visualization library for plotting graphs, routes, and edge weights dynamically.

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/username/aeronav-pro.git
   cd aeronav-pro
2. Install the required Python libraries:
   ```bash
   pip install matplotlib networkx numpy
3. Run the program:
   ```bash
   python aeronav_pro.py

---

## Usage
1. Enter the number of cities to include in the navigation system (between 2 and 20).
2. Select a starting city and an ending city from the generated list.
3. View:
   - **Shortest Path**: Optimal route based on the minimum travel cost.
   - **Most Luxurious Path**: Path with the highest travel cost.
4. Explore cost-efficient and luxurious city rankings.
5. Visualize the graph of cities and routes, with distinct color coding for clarity.

---

## Real-World Applications
- **Smart Transportation**: Optimize routes in urban mobility systems.
- **Travel Planning**: Assist travelers in identifying cost-effective or scenic travel options.
- **Supply Chain Optimization**: Model transportation networks for logistics and goods delivery.

---

## Future Enhancements 
- Integration of real-time traffic or cost data from APIs.
- AI-driven predictions for optimal travel paths.
- Support for multi-modal transportation networks (e.g., flights, trains, buses).
- Deployment as a web or mobile application for wider accessibility.

---

## Contributers
Programmers: Monil Patel  
For inquiries, email: monilp12340@gmail.com 

