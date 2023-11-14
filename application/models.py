from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class AuthUser(AbstractUser):
    # Tus campos personalizados

    perfil = models.ForeignKey(
        'Perfil',  # Nombre del modelo relacionado en forma de cadena
        on_delete=models.CASCADE,
        related_name='usuarios',
        blank=True,
        null=True,
    )

    # # Añade estos atributos para evitar el conflicto con los atributos de AbstractUser
    groups = None
    user_permissions = None

class Temas(models.Model):
    id_tema = models.AutoField (primary_key=True)
    descripcion = models.CharField(max_length=250)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'temas'

class Tipo_alternativa(models.Model):
    id_tipo_alternativa = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=250)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'tipo_alternativa'

class Tipo_encuesta(models.Model):
    id_tipo_encuesta = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=250)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'tipo_encuesta'

class Modulos(models.Model):
    id_modulo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=250)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'modulos'

class Facultad(models.Model):
    id_facultad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'facultad'

class Encuesta(models.Model):
    id_encuesta = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=250)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_inicio = models.DateField(default=None, null=True, blank=True)
    fecha_fin = models.DateField(default=None, null=True, blank=True)
    autor = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    id_tipo_encuesta = models.ForeignKey(Tipo_encuesta, models.DO_NOTHING, db_column='id_tipo_encuesta')

    class Meta:
        db_table = 'encuesta'

class Permisos(models.Model):
    id_permiso = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=250)
    estado = models.BooleanField(default=True)
    id_modulo = models.ForeignKey(Modulos, models.DO_NOTHING, db_column='id_modulo')

    class Meta:
        db_table = 'permisos'

class Escuela(models.Model):
    id_escuela = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    id_facultad = models.ForeignKey(Facultad, models.DO_NOTHING, db_column='id_facultad')

    class Meta:
        db_table = 'escuela'

class Preguntas(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=300)
    estado = models.BooleanField(default=True)
    id_tema = models.ForeignKey(Temas, models.DO_NOTHING, db_column='id_tema')

    class Meta:
        db_table = 'preguntas'

class Perfil(models.Model):
    id_perfil = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=250)
    estado = models.BooleanField(default=True)
    id_permiso = models.ForeignKey(Permisos, models.DO_NOTHING, db_column='id_permiso')

    class Meta: 
        db_table = 'perfil'

class Alternativas(models.Model):
    id_alternativa = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=250)
    estado = models.BooleanField(default=True)
    id_tipo_alternativa = models.ForeignKey(Tipo_alternativa, models.DO_NOTHING, db_column='id_tipo_alternativa')
    value = models.IntegerField(default=0)

    class Meta:
        db_table = 'alternativas'

class Preguntas_x_encuesta(models.Model):
    id_pregunta_x_encuesta = models.AutoField(primary_key=True)
    estado = models.BooleanField(default=True)
    id_encuesta = models.ForeignKey(Encuesta, models.DO_NOTHING, db_column='id_encuesta')
    id_pregunta = models.ForeignKey(Preguntas, models.DO_NOTHING, db_column='id_pregunta')

    class Meta:
        db_table = 'preguntas_x_encuesta'

class Alternativas_x_pregunta(models.Model):
    id_alternativa_x_pregunta = models.AutoField(primary_key=True)
    estado = models.BooleanField(default=True)
    id_pregunta_x_encuesta = models.ForeignKey(Preguntas_x_encuesta, models.DO_NOTHING, db_column='id_pregunta_x_encuesta')
    id_alternativa = models.ForeignKey(Alternativas, models.DO_NOTHING, db_column='id_alternativa')

    class Meta:
        db_table = 'alternativas_x_pregunta'

class Datos_personales(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=8)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    edad = models.PositiveSmallIntegerField(default=0)
    sexo = models.CharField(max_length=20)
    estado_civil = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(default=None, null=True, blank=True)
    grado_instruccion = models.IntegerField(default=1)
    ocupacion = models.CharField(max_length=20)
    anio_ingreso = models.IntegerField(default=0)
    direccion_actual = models.CharField(max_length=50)
    numero_celular = models.IntegerField(default=0)
    vive_con = models.CharField(max_length=20)
    numero_de_hermanos = models.IntegerField(default=0)
    apoderado = models.CharField(max_length=50)
    numero_celular_apoderado = models.IntegerField(default=0)
    beneficio = models.CharField(max_length=30)
    religion = models.CharField(max_length=30)
    estado = models.BooleanField(default=True)
    id_escuela = models.ForeignKey(Escuela, models.DO_NOTHING, db_column='id_escuela')
    id_auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_auth_user')
    
    class Meta:
        db_table = 'datos_personales'

class Detalle(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    numero_intentos = models.IntegerField(default=0)
    estado = models.BooleanField(default=True)
    id_auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_auth_user')   
    id_alternativa_x_pregunta = models.ForeignKey(Alternativas_x_pregunta, models.DO_NOTHING, db_column='id_alternativa_x_pregunta')

    class Meta:
        db_table = 'detalle'