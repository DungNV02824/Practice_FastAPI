from app.database import engine, Base
from app.models import Product

print("Đang tạo bảng...")
Base.metadata.create_all(bind=engine)
print("Tạo bảng xong!")
