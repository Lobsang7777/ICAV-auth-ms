from rest_framework import generics
from authApp.serializers.userEmailSerializer import UserEmailSerializer
from authApp.models.user import User

class UserDeleteView(generics.DestroyAPIView):

    queryset = User.objects.all()
    serializer_class   = UserEmailSerializer
    
    def delete(self, request, *args, **kwargs):  
        
        return super().delete(self, request, *args, **kwargs) 