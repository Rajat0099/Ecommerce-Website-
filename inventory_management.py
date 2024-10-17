def process_orders(products, orders, threshold=10):
    for order in orders:
        product_id = order['product_id']
        quantity = order['quantity']
        for product in products:
            if product.product_id == product_id:
                if product.stock < quantity:
                    print(f"Insufficient stock for {product.name}")
                else:
                    product.stock -= quantity
                    if product.stock < threshold:
                        print(f"Alert: {product.name} stock is below {threshold} units.")

def restock_items(products, restocks):
    for restock in restocks:
        product_id = restock['product_id']
        restock_qty = restock['quantity']
        for product in products:
            if product.product_id == product_id:
                product.stock += restock_qty
                print(f"{product.name} restocked. New stock level: {product.stock}")
