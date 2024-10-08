from django.db  import models

class Blog(models.Model):
    """
    Models documentation: https://docs.djangoproject.com/en/5.0/topics/db/models/?ref=mostlypython.com
    generate migration code via: python manage.py makemigrations blogs
    run migration code via: python manage.py migrate
    """
    # field for blog title corresponds to field in a database table
    title = models.CharField(max_length=200)
    # field for blog description
    description = models.TextField()
    # field for automatic blog timestamp
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """tells python how to represent this object as a string, such as in a terminal"""
        return self.title
    
class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:50]