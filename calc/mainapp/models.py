from django.db import models
from uuid import uuid4


class ModelControlActions(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=64)
    designation = models.CharField(max_length=64, verbose_name='обозначение')


class Cell_names(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    model = models.ForeignKey(ModelControlActions, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, unique=True)


class Equilibrium(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    model_name = models.ForeignKey(ModelControlActions, on_delete=models.CASCADE, related_name="model")
    cell_name = models.ForeignKey(ModelControlActions, on_delete=models.CASCADE, related_name="cell")
    value = models.DecimalField(max_digits=20, decimal_places=20, verbose_name='значение')
