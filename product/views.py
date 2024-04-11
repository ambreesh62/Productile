from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from product.models import Product,Category
from product.serializers import ProductSerializer, CategorySerializer
from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class ProductAPIView(APIView):

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        product_objs = Product.objects.all()
        serializer = ProductSerializer(product_objs, many=True)
        return Response({'Playload' : serializer.data}, status=status.HTTP_200_OK)

    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'errors' : serializer.errors, 'massage' : 'Somthing Went Worng'}, status=status.HTTP_404_NOT_FOUND)
        serializer.save()
        return Response({'Playload' : serializer.data, 'massage' : 'Data has been saved'}, status=status.HTTP_201_CREATED)
    
    
    def put(self, request, pk=None):
        try:
            product_objs = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product_objs, data=request.data)
                
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'errors' : serializer.errors, 'massage' : 'Somthing Went Worng'}, status=status.HTTP_404_NOT_FOUND)
            serializer.save()
            return Response({'Playload' : serializer.data, 'massage' : 'Data has been updated'}, status=status.HTTP_202_ACCEPTED)
        except Product.DoesNotExist:
            return Response({'massage': 'Data is DoesNotExist'}, status=status.HTTP_400_BAD_REQUEST)
        

    def patch(self, request, pk=None):
        try:
            product_objs = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product_objs, data=request.data, partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'errors' : serializer.errors, 'massage' : 'Somthing Went Worng'}, status=status.HTTP_404_NOT_FOUND)
            serializer.save()
            return Response({'Playload' : serializer.data, 'massage' : 'Data has been updated'}, status=status.HTTP_202_ACCEPTED)
        except Product.DoesNotExist:
            return Response({'massage': 'Data is DoesNotExist'}, status=status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self, request, pk=None):
        try:
            product_objs = Product.objects.get(pk=pk)
            product_objs.delete()
            return Response({'massage' : "Data has been deleted "})
        except Product.DoesNotExist:
            return Response({'massage': 'Data is DoesNotExist'}, status=status.HTTP_400_BAD_REQUEST)

class CategoryAPIView(APIView):
        
        # authentication_classes = [JWTAuthentication]
        # permission_classes = [IsAuthenticated]


        def get(self, request):
            category_objs = Category.objects.all()
            serializer = CategorySerializer(category_objs, many=True)
            return Response({'Playload' : serializer.data}, status=status.HTTP_200_OK)
        
        def post(self, request):
            serializer = CategorySerializer(data=request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'errors' : serializer.errors, 'massage' : 'Somthing went worng'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'Playload' : serializer.data, 'massage' : 'Data has been saved'}, status=status.HTTP_201_CREATED)

        def put(self, request, pk=None):
            try:
                category_objs = Category.objects.get(pk=pk)
                serializer = CategorySerializer(category_objs, data=request.data)

                if not serializer.is_valid():
                    print(serializer.errors)
                    return Response({'errors' : serializer.errors, 'massage' : 'Somthing went worng'}, status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
                return Response({'Playload' : serializer.data, 'massage' : 'Data has been updated'},status=status.HTTP_200_OK)
            except Category.DoesNotExist:
                   return Response({'massage': 'Data is DoesNotExist'}, status=status.HTTP_400_BAD_REQUEST)

        
        def patch(self, request, pk=None):
            try:
                category_objs = Category.objects.get(pk=pk)
                serializer = CategorySerializer(category_objs, data=request.data, partial=True)

                if not serializer.is_valid():
                    print(serializer.errors)
                    return Response({'errors' : serializer.errors, 'massage' : 'Somthing went worng'}, status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
                return Response({'Playload' : serializer.data, 'massage' : 'Data has been updated'}, status=status.HTTP_200_OK)
            except Category.DoesNotExist:
                return Response({'massage' : 'Data is DoesNotExist'}, status=status.HTTP_400_BAD_REQUEST)
            

        def delete(self, request, pk=None):
            try:
                category_objs = Category.objects.get(pk=pk)
                category_objs.delete()
                return Response({'massage' : 'Data has been deleted'})
            except Category.DoesNotExist:
                return Response({'massage' : 'Data DoesNotExist'}, status=status.HTTP_400_BAD_REQUEST)