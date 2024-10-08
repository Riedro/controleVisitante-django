from django.db import models # type: ignore
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager) # type: ignore
 
class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None):
        usuario = self.model(
            email = self.normalize_email(email)
        )
        usuario.is_active = True
        usuario.is_staff = False    
        usuario.is_superuser = False

        if password:
            usuario.set_password(password) 

        usuario.save()
        return usuario
# superUser
    def create_superuser(self, email, password):
        usuario = self.create_user(
            email = self.normalize_email(email),
            password = password,
            )
        
        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        if password:
            usuario.set_password(password) 

        usuario.save()
        return usuario

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='E-mail do usuário', max_length=200, unique=True)
    is_active = models.BooleanField(verbose_name='Usuário está ativo.', default=True)
    is_staff = models.BooleanField(verbose_name='Usuário da equipe de desenvolvimento', default=False)
    is_superuser = models.BooleanField(verbose_name='Usuário é um super usuário.', default=False)

    USERNAME_FIELD = 'email'
    objects = UsuarioManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuario'

        def __str__(self):
            return self.email
 

