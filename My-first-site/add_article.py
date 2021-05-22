
import bottle
from bottle import post, request
import json, checks, datetime

@post('/articles', method='post')
# метод для добавления в файл информации о статьях
def add_article():
    # берем введенные значения, а также текущую дату
    title = request.forms.get('TITLE')
    description = request.forms.get('DESCRIPTION')
    author = request.forms.get('AUTHOR')
    published_date = datetime.date.today().isoformat()
    author_email = request.forms.get('AUTHOR_EMAIL')

    # проверка того, все ли поля заполнены
    if title=="" or description=="" or author=="" or author_email=="":
        return "Fill all the fields!"

    # вызов метода для проверки корректности ввода почты
    if not checks.input_check.author_email_correct(author_email):
        return "Please, put a correct email (like www@mail.com)"

    # открытие файла для чтения для подсчета количества статей
    with open('./articles.json', 'r') as file:
        articles=json.load(file)
        articles_number = len(articles)

    # открытие файла для записи
    with open('./articles.json', 'w') as file:
        articles[articles_number+1] = {'author':author, 'title':title,'description':description,
                                       'published_date': published_date, 'author_email': author_email}
        json.dump(articles, file)

    return "The article is added!"


