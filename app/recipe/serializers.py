from rest_framework import serializers

from core.models import Tag, Ingredient, Recipe


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('name', 'id')
        read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):

    # check mikne aslan aya in idiye dar tags ya ingredients vojod darad ya na
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all(),
    )

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_miniutes', 'price', 'link', 'ingredients', 'tags']
        read_only_fields = ('id',)


class RecipeDetailSerializer(RecipeSerializer):

    ingredients = IngredientSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

