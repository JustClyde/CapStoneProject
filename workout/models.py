from django.db import models

class Workout(models.Model):
    EXERCISE_CHOICES = [
        ('CARDIO', 'Cardio'),
        ('STRENGTH', 'Strength Training'),
        ('FLEXIBILITY', 'Flexibility'),
        ('BALANCE', 'Balance Training'),
        ('OTHER', 'Other'),
    ]

    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    calories_burned = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)
    exercise_type = models.CharField(max_length=20, choices=EXERCISE_CHOICES, default='OTHER')

    def __str__(self):
        return f"{self.name} - {self.get_exercise_type_display()}"