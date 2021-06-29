# Challenge Summary

The Challenge is to implement a depth-first traversal on a graph.

## Whiteboard Process

![breadth](/Assets/depth_graph.png)

## Approach & Efficiency

### The approach used was

I used a traversal method, get_nodes, and get_neighbors

### Big O Notation

* Time: O(V + E)
* Space: O(V)

## Solution

### To return the preorder Depth-first of the graph nodes
* Use `graph.depth_first()` function
### To return the values of the graph in preorder depth in a list
* Declare an empty list
* loop over the nodes and push their values to the empty list.
* return the list

```python
def get_values(graph):
    values = []
    for node in graph.depth_first():
        values.append(node.value)
    return values
```
[Code file](graph.py)
