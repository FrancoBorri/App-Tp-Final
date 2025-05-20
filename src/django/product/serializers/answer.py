from rest_framework import serializers
from ..models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
        read_only_fields = ["id"]
        extra_kwargs = {
            "answer_text": {"required": True},
        }

        def validate_answer(self, value):
            """
            Validate answer text is not empty.
            """
            if not value:
                raise serializers.ValidationError("Answer cannot be empty")
            return value

        def create(self, validated_data):
            """
            Create a new answer text with the provided validated data.
            """
            return Answer.objects.create(**validated_data)

        def update(self, instance, validated_data):
            """
            Update answer text with the provided validated data.
            """
            instance.answer_text = validated_data.get(
                "answer_text", instance.answer_text
            )
            instance.save()
            return instance
