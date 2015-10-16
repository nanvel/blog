labels: Blog
        Django
created: 2012-03-20T00:00
place: Alchevs'k, Ukraine

# Django template tags

Цей пост - моя шпаргалка з шаблонних тегів і фільтрів Django.

## 1. Шаблонні теги

1.1. Блоки:
```django
{% extends %}
{% include template_name %}
{{ block.super }} - вміст блоку
{% ssi %} - включення іншого файлу за абсолютним шляхом
{% ssi ... parsed %} - якщо потрібна обробка файлу у контексті шаблона (!ALLOWED_INCLUDE_ROOTS required)
```

1.2. Теги:
```django
{% load my_template_tag %}
{% templatetag %} - замість
екранування ({%, %}, {{, }}, {, }, {#, #})
{% with object.item.count as count %} ... {% endwith %}
```

1.3. Розгалуження:
```django
{% if %} {% else %} {% endif %}
{% ifequal %} {% endifequal %}
{% ifnotequal %} {% endifnotequal %}
```

1.4. Цикли:

```django
{% for %} {% endfor %}
Зворотний порядок:
{% for a in b reversed %} {% endfor %}
Список, що містить списки:
{% for x,y in points %} {% endfor %}
Якщо список порожній:
{% for %} {% empty %} {% endfor %}
Чи змінилось значення:
{% for %} {% ifchanged %} {% else %}
{% endifchanged %} {% endfor %}
Змінна forloop
forloop.counter
forloop.counter0
forloop.revcounter
forloop.revcounter0
forloop.first - True for firsy item
forloop.last
forloop.parentloop - посилання на зовнішній forloop
```

1.5. Форматування:
```django
{% autoescape on|off %}...{{% autoescape %}}
{% cycle 'row1' 'row2' a b 'row10'... %}
{% cycle 'row1' 'row2' a b 'row10'... as rows %}
{% cycle rows %}
{% spaceless %} - видалення пробілів
{% url %} - зворотний reverse
{% widthratio this_val max_val 100 %} - this_val / max_val * 100
{% filter force_escape|lover %} {% endfilter %}
{% firstof a b c ... %} - перша Not False
{% now "jS o\f F" %}
{% regroup %} - перегрупування на загальним атрибутом
{% regroup people by gender as gender_list %}
{% for gender in gender_list %} {% for item in gender.list %}
{% endfor %} {% endfor %}
```

1.6. Додатково:
```django
{# comment #}
{% comment %} {% endcomment %}
{% debug %} - вивід відлагоджувальної інформації
{% csrf_token %}
```

## 2. Шаблонні фільтри

2.1. Форматування:
```django
{{ name|lower }} - у нижній регістр
{{ name|upper }}
{{ names|truncatewords:"30" }} - тільки перші 30 слів
{{ names|addslashes }}
{{ text|addslashes }} - add slashes before quotes
{{ text|capfirst }} - перший символ у верхній регістр
{{ text|cut:" " }} - видаляє символи
{{ value|date:"D d M Y" }}
{{ value|default:"nothing" }}
{{ value|default_if_none:"nothing" }}
{{ value|center:"10" }} - "I am" -> "   i am   "
{{ value|ljust:"10" }}
{{ value|rjust:"10" }}
{{ value|filesizeformat }} - 'humen-readable' filename
{{ value|fix_ampersands }} - & -> &amp;
{{ value|floatformat }} - 34, 34.2
{{ value|floatformat:3 }} - 34.000, 34,444
{{ value|floatformat:"-3" }} - 34, 34,444
{{ value|join:"/" }}
{{ value|linebreaks }} ...\n... -> <p>...<br>...</p>
{{ value|linebreaksbr }} ...\n... -> ...<br>...
{{ value|pluralize }} - returns s if not 1
{{ value|removetags:"b span" }} - remove <b>,</b>,<span>,</span>
{{ value|safe }} - not required filtering
{{ value|slugify }} - Hello world -> Hello-world
{{ value|striptags }} - remove html tags
{{ value|time:"H" }}
{{ value|tumesince:comment_date }}
{{ value|timeuntil:from_date }}
{{ value|title }} - my first post -> My First Post
{{ value|truncatechars:9 }} - Joel is a slug -> Joel i...
{{ value|truncatewords:2 }} - Joel is a slug -> Joel is ...
{{ value|truncatewords_html:2 }} - <p> Joel is ... </p>
{{ value|urlencode }} - example.org/foo?a=b&c=d -> example.org/foo%3Fa%3Db%26c%3Dd
{{ value|urlize }} - www.....com -> <a href=""...>www.....com</a>
{{ value|urlizetrunc:15 }}
{{ value|wordwrap:5 }} - Joel is a slug -> Joel \n is a \n slug
{{ value|yesno:"yeah,no,maybe" }}
{{ value|divisibleby:2 }} - bool(value % 2 == 0)
```

2.2. Упорядкування:
```django
{{ value|dictsort:"name" }}
{{ value|dictsortreversed:"name" }}
{{ list|first }} - the first item in the list
{{ list|last }}
{{ value|linenumbers }} one two ... -> 1. one 2. two ...
{{ list|slice:"2" }} ['a', 'b', 'c'] -> ['a', 'b']
{{ value|unordered_list }}
```

2.2. Властивості:
```django
{{ names|length }}
{{ value|add:"2" }}
{{ value|divisibley:"3" }} - Ділиться на 3
{{ value|langth_is:"4" }}
{{ value|wordcount }}
```

## 3. Форматування дат

Для фільтрів Django:
```|date:"F j, Y"```
У дужках - для datetime:
```datetime.datetime.strfdate(date, format)```

```
a    - a.m., p.m.
A(p) - AM, PM
b(a) - jan, feb, ...
d    - 01..31
D    - Sun, Fri, ...
f    - 1, 2, 2:23, ..., 11:59
F(B) - January
g(I) - 1..12 h
G(H) - 0..23
h    - 01..12 h
H    - 00..23 h
i(M) - 00..59 m
j    - 1..31
l(A) - Friday
L    - True | False - високосний рік
m    - 01..12 month
M    - Jan, Feb, ...
n    - 1..12 month
N    - Jan., Feb., March, May, ...
O    - +0200
P    - 1 a.m., 1:30 p.m., ..., midnight|noon
r    - Sat, 10 Feb 2012
s(S) - 00..59
S    - st, nd, rd, th - закінчення для нора дня у місяці
t    - 28..31 - кількість днів у місяці
T    - EST, MDT - часовий пояс
w    - 0..6 - день тижня
W(U) - 1..53 - номер тижня
y    - 0..99 - рік
Y    - 1999
z    - 0..365
Z    - -43200 ... 43200 - зміщення часового поясу у секундах
```
