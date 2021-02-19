# Created by Daniel Sanchez
# CSCI 404 - Project 1: Uninformed Search
# Due February 18, 2021

import copy

# Node class of node objects that will make up the graph.
# Global Variables:
#   Name:   Name of node object (in the case of input1, the name of a city)
#   Connections:    A dictionary of "connections", which are edges between nodes.
#                   The key is a Node object, the value is the distance between nodes
#   Path:   An array that will be updated as each node is visited. 
#           When the goal node is reached, the path containing the shortest path will be output.
class Node:
    # Initializes variables
    def __init__(self, name):
        self.name = name
        self.connections = {}
        self.path = [name]

    # Used for building the graph. Adds an edge between this node object and another node object.
    def add_connection(self, connection, distance):
        self.connections[connection] = distance

    # Returns the name of the node object
    def getName(self):
        return self.name

    # Gets the connection cost between this node and any other given node (assuming it exists as a connection)
    def getConnectionCost(self, destination):
        return int(self.connections[destination])

    # Updates the path when this node object is visited.
    def updatePath(self, destination):
        self.path += copy.deepcopy(destination)

    # Returns the path of the node object
    def getPath(self):
        return self.path


# Graph class, consisting of node objects and methods to traverse the nodes.
# Global Variables:
#   Cities:     A dictionary {key - String representing city: value - Node object that corresponds to key}
class Graph:
    # Initiates global variables
    def __init__(self):
        self.cities = {}
        self.diameter = 0
    
    # Adds a node object to the graph
    def add_node(self, node):
        new_node = Node(node)
        self.cities[node] = new_node
        return new_node

    # Creates paths between two nodes
    def add_path(self, origin, destination, length):
        if origin not in self.cities:
            self.add_node(origin)
        if destination not in self.cities:
            self.add_node(destination)
        self.cities[origin].add_connection(destination, length)
        self.cities[destination].add_connection(origin, length)
        self.diameter += int(length)

    # Returns a specific node given it's name
    def getNode(self, name):
        if name in self.cities:
            return self.cities[name]
        else:
            exit("Incorrect input")

    def getDiameter(self):
        return self.diameter

