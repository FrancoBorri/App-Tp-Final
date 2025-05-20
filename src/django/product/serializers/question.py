from rest_framework import serializers
from ..models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
        read_only_fields = ["id"]
        extra_kwargs = {"question_text": {"write_only": True}}

        def validate_question(self, value):
            """
            Validate that the question is not empty.
            """
            if not value.strip():
                raise serializers.ValidationError("Question cannot be empty.")
            return value

        def create(self, validated_data):
            """
            Create a new question with the provided validated data.
            """
            return Question.objects.create(**validated_data)

        def update(self, instance, validated_data):
            """
            Update question with the provided validated data.
            """
            for key, attr in validated_data.items():
                setattr(instance, key, attr)
            instance.save()
            return instance
