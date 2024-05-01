import stripe
import os
from stripe import Customer, Invoice

stripe.api_key = os.getenv("stripe-key")


def create_customer(name: str, email: str) -> str:
    customer: Customer = Customer.create(
        name = name,
        email = email
    )
    print(customer.id)
    return customer.id


def create_invoice(customer_id: str):
    # need invoice line items
    # need invoice shipping rates
    Invoice.create(
        customer = customer_id
    )

if __name__ == "__main__":
    customer_id = create_customer("test_2", "test_2@gmail.com")
    invoice = create_invoice(customer_id)