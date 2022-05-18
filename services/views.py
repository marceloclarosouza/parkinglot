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
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': 'error', 'data': serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(Feedback, id=id)
        item.delete()
        return Response({'status': 'success', 'data': 'Item deleted. Good luck :-)'})
