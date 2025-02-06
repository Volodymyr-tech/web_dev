from catalog.models import Product


class GetCategory:
    @staticmethod
    def get_product_by_category(category_id):

        product_by_category = Product.objects.filter(category_id=category_id)

        if not product_by_category:
            product_by_category = None

        return product_by_category