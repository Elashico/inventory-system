from itertools import product
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import database_models
from models import Product
from database_models import Products
from database import SessionLocal, engine, get_db

database_models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)


@app.get("/")
def greet():
    return "Hello, welcome to the frontend!"

products = [
    Product(id=1, name="Product 1", description="Description of Product 1", price=10.99, quantity=100),
    Product(id=2, name="Product 2", description="Description of Product 2", price=19.99, quantity=50),
    Product(id=3, name="Product 3", description="Description of Product 3", price=5.99, quantity=200),
    Product(id=4, name="Product 4", description="Description of Product 4", price=15.49, quantity=75)
]

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

def init_db():
    db = SessionLocal()
    count = db.query(database_models.Products).count()
    if count == 0:
        for product in products:
            db.add(database_models.Products(**product.model_dump()))
        db.commit()

init_db()

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(database_models.Products).all()
    return db_products

@app.get("/products/{product_id}")
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Products).filter(database_models.Products.id == product_id).first()
    if db_product:
        return db_product
    return {"error": "Product not found"}

@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Products(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Products).filter(database_models.Products.id == product_id).first()
    if db_product:
        # for key, value in product.model_dump().items():
        #     setattr(db_product, key, value)
        # or do it like this:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product updated successfully"
    else:
        return {"error": "Product not found"}

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Products).filter(database_models.Products.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return {"message": "Product deleted successfully"}
    else:
        return {"error": "Product not found"}