from django.db import models

# Create your models here.
class Book(models.Model):
   title = models.CharField(max_length=100)
   author = models.CharField(max_length=100)
   published_date = models.DateField()
   
   
   def __str__(self):
       return self.title
   













   
#    
# class StreamPlatform(models.Model):
#     name = models.CharField(max_length=100)
#     about = models.TextField()
#     website = models.URLField(max_length=100)

#     def __str__(self):
#         return self.name

# class WatchList(models.Model):
#     title = models.CharField(max_length=100)
#     storyline = models.TextField()
#     platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.title

# class Review(models.Model):
#     review_user = models.ForeignKey('User', on_delete=models.CASCADE)
#     rating = models.PositiveIntegerField()
#     description = models.TextField()
#     watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
#     active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return str(self.rating)