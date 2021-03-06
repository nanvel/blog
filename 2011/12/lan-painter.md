labels: Blog
        Projects
        Qt
created: 2011-12-01T00:00
place: Alchevs'k, Ukraine
comments: true

# Lan Painter project

![Lan painter](lp1.png)

Було розроблено для обчислювального центру Донбаського Державного Технічного Університету.

Можливості:

- Малювання мережі (користувач додає вузли)
- Експорт схеми у PDF
- Збереження інформації про вузли
- Пошук вузлів на схемі
- Сканування елементів на схемі (ping вузлів) що дозволяє виявили обриви у мережі

Програма написана на C++/Qt у 2011 році.

## Додавання/видалення/редагування вузлів

Вузлами я називаю комутатори, на схемі відображаються у вигляді прямокутників. Всередині прямокутників знаходиться список комп'ютерів що під'єднані до комутатора.

Контекстне меню:

![Lan painter, context menu](lp2.png)

Редагування вузла:

![Lan painter, node edit](lp3.png)

## Пошук на схемі

![Lan painter, search](lp4.png)

І можна обрати вузол який буде вважатися коренем (вузли що знаходяться вище нього будуть сховані).

## Збереження схеми у файл

![Lan painter, save scheme](lp5.png)

Збереження схеми у форматі PDF:

![Lan painter, save as pdf](lp6.png)

## Сканування

![Lan painter, scan nodes](lp7.png)

Сканування виконується у фоновому режимі. Вікно програми можна згорнути у панель задач.

![Lan painter, system panel](lp8.png)

## Пошук вузлів за шаблоном

![Lan painter, search nodes](lp9.png)

## Вбудована довідка

![Lan painter, help page](lp10.png)

## Інтерфейс перекладено на англійську, українську та російську мови

![Lan painter, select language](lp11.png)

Links:

- [Програма на Qt-apps.org](http://qt-apps.org/content/show.php/Lan+painter?content=142898)
- [Source code](lan_painter.zip)
