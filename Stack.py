class Stack:
    def __init__(self, maxSize, top):
        self.maxSize = maxSize
        self.tops = top
        self.list = []
        
    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return '\n'.join(values)
    
    def push(self, value):
        if self.tops==self.maxSize:
            print("The stack is full:")
        else:
            self.list.append(value)
            self.tops+=1
            print(value,"Has been successfully added is the stack:")
            
    def pop(self):
        if self.tops==-1:
            print("The stack is empty:")
        else:
            print("Poppend item=",self.list.pop())
            self.tops-=1
            
    def display(self):
        if self.tops==-1:
            print("The stack is empty:")
        else:
            print("Contents of the stack are")
            print(self)    
            
tempstack = Stack (3, -1)
tempstack.push(60)
tempstack.push(20)
tempstack.push(90)
tempstack.display()
tempstack.pop()
tempstack.display()