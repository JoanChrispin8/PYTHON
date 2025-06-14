delivery_app = "swiggy"
def food():
    item = "dosa"
    def no_of_item():
        quantity=5
        print(f"Ordering {quantity} {item} from {delivery_app}")
    no_of_item()

food() 