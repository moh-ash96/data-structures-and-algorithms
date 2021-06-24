# Graphs

A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

## Challenge

The challenge was to create an adjacent list, which is the most common way to represent graphs and it is a collection of linked lists or array that lists all of the other vertices that are connected. It makes it easy to view if one vertices connects to another.

## Approach & Efficiency

### Approach

Each node is stored in a different linked list and each linked list is sorted in the adjacency list array.
Each node has a value and edges.
Edges represent the relation between nodes

### Efficiency

* Time: O(N)
* Space: O(N)

## API

The function:

* Adds a node.
* Adds an edge.
* Gets all the nodes.
* Gets the neighbors of an input node.
* Gets the size of the graph.
