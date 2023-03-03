from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from profile_app.permissions import *
from .serializers import ServiceSerializer
from .models import Service


class ServiceAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        services = Service.objects.all().order_by('name').values()
        auth = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response({'GET': ServiceSerializer(services, many=True).data, 'auth': auth})

    def post(self, request):
        context = {'request': request}
        serializer = ServiceSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'POST': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'ERROR': 'Method PUT not allowed'})
        try:
            instance = Service.objects.get(pk=pk)
        except:
            return Response({'ERROR': 'Method PUT not exists'})
        serializer = ServiceSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'PUT': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'ERROR': 'Method PUT not allowed'})
        try:
            instance = Service.objects.get(pk=pk)
        except:
            return Response({'ERROR': 'Method PUT not exists'})
        instance.delete()
        return Response({'DELETE': 'Successful'})
