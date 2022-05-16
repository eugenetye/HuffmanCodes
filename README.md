# Huffman Codes
This is a Python program that implements the Huffman Codes algorithm.

## Project Specification

A Huffman code uses different numbers of bits to encode the letters: more bits for rare letters, and fewer bits for common letters. The Huffman codes are determined using the English alphabet and frequencies provided below:


![Screen Shot 2022-05-16 at 1 55 26 PM](https://user-images.githubusercontent.com/105037989/168668400-87e02d4b-ae1a-428c-a134-7674d32c764c.png)

Huffman coding assigns codes to characters such that the length of the code depends on the relative frequency or weight of the corresponding character. Huffman codes are of variable-length, and prefix-free (no code is prefix of any other). Any prefix-free binary code can be visualized as a binary tree with the encoded characters stored at the leaves. This is called a **Huffman tree**, a full binary tree in which each leaf of the tree corresponds to a letter in the given alphabet. It is also the binary tree with *weighted minimum path length*, which is obtained by summing up the product of the length of each letter’s frequency and the length of each code. 

There are mainly two major parts in this program:
1. Building a Huffman tree from input characters
2. Traverse the Huffman tree and assign codes to characters

Steps to build a Huffman tree:
1. Create a leaf node for each unique character and build a min heap of all leaf nodes (Min Heap is used as a priority queue. The value of frequency field is used to compare two nodes in min heap. Initially, the least frequent character is at root).
2. Extract two nodes with the minimum frequency from the min heap.
3. Create a new internal node with a frequency equal to the sum of the two nodes' frequencies. Make the first extracted node as its left child and the other extracted node as its right child. Add this node to the min heap.
4. Repeat Steps 2 and 3 until the heap contains only one node. The remaining node is the root node and the tree is complete.

To print codes from Huffman tree:
1. Traverse the tree formed starting from the root. 
2. While moving to the left child, write 0 to the string. While moving to the right child, write 1 to the string. 
3. Print the string when a leaf node is encountered.

## Example Output
<img width="385" alt="Screen Shot 2022-05-16 at 4 10 20 PM" src="https://user-images.githubusercontent.com/105037989/168674336-1fa95b96-653a-4e1d-a514-abef1669e11d.png">




