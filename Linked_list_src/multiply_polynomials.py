from Linked_list_src.Polynomial import Polynomial
from Linked_list_src.add_polynomials import add_polynomials

def multiply_polynomials(poly1 , poly2):
    result = Polynomial()
    p1 = poly1.head
    
    while p1:
        temp_poly = Polynomial()
        p2 = poly2.head
        
        while p2:
            temp_poly.insert_term(p1.coefficient * p2.coefficient , p1.power + p2.power)
            p2 = p2.next 
            
        result = add_polynomials(result, temp_poly)
        p1 = p1.next 
        
    return result