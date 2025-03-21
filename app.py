from flask import Flask
from flask import request
from flask import jsonify
from datetime import datetime
app = Flask(__name__)

DB = [	{
		1: {
			"deadline": "12-03-2025",
			"description": "disk",
			"title": "tit"
		}
	},
	{
		2: {
			"deadline": "12-03-2022",
			"description": "disk1",
			"title": "tit1"
		}
	},
	{
		3: {
			"deadline": "12-03-2023",
			"description": "disk2",
			"title": "tit2"
		}
	}] # локальная база данных

def check_date(date): #функция проверки формата даты
    try:
        datetime.strptime(date, '%d-%m-%Y')
        return True
    except ValueError:
        return False
       
ccc = ['22-03-2021', 
'22-03-2023',
'22-03-2022',
'12-03-2025']
    
@app.route('/tasks', methods = ['POST', 'GET'])
def tasks():
    global DB
    if request.method == 'GET': #вывод всех задач
        sorted_tasks = sorted(DB, key=lambda task: datetime.strptime(list(task.values())[0]['deadline'], '%d-%m-%Y'), reverse=False)
        return jsonify(sorted_tasks)
    
    elif request.method == 'POST': #формирование новой задачи, принимает {"title": "str", "description": "str", "deadline": "dd-mm-yyyy"}
        title = request.json['title']
        description = request.json['description']
        deadline = request.json['deadline']
        id = len(DB)+1
        if check_date(deadline) == True:# проверка корректности введения формата даты 
            new_task = {id :{'title': title, 'description': description, 'deadline': deadline}}
            DB.append(new_task)#добавил в БД новую задачу
            return new_task
        else: return 'Ошибка ввода формата даты'

@app.route('/tasks/<int:id>', methods = ['DELETE']) #удаление задачи по id
def delete_task(id):
    global DB
    for i in range(len(DB)):
        if id in DB[i]:
            DB.pop(i)
            return 'Задача удалена'
    return 'Задача не найдена'

if __name__ == '__main__':
    app.run(debug=True) 
    
    
# Для продакшена я бы использовал базу данных, например, PostgreSQL, а не локальный список.
# Также я бы использовал ORM, например, SQLAlchemy, для взаимодействия с базой данных. Это бы упростило работу с базой данных и оптимизировало код.
# Я бы также добавил отслеживание задачи по времени, чтобы была возможность добавлять несколько задачь на один день и более деетально их отслеживать.
# Я бы добавил возможность редактирования задачи.
# Так же довалил бы проверку на свободной даты и времени, чтобы не было пересечений.