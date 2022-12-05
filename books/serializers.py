from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        book = Book.objects.create(owner=user, **validated_data)

        return book
