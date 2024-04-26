from products.models import (
    Product, 
    Category,
)
from typing import (
    List,
    Optional,
    Tuple
)

class ProductRepository:
    def create(
        self,
        name: str,
        price: float,
        stock: int,
        category: Optional[Category] = None,
        desc: Optional[str] = "PELOTUDO",
    ) -> Product.objects:
        return Product.objects.create(
            name=name,
            price=price,
            desc=desc,
            stock=stock,
            category=category,
        )
    
    def get_all(self) -> List[Product]:
        return Product.objects.all()
    
    def get_by_id(self, id) -> Optional[Product]:
        return Product.objects.filter(id=id).first()

    def get_by_price_range(
        self,
        min_price: float,
        max_price: float,
    ) -> List[Product]:
        return Product.objects.filter(
            price__range=(min_price, max_price)
        )

    def get_by_category(
        self,
        category_id: int,
    ) -> List[Product]:
        return Product.objects.filter(category=category_id).first()
    
    def delete(
        self,
        product: Product,
    ):
        Product.delete(product)






