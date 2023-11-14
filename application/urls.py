from rest_framework import routers
from .views import *
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *
from application import views

router = routers.DefaultRouter()
router.register('api/temas', views.TemasViewSet, basename='tema')
router.register('api/tipo_alternativa', views.Tipo_alternativaViewSet, basename='tipo_alternativa')
router.register('api/tipo_encuesta', views.Tipo_encuestaViewSet, basename='tipo_encuesta')
router.register('api/modulos', views.ModulosViewSet, basename='modulo')
router.register('api/facultad', views.FacultadViewSet, basename='facultad')
router.register('api/encuesta', views.EncuestaViewSet, basename='encuesta')
router.register('api/permisos', views.PermisosViewSet, basename='permiso')
router.register('api/escuela', views.EscuelaViewSet, basename='escuela')
router.register('api/preguntas', views.PreguntasViewSet, basename='pregunta')
router.register('api/perfil', views.PerfilViewSet, basename='perfil')
router.register('api/alternativas', views.AlternativasViewSet, basename='alternativa')
router.register('api/preguntas_x_encuesta', views.Preguntas_x_encuestaViewSet, basename='pregunta_x_encuesta')
router.register('api/alternativas_x_pregunta', views.Alternativas_x_preguntaViewSet, basename='alternativa_x_pregunta')
router.register('api/datospersonales', views.Datos_personalesViewSet,
                basename='datos_personales')
router.register('api/detalle', views.DetalleViewSet, basename='detalle')
router.register('api/usuarios', views.AuthUserViewSet, basename='usuario')

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]