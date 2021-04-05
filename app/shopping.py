import os
from datetime import datetime
from pandas import read_csv

def format_usd(i):
    return f"${i:.2f}"

def find_product(selected_id, products):
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    return matching_products

if __name__ == "__main__":
    # READ INVENTORY OF PRODUCTS

    products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
    products_df = read_csv(products_filepath)
    products = products_df.to_dict("records")

    # CAPTURE PRODUCT SELECTIONS

    selected_products = []
    while True:
        selected_id = input("Please select a product identifier: ")
        if selected_id.upper() == "DONE":
            break
        else:
            matching_products = find_product(selected_id, products)
            if any(matching_products):
                selected_products.append(matching_products[0])
            else:
                print("OOPS, Couldn't find that product. Please try again.")

    checkout_at = datetime.now()

    subtotal = sum([float(p["price"]) for p in selected_products])

    # PRINT RECEIPT

    print("---------")
    print("CHECKOUT AT: " + str(checkout_at.strftime("%Y-%M-%d %H:%m:%S")))
    print("---------")
    for p in selected_products:
        print("SELECTED PRODUCT: " + p["name"] + "   " + format_usd(p["price"]))

    print("---------")
    print("SUBTOTAL:", format_usd(subtotal))
    print("TAX:", format_usd(subtotal * 0.0875))
    print("TOTAL:", format_usd((subtotal * 0.0875) + subtotal))
    print("---------")
    print("THANK YOU! PLEASE COME AGAIN SOON!")
    print("---------")

    # WRITE RECEIPT TO FILE

    receipt_id = checkout_at.strftime('%Y-%M-%d-%H-%m-%S')
    receipt_filepath = os.path.join(os.path.dirname(__file__), "..", "receipts", f"{receipt_id}.txt")

    with open(receipt_filepath, "w") as receipt_file:
        receipt_file.write("------------------------------------------")
        for p in selected_products:
            receipt_file.write("\nSELECTED PRODUCT: " + p["name"] + "   " + format_usd(p["price"]))

        receipt_file.write("\n---------")
        receipt_file.write("\nSUBTOTAL: "+format_usd(subtotal))
        receipt_file.write(f"\nTAX: " + format_usd(subtotal * 0.0875))
        receipt_file.write(f"\nTOTAL: " + format_usd((subtotal * 0.0875) + subtotal))
        receipt_file.write("\n---------")
        receipt_file.write("\nTHANK YOU! PLEASE COME AGAIN SOON!")
        receipt_file.write("\n---------")
