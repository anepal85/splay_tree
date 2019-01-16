## In this Tutorial im going to splay a Binary search Tree.  
## So here is the Code 
class Node:
    def __init__(self,key,data):
        self.key=key
        self.left=None
        self.right=None
        self.p=None
        self.data=data
class SplayTree(Node):
    def __init__(self,key,data):
        Node.__init__(self,key,data)
        self.root=None
        self.counter=0
        self.kera=1
        self.crot=0
        if self.root==None:
            self.root=Node(key,data)
    def mini(self,x):           #Tree_Minimum
        while x.left!=None:
            x=x.left
        return x
    def search(self,key):   
        x=self.root
        while x!=None and key!=x.key:
            if key<x.key:
                a=x
                x=x.left
                if x==None:
                    self.splay(a)
                
            else:
                b=x
                x=x.right
                if x==None:
                    self.splay(b)
        if x!=None:      
            self.splay(x)
         return x 
##Splay to be written 
