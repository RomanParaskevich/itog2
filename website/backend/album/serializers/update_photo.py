from rest_framework import serializers
from ..models import Photo, Tag
from .tag import TagSerializer


class UpdatePhotoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Photo
        fields = ('title', 'tags')

    def create_or_update_tags(self, tags):
        tag_ids = []
        for tag in tags:
            tag_instance, created = Tag.objects.update_or_create(name=tag.get('name'), defaults=tag)
            tag_ids.append(tag_instance.id)
        return tag_ids

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', [])
        instance.tags.set(self.create_or_update_tags(tags))
        try:
            setattr(instance, 'title', validated_data['title'])
        except KeyError:
            pass
        instance.save()
        return instance
