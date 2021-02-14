class Node:
    def __init__(self, name):
        self.name = name
        self.connections = {}

    def add_connection(self, connection, distance):
        self.connections[connection] = distance


class Graph:
    def __init__(self):
        self.cities = {}

    def add_node(self, node):
        new_node = Node(node)
        self.cities[node] = new_node
        return new_node

    def add_path(self, origin, destination, length):
        if origin not in self.cities:
            self.add_node(origin)
        if destination not in self.cities:
            self.add_node(destination)
        self.cities[origin].add_connection(destination, length)
        self.cities[destination].add_connection(origin, length)


"""
from node import Node
import copy
class Graph:
    #Global Variables
    cities = {}
    file_name = ""
    origin_city = ""
    destination_city = ""

    def __init__(self, file_name, origin_city, destination_city):
        self.file_name = file_name
        self.origin_city = origin_city
        self.destination_city = destination_city

    def createGraph(self):
        f = open(self.file_name, "r")
        f_lines = f.readlines()

        for i in f_lines:
            s = i.split()
            if s[0] == "END":
                break
            if s[0] not in self.cities:
                self.cities[s[0]] = Node(s[0])
            if s[1] not in self.cities:
                self.cities[s[1]] = Node(s[1])
            self.cities[s[0]].addConnection(s[1], int(s[2]))
            self.cities[s[1]].addConnection(s[0], int(s[2]))

    def output(self, distance, route):
        if distance == -1:
            print("distance: infinity")
        else:
            print("distance: %d km" % distance)
        print("route:")
        if len(route) == 0:
            print("none")
        else:
            for i in route:
                print(i)
"""
