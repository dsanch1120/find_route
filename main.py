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

#Given an origin and destination, finds the optimal path between them.
def findPaths(g, origin, destination):
    node = g.getNode(origin)
    cost = 0
    frontier = [{node: copy.deepcopy(cost)}]

    while len(frontier) > 0:
        mk = frontier.pop(findMin(frontier))
        node = list(mk.keys())[0]
        cost = int(mk[node])
        if cost >= g.getDiameter():
            continue
        if node.getName() == destination:
            return [cost, formatSolution(g, node.getPath())]
        for n in node.connections:
            n = copy.deepcopy(g.getNode(n))
            replace = False
            for i in range(len(frontier)):
                name = list(frontier[i].keys())[0]
                c = int(frontier[i][name])
                if name.getName() == n.getName():
                    if c < node.getConnectionCost(n.getName()):
                        frontier.pop(i)
                        frontier.append({n: cost + node.getConnectionCost(n.getName())})
                        n.updatePath(copy.deepcopy(node.getPath()))
                        replace = True
                        break
                    replace = True
            if replace:
                continue
            frontier.append({n: cost + node.getConnectionCost(n.getName())})
            n.updatePath(copy.deepcopy(node.getPath()))
    return -1

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
    op = findPaths(createGraph(args[0], args[1], args[2]), args[1], args[2])
    handleOutput(op, args)