from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, DevOps"}

def test_get_invoices():
    response = client.get("/invoices")
    assert response.status_code == 200
    assert len(response.json()) >= 2

def test_get_invoice_not_found():
    response = client.get("/invoices/9999")
    assert response.status_code == 200
    assert response.json() == {"error": "Invoice not found"}