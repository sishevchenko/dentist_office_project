from django.contrib.auth.models import Group

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from .permissions import IsAdminOrReedOnly, IsAdminOrOwnerOrReedOnly
from .serializers import UserSerializer, GroupSerializer
from .models import User


class UserAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminOrOwnerOrReedOnly]

    def get(self, request):
        users = User.objects.all().order_by('username').values()
        auth = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response({'GET': UserSerializer(users, many=True).data, 'auth': auth})

    def post(self, request):
        context = {'request': request}
        serializer = UserSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'POST': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'ERROR': 'Method PUT not allowed'})
        try:
            instance = User.objects.get(pk=pk)
        except:
            return Response({'ERROR': 'Method PUT not exists'})
        serializer = UserSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'PUT': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'ERROR': 'Method PUT not allowed'})
        try:
            instance = User.objects.get(pk=pk)
        except:
            return Response({'ERROR': 'Method PUT not exists'})
        instance.delete()
        return Response({'DELETE': 'Successful'})


class GroupAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminOrReedOnly]

    def get(self, request):
        groups = Group.objects.all().order_by('name').values()
        auth = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response({'GET': GroupSerializer(groups, many=True).data, 'auth': auth})

    def post(self, request):
        serializer = GroupSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'POST': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'ERROR': 'Method PUT not allowed'})
        try:
            instance = Group.objects.get(pk=pk)
        except:
            return Response({'ERROR': 'Method PUT not exists'})
        serializer = GroupSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'PUT': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'ERROR': 'Method PUT not allowed'})
        try:
            instance = Group.objects.get(pk=pk)
        except:
            return Response({'ERROR': 'Method PUT not exists'})
        instance.delete()
        return Response({'DELETE': 'Successful'})
