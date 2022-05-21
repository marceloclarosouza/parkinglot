from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClientSerializer, OrderSerializer, ServicesSerializer, FeedbackSerializer
from .models import Client, Order, Services, Feedback
from .forms import FeedbackForm


def feedback_form(request):
    if request.method =='POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'services/thanks.html')
    else:
        form=FeedbackForm()
        return render(request, 'services/feedback_form.html', {'form':form})

class FeedbackViews(APIView):
    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            feedback = Feedback.objects.get(id=id)
            serializer = FeedbackSerializer(feedback)
            return Response ({'status': 'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        
        feedbacks = Feedback.objects.all()
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        feedback = Feedback.objects.get(id=id)
        serializer = FeedbackSerializer(feedback, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        feedback = get_object_or_404(Feedback, id=id)
        feedback.delete()
        return Response({'status': 'success', 'data': 'Item deleted. Good luck :-)'})

class ClientViews(APIView):
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer:
            serializer.is_valid()
            serializer.save()
            return Response({'status': 'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Client.objects.get(id=id)
            serializer = ClientSerializer(item)
            return Response ({'status': 'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        
        items = Client.objects.all()
        serializer = ClientSerializer(items, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Client.objects.get(id=id)
        serializer = ClientSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        item = get_object_or_404(Client, id=id)
        item.delete()
        return Response({'status': 'success', 'data': 'Item deleted. Good luck :-)'})

class ServicesViews(APIView):
    def post(self, request):
        serializer = ServicesSerializer(data=request.data)
        if serializer:
            serializer.save()
            return Response({'status': 'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Services.objects.get(id=id)
            serializer = ServicesSerializer(item)
            return Response ({'status': 'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        
        items = Services.objects.all()
        serializer = ServicesSerializer(items, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Services.objects.get(id=id)
        serializer = ServicesSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        item = get_object_or_404(Services, id=id)
        item.delete()
        return Response({'status': 'success', 'data': 'Item deleted. Good luck :-)'})

class OrderViews(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer:
            serializer.save()
            return Response({'status': 'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Order.objects.get(id=id)
            serializer = OrderSerializer(item)
            return Response ({'status': 'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        
        items = Order.objects.all()
        serializer = OrderSerializer(items, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Order.objects.get(id=id)
        serializer = OrderSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        item = get_object_or_404(Order, id=id)
        item.delete()
        return Response({'status': 'success', 'data': 'Item deleted. Good luck :-)'})
