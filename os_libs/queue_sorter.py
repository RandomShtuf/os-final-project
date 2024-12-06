from time import sleep

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None


def conquer(left, right, attribute_getter):
    left_nums = left.data
    right_nums = right.data
    sorted_arr = []

    while True:
        if len(left_nums) == 0 or len(right_nums) == 0: break
        for i in range(len(right_nums)):
            left_attribute = getattr(left_nums[0], attribute_getter)
            right_attribute = getattr(right_nums[i], attribute_getter)
            if left_attribute() > right_attribute():
                sorted_arr.append(right_nums.pop(i))
                i -= 1
            else: sorted_arr.append(left_nums.pop(0))
            if len(left_nums) == 0 or len(right_nums): break

    if len(left_nums) == 0:
        sorted_arr += right_nums
        right_nums = []
    else:
        sorted_arr += left_nums
        left_nums = []
    
    return sorted_arr

def divide(tree_node, attribute_getter):
    arr = tree_node.data
    if len(arr) <= 1:
        return
    tree_node.left = TreeNode(arr[:len(arr)//2])
    tree_node.right = TreeNode(arr[len(arr)//2:])
    divide(tree_node.left, attribute_getter)
    divide(tree_node.right, attribute_getter)
    tree_node.data = conquer(tree_node.left, tree_node.right, attribute_getter)

def sortByAttribute(queue, attribute_name = "process_num"):
    arr = queue.getQueue()
    match attribute_name:
        case "process_num": attribute_getter = "getProcessNum"
        case "arrival_time": attribute_getter = "getArrivalTime"
        case "burst_time": attribute_getter = "getBurstTime"

    sorting_tree = Tree()
    unsorted_arr = arr
    sorting_tree.root = TreeNode(unsorted_arr)
    divide(sorting_tree.root, attribute_getter)
    sorted_arr = sorting_tree.root.data

    return sorted_arr