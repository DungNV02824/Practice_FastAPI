from app.database import engine, Base
from app.models.products import Product
from app.models.customer import Customer

print("Đang tạo bảng...")
Base.metadata.create_all(bind=engine)
print("Tạo bảng xong!")
