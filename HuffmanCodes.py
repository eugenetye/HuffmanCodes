class Node:
    # constructor for Node class
	def __init__(self, freq, letter, left=None, right=None):
		
        # frequency of letter
		self.freq = freq

		# name of letter 
		self.letter = letter

		# the node on the left of current node
		self.left = left

		# the node on the right of current node
		self.right = right

		# direction of tree 
		self.direction = ''

# function to build a Huffman tree
def buildTree():
    # dictionary to store letters and its corresponding frequencies
    letters_dict = {'A':77,'B':17,'C':32,'D':42,'E':120,'F':24,'G':17,'H':50,'I':76,'J':4,'K':7,'L':42,
    'M':24,'N':67,'O':67,'P':20,'Q':5,'R':59,'S':67,'T':85,'U':37,'V':12,'W':22,'X':4,'Y':22,'Z':2}

    # create Huffman tree nodes for each letter
    # and store them in an empty list 
    nodes = []
    for key in letters_dict:
        nodes.append(Node(letters_dict[key],key))

    # repeat process until the heap only contains the root node
    while len(nodes) > 1:
        # sort all the nodes in ascending order based on their frequencies
        nodes = sorted(nodes, key=lambda x: x.freq)

        # choose the 2 nodes with the minimum frequency in the min heap
        left = nodes[0]
        right = nodes[1]

        # set value to these nodes according to the direction, 
        # 0 for left and 1 for right
        left.direction = 0
        right.direction = 1

        # merge the 2 chosen nodes to create new node as their parent
        newNode = Node(left.freq + right.freq, left.letter + right.letter, left, right)

        # remove the 2 merged nodes, add the newly formed node then compare with 
        # other remaining nodes in the list
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
 
    return nodes

#function to traverse Huffman tree and assign codes to letters
def HuffmanCode(node,code = ''):
	# Huffman code for current node
	newCode = code + str(node.direction)
    
	# if its left node, call function again with left node
	if node.left:
		HuffmanCode(node.left, newCode)

    # if its right node, call function again with right node
	if node.right:
		HuffmanCode(node.right, newCode)

	# store the letter, its corresponding frequency, Huffman Code, length of each node, 
    # and product of length and frequency in global list if leaf node is reached
	if not node.left and not node.right:
		lst.append([node.letter,node.freq,newCode,len(newCode), node.freq * len(newCode)])


# global list used in HuffmanCode function to store letters 
# and its corresponding frequencies and Huffman codes 
lst = []

def main():
    nodes = buildTree()
    print('Letter | Frequency | Code | Length | Freq X Len')
    print('-------  ---------  ------- ------- ------------')
    HuffmanCode(nodes[0])
     
    # counter for weighted minimum path length
    counter = 0

    # print the output in alphabetical order
    for x, y, z, a, b in sorted(lst):
        print(f"   {x} {y:10}      {z:9} {a} {b:10}")
        counter += b
    
    print()
    print(f"The weighted mininum path length is: {counter}")
 
 # call the main function
if __name__ == "__main__":
    main()




 