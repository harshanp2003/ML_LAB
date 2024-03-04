

# 1) Python Program to Left Rotate a NumPy Array by n:


# import numpy as np

# def left_rotate_array(arr, n):
#     return np.roll(arr, -n)

# # Example usage:
# array_to_rotate = np.array([1, 2, 3, 4, 5])
# n = 2
# result = left_rotate_array(array_to_rotate, n)
# print(result)


# 2) Python Program to Right Rotate a NumPy Array by n:

# python
# import numpy as np

# def right_rotate_array(arr, n):
#     return np.roll(arr, n)

# # Example usage:
# array_to_rotate = np.array([1, 2, 3, 4, 5])
# n = 2
# result = right_rotate_array(array_to_rotate, n)
# print(result)


# # 3) Python Program to Find Smallest Item in a Tuple:

# # python
# def find_smallest_in_tuple(tuple_data):
#     return min(tuple_data)

# # Example usage:
# my_tuple = (3, 1, 5, 2, 4)
# result = find_smallest_in_tuple(my_tuple)
# print(result)


# # 4) Python Program to Find Largest Item in a Tuple:

# # python
# def find_largest_in_tuple(tuple_data):
#     return max(tuple_data)

# # Example usage:
# my_tuple = (3, 1, 5, 2, 4)
# result = find_largest_in_tuple(my_tuple)
# print(result)


# 5) Python Program to Print Tuple Items:

# python
# def print_tuple_items(tuple_data):
#     for item in tuple_data:
#         print(item)

# # Example usage:
# my_tuple = (1, 2, 3, 4, 5)
# print_tuple_items(my_tuple)


# 6) Python Program to Find Tuple Length:

# python
# def tuple_length(tuple_data):
#     return len(tuple_data)

# # Example usage:
# my_tuple = (1, 2, 3, 4, 5)
# result = tuple_length(my_tuple)
# print(result)


# 7) Python Program to Convert List to String:

# python
# def list_to_string(my_list):
#     return ''.join(map(str, my_list))

# # Example usage:
# my_list = ['a', 'b', 'c', 'd']
# result = list_to_string(my_list)
# print(result)


# 8) Python Program to Convert List to Tuple:

# python
# def list_to_tuple(my_list):
#     return tuple(my_list)

# # Example usage:
# my_list = [1, 2, 3, 4, 5]
# result = list_to_tuple(my_list)
# print(result)


# 9) Python program to Count words in a String using Dictionary:

# python
# def count_words(string_data):
#     words = string_data.split()
#     word_count = {}
#     for word in words:
#         word_count[word] = word_count.get(word, 0) + 1
#     return word_count

# # Example usage:
# my_string = "This is a sample string. This string contains some words."
# result = count_words(my_string)
# print(result)


# 10) Implementation of linked list in python:

# python
# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" ")
#             current = current.next

# # Example usage:
# linked_list = LinkedList()
# linked_list.append(1)
# linked_list.append(2)
# linked_list.append(3)
# linked_list.display()


# 11) Implementation of array operation in python:

# python
# # Assuming you mean basic array operations, here's an example:
# my_array = [1, 2, 3, 4, 5]

# # Accessing elements
# print(my_array[0])  # Output: 1

# # Updating elements
# my_array[1] = 10

# # Deleting an element
# del my_array[2]

# # Finding the length
# array_length = len(my_array)
# print(array_length)


# 12) Implementation of binary search tree in python:

# python
# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key

# def insert(root, key):
#     if root is None:
#         return Node(key)
#     else:
#         if root.val < key:
#             root.right = insert(root.right, key)
#         else:
#             root.left = insert(root.left, key)
#     return root

# # Example usage:
# root = None
# keys = [50, 30, 20, 40, 70, 60, 80]

# for key in keys:
#     root = insert(root, key)


# 13) Implementation of graph traversal algorithm in python:

# ```python
from collections import defaultdict

class Graph:
    def _init_(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=' ')
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.DFS(neighbor, visited)

# Example usage:
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

print("Depth First Traversal (starting from vertex 2): ")
visited = [False] * (max(graph.graph) + 1)
graph.DFS(2)
