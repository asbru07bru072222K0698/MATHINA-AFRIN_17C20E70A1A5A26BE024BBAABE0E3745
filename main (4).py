def linear_search_product(product_list, target_product):
    indices = [i for i, product in enumerate(product_list) if product == target_product]
    return indices

if __name__ == "__main__":
    products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]
    target = "Apple"
    
    result = linear_search_product(products, target)
    
    if result:
        print(f"{target} found at indices: {', '.join(map(str, result))}")
    else:
        print(f"{target} not found in the list.")
