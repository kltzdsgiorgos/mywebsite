from myapp.models import Receipt
from myapp.serializers import ReceiptSerializer
from rest_framework import generics

class ReceiptList(generics.ListCreateAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    
class ReceiptDetail(generics.RetrieveUpdateDestroyAPIView):
    quesyset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
