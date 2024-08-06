class Recipe:
    def __init__(self, name, author, recipe_type, description, ingredients, cuisine, youtube_link=None):
        self.name = name
        self.author = author
        self.recipe_type = recipe_type
        self.description = description
        self.ingredients = ingredients
        self.cuisine = cuisine
        self.youtube_link = youtube_link

class RecipeView:
    def display_recipe(self, recipe):
        print(f"Название рецепта: {recipe.name}")
        print(f"Автор рецепта: {recipe.author}")
        print(f"Тип рецепта: {recipe.recipe_type}")
        print(f"Описание рецепта: {recipe.description}")
        print(f"Ингредиенты: {', '.join(recipe.ingredients)}")
        print(f"Кухня: {recipe.cuisine}")
        if recipe.youtube_link:
            print(f"Ссылка на рецепт: {recipe.youtube_link}")

class RecipeController:
    def __init__(self, recipe, view):
        self.recipe = recipe
        self.view = view

    def update_recipe(self, name=None, author=None, recipe_type=None, description=None, ingredients=None, cuisine=None, youtube_link=None):
        if name:
            self.recipe.name = name
        if author:
            self.recipe.author = author
        if recipe_type:
            self.recipe.recipe_type = recipe_type
        if description:
            self.recipe.description = description
        if ingredients:
            self.recipe.ingredients = ingredients
        if cuisine:
            self.recipe.cuisine = cuisine
        if youtube_link:
            self.recipe.youtube_link = youtube_link

    def display_recipe(self):
        self.view.display_recipe(self.recipe)

# Пример
recipe = Recipe("Борщ", "Иван Иванов", "Первое блюдо", "Очень вкусный борщ", ["свекла", "картошка", "морковь"], "украинская")
view = RecipeView()
controller = RecipeController(recipe, view)

controller.display_recipe()

controller.update_recipe(author="Петр Петров", description="Очень вкусный и полезный борщ")
controller.display_recipe()