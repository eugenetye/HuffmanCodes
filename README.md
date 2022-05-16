# Huffman Codes
This is a Python program that implements the Huffman Codes algorithm.

## Project Specification

A Huffman code uses different numbers of bits to encode the letters: more bits for rare letters, and fewer bits for common letters. The Huffman codes are determined using the English alphabet and frequencies provided below:


![Screen Shot 2022-05-16 at 1 55 26 PM](https://user-images.githubusercontent.com/105037989/168668400-87e02d4b-ae1a-428c-a134-7674d32c764c.png)

Huffman coding assigns codes to characters such that the length of the code depends on the relative frequency or weight of the corresponding character. Huffman codes are of variable-length, and prefix-free (no code is prefix of any other). Any prefix-free binary code can be visualized as a binary tree with the encoded characters stored at the leaves. This is called a Huffman tree, a full binary tree in which each leaf of the tree corresponds to a letter in the given alphabet. It is also the binary tree with weighted minimum path length, which is obtained by summing up the product of the length of each letter’s frequency and the length of each code. 

