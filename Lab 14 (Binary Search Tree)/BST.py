class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    #Insert a node into BST
    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
        else:
            self.__insert(key, self.root)

    def __insert(self, key, curr):
        if key < curr.value:
            if curr.left:
                self.__insert(key, curr.left)
            else:
                curr.left = Node(key)

        elif key > curr.value:
            if curr.right:
                self.__insert(key, curr.right)
            else:
                curr.right = Node(key)

        elif key == curr.value:
            pass
        
    #Check if key exists in BST
    def exist(self, key):
        if self.root.value == key:
            return True
        else:
            return self.__exist(key, self.root)

    def __exist(self, key, curr):
        if key == curr.value:
            return True
        elif key < curr.value:
            if curr.left:
                return self.__exist(key, curr.left)
            else:
                return False
        elif key > curr.value:
            if curr.right:
                return self.__exist(key, curr.right)
            else:
                return False

    #Get tree height
    def height(self):
        if self.root == None: 
            return 0
        else:
            return self.__height(self.root)

    def __height(self, curr_node, curr_height=0):
        if curr_node == None:
            return curr_height
        left_height = self.__height(curr_node.left, curr_height + 1)
        right_height = self.__height(curr_node.right, curr_height + 1)
        print(left_height, right_height)
        return max(left_height, right_height)


    #Node with min value
    def minimum(self, key):
        return self.__minimum(key, self.root)

    def __minimum(self, key, curr):
        if key == curr.value:
            while curr.left != None:
                curr = curr.left
            return curr.value
        
        elif key < curr.value:
            if curr.left:
                return self.__minimum(key, curr.left)
        
        elif key > curr.value:
            if curr.right:
                return self.__minimum(key, curr.right)

    #Node with max value
    def maximum(self, key):
        return self.__maximum(key, self.root)

    def __maximum(self, key, curr):
        if key == curr.value:
            while curr.right != None:
                curr = curr.right
            return curr.value
        
        elif key < curr.value:
            if curr.left:
                return self.__maximum(key, curr.left)
        
        elif key > curr.value:
            if curr.right:
                return self.__maximum(key, curr.right)
        
    # Inorder Traversal
    # Left Root Right
    def inorder_traversal(self):
        self.order = []
        if self.root:
            self.__inorder_traversal(self.root)
        return self.order

    def __inorder_traversal(self, curr):
        if curr:
            self.__inorder_traversal(curr.left)
            self.order.append((curr.value))
            self.__inorder_traversal(curr.right)

    # Pre-order Traversal
    # Root Left Right
    def preorder_traversal(self):
        self.order = []
        if self.root:
            self.__preorder_traversal(self.root)
        return self.order

    def __preorder_traversal(self, curr):
        if curr:
            self.order.append((curr.value))
            self.__preorder_traversal(curr.left)
            self.__preorder_traversal(curr.right)

    # Post-order Traversal
    # Left Right Root
    def postorder_traversal(self):
        self.order = []
        if self.root:
            self.__postorder_traversal(self.root)
        return self.order

    def __postorder_traversal(self, curr):
        if curr:
            self.__postorder_traversal(curr.left)
            self.__postorder_traversal(curr.right)
            self.order.append((curr.value))



bst = BST()

bst.insert(68)
bst.insert(88)
bst.insert(61)
bst.insert(89)
bst.insert(94)
bst.insert(50)
bst.insert(4)
bst.insert(76)
bst.insert(66)
bst.insert(82)

print(bst.height())