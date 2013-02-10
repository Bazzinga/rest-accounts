from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from accounts.models import Account, Hotel
from accounts.serializers import AccountSerializer, HotelSerializer


class AccountList(APIView):
    """
    List all accounts or create a new account.
    """
    def get(self, request, format=None):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountDetail(APIView):
    """
    Retrieve, update or delete an account instance.
    """
    def get(self, request, pk, format=None):
        account = get_object_or_404(Account, pk=pk)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        account = get_object_or_404(Account, pk=pk)
        serializer = AccountSerializer(account, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        account = get_object_or_404(Account, pk=pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# The next classes are written via generic class based views.
class HotelList(generics.ListAPIView):
    model = Hotel
    serializer_class = HotelSerializer


class HotelInstance(generics.RetrieveAPIView):
    model = Hotel
    serializer_class = HotelSerializer
