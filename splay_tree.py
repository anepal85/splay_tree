from tkinter import *
class Node:
    def __init__(self,key,data):
        self.key=key
        self.left=None
        self.right=None
        self.p=None
        self.data=data
        self.posx=0
        self.posy=0
    
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
    def insert(self,key,data):
        z=Node(key,data)
        y=None
        x=self.root
        while x!=None:
            y=x
            if z.key<x.key:
                x=x.left
            else:
                x=x.right
        z.p=y
        if y==None:
            self.root=z
            
        elif z.key<y.key:
            y.left=z
        else:
            y.right=z
        self.splay(z)
            
    def delete(self,key):
        z=self.search(key)
        if z==None:
            return None
        if z.left==None:
            self.transplant(z,z.right)
        elif z.right==None:
            self.transplant(z,z.left)
        else:
            y=self.mini(z.right)
            if y.p!=z:
                self.transplant(y,y.right)
                y.right=z.right
                y.right.p=y
            self.transplant(z,y)
            y.left=z.left
            y.left.p=y
            
    def transplant(self,u,v):
        if u.p==None:
            self.root=v
        elif u==u.p.left:
            u.p.left=v
        else:
            u.p.right=v
            
        if v!=None:
            v.p=u.p
    def rotateright(self,x):
        self.crot+=1
        y=x.left
        if x.p==None:
            self.root=y
        elif x.p.left==x:
            x.p.left=y
        else:
            x.p.right=y
        y.p=x.p
        x.left=y.right
        if x.left!=None:
            x.left.p=x
        y.right=x
        x.p=y

        
    def rotateleft(self,x):
        self.crot+=1
        y=x.right
        if x.p==None:
            self.root=y
        elif x.p.left==x:
            x.p.left=y
        else:
            x.p.right=y
        y.p=x.p
        x.right=y.left
        if x.right!=None:
            x.right.p=x
        y.left=x
        x.p=y
    def splaystep(self,x):
        if x.p==None:
            return None
        elif x.p.p==None and x==x.p.left:
            self.rotateright(x.p)
        elif x.p.p==None and x==x.p.right:
            self.rotateleft(x.p)
        elif x==x.p.left and x.p==x.p.p.left:
            self.rotateright(x.p.p)
            self.rotateright(x.p)
        elif x==x.p.right and x.p==x.p.p.right:
            self.rotateleft(x.p.p)
            self.rotateleft(x.p)
        elif x==x.p.left and x.p==x.p.p.right:
            self.rotateright(x.p)
            self.rotateleft(x.p)
        else:
            self.rotateleft(x.p)
            self.rotateright(x.p)
    def splay(self,x):
        print("Splay an Knoten:",x.key)
        self.crot=0
        r_x=self.call_s(x)
        r_troot=self.call_s(self.root)
        a=self.call_potential(self.root)
        while x.p!=None:
            self.splaystep(x)
        b=self.call_potential(x)
        c=2**(self.crot)
        print("2^Rotationen:",c)
        print("2^Potential vorher:",a)
        print("2^Potential nachher:",b)
        print("2^amortisierte Rotationen:",'{}/{}'.format(c*b,a))
        print("2^obere Schranke:",'{}/{}'.format(2*(r_troot**3),r_x**3))
        
    def call_s(self,x): #Berechnung der Anzahl Knoten im Teilbaum mit wurzel als x selbst
        self.s(x)
        a= self.counter
        self.counter=0
        return a
    
    def s(self,x):      ##Inorder Tree Walk 
        if x!=None:
            self.s(x.left)
            self.counter+=1
            self.s(x.right)
    def call_potential(self,x):     #Berechnung der Potential jeder knoten x
        self.potential(x)
        b=self.kera
        self.kera=1
        return b
            
    def potential(self,x):          #Inorder Tree Walk 
        if x!=None:
            self.kera*=self.call_s(x)
            self.potential(x.left)
            self.potential(x.right)
    def depth(self,node):
        r = 0
        while node.p:
            node = node.p
            r+=1
        return r
    def drawnode(self,node,c):      #Recursiv drawing Node and Edges 
        self.position(node)
        x=node.posx
        y=node.posy
        self.create_rectangle(node,x,y,c)
        if node.left:
            self.drawnode(node.left,c)
            self.create_line(node,node.left,c)
        if node.right:
            self.drawnode(node.right,c)
            self.create_line(node,node.right,c)
    def position(self,node):        #Finds position of every Node after Splay
        w=node.p
        if w==None:
            w=Tree.root
            node.posx=500
            node.posy=30
        if node==w.left:
           node.posx=w.posx-self.width*2**(-self.depth(node)-1)
           node.posy=w.posy+100
        elif node==w.right:
            node.posx=w.posx+self.width*2**(-self.depth(node)-1)
            node.posy=w.posy+100
    def draw(self,c):
        c.delete("all")
        self.drawnode(Tree.root,c)
    def create_rectangle(self,node,a,b,c):
        c.create_rectangle(a,b,a+20,b+20,fill="yellow")
        c.create_text(a+10,b+10,text=node.key)
    def create_line(self,knot1,knot2,c):
        c.create_line(knot1.posx,knot1.posy+20,knot2.posx+20,knot2.posy)                
class TreeVisualizer(SplayTree):
    def __init__(self,master):
        frame=Frame(master)
        frame.grid(column=1)
        Label(frame,text="Key").grid(row=0)
        Label(frame,text="Data").grid(row=1)
        self.e1=Entry(frame)
        self.e2=Entry(frame)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.b = Button(frame, text="Construct", command=self.construct)
        self.b.grid(row=2,column=1)
        self.e1.delete(0,END)
        self.e2.delete(0,END)
       

    def construct(self):
        self.b.destroy()
        keys=int(self.e1.get())
        datas=self.e2.get()
        global Tree
        Tree=SplayTree(keys,datas)
        self.e=Button(master,text="Search",command=self.suche)
        self.e.grid(row=3,column=0)
        self.c=Button(master,text="Insert",command=self.einfugen)
        self.c.grid(row=3,column=1)
        self.d=Button(master,text="Delete",command=self.loeschen)
        self.d.grid(row=3,column=2)
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.width=1000
        self.height=500
        self.w=Canvas(master,width=self.width,height=self.height,bg="white")
        self.w.grid(row=4,column=1)
        self.draw(self.w)
    def suche(self):
        keys=int(self.e1.get())
        datas=self.e2.get()
        print(Tree.search(keys))
        self.draw(self.w)
        self.e1.delete(0,END)
        self.e2.delete(0,END)
    def einfugen(self):
        keys=int(self.e1.get())
        datas=self.e2.get()
        Tree.insert(keys,datas)
        self.draw(self.w)
        self.e1.delete(0,END)
        self.e2.delete(0,END)
    def loeschen(self):
        keys=int(self.e1.get())
        datas=self.e2.get()
        Tree.delete(keys)
        self.draw(self.w)
        self.e1.delete(0,END)
        self.e2.delete(0,END)
    
        
master=Tk()
a=TreeVisualizer(master)
master.mainloop()


