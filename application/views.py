from .models import *
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TemasViewSet(viewsets.ModelViewSet):
    queryset = Temas.objects.all()
    permission_classes = [
        IsAuthenticated,
        #permissions.AllowAny,
    ]
    serializer_class = TemasSerializer

class Tipo_alternativaViewSet(viewsets.ModelViewSet):
    queryset = Tipo_alternativa.objects.all()
    permission_classes = [
        IsAuthenticated,
        #permissions.AllowAny,
    ]
    serializer_class = Tipo_alternativaSerializer

class Tipo_encuestaViewSet(viewsets.ModelViewSet):
    queryset = Tipo_encuesta.objects.all()
    permission_classes = [
        IsAuthenticated,
        #permissions.AllowAny,
    ]
    serializer_class = Tipo_encuestaSerializer

class ModulosViewSet(viewsets.ModelViewSet):
    queryset = Modulos.objects.all()
    permission_classes = [
        IsAuthenticated,
        #permissions.AllowAny,
    ]
    serializer_class = ModulosSerializer

class FacultadViewSet(viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    permission_classes = [
        IsAuthenticated,
        #permissions.AllowAny,
    ]
    serializer_class = FacultadSerializer

class EncuestaViewSet(viewsets.ModelViewSet):
    queryset = Encuesta.objects.all()
    permission_classes = [
        IsAuthenticated,
        #permissions.AllowAny,
    ]
    serializer_class = EncuestaSerializer

class PermisosViewSet(viewsets.ModelViewSet):
    queryset = Permisos.objects.all()
    permission_classes = [
        IsAuthenticated,
        #permissions.AllowAny,
    ]
    serializer_class = PermisosSerializer

class EscuelaViewSet(viewsets.ModelViewSet):
    queryset = Escuela.objects.all()
    permission_classes = [
        IsAuthenticated,
        #permissions.AllowAny,
    ]
    serializer_class = EscuelaSerializer

class PreguntasViewSet(viewsets.ModelViewSet):
    queryset = Preguntas.objects.all()
    permission_classes = [
        IsAuthenticated,
        #permissions.AllowAny,
    ]
    serializer_class = PreguntasSerializer

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    permission_classes = [
        IsAuthenticated,
        #permissions.AllowAny,
    ]
    serializer_class = PerfilSerializer

class AlternativasViewSet(viewsets.ModelViewSet):
    queryset = Alternativas.objects.all()
    permission_classes = [
        IsAuthenticated,
       #permissions.AllowAny,
    ]
    serializer_class = AlternativasSerializer

class Preguntas_x_encuestaViewSet(viewsets.ModelViewSet):
    queryset = Preguntas_x_encuesta.objects.all()
    permission_classes = [
        IsAuthenticated,
        #permissions.AllowAny,
    ]
    serializer_class = Preguntas_x_encuestaSerializer

class Alternativas_x_preguntaViewSet(viewsets.ModelViewSet):
    queryset = Alternativas_x_pregunta.objects.all()
    permission_classes = [
        IsAuthenticated,
        #permissions.AllowAny,
    ]
    serializer_class = Alternativas_x_preguntaSerializer

class Datos_personalesViewSet(viewsets.ModelViewSet):
    queryset = Datos_personales.objects.all()
    permission_classes = [
        IsAuthenticated,
        #permissions.AllowAny,
    ]
    serializer_class = Datos_personalesSerializer 

class DetalleViewSet(viewsets.ModelViewSet):
    queryset = Detalle.objects.all()
    
    permission_classes = [
        IsAuthenticated,
        #permissions.AllowAny,
    ]
    serializer_class = DetalleSerializer

class AuthUserViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = AuthUserSerializer
