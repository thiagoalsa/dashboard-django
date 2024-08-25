from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser

# Custom user manager for handling the creation of users and superusers.
class UserManager(BaseUserManager):
    use_in_migrations = True  # Ensures this manager can be used during migrations.

    # Internal method to create a user with an email and password.
    def _create_user(self, email, password, **extra_fields):
        if not email:  # Checks if the email is provided.
            raise ValueError('Email is required')  # Raises an error if no email is given.
        email = self.normalize_email(email)  # Normalizes the email address.
        user = self.model(email=email, username=email, **extra_fields)  # Creates a new user instance with the provided email and additional fields.
        user.set_password(password)  # Hashes and sets the user's password.
        user.save(using=self._db)  # Saves the user to the database.
        print(user)
        return user  # Returns the created user object.

    # Public method to create a regular user.
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)  # Ensures that a regular user is not a superuser.
        print(self._create_user(email, password, **extra_fields))
        return self._create_user(email, password, **extra_fields)  # Calls the internal user creation method.

    # Public method to create a superuser (admin).
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)  # Ensures that the superuser has is_superuser set to True.
        extra_fields.setdefault('is_staff', True)  # Ensures that the superuser has is_staff set to True.

        if extra_fields.get('is_superuser') is not True:  # Checks if is_superuser is properly set.
            raise ValueError('Superuser must have is_superuser=True')  # Raises an error if not set.

        if extra_fields.get('is_staff') is not True:  # Checks if is_staff is properly set.
            raise ValueError('Superuser must have is_staff=True')  # Raises an error if not set.
        print(self._create_user(email, password, **extra_fields))
        return self._create_user(email, password, **extra_fields)  # Calls the internal user creation method for the superuser.


# Custom user model that extends the default Django user model.
class CustomUser(AbstractUser):
    email = models.EmailField('E-mail', unique=True)  # Adds an email field that must be unique for each user.

    USERNAME_FIELD = 'email'  # Specifies that the email will be used as the unique identifier (instead of username).
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Defines required fields that must be provided when creating a user.

    def __str__(self):  # String representation of the user object.
        return self.email  # Returns the email as the string representation.

    objects = UserManager()  # Assigns the custom user manager to the model.