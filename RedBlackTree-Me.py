def prRed(prt): print(f'\033[91m{prt}\033[00m',end='')
def prYellow(prt): print(f'\033[93m{prt}\033[00m',end='')
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
    def __init__(self):
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
                        self.__recoler(current.LeftChild)
                        break
                    current=current.LeftChild
                else:
                    if current.RightChild is None:
                        self.index+=1
                        current.RightChild = Node(name,family,self.index)
                        current.RightChild.parent = current
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
                    print(f'Found:  {current.name}   {current.family}')
                    exist = True
                    mem.append(current.index)
            if tmp <= current.family:
                current=current.LeftChild
            elif tmp > current.family:
                current=current.RightChild
        if exist is False:
            print('Not found. :(')
    
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

    # def Delete(self , name , family):
    
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
            self.__ShowTree(self.__root.RightChild,1) 
            if self.__root.red:
                prRed(f'{self.__root.index}\n')
            else:
                print(f'{self.__root.index}')
            self.__ShowTree(self.__root.LeftChild,1)
        print('\n____________________________________________')
    
    def __ShowTree(self,tmp,d):
        depth = d+1
        if tmp is None:
            return
        self.__ShowTree(tmp.RightChild,depth)
        for i in range (1,depth):
            print('   ',end='')
        if tmp.red:
            prRed(f'--{tmp.index}\n')
        else:
            print(f'--{tmp.index}')
        self.__ShowTree(tmp.LeftChild,depth)
        
    def getroot(self):
        return self.__root

a = Tree()
student = []
stfile = open("input.txt", "r")
stlist = stfile.readlines()
stfile.close()
for l in stlist:
    l = l.split('\n')[0].split(",")
    a.Insert(l[0],l[1])
a.ShowList()
a.ShowTree()
while True:
    st = input('Enter name:  ')
    a.Search(st)
