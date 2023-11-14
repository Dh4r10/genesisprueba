from rest_framework import serializers
from .models import *
from .models import AuthUser # Asegúrate de importar tu modelo personalizado
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # get perfil
        # Obtén el perfil asociado al usuario
        perfil = user.perfil

        # Si el perfil existe, obtén su idperfil
        if perfil:
            token['id_perfil'] = perfil.id_perfil
        else:
            # Si no hay perfil asociado, puedes manejarlo como desees
            token['id_perfil'] = None
        # ...

        return token


# this serializer is already with url


class TemasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temas
        fields = '__all__'

class Tipo_alternativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_alternativa
        fields = '__all__'

class Tipo_encuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_encuesta
        fields = '__all__'

class ModulosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulos
        fields = '__all__'

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = '__all__'

class EncuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encuesta
        fields = '__all__'

class PermisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permisos
        fields = '__all__'

class EscuelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escuela
        fields = '__all__'

class PreguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preguntas
        fields = '__all__'

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class AlternativasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativas
        fields = '__all__'

class Preguntas_x_encuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preguntas_x_encuesta
        fields = '__all__'

class Alternativas_x_preguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativas_x_pregunta
        fields = '__all__'

class DetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle
        fields = '__all__'

class Datos_personalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datos_personales
        fields = '__all__'

class AuthUserSerializer(serializers.ModelSerializer):
    # Campo para proporcionar el ID del perfil al crear el usuario
    perfil_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = AuthUser
        fields = ('username','password', 'perfil_id')

    def create(self, validated_data):
        # Extraemos el valor del ID del perfil
        user = AuthUser(**validated_data)
        validated_data['password'] = make_password(
            validated_data.get('password'))
        id_perfil = validated_data.get('id_perfil')

        return super().create(validated_data)