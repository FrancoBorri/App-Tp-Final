from rest_framework import serializers
from ..models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ["id"]
        extra_kwargs = {
            "review_text": {"write_only": True},
            "rating": {"write_only": True},
        }

        def validate_review_text(self, value):
            """
            Validate that the review text is not empty.
            """
            if not value.strip():
                raise serializers.ValidationError("Review cannot be empty.")
            return value

        def validate_rating(self, value):
            if value < 0:
                raise serializers.ValidationError("Rating cannot be negative")
            if value > 5:
                raise serializers.ValidationError("Rating cannot be grater than 5")
            return value

        def create(self, validated_data):
            """
            Create a new review with the provided validated data.
            """
            return Review.objects.create(**validated_data)

        def update(self, instance, validated_data):
            """
            Update review with the provided validated data.
            """
            for key, attr in validated_data.items():
                setattr(instance, key, attr)
            instance.save()
            return instance
