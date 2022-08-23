from uuid import uuid4
from rest_framework.serializers import HyperlinkedModelSerializer
from mainapp.models import ModelControlActions, Cell_names, Equilibrium
from rest_framework import serializers

from mainapp.parcer import control_actions_dict


class ModelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    designation = serializers.CharField(max_length=64)

    def create(self, validated_data):
        return ModelControlActions(**validated_data)

    def update(self, instance, validated_data):
        instance.uid = validated_data.get('uid', instance.name)
        instance.name = validated_data.get('name', instance.name)
        instance.name = validated_data.get('designation', instance.name)
        return instance

# Создаем
# data = {'name': 'Курс RUB/USD', 'designation': 'ER_0'}
# serializer = ModelSerializer(data=data)
# serializer.is_valid()
# model = serializer.save
# в base хранится {'name': 'Курс RUB/USD', 'designation': 'ER'}

# # Изменяем
# new_data = {'name': 'Курс RUB/USD', 'designation': 'ER_0'}
# serializer = ModelSerializer(model, data=new_data)
# serializer.is_valid()
# new_base = serializer.save


queryset = ModelControlActions.objects.all(control_actions_dict)
serializer = ModelSerializer(queryset, many=True)
serializer.data




# class ModelSerializer(HyperlinkedModelSerializer):
#     class Meta:
#         model = ModelControlActions
#         fields = '__all__'

class CellnameSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Cell_names
        fields = '__all__'

class EquilibriumSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Equilibrium
        fields = '__all__'










# class ModelSerializer(serializers.Serializer):
#     uid = models.UUIDField(primary_key=True, default=uuid4)
#     name = models.CharField(max_length=64)
#
#     def create(self, validated_data):
#         return Model(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.uid = validated_data.get('uid', instance.name)
#         instance.name = validated_data.get('name', instance.name)
#         return instance

#     def validate_value(self, value):
#         if value < 0:
#             raise serializers.ValidationError(f'Значение не может быть отрицательным')
#         return value
#
#     def validate(self, attrs):
#         if attrs['name'] == 'Пушкин' and attrs['birthday_year'] != 1799:
#             raise serializers.ValidationError('Неверный год рождения Пушкина')
#         return attrs



