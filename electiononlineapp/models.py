"""Models for election online application."""

# pylint: disable=no-member, too-few-public-methods

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """User profile model storing registration type."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    regtype = models.CharField(
        max_length=20,
        choices=[
            ('Admin', 'Admin'),
            ('Student', 'Student'),
        ],
    )

    def __str__(self) -> str:
        return str(self.user.username)


class Position(models.Model):
    """Election position model."""

    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)


class Candidate(models.Model):
    """Candidate model representing contestants for a position."""

    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name='candidates',
    )
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.name)


class Vote(models.Model):
    """Vote model storing which user voted for which candidate."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    class Meta:
        """Meta configuration for Vote model."""

        unique_together = ('user', 'position')

    def __str__(self) -> str:
        return f"{self.user.username} - {self.position.name}"
        