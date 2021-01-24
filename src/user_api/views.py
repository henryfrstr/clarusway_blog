from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from blog_api import serializers
from rest_framework import status
from users.models import Profile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer, ProfileSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(["GET", "PUT"])
def Profile_get_update(request):
    # profile = get_object_or_404(Profile, user__id=id)
    if request.method == "GET":
        serializer = ProfileSerializer(request.user.profile)

        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ProfileSerializer(request.user.profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Profile updated succesfully!"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["PUT"])
# def profile_update(request):
#     p_serializer = ProfileSerializer(request.user.profile, data=request.data)
#     u_serializer = UserSerializer(request.user, data=request.data)
#     if u_serializer.is_valid() and p_serializer.is_valid():
#         u_serializer.save()
#         p_serializer.save()
#         data = {
#             "message": "Profile updated succesfully!"
#         }
#         return Response(data)
#     return Response(u_serializer.errors, p_serializer.erros, status=status.HTTP_400_BAD_REQUEST)
