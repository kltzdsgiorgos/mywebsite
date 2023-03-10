from django.contrib.auth.models import User
from myapp.models import Receipt
from myapp.serializers import ReceiptSerializer, UserSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from myapp.permissions import IsOwnerOrReadOnly



class ReceiptList(generics.ListCreateAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        receipt = self.get_object(pk)
        serializer = ReceiptSerializer(receipt)
        serializer.save(owner=self.request.user)
        return Response(serializer.data)
    
    
class ReceiptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
