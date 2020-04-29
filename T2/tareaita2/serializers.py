from rest_framework import serializers
from .models import Hamburguesa, Ingrediente





class HamburguesaSerializer(serializers.ModelSerializer):
    # ingredientes = IngredientsEnHamburguesaSerializer(read_only=True, many=True)
    class Meta:
        model = Hamburguesa
        fields = ['id','nombre', 'precio', 'descripcion', 'imagen', 'ingredientes']
        #fields = '__all__'
    # def create(self, validated_data):
    #     print(validated_data)
        # ingredientes_data = validated_data.pop('ingredientes')
        # hamburguesa = Hamburguesa.objects.create(**validated_data)
        # for ingrediente_data in ingredientes_data:
        #     IngredienteEnHamburguesa.objects.create(path=hamburguesa)
        # return hamburguesa


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        #fields = ['nombre', 'precio', 'descripcion', 'imagen', 'ingredientes']
        fields = '__all__'