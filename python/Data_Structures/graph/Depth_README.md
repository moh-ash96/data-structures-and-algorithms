# Challenge Summary

The Challenge is to implement a depth-first traversal on a graph.

## Whiteboard Process

![breadth](/Assets/depth_graph.png)

## Approach & Efficiency

### The approach used was

I used a traversal method, get_nodes, and get_neighbors

### Big O of N

* Time: O(V + E)
* Space: O(V)

## Solution

The function takes the first node of an input graph, adds it to the output list, then goes to its neighbor, then the neighbor of the neighbor, and so on, using recursion pushing each of them to the output list, so the list will be returned in it's depth-first order.
