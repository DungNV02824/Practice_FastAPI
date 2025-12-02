from fastapi import FastAPI
from app.routers import products
from app.routers import customer

app = FastAPI()

app.include_router(products.router)
app.include_router(customer.router)

