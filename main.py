# Created by Daniel Sanchez
# CSCI 404 - Project 1: Uninformed Search
# Due February 18, 2021

import sys
import copy
from graph import Graph


# Checks for proper number of arguments. Returns array of arguments
def handleArgs():
    if len(sys.argv) != 4:
        sys.exit("Incorrect number of arguments")
    return [sys.argv[1], sys.argv[2], sys.argv[3]]


# Converts text file input to a graph
def createGraph(f_name, origin, destination):
    f = open(f_name, "r")
    f_lines = f.readlines()

    g = Graph()
    for i in f_lines:
        if i == '\n':
            continue
        s = copy.deepcopy(i.split())
        if s[0] == "END":
            break
        g.add_path(s[0], s[1], s[2])
    g.getNode(origin)
    g.getNode(destination)
    return g


# Finds the options to explore with the minimum cost
def findMin(frontier):
    minKey = -1
    minVal = -1
    index = 0

    for i in frontier:
        key = list(i.keys())[0]
        val = i[key]
        if minVal == -1 or val < minVal:
            minVal = val
            minKey = index
        index += 1
    return minKey


# Takes in an array of solutions and formats it according to project requirements
def formatSolution(g, solution):
    output = []
    i = len(solution) - 1
    while i != 0:
        n = g.getNode(solution[i])
        d = g.getNode(solution[i - 1])
        c = n.getConnectionCost(d.getName())
        temp = n.getName() + " to " + d.getName() + ", " + str(c) + " km"
        output += [temp]
        i -= 1
    return output


# Given a graph, finds the optimal path between two nodes.
def findPaths(g, origin, destination):
    node = g.getNode(origin)
    cost = 0
    frontier = [{node: copy.deepcopy(cost)}]
    explored = set()
    while len(frontier) > 0:
        mk = frontier.pop(findMin(frontier))
        node = list(mk.keys())[0]
        cost = int(mk[node])
        if node.getName() == destination:
            return [cost, formatSolution(g, node.getPath())]
        explored.add(copy.deepcopy(node.getName()))
        for n in node.connections:
            n = copy.deepcopy(g.getNode(n))
            if copy.deepcopy(n.getName()) not in explored:
                frontier.append({n: cost + node.getConnectionCost(n.getName())})
                n.updatePath(copy.deepcopy(node.getPath()))
    return -1

def findPaths2(g, origin, destination):
    node = g.getNode(origin)
    cost = 0
    frontier = [{node: copy.deepcopy(cost)}]
    count = 0
    while len(frontier) > 0:
        mk = frontier.pop(findMin(frontier))
        node = list(mk.keys())[0]
        cost = int(mk[node])
        if node.getName() == destination:
            return [cost, formatSolution(g, node.getPath())]
        for n in node.connections:
            n = copy.deepcopy(g.getNode(n))
            frontier.append({n: cost + node.getConnectionCost(n.getName())})
            n.updatePath(copy.deepcopy(node.getPath()))
        if count == 10000:
            return -1
        else:
            count += 1

# Depending on the inputs, creates output in accordance with project requirements
def handleOutput(output, args):
    distance = ""
    route = []
    if output == -1:
        distance = "infinity"
        route = ["none"]
    elif output[0] == 0:
        distance = "0 km"
        route = [args[1] + " to " + args[2] + ", 0 km"]
    else:
        distance = str(output[0]) + " km"
        route = output[1]

    print("distance: %s" % distance)
    print("route:")
    for i in route:
        print(i)

# Main function
if __name__ == '__main__':
    args = handleArgs()
    op = findPaths2(createGraph(args[0], args[1], args[2]), args[1], args[2])
    handleOutput(op, args)