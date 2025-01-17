#from django.shortcuts import render
#from rest_framework import generics
from django.contrib.auth.models import User #we will use this for user instead of using it from the database since django handles users
from django.contrib.auth import get_user_model
from .models import AllRecipe, Diet, Favorite, Partner, Recipe  # Include all models
from .serializers import UserSerializer, RecipeSerializer, AllRecipeSerializer, DietSerializer, FavoriteSerializer, PartnerSerializer
from rest_framework import viewsets
# Create your views here.
 #user views 

User = get_user_model()

# User views
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all() 
    serializer_class = UserSerializer

# Recipe views
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

# AllRecipe views
class AllRecipeViewSet(viewsets.ModelViewSet):
    queryset = AllRecipe.objects.all()
    serializer_class = AllRecipeSerializer

# Diet views
class DietViewSet(viewsets.ModelViewSet):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer

# Favorite views
class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

# Partner views
class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

''' 
we cant use ingredient yet because our database doesnt have ingredients therefore neither does our models
#ingredient views
class IngredientListCreateView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
'''