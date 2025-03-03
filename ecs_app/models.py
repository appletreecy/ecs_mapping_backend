from django.db import models

class ECSMapping(models.Model):
    log_field = models.CharField(max_length=255, unique=True)
    ecs_field = models.CharField(max_length=255)
    embedding = models.BinaryField() # Store FAISS embedding as binary

    def __str__(self):
        return f"{self.log_field} -> {self.ecs_field}"
