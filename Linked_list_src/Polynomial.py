from Linked_list_src.Node import Node

class Polynomial:
    
    def __init__(self):
        self.head = None
        
    def insert_term (self, coefficient , power):
        new_node = Node(coefficient , power)
        if self.head is None:
            self.head = new_node
            
        else:
            current = self.head
            while current.next:
                current = current.next 
            
            current.next = new_node
            
    def display (self):
        current = self.head
        poynomial_str = ""
        while current:
            if current.coefficient != 0:
                if poynomial_str != "":
                    poynomial_str += "+"
                    
                poynomial_str += f"{current.coefficient}x^{current.power}"
                
            current = current.next
            
        print(poynomial_str)