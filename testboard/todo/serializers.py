from rest_framework import serializers

from .models import Todo, Label


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ('name',)


class TodoSerializer(serializers.ModelSerializer):
    label = LabelSerializer(many=True)

    class Meta:
        model = Todo
        fields = ('task', 'label')

    def create(self, validated_data):
        labels = validated_data.pop('label', [])

        obj = super().create(validated_data)

        for label in labels:
            label_name = label.get('name')
            label, _ = Label.objects.get_or_create(name=label_name)
            obj.label.add(label)

        return obj
