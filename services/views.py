# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views.generic import ListView

# from django.template import loader
# from .models import Feedback, Service

# class IndexView(ListView):
#     template_name = 'services/index.html'

#     def index(request):
#         return HttpResponse("Wellcome to the Ace Parking Lot")

# class FeedbackView(ListView):
    
#     model = Feedback
#     template_name = 'services/feedback.html'
#     context_obj_name = 'feed'
    
#     def get_queryset(request):
        
#         feed = Feedback.objects.all()
       

#         return render(request, 'services/feedback.html', context )



# class ServicesView(ListView):
#     model = Service
#     template_name = 'services/services.html'

#     def get_services(request):
#         service = Service.objects.all()
#         context = {'service': service}
        
#         return render(request, 'services/services.html', context)



from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClientSerializer, OrderSerializer, ServiceSerializer, FeedbackSerializer
from .models import Client, Order, Service, Feedback

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
            item = Feedback.objects.get(id=id)
            serializer = FeedbackSerializer(item)
            return Response ({'status': 'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        
        items = Feedback.objects.all()
        serializer = FeedbackSerializer(items, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Feedback.objects.get(id=id)
        serializer = FeedbackSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = get_object_or_404(Feedback, id=id)
        item.delete()
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

class ServiceViews(APIView):
    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer:
            serializer.save()
            return Response({'status': 'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Service.objects.get(id=id)
            serializer = ServiceSerializer(item)
            return Response ({'status': 'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        
        items = Service.objects.all()
        serializer = ServiceSerializer(items, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Service.objects.get(id=id)
        serializer = ServiceSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        item = get_object_or_404(Service, id=id)
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