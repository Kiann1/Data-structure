from Linked_list_src.Polynomial import Polynomial

def add_polynomials(poly1 , poly2):
    result = Polynomial()
    p1 = poly1.head
    p2 = poly2.head
    
    while p1 and p2:
        if p1.power > p2.power:
            result.insert_term(p1.coefficient , p1.power)
            p1 = p1.next 
            
        elif p1.power < p2.power:
            result.insert_term(p2.coefficient , p2.power)
            p2 = p2.next 
            
        else:
            result.insert_term(p1.coefficient + p2.coefficient , p1.power)
            p1 = p1.next 
            p2 = p2.next 
        
    while p1:
        result.insert_term(p1.coefficient , p1.power)
        p1 = p1.next 
        
    while p2:
        result.insert_term(p2.coefficient , p2.power)
        p2 = p2.next 
        
    return result

            