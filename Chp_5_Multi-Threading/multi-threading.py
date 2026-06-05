import time
from concurrent.futures import ThreadPoolExecutor


class FoodDeliverySystem:

    def __init__(self, customer):
        self.customer = customer

    def payment_verification(self):
        print(f"{self.customer} Your payment is being verified....")
        time.sleep(2)
        print(f"{self.customer} Your payment is verified successfully")

    def food_processing(self):
        print(f"{self.customer} Your food is being processed....")
        time.sleep(5)
        print(f"{self.customer} Your food is ready")

    def deliver_partner(self):
        print(f"{self.customer} We are assigning your order to deliver partner....")
        time.sleep(3)
        print(f"{self.customer} Your order is assigned to the deliver partner.")

    def process_order(self):
        print(f"{self.customer} The order has been received.")
        self.payment_verification()
        self.food_processing()
        self.deliver_partner()
        print(f"{self.customer} The order is ready.")


customers = ["Mehek", "Jaypal", "Rahul", "Smita", "Aman"]
with ThreadPoolExecutor(max_workers=len(customers)) as exe:
    exe.map( lambda customer : FoodDeliverySystem(customer).process_order(), customers)
