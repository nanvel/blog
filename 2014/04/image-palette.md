labels: Blog
        Python
        ImageProcessing
created: 2014-04-07T00:00
place: Starobilsk, Ukraine
comments: true

# Image palette using PIL

![Image palette](image_palette.png)

The goal is to find limited list of most used colors and use this information to find similar images.
What this code does is reduce colors count and then just use ```img.getcolors()``` that returns list of used colors and how many times they were used.

```python
import operator

from PIL import Image


IMG_PATH = 'path/to/image.png'


def main():
    img = Image.open(IMG_PATH)
    img = img.convert('P', palette=Image.ADAPTIVE, colors=5)
    img.putalpha(0)
    colors = img.getcolors()

    result = """<html>
    <head><title>Colors</title>
    <style>
        .col-block {{
            display: inline-block;
            width: 50px;
            height: 100px;
        }}
        .col-block:first-child {{
            margin-left: 10px;
        }}
    </style>
    </head>
    <body>
    <img src="{src}">
    """.format(src=IMG_PATH)

    for c in sorted(colors, key=operator.itemgetter(0)):
        result += '<span class="col-block" style="background-color: rgb({r}, {g}, {b})"></span>'.format(
            r=c[1][0], g=c[1][1], b=c[1][2])

    result += '</body></html>'

    with open('index.html', 'w') as f:
        f.write(result)


if __name__ == '__main__':
    main()
```
