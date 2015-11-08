labels: Blog
        HTML
created: 2013-03-24T00:00
place: Starobilsk, Ukraine
comments: true

# ```<time>``` - HTML5 тег для зазначення часу

HTML4:
```html
<p class="post-date">24 березня, 2013</p>
```

У HTML5 для цього є семантичний (читай правильний) тег ```<time>```.
Під "семантичний" розуміється те, що тег використовується за прямим призначенням.
Semantics (from Ancient Greek: σημαντικός sēmantikós) is the study of meaning. It focuses on the relation between signifiers, like words, phrases, signs, and symbols, and what they stand for, their denotation ([wikipedia](http://en.wikipedia.org/wiki/Semantics)).

HTML5:
```html
<time datetime="2013-03-24" pubdate>24 березня, 2013</time>
```

Атрибут datetime повинен містити дату у форматі зрозумілому машині.

Формат для дати:
```
yyyy-mm-dd
```

Якщо потрібно вказати час:
```
2013-03-24T12:38:10+02:00
```

Де ```+02:00``` - зсув часу для часової зони.

У тілі тега має бути зазначена дата у форматі зрозумілому людині.

Прапор ```pubdate``` (опціонально): якщо ```<time>``` знаходиться у тезі ```<article>```, то буде вважатись, що зазначена дата - дата пудблікації статті, інакше - дата публікації документа.

Links:

- [http://diveintohtml5.info/semantics.html](http://diveintohtml5.info/semantics.html)
