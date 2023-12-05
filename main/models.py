from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    svg_icon = models.CharField(max_length=20)
    description_top_image = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "service"
        ordering = ["-id"]