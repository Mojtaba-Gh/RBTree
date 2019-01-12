#Red Black Tree Project for "Design snd analysis of algorithms".
#Teacher: Dr Reza Nadimi
#Student: Mojtaba JafarGholizadeh
#Student Number: 951542181014
#date: january 2019
#https://github.com/Mojtaba-Gh/RBTree

#NOTE: if you Want to run this program completely Right ( with Color ), Run this in Linux With Python 3 .

def prRed(prt): print(f'\033[91m{prt}\033[00m',end='')
def prYellow(prt): print(f'\033[93m{prt}\033[00m',end='')
def prGreen(prt): print(f'\033[92m{prt}\033[00m',end='')

class Node:
    def __init__(self , name , family,i,red = True):
        self.name = name
        self.family = family
        self.parent = None
        self.LeftChild = None
        self.RightChild = None
        self.red = red
        self.index = i

class Tree:
    def __init__(self,rb):
        while rb is not True and rb is not False:
            rb = bool(int(input('Unavailable Value!\nEnter "1" for Red Black Tree Or "0" for Normal Tree:  ')))
        self.rb = bool(rb)
        self.__root = None
        self.index = 0
    
    def Insert(self , name , family):
        if not self.__root:
            self.index+=1
            self.__root = Node(name,family,self.index)
            self.__root.red = False
            self.__root.parent = None
        else:
            current = self.__root
            while True:
                if family <= current.family:
                    if current.LeftChild is None:
                        self.index+=1
                        current.LeftChild = Node(name,family,self.index)
                        current.LeftChild.parent = current
                        if self.rb is True:
                            self.__recoler(current.LeftChild)
                        break
                    current=current.LeftChild
                else:
                    if current.RightChild is None:
                        self.index+=1
                        current.RightChild = Node(name,family,self.index)
                        current.RightChild.parent = current
                        if self.rb is True:
                            self.__recoler(current.RightChild)
                        break
                    current=current.RightChild      

    def Search(self , tmp):
        current = self.__root
        exist = False
        mem = []
        while current is not None:
            if tmp in current.family:
                if not current.index in mem:
                    prGreen(f'Found:  {current.name}   {current.family}\n')
                    exist = True
                    mem.append(current.index)
            if tmp <= current.family:
                current=current.LeftChild
            elif tmp > current.family:
                current=current.RightChild
        if exist is False:
            prRed('Not found. :(\n')
    
    def __rotate(self , tmp , dr):
        if not tmp:
            return
        pivot = tmp.LeftChild if dr is 'right' else tmp.RightChild
        if not pivot:
            return
        if dr is 'right':
            tmp.LeftChild = pivot.RightChild
            if pivot.RightChild:
                pivot.RightChild.parent = tmp
            pivot.RightChild = tmp
            if tmp.parent:
                if tmp.parent.LeftChild is tmp:
                    tmp.parent.LeftChild = pivot
                else:
                    tmp.parent.RightChild = pivot
        elif dr is 'left':
            tmp.RightChild = pivot.LeftChild
            if pivot.LeftChild:
                pivot.LeftChild.parent = tmp
            pivot.LeftChild = tmp
            if tmp.parent:
                if tmp.parent.LeftChild is tmp:
                    tmp.parent.LeftChild = pivot
                else:
                    tmp.parent.RightChild = pivot
        else:
            prYellow('\nDirection undefined !!!\n\n')
            return
        pivot.parent = tmp.parent
        tmp.parent = pivot
        if tmp is self.__root:
            self.__root = pivot

    def __recoler(self,tmp):
        p = tmp.parent
        if not p or not p.red:
            return
        grand_p = p.parent
        if grand_p:
            uncle = grand_p.RightChild if grand_p.LeftChild is p else grand_p.LeftChild
            grand_p.red = True
        else:
            uncle = Node(None,None,None,False)
        p.red = False
        if uncle and uncle.red:
            uncle.red = False
            self.__recoler(grand_p)
        elif grand_p:
            self.__rotate(grand_p ,'right' if grand_p.LeftChild is p else 'left')

    def ShowList(self):
        if not self.__root:
            print("List is empty !! :(")
        else:
            self.__ShowList(self.__root)
    
    def __ShowList(self , tmp):
        if tmp is None:
            return
        self.__ShowList(tmp.LeftChild)
        print(f'{tmp.parent.index if tmp.parent else 0}  {tmp.index}\t{tmp.name}\t\t{tmp.family}')
        self.__ShowList(tmp.RightChild)
    
    def ShowTree(self):
        if not self.__root:
            print("List is empty !! :(")
        else:
            print('____________________________________________\n')
            self.__ShowTreeR(self.__root.RightChild,1) 
            if self.__root.red:
                prRed(f'{self.__root.index}\n')
            else:
                print(f'{self.__root.index}')
            self.__ShowTreeL(self.__root.LeftChild,1)
        print('\n____________________________________________')
    
    def __ShowTreeR(self,tmp,d):
        depth = d+1
        if tmp is None:
            return
        self.__ShowTreeR(tmp.RightChild,depth)
        for i in range (1,depth):
            print('   ',end='')
        if tmp.red:
            prRed(f'┌──{tmp.index}\n')
        else:
            print(f'┌──{tmp.index}')
        self.__ShowTreeL(tmp.LeftChild,depth)
        
    def __ShowTreeL(self,tmp,d):
        depth = d+1
        if tmp is None:
            return
        self.__ShowTreeR(tmp.RightChild,depth)
        for i in range (1,depth):
            print('   ',end='')
        if tmp.red:
            prRed(f'└──{tmp.index}\n')
        else:
            print(f'└──{tmp.index}')
        self.__ShowTreeL(tmp.LeftChild,depth)

    def getroot(self):
        return self.__root

a = Tree(True)
student = []
stfile = open("input.txt", "r")
stlist = stfile.readlines()
stfile.close()
b = Tree(False)
for l in stlist:
    l = l.split('\n')[0].split(",")
    b.Insert(l[0],l[1])
print('\nNormal Tree:')
b.ShowTree()
for l in stlist:
    l = l.split('\n')[0].split(",")
    a.Insert(l[0],l[1])
a.ShowList()
print('\n\nRed Black Tree:\n')
a.ShowTree()
while True:
    st = input('Enter name for Search:  ')
    a.Search(st)