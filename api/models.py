from django.db import models

class Question(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    translation = models.CharField(max_length=100, blank=False)
    to_guess = models.CharField(max_length=100, blank=False)
    text = models.CharField(max_length=100, blank=True, default='')

    class TONES_CHOICES(models.IntegerChoices):
        ZERO = 0, "Mid tone"
        ONE = 1, "Low tone"
        TWO = 2, "Falling tone"
        THREE = 3, "High tone"
        FOUR = 4, "Rising tone"

    answer = models.CharField(
        max_length=5,
        choices=TONES_CHOICES.choices,
    )

    class Meta:
        ordering = ['created']
