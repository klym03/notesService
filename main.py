import requests


BASE_URL = "http://localhost:8000/api/notes/"
def get_notes():
    response = requests.get(BASE_URL)

    if response.status_code == 200:
        try:
            notes = response.json()
            print("Список заметок:")
            for note in notes:
                print(f"ID: {note['id']}, Заголовок: {note['title']}, Содержание: {note['content']}")
        except requests.exceptions.JSONDecodeError:
            print("Ошибка декодирования JSON: Пустой ответ или некорректный формат JSON.")
    else:
        print(f"Не удалось получить заметки. Статус код: {response.status_code}")


def create_note(title, content):
    data = {"title": title, "content": content}
    response = requests.post(BASE_URL, data=data)

    if response.status_code == 201:
        note = response.json()
        print(f"Заметка создана. ID: {note['id']}")
    else:
        print(f"Не удалось создать заметку. Статус код: {response.status_code}")
        try:
            error_message = response.json().get('detail')
            if error_message:
                print(f"Ошибка от сервера: {error_message}")
        except requests.exceptions.JSONDecodeError:
            print("Не удалось декодировать JSON ответа от сервера.")


def delete_note(note_id):
    url = f"{BASE_URL}{note_id}/"
    response = requests.delete(url)
    if response.status_code == 204:
        print(f"Заметка с ID {note_id} удалена.")
    else:
        print(f"Не удалось удалить заметку. Статус код: {response.status_code}")

if __name__ == "__main__":
    while True:
        print("\n1. Просмотреть заметки")
        print("2. Создать заметку")
        print("3. Удалить заметку")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            get_notes()
        elif choice == "2":
            title = input("Введите заголовок заметки: ")
            content = input("Введите содержание заметки: ")
            create_note(title, content)
        elif choice == "3":
            note_id = input("Введите ID заметки для удаления: ")
            delete_note(note_id)
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")
