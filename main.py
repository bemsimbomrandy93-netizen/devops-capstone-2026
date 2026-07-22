from fastapi import FastAPI

app = FastAPI()

invoices = [
    {"id": 1, "customer": "Randy", "amount": 150.00, "paid": True},
    {"id": 2, "customer": "Sarah", "amount": 89.50, "paid": False},
]

@app.get("/")
def read_root():
    return {"message": "Hello, DevOps"}

@app.get("/invoices")
def get_invoices():
    return invoices