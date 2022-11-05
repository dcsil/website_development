from djongo import models


# Create your models here.
class ModelStats(models.Model):
    followerCount = models.BigIntegerField(default=-1)
    followingCount = models.BigIntegerField(default=-1)
    heart = models.BigIntegerField(default=-1)
    heartCount = models.BigIntegerField(default=-1)
    videoCount = models.BigIntegerField(default=-1)
    diggCount = models.BigIntegerField(default=-1)

    class Meta:
        abstract = True


class Model(models.Model):
    id = models.CharField(max_length=300, default='DEFAULT VALUE')
    nickname = models.CharField(max_length=300, default='DEFAULT VALUE')
    avatar = models.TextField(default='DEFAULT VALUE')
    signature = models.CharField(max_length=500, default='DEFAULT VALUE')
    region = models.CharField(max_length=500, default='DEFAULT VALUE')
    stats = models.EmbeddedField(
        model_container=ModelStats, default='DEFAULT VALUE'
    )

    class Meta:
        abstract = True


class VideoListStats(models.Model):
    diggCount = models.BigIntegerField(default=-1)
    shareCount = models.BigIntegerField(default=-1)
    commentCount = models.BigIntegerField(default=-1)
    playCount = models.BigIntegerField(default=-1)

    class Meta:
        abstract = True


# class StringFd(models.Model):
#     stringfd = models.CharField(max_length=200)
#
#     class Meta:
#         abstract = True


class VideoList(models.Model):
    id = models.CharField(max_length=500, default='DEFAULT VALUE')
    description = models.TextField(default='DEFAULT VALUE')
    epoch_create_time = models.CharField(max_length=200, default='DEFAULT VALUE')
    create_location = models.CharField(max_length=300, default='DEFAULT VALUE')
    stats = models.EmbeddedField(
        model_container=VideoListStats, default='DEFAULT VALUE'
    )
    # label_list = models.ArrayField(
    #     model_container=StringFd,
    # )
    label_list = models.JSONField(default=['DEFAULT VALUE'])

    class Meta:
        abstract = True


class influencer_info(models.Model):
    # _id = models.ObjectIdField()
    url = models.TextField(default='DEFAULT VALUE')
    author_stats = models.EmbeddedField(
        model_container=Model, default='DEFAULT VALUE'
    )
    video_list = models.ArrayField(
        model_container=VideoList, default='DEFAULT VALUE'
    )

    # _id: ObjectId('')
    # url = ""
    # author_stats: Object
    #     id: ""
    #     nickname: ""
    #     avatar: ""
    #     signature: ""
    #     region: ""
    #     stats: Object
    #         followerCount: int
    #         followingCount: int
    #         heart: int
    #         heartCount: int
    #         videoCount: int
    #         diggCount: int
    # video_list: Array
    #     0: Object
    #         id: ""
    #         description: ""
    #         epoch_create_time: ""
    #         create_location:""
    #         stats: Object
    #             diggCount: int
    #             shareCount: int
    #             commentCount: int
    #             playCount: int
    #         label_list: Array (can be empty)
    #             0: ""
    #             1: ""
    #             ...
    #     1:
    #     ...
    #     29:


# class user_info(models.Model):

