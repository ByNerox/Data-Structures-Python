
from SingleLinkedList import Node as Node, SingleLinkedList as SLL

a = Node(36)
b = Node(24, a)
c = Node(12, b)
e = Node(0, c)

d = SLL(e)
d.insertAtBeginning(-12)
d.insertAtEnd(48)
print(d.getSize())
print(d.isInLL(48))
d.deleteNode(48)
d.printAllData()