from django.db import models

def user_directory_path(instance, filename):
    ext = filename.split(".")
