# publications/serializers.py

from rest_framework import serializers
from .models import Publication
from projects.models import ResearchProject
from users.models import User

class PublicationSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    project = serializers.PrimaryKeyRelatedField(queryset=ResearchProject.objects.all())

    class Meta:
        model = Publication
        fields = [
            'id',
            'title',
            'abstract',
            'doi',
            'co_authors',
            'publication_date',
            'file',
            'project',
            'created_by',
            'created_at',
        ]
        read_only_fields = ['created_by', 'created_at']

    def create(self, validated_data):
        """Attach current user as the creator"""
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
