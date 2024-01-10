class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SingleLinkedList:
    def __init__(self, header:Node):
        self.header = header
        self.currentNode = header
    
    def getNextNode(self):
        if self.currentNode.next != None:
            self.currentNode = self.currentNode.next
            return self.currentNode
        print("No next Node found")

    def getCurrentData(self):
        return self.currentNode.data

    def printAllData(self):
        for data in self.traverseLL():
            print(data)

    def traverseLL(self):
        currentNode = self.header
        while currentNode is not None:
            yield currentNode.data
            currentNode = currentNode.next

    def resetTraversation(self):
        self.currentNode = self.header

    def getSize(self):
        count = 0
        currentNode = self.header
        while currentNode is not None:
            count += 1
            currentNode = currentNode.next
        return count
    
    def insertAtBeginning(self, data):
        newNode = Node(data, self.header)
        self.header = newNode

    # insert per Index or insert after a certain data

    def insertAtEnd(self, data):
        currentNode = self.header
        newNode = Node(data)
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = newNode

    def deleteNode(self, data):
        if self.isInLL(data):
            currentNode = self.header
            # if header is the Node that gets deleted
            if currentNode is not None and currentNode.data == data:
                self.header = currentNode.next
                return
            # everything else
            while currentNode is not None:
                # If the next node contains the sought data, update the current Node's next Node to be the node after the next one.
                if currentNode.next.data == data:
                    currentNode.next = currentNode.next.next
                    return
                currentNode = currentNode.next
        else:
            print("Data not in List")



    def isInLL(self, data):
        currentNode = self.header
        while currentNode is not None:
            print(currentNode.data)
            if currentNode.data == data:
                return True
            currentNode = currentNode.next
        return False



