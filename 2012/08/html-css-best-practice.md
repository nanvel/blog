labels: Blog
        CSS
        HTML
created: 2012-08-23T00:00
place: Alchevs'k, Ukraine

# HTML/CSS best practice

## 1. Hold styles inside .css file

```html
<link href="/styles/style.css" rel="stylesheet">
```

## 2. Class selectors for styles

## 3. Readable and clear names. Use hyphen instead of underscore

```css
.comment-body
```

## 4. Urls without http/https

```html
<script src="//www.site.com/static/js/script.js"></script>
```

## 5. Don't use quotes in url()

```css
background: url(//www.site.com/static/img/bg.png);
```

## 6. Divide blocks by one empty line and section - by 2 lines

## 7. 2 chars length spaces
```html
<ul>
  <li>One Piece</li>
  <li>Bleach</li>
</ul>
```

## 8. Only lower case for classes/ids

## 9. utf-8

```html
<meta charset="utf-8">
```

## 10. Comments inside css

```css
{# TODO(Developer Name): What to do #}
```

## 11. HTML5

## 12. Set 'alt' attribute

```html
<img src="image.png" alt="Image title">
```

## 13. Single line for short definitions

```css
.style-white {color: #fff;}
```

## 14. Ordering - alphabetically

## 15. Split css files into sections, add comment at the top of the section with section name

## 16. Start section name from '$'

## 17. Don't use measurement units for line-height

## 18. Use '.8em' instead of '0.8em'

## 19. '#fff' better than '#ffffff'

## 20. New line for every selector

```css
h1,
h2,
h3 {color: #fff;}
```

Links:

- [Руководство по оформлению HTML/CSS кода от Google](http://habrahabr.ru/post/143452/)
- [Руководство по форматированию CSS](http://habrahabr.ru/post/149986/)
