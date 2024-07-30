from django.db import models

class StatusChoices(models.TextChoices):
    PUBLISH = 'pb', 'Publish'
    DRAFT = 'df', 'Draft'

class MassaChoices(models.TextChoices):
    KG = 'kg', 'Kg'
    MG = 'mg', 'Mg'
    LG = 'lg', 'Lg'
    PC = 'pc', 'Piece'




