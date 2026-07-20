from django.db import models

class coment(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=70)
    email = models.EmailField()
    tiltle = models.CharField(max_length=100)
    discribshen = models.TextField()

    def __str__(self):
        return self.name

class Reply(models.Model):
    comment = models.ForeignKey(coment, on_delete=models.CASCADE, related_name='replies')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ریپلای به {self.comment.name}"