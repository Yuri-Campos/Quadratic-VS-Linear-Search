import helpers as h
import linear_search as ls
import quadratic_search as qs
import math
def main():

    new_list: list = h.list_generator(int(input("List size: ")))
    target: int = int(input("Target: "))
    qs_result = qs.search(new_list, target)
    ls_result = ls.search(new_list, target)
    print(f"\nQuadratic Search Operations: {qs_result}\nQuadratic Search Complexity: {h.log(qs_result)}\n")
    print(f"Linear Search Operations: {ls_result}\nLinear Search Complexity: {ls_result}\n")


if __name__ == '__main__':
    main()