from rest_framework import serializers
from .models import Group, Post, Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    # group = serializers.PrimaryKeyRelatedField(
    #     queryset=Group.objects.all(),
    #     allow_null=True,
    #     default=None
    # )

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')
        read_only_fields = ('author',)
        extra_kwargs = {
            'group': {
                'queryset': Group.objects.all(),
                'allow_null': True,
                'default': None
            }
        }


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    # post = serializers.PrimaryKeyRelatedField(
    #     read_only=True,
    #     pk_field=serializers.IntegerField()
    # )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        extra_kwargs = {
            'post': {
                'required': False,
                'read_only': False
            }
        }
