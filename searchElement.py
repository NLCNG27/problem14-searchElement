# Author: Nguyen L.
# Date: June 9th, 2020
# Searching for an element in the list iteratively (this could be done recursively also)

from random import randint

# Node class
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# LinkedList class
class LinkedList:
    def __init__(self, data=None):
        self.head = Node(data)

    # insert beginning method
    def addBeginning(self, newData):
        temp = Node(newData)
        temp.next = self.head
        self.head = temp

    # generating random list of nodes
    def randomList(self, limit=5):
        i = 0

        while i < limit:
            value = randint(1, 20)
            self.addBeginning(value)
            i += 1

        self.display()

    # searching iteratively function
    def searchElement(self, number):

        # default case if there's no list in the first place
        if not self.head:
            return False

        current = self.head

        # going through the linked list
        while current is not None:
            if current.data == number:
                return True
            current = current.next

        return False

    # display method
    def display(self):
        temp = self.head

        while temp.next != None:
            print(temp.data, end=" ")
            temp = temp.next    


# TESTING OUT THE PROGRAM
myList = LinkedList()
limit = randint(5, 10)
print("*" * 40)
print("Original list: ", end="")
myList.randomList(limit)
print()

itemToSearch = int(input("Enter item to search: "))
if myList.searchElement(itemToSearch):
    print("Item FOUND")
else:
    print("Item NOT found...")


