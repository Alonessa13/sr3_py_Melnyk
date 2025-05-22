import json  # модуль для роботи з JSON
import os    # модуль для перевірки існування файлу

# Клас Movie описує окремий фільм
class Movie:
    def __init__(self, title, genre, year, rating):
        self.title = title      # Назва фільму
        self.genre = genre      # Жанр фільму
        self.year = year        # Рік виходу
        self.rating = rating    # Рейтинг (наприклад, від 1 до 10)

    # Перетворення фільму в словник (для збереження у JSON)
    def to_dict(self):
        return {
            "title": self.title,
            "genre": self.genre,
            "year": self.year,
            "rating": self.rating
        }

# Список для зберігання фільмів
movies = []

# Завантаження фільмів з файлу, якщо такий існує
def load_movies():
    if os.path.exists("movies.json"):
        with open("movies.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data:
                # Створюємо об'єкти фільмів із словників
                movie = Movie(item["title"], item["genre"], item["year"], item["rating"])
                movies.append(movie)

# Збереження всіх фільмів у JSON-файл
def save_movies():
    with open("movies.json", "w", encoding="utf-8") as f:
        json.dump([m.to_dict() for m in movies], f, ensure_ascii=False, indent=4)

# Додати новий фільм
def add_movie():
    title = input("Назва фільму: ")
    genre = input("Жанр: ")
    year = int(input("Рік: "))
    rating = float(input("Рейтинг (0-10): "))
    movie = Movie(title, genre, year, rating)
    movies.append(movie)
    print("Фільм додано!")

# Фільтрація фільмів за жанром
def filter_by_genre(genre):
    return [m for m in movies if m.genre.lower() == genre.lower()]

# Сортування фільмів за рейтингом (від найвищого)
def sort_by_rating():
    return sorted(movies, key=lambda m: m.rating, reverse=True)

# Збереження обраного списку фільмів у файл
def save_selected_movies(movie_list, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([m.to_dict() for m in movie_list], f, ensure_ascii=False, indent=4)
    print(f"Список збережено у {filename}")

# Основне меню програми
def main():
    load_movies()  # завантажити фільми з файлу, якщо є

    while True:
        print("\n=== Каталог українського кіно ===")
        print("1. Додати фільм")
        print("2. Показати всі фільми")
        print("3. Фільтрувати за жанром")
        print("4. Сортувати за рейтингом")
        print("5. Зберегти у файл")
        print("6. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            add_movie()
        elif choice == "2":
            for m in movies:
                print(f"{m.title} ({m.year}), жанр: {m.genre}, рейтинг: {m.rating}")
        elif choice == "3":
            genre = input("Введіть жанр для фільтрації: ")
            filtered = filter_by_genre(genre)
            for m in filtered:
                print(f"{m.title} - {m.genre}")
        elif choice == "4":
            sorted_movies = sort_by_rating()
            for m in sorted_movies:
                print(f"{m.title}: {m.rating}")
        elif choice == "5":
            filename = input("Введіть ім'я файлу (наприклад, top_movies.json): ")
            save_selected_movies(movies, filename)
        elif choice == "6":
            save_movies()  # зберегти всі фільми перед виходом
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Запускаємо програму
main()
