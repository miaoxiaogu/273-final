import hashlib
from dataclasses import dataclass

class Node(object):
    def __init__(self, val=None, left=None, right=None):
        # Hash value of the node via hashlib.sha256(xxxxxx.encode()).hexdigest()
        self.val = val
        # Left node
        self.left = left
        # Right node
        self.right = right

    def __str__(self):
        return f':val={self.val},left={self.left},right={self.right}:'


class MerkleTrees(object):
    def __init__(self):
        self.root = None
        # txns dict: { hash_val -> 'file_path' } 
        self.txns = None

        # self.res = None
        # res.insert(0,txns)
        
    def get_root_hash(self):
        return self.root.val if self.root else None


    def build(self, txns):
        """
        Construct a Merkle tree using the ordered txns from a given txns dictionary.
        """
        # save the original txns(files) dict while building a Merkle tree.
        self.txns = txns
        txns_list = list(txns.keys())
        if len(txns_list)%2 != 0:
            txns_list.append(txns_list[-1])
        # to add a child to avoid a root have only one child
        parents = {}
        for index in range(0, len(txns_list)-1, 2):
            left = txns_list[index]
            right = txns_list[index+1]
            combine = left + right
            root = hashlib.sha256(combine.encode()).hexdigest()
            current_node = Node(root, Node(left), Node(right))
            # TODO
            parents[current_node.val] = str(combine)
            index +=2
        # res.insert(0,parents)
        self.build(parents)
        return parents[0]


    # def create_parent(self,left,right):
    #     combine = left + right
    #     parent = Node(self.hashlib.sha256(combine.encode()).hexdigest(),Node(left),Node(right))
    #     return parent





    def print_level_order(self):
        """
          1             1
         / \     -> --------------------    
        2   3       2 3
        """
        # TODO
        res = []
        queue  = [(self,0)]
        while len(queue) > 0:
                node,depth = queue.pop()
                if node:
                    if len(res)<=depth:
                        res.insert(0,[])
                    res[-(depth+1)].append(node.val)
                    queue.insert(0,(node.left,depth+1))
                    queue.insert(0,(node.right,depth+1))
        return res

        


        

    @staticmethod
    def compare(x, y):
        """
        Compare a given two merkle trees x and y.
        x: A Merkle Tree
        y: A Merkle Tree
        Pre-conditions: You can assume that number of nodes and heights of the given trees are equal.
        
        Return: A list of pairs as Python tuple type(xxxxx, yyyy) that hashes are not match.
        https://realpython.com/python-lists-tuples/#python-tuples
        """
        diff = []
        if x.get_root_hash() == y.get_root_hash():
            return diff
            
        
        # TODO

        else:
            xl = x.left
            yl = y.left
            xr = x.right
            yr = y.right
            if xl.get_root_hash() != yl.get_root_hash():
                diff.append(xl.value(),yl,value())
                compare(xl,yl)
            if xr.get_root_hash != yr.get_root_hash():
                diff.append(xr.value(),yr.value())
                compare(xr,yr)       
        return diff
