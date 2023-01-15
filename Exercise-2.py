class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def old_delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.old_delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.old_delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.old_delete(min_val)

        return self

    def new_delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.new_delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.new_delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.new_delete(max_val)

        return self

def build_tree(elements):
    print("\nBuilding tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    name = ['J','O','S','H','U','A','C,','M','I','N','a']
    name_tree = build_tree(name)
    name_tree.new_delete('J')
    print("After deleting J ",name_tree.in_order_traversal())

    name_tree = build_tree(name)
    name_tree.new_delete('a')
    print("After deleting a ", name_tree.in_order_traversal())

    name_tree = build_tree(name)
    name_tree.new_delete("O")
    print("After deleting O ", name_tree.in_order_traversal())