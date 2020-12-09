class Node:
    def __init__(self, num):
        self.value = num
        self.left = None
        self.right = None
    def insert_left(self, value):
        self.left = Node(value)
        print('new       left inserted ' + str(self.left.value))
    def insert_right(self, value):
        self.right = Node(value)
        print('new       right inserted ' + str(self.right.value))
    def right_child(self):
        if self.right != None:
            return True
        return False
    def left_child(self):
        if self.left != None:
            return True
        return False
    def insert(self, cur_node, val):
        if cur_node.value == val:
            return
        elif cur_node.value < val:
            if cur_node.right_child():
                cur_node.right.insert(cur_node.right, val)
            else:
                cur_node.insert_right(val)
        else:
            if cur_node.left_child():
                cur_node.left.insert(cur_node.left, val)
            else:
                cur_node.insert_left(val)



list= [100, 5, 72, 33, 69, 503, 389, 2]

root_node = Node(list[0])

for i in range(len(list)):
    root_node.insert(root_node, list[i])