from rest_framework import generics
from authApp.serializers.userEmailSerializer import UserEmailSerializer
from authApp.models.user import User

class UserUpdateView(generics.UpdateAPIView):

    queryset = User.objects.all()
    serializer_class   = UserEmailSerializer
    
    def patch(self, request, *args, **kwargs):  
        
        return super().update(self, request, *args, **kwargs) 