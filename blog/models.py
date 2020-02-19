from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='image/')


    #in admin returns the title of the blog
    def __str__(self):
        return self.title
        

    #returns a new body with 25 characters 
    def summary(self):
        return self.body[:50]


    #returns a string with date, day and year
    def pub_date_time(self):
        return self.pub_date.strftime('%b %e %Y')