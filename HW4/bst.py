# bst.py
# ===================================================
# Implement a binary search tree that can store any
# arbitrary object in the tree.
# ===================================================


class Student:
    def __init__(self, number, name):
        self.grade = number  # this will serve as the object's key
        self.name = name

    def __lt__(self, kq):
        return self.grade < kq.grade

    def __gt__(self, kq):
        return self.grade > kq.grade

    def __eq__(self, kq):
        return self.grade == kq.grade

    def __str__(self):
        if self.grade is not None:
            return "Name " + str(self.name) + ", Grade " + str(self.grade)


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val  # when this is a primitive, this serves as the node's key


class BST:
    def __init__(self, start_tree=None) -> None:
        """ Initialize empty tree """
        self.root = None

        # populate tree with initial nodes (if provided)
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self):
        """
        Traverses the tree using "in-order" traversal
        and returns content of tree nodes as a text string
        """
        values = [str(_) for _ in self.in_order_traversal()]
        return "TREE in order { " + ", ".join(values) + " }"

    def add(self, val):
        """
        Creates and adds a new node to the BSTree.
        If the BSTree is empty, the new node should added as the root.

        Args:
            val: Item to be stored in the new node
        """
        root = self.root
        #if the root has no node
        if root == None:
            self.root = TreeNode(val)
            return
        else:
            #function searches through the tree to input the correct value placement
            def searchTree(root):
                #if the value is less than the parent node place it on the the left side
                if val < root.val:
                    #if there is no value on the left side
                    if root.left == None:
                        root.left = TreeNode(val)
                        return
                    #if there is a value call the searchTree function to determine
                    #if the value is lesser than or greater than the parent node
                    elif root.left != None:
                        return searchTree(root.left)
                #if the value is greater than the root move to the right side
                elif val > root.val:
                    #if no value on the right input new node
                    if root.right == None:
                        root.right = TreeNode(val)
                        return
                    #if there is a value call the function to determine placement
                    elif root.right != None:
                        return searchTree(root.right)
                else:
                    return
            return searchTree(root)

    def in_order_traversal(self, cur_node=None, visited=None) -> []:
            """
            Perform in-order traversal of the tree and return a list of visited nodes
            """
            if visited is None:
                # first call to the function -> create container to store list of visited nodes
                # and initiate recursive calls starting with the root node
                visited = []
                self.in_order_traversal(self.root, visited)

            # not a first call to the function
            # base case - reached the end of current subtree -> backtrack
            if cur_node is None:
                return visited

            # recursive case -> sequence of steps for in-order traversal:
            # visit left subtree, store current node value, visit right subtree
            self.in_order_traversal(cur_node.left, visited)
            visited.append(cur_node.val)
            self.in_order_traversal(cur_node.right, visited)
            return visited

    def pre_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform pre-order traversal of the tree and return a list of visited nodes

        Returns:
            A list of nodes in the specified ordering
        """
        if visited is None:
            visited = []
            self.pre_order_traversal(self.root, visited)
        
        if cur_node is None:
            return visited
        
        visited.append(cur_node.val)
        self.pre_order_traversal(cur_node.left, visited)
        self.pre_order_traversal(cur_node.right, visited)
        return visited

    def post_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform post-order traversal of the tree and return a list of visited nodes

        Returns:
            A list of nodes in the specified ordering
        """
        if visited is None:
            visited = []
            self.post_order_traversal(self.root, visited)
        
        if cur_node is None:
            return visited
        
        self.post_order_traversal(cur_node.left, visited)
        self.post_order_traversal(cur_node.right, visited)
        visited.append(cur_node.val)
        return visited

    def contains(self, kq):
        """
        Searches BSTree to determine if the query key (kq) is in the BSTree.

        Args:
            kq: query key

        Returns:
            True if kq is in the tree, otherwise False
        """
        node = self.root
        while node is not None:
            #if the node is equivalent to kq the nwe have found the node
            if node.val == kq:
                return True
            #traverse thru the tree if the kq is less than the value of the current node
            #we are on
            elif kq < node.val:
                node = node.left
            else:
                node = node.right
        return False

    def left_child(self, node):
        """
        Returns the left-most child in a subtree.

        Args:
            node: the root node of the subtree

        Returns:
            The left-most node of the given subtree
        """
        if node == None:
            return node
        else:
            #traverse thur the left side to find the left most child
            while node.left is not None:
                node = node.left 
            return node
    
    def parent_node(self, node):
        #return if the root node is the parent
        if node is self.root:
            return 
        else:
            cur_node = self.root
            #we want to search thru the tree if the root is not the node
            #we are passing thru
            while cur_node != node:
                #if the value of the node being passed is less than the parent node
                # and the value on the left is found return the current node
                if node.val < cur_node.val:
                    if cur_node.left.val == node.val:
                        return cur_node
                    #else continue to search thru the left side of the tree
                    else:
                        cur_node = cur_node.left 
                #if the value is greater traverse the right side
                else:
                    if cur_node.right.val == node.val:
                        return cur_node 
                    else:
                        cur_node = cur_node.right 
            return False 

    def remove(self, kq):
        """
        Removes node with key k, if the node exists in the BSTree.

        Args:
            node: root of Binary Search Tree
            kq: key of node to remove

        Returns:
            True if k is in the tree and successfully removed, otherwise False
        """
        #if the root value
        if kq == self.root.val:
            self.remove_first() 
            return
        #traverse thru the tree to find the value
        if self.contains(kq):
            node = self.root
            while node.val != kq:
                if kq < node.val:
                    node = node.left 
                else:
                    node = node.right
        else:
            return False
        #get the parent of kq
        parent_node = self.parent_node(node)
        
        #if there are no children
        if node.left is None and node.right is None:
            #if the root val is less than the parent node set the left parent to None
            if node.val < parent_node.val:
                parent_node.left = None 
            else:
                parent_node.right = None
        else:
            #traverse thru the inorder successor of the left side
            if node.right is None:
                inorder = node.left 
                #if the node val is less than the parent node set the parent node
                #to the inorder successor node
                if node.val < parent_node.val:
                    parent_node.left = inorder 
                else:
                    parent_node.right = inorder 
                #remove nodes
                node.left = None 
                node.right = None 
                return True
            else:
                #if there is a right side on the left then set the inorder successor
                #to the right side of the left
                inorder = self.left_child(node.right)
            #set the inorder successor parent to traverse thru the tree to porperly place
            #the right children
            inorder_par = self.parent_node(inorder)
            inorder.left = node.left 
            if inorder is not node.right:
                inorder_par = inorder.right 
                inorder.right = node.right 
            #point ot the inorder successor
            if node.val < parent_node:
                parent_node.left = inorder 
            else:
                parent_node.right = inorder 
        #remove nodes
        node.left = None 
        node.right = None
        return True

    def get_first(self):
        """
        Gets the val of the root node in the BSTree.

        Returns:
            val of the root node, return None if BSTree is empty
        """
        if self.root == None:
            return None
        else:
            return self.root.val

    def remove_first(self):
        """
        Removes the val of the root node in the BSTree.

        Returns:
            True if the root was removed, otherwise False
        """
        if self.root is None:
            return False 
        else:
            #if the root has no children
            if self.root.left is None and self.root.right is None:
                self.root = None 
                return True
            #if no right child then set the root to the left parent
            elif self.root.right is None:
                self.root = self.root.left
            #if the root has two children then search thru the left most child 
            #and remove 
            else:
                #set the inorder successor to the left most child on the right side
                left_node = self.left_child(self.root.right)
                #set the parent of the inorder successor after traversing thru the left most side
                left_parent = self.parent_node(left_node)
                
                #if the parent of the inorder successor is equal to the self.root then
                #remove and reset the parent root and its children
                if left_parent == self.root:
                    left_node.left = self.root.left 
                    self.root = left_node
                    return True 
                else:
                    #if there all multiple children begin arranging the tree on the left side
                    #then arrange on the right to the proper parent root
                    left_node.left = self.root.left 
                    left_parent.left = left_node.right 
                    left_node.right = self.root.right 
                    self.root = left_node
                    return True
