from django.db import models
from django.contrib.auth.models import User

# Model for the extended Django user class. This model extends the default Django userclass to store the users toto points.
class UserTotoInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    toto_points = models.DecimalField(decimal_places=2, max_digits=9999, default=50.00)

    def __str__(self):
        return self.user.username
