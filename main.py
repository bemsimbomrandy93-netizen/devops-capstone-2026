from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

invoices = [
    {"id": 1, "customer": "Randy", "amount": 150.00, "paid": True},
    {"id": 2, "customer": "Sarah", "amount": 89.50, "paid": False},
]

class InvoiceCreate(BaseModel):
    customer: str
    amount: float

@app.get("/")
def read_root():
    return {"message": "Hello, DevOps"}

@app.get("/invoices")
def get_invoices():
    return invoices

@app.get("/invoices/{invoice_id}")
def get_invoice(invoice_id: int):
    for inv in invoices:
        if inv["id"] == invoice_id:
            return inv
    return {"error": "Invoice not found"}

@app.post("/invoices")
def create_invoice(invoice: InvoiceCreate):
    new_id = len(invoices) + 1
    new_invoice = {"id": new_id, "customer": invoice.customer, "amount": invoice.amount, "paid": False}
    invoices.append(new_invoice)
    return new_invoice