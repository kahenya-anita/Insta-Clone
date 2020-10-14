from django.db import models
from django.contrib.models import User
from django.models.signals importpost_save
from django.utils.text import slugfy
from django.urls import reverse

def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id, fileame)
class Tag(models.Model):
    title = models.CharField(max_length=75, verbose_name='Tag')
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name_plural='Tags'


    def get_absolute_url(self):
        return reverse('tags',arg=[self.slug])

    def __str__(self):
        self.title

    def save(self,*args,**kwargs)

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    picture = models.ImageField(upload_to=user_directory_path, verbose_name='Picture', null=False)
    caption = models.TextField(max_length=1500, verbose_name='Caption')
    posted = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag,related_name='tags')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField()

    def get_absolute_url(self):
        return reverse('postdetails', args=[str(self.id)])

    def __str__(self):
    return self.posted

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')

class Stream(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stream_following')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def add_post(sender, instance, *args, **kwargs):
        post = instance
        user = post.user
        followers = Follow.objects.all().filter(following=user)
        for follower i n followers:
            stream = Stream(post=post, user=follower.follower, date=post.posted, following=user)
            stream.save()


post_save.connect(Stream.add_post, sender=Post)