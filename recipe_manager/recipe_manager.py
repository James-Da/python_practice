from pathlib import Path
import os

# Define the path to the recipes directory
RECIPES_PATH = Path("C:\\Users\\Bruker\\PycharmProjects\\TotalPython\\Challenges\\recipe_manager\\recipes")


def count_recipes(path):
    """Count the number of recipe files in the given path"""
    return len(list(Path(path).glob('**/*.txt')))


def clear_console():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    """Print the header for the recipe administrator"""
    print('*' * 50)
    print('*' * 5 + " Welcome to the recipe administrator " + '*' * 5)
    print('*' * 50)
    print('\n')


def print_menu():
    """Print the menu options"""
    print("Choose an option: ")
    print('''
    [1] - Read recipe
    [2] - Create new recipe
    [3] - Create new category
    [4] - Delete recipe
    [5] - Delete category
    [6] - Exit''')


def validate_menu_choice(menu_choice):
    """Validate if the menu choice is a valid option"""
    return menu_choice.isnumeric() and int(menu_choice) in range(1, 7)


def get_menu_choice():
    """Get a valid menu choice from the user"""
    menu_choice = input()
    while not validate_menu_choice(menu_choice):
        print("Invalid choice. Please enter a valid option.")
        menu_choice = input()
    return int(menu_choice)


def print_categories(path):
    """Print the available categories in the given path"""
    print("Categories:")
    categories_path = Path(path)
    categories_list = list(categories_path.iterdir())
    for i, folder in enumerate(categories_list, start=1):
        print(f"[{i}] - {folder.name}")
    return categories_list


def choose_category(a_list):
    """Choose a category from the provided list"""
    while True:
        choice = input("\nChoose a category: ")
        if choice.isnumeric() and int(choice) in range(1, len(a_list) + 1):
            return a_list[int(choice) - 1]
        print("Invalid choice. Please enter a valid option.")


def print_recipes(path):
    """Print the available recipes in the given path"""
    print("These are the recipes:")
    recipes_path = Path(path)
    recipes_list = list(recipes_path.glob('*.txt'))
    for i, recipe in enumerate(recipes_list, start=1):
        print(f"[{i}] - {recipe.name}")
    return recipes_list


def choose_recipe(a_list):
    """Choose a recipe from the provided list"""
    while True:
        choice = input('Choose a recipe: ')
        if choice.isnumeric() and int(choice) in range(1, len(a_list) + 1):
            return a_list[int(choice) - 1]
        print("Invalid choice. Please enter a valid option.")


def read_recipe(recipe):
    """Read and print the content of a recipe file"""
    print(recipe.read_text())


def create_recipe(path):
    """Create a new recipe file in the provided path"""
    while True:
        print("Write the name of your recipe: ")
        recipe_name = input() + '.txt'
        new_path = Path(path, recipe_name)

        if not new_path.exists():
            print("Write your new recipe (Press Enter to finish): ")
            recipe_content = []
            while True:
                line = input()
                if not line:
                    break
                recipe_content.append(line)
            new_path.write_text('\n'.join(recipe_content))
            print(f"Your recipe {recipe_name} has been created")
            break
        else:
            print("Sorry, that recipe already exists")


def create_category(path):
    """Create a new category directory in the provided path"""
    while True:
        print("Write the name of the new category: ")
        category_name = input()
        new_path = Path(path, category_name)

        if not new_path.exists():
            new_path.mkdir()
            print(f"Your new category {category_name} has been created")
            break
        else:
            print("Sorry, that category already exists")


def delete_recipe(recipe):
    """Delete a recipe file"""
    recipe.unlink()
    print(f"The recipe {recipe.name} has been deleted")


def delete_category(category):
    """Delete a category directory"""
    category.rmdir()
    print(f"The category {category.name} has been removed")


def return_to_menu():
    """Wait for user input to return to the menu"""
    input("\nPress Enter to return to the menu: ")


def start():
    clear_console()
    print_header()
    print(f'The recipes are in {RECIPES_PATH}')
    print(f'Total recipes: {count_recipes(RECIPES_PATH)}')

    while True:
        print_menu()
        menu_choice = get_menu_choice()

        if menu_choice == 1:
            categories = print_categories(RECIPES_PATH)
            if not categories:
                print("There are no categories.")
                return_to_menu()
                continue
            category = choose_category(categories)
            recipes = print_recipes(category)
            if not recipes:
                print("There are no recipes in this category.")
                return_to_menu()
                continue
            recipe = choose_recipe(recipes)
            read_recipe(recipe)
            return_to_menu()

        elif menu_choice == 2:
            categories = print_categories(RECIPES_PATH)
            if not categories:
                print("There are no categories.")
                return_to_menu()
                continue
            category = choose_category(categories)
            create_recipe(category)
            return_to_menu()

        elif menu_choice == 3:
            create_category(RECIPES_PATH)
            return_to_menu()

        elif menu_choice == 4:
            categories = print_categories(RECIPES_PATH)
            if not categories:
                print("There are no categories.")
                return_to_menu()
                continue
            category = choose_category(categories)
            recipes = print_recipes(category)
            if not recipes:
                print("There are no recipes in this category.")
                return_to_menu()
                continue
            recipe = choose_recipe(recipes)
            delete_recipe(recipe)
            return_to_menu()

        elif menu_choice == 5:
            categories = print_categories(RECIPES_PATH)
            if not categories:
                print("There are no categories.")
                return_to_menu()
                continue
            category = choose_category(categories)

            try:
                delete_category(category)
            except OSError:  # If category directory is not empty
                print("Please remove recipes from category before deleting")
            finally:
                return_to_menu()

        elif menu_choice == 6:
            print("Ending program...")
            break


start()
