from rest_framework import serializers
from api.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'translation', 'to_guess', 'text', 'answer']

    def create(self, validated_data):
        """
        Create and return a new `Question` instance, given the validated data.
        """
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Question` instance, given the validated data.
        """
        instance.translation = validated_data.get('translation', instance.translation)
        instance.to_guess = validated_data.get('to_guess', instance.to_guess)
        instance.text = validated_data.get('text', instance.text)
        instance.answer = validated_data.get('answer', instance.answer)
        instance.save()
        return instance