from rest_framework import serializers

from .models import Todo, Label


class TodoSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(many=True, read_only=True)
    label_input = serializers.ListField(
        child=serializers.CharField(),
        allow_empty=True, required=False,  write_only=True,
    )

    class Meta:
        model = Todo
        fields = ('task', 'label', 'label_input')

    def create(self, validated_data):
        label_inputs = validated_data.pop('label_input', [])

        obj = super().create(validated_data)

        for label_input in label_inputs:
            label, _ = Label.objects.get_or_create(name=label_input)
            obj.label.add(label)

        return obj
