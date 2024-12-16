from flask import Flask, json, jsonify, request, Blueprint

people = Blueprint('people_data', __name__)

## Получение данных

people = Flask(__name__)

@people.route('/people', methods=['GET'])
def get_info():
    # Чтение данных из JSON файла
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    return jsonify(data)

##


## Добавление данных

@people.route('/items', methods=['POST'])
def post_data():
    # Преобразование данных из запроса в формат Python
    item = request.get_json()

    # Добавление данных в список
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    data.append(item)

    # Запись обновленных данных в JSON файл
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return jsonify({'message': 'Ученик был успешно добавлен'}), 201

##

if __name__ == '__main__':
    people.run(debug=True)