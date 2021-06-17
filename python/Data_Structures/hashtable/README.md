# Hashtables

Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.

## Challenge

The challenge was with collisions and implementing a linked list to solve them, also with testing internals.

## Approach & Efficiency

The approach used is to convert the key of the input into index and put the key value object in the hashtable, that contains a linked list for the collisions.

### Big O Notation

* Time: O(N)
* Space: O(1)

## API

* Create a hashtable.
* Insert key, value pair in the hashtable.
* Hash keys to determine is which index it should be added.
* Make a link_list to handle collisions.
* Retrieve the value of the bucket using its key.
* Determine if a specific key is inside the hashtable or not.
