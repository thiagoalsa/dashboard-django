from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser

# Gerenciador de usuários personalizados para lidar com a criação de usuários e superusuários.
class UserManager(BaseUserManager):
    use_in_migrations = True  # Garante que este gerenciador pode ser usado durante as migrações.

    # Método interno para criar um usuário com email e senha.
    def _create_user(self, email, password, **extra_fields):
        if not email:  # Verifica se o e-mail foi fornecido.
            raise ValueError('O e-mail é obrigatório')  # Lança um erro se o e-mail não foi informado.
        email = self.normalize_email(email)  # Normaliza o endereço de e-mail.
        user = self.model(email=email, username=email, **extra_fields)  # Cria uma nova instância de usuário com o e-mail e campos adicionais fornecidos.
        user.set_password(password)  # Criptografa e define a senha do usuário.
        user.save(using=self._db)  # Salva o usuário no banco de dados.
        print(user)
        return user  # Retorna o objeto do usuário criado.

    # Método público para criar um usuário regular.
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)  # Garante que um usuário regular não seja um superusuário.
        print(self._create_user(email, password, **extra_fields))
        return self._create_user(email, password, **extra_fields)  # Chama o método interno de criação de usuário.

    # Método público para criar um superusuário (admin).
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)  # Garante que o superusuário tenha is_superuser definido como True.
        extra_fields.setdefault('is_staff', True)  # Garante que o superusuário tenha is_staff definido como True.

        if extra_fields.get('is_superuser') is not True:  # Verifica se is_superuser está devidamente configurado.
            raise ValueError('O superusuário deve ter is_superuser=True')  # Lança um erro se não estiver configurado.

        if extra_fields.get('is_staff') is not True:  # Verifica se is_staff está devidamente configurado.
            raise ValueError('O superusuário deve ter is_staff=True')  # Lança um erro se não estiver configurado.
        print(self._create_user(email, password, **extra_fields))
        return self._create_user(email, password, **extra_fields)  # Chama o método interno de criação de superusuário.


# Modelo de usuário personalizado que estende o modelo de usuário padrão do Django.
class CustomUser(AbstractUser):
    email = models.EmailField('E-mail', unique=True)  # Adiciona um campo de e-mail que deve ser único para cada usuário.

    USERNAME_FIELD = 'email'  # Especifica que o e-mail será usado como identificador único (em vez de username).
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Define os campos obrigatórios que devem ser fornecidos ao criar um usuário.

    def __str__(self):  # Representação em string do objeto usuário.
        return self.email  # Retorna o e-mail como a representação em string.

    objects = UserManager()  # Atribui o gerenciador de usuários personalizados ao modelo.


class Product(models.Model):
    product_name = models.CharField('Produto', max_length=100)  # Campo de nome do produto com no máximo 100 caracteres.
    quantity = models.IntegerField('Quantidade')  # Campo de quantidade do produto.
