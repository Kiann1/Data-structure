from Linked_list_src.Polynomial import Polynomial
from Linked_list_src.add_polynomials import add_polynomials
from Linked_list_src.multiply_polynomials import multiply_polynomials

def main():
    
    poly1 = Polynomial()
    poly1.insert_term(3, 2)
    poly1.insert_term(5, 1)
    poly1.insert_term(6, 0)

    poly2 = Polynomial()
    poly2.insert_term(6, 1)
    poly2.insert_term(8, 0)

    print("Polynomial 1:")
    poly1.display()
    print("Polynomial 2:")
    poly2.display()

    result_add = add_polynomials(poly1, poly2)
    result_mult = multiply_polynomials(poly1, poly2)

    print("Sum of polynomials:")
    result_add.display()
    print("Product of polynomials:")
    result_mult.display()
    
if __name__ == "__main__":
    main()

