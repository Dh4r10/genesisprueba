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
    id_tipo_encuesta = serializers.PrimaryKeyRelatedField(queryset=Tipo_encuesta.objects.all(), write_only=True)
    tipo_encuesta = Tipo_encuestaSerializer(source='id_tipo_encuesta', read_only=True)

    class Meta:
        model = Encuesta
        fields = '__all__'

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class PermisosSerializer(serializers.ModelSerializer):
    id_modulo = serializers.PrimaryKeyRelatedField(queryset=Modulos.objects.all(), write_only=True)
    modulo = ModulosSerializer(source='id_modulo', read_only=True)
    id_perfil = serializers.PrimaryKeyRelatedField(queryset=Perfil.objects.all(), write_only=True)
    perfil = PerfilSerializer(source='id_perfil', read_only=True)

    class Meta:
        model = Permisos
        fields = '__all__'

class EscuelaSerializer(serializers.ModelSerializer):
    id_facultad = serializers.PrimaryKeyRelatedField(queryset=Facultad.objects.all(), write_only=True)
    facultad = FacultadSerializer(source='id_facultad', read_only=True)

    class Meta:
        model = Escuela
        fields = '__all__'

class PreguntasSerializer(serializers.ModelSerializer):
    id_tema = serializers.PrimaryKeyRelatedField(queryset=Temas.objects.all(), write_only=True)
    tema = TemasSerializer(source='id_tema', read_only=True)

    class Meta:
        model = Preguntas
        fields = '__all__'

class AlternativasSerializer(serializers.ModelSerializer):
    id_tipo_alternativa = serializers.PrimaryKeyRelatedField(queryset=Tipo_alternativa.objects.all(), write_only=True)
    tipo_alternativa = Tipo_alternativaSerializer(source='id_tipo_alternativa', read_only=True)

    class Meta:
        model = Alternativas
        fields = '__all__'

class Preguntas_x_encuestaSerializer(serializers.ModelSerializer):
    id_pregunta = serializers.PrimaryKeyRelatedField(queryset=Preguntas.objects.all(), write_only=True)
    pregunta = PreguntasSerializer(source='id_pregunta', read_only=True)
    id_encuesta = serializers.PrimaryKeyRelatedField(queryset=Encuesta.objects.all(), write_only=True)
    encuesta = EncuestaSerializer(source='id_encuesta', read_only=True)

    class Meta:
        model = Preguntas_x_encuesta
        fields = '__all__'

class Alternativas_x_preguntaSerializer(serializers.ModelSerializer):
    id_alternativa = serializers.PrimaryKeyRelatedField(queryset=Alternativas.objects.all(), write_only=True)
    alternativa = AlternativasSerializer(source='id_alternativa', read_only=True)
    id_pregunta_x_encuesta = serializers.PrimaryKeyRelatedField(queryset=Preguntas_x_encuesta.objects.all(), write_only=True)
    pregunta_x_encuesta = Preguntas_x_encuestaSerializer(source='id_pregunta_x_encuesta', read_only=True)

    class Meta:
        model = Alternativas_x_pregunta
        fields = '__all__'

class AuthUserSerializer(serializers.ModelSerializer):
    # Campo para proporcionar el ID del perfil al crear el usuario
    perfil_id = serializers.PrimaryKeyRelatedField(queryset=Perfil.objects.all(), write_only=True)

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
    
class Datos_personalesSerializer(serializers.ModelSerializer):
    id_escuela = serializers.PrimaryKeyRelatedField(queryset=Escuela.objects.all(), write_only=True)
    escuela = EscuelaSerializer(source='id_escuela', read_only=True)
    id_auth_user = serializers.PrimaryKeyRelatedField(queryset=AuthUser.objects.all(), write_only=True)
    auth_user = AuthUserSerializer(source='id_auth_user', read_only=True)

    class Meta:
        model = Datos_personales
        fields = '__all__'

class DetalleSerializer(serializers.ModelSerializer):
    id_auth_user = serializers.PrimaryKeyRelatedField(queryset=AuthUser.objects.all(), write_only=True)
    auth_user = AuthUserSerializer(source='id_auth_user', read_only=True)
    id_alternativa_x_pregunta = serializers.PrimaryKeyRelatedField(queryset=Alternativas_x_pregunta.objects.all(), write_only=True)
    alternativa_x_pregunta = Alternativas_x_preguntaSerializer(source='id_alternativa_x_pregunta', read_only=True)

    class Meta:
        model = Detalle
        fields = '__all__'