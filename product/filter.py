from product.views import ProductSerializer, Product
from rest_framework import generics

# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from product.pagination import SmallSetPagination


class ProductFilterView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name", "id", "price"]
    pagination_class = SmallSetPagination
