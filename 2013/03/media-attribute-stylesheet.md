labels: Blog
        HTML
created: 2013-03-08T00:00
place: Starobilsk, Ukraine
comments: true

# media attribute in link[rel=stylesheet]

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>media attribute for link[rel=stylesheet]</title>
        <link rel="stylesheet" type="text/css" media="screen" href="normal.css" />
        <link rel="stylesheet" type="text/css" media="screen and (max-device-width: 800px)" href="small.css" />
    </head>
    <body>
        <div class="cube"></div>
    </body>
</html>
```

```css
/* normal.css */
.cube {
    width: 100px;
    height: 100px;
    background-color: #a00;
}
small.css:
.cube {
    background-color: #0a0;
}
```

Result:

![Stylesheet media attribute](stylesheet_media.jpg)

Links:

- [http://alistapart.com/article/responsive-web-design](http://alistapart.com/article/responsive-web-design)
