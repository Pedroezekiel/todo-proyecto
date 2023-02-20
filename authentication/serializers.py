from rest_registration.api.serializers import DefaultRegisterUserSerializer
from authentication.models import AppUser


class RegisterUser(DefaultRegisterUserSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'email', 'last_name', 'first_name', 'password']

    def register_user(self, data):
        request = self.context.get('request')
        email = request.data.get('email')
        last_name = request.data.get('last_name')
        first_name = request.data.get('first_name')
        password = request.data.get('password')
        user = AppUser.objects.create_user(email=email, last_name=last_name, first_name=first_name, password=password)

        return user
