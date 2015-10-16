labels: Blog
        CSS
created: 2012-11-10T00:00
place: Alchevs'k, Ukraine

# CSS shadows

## box-shadow

```css
box-shadow: h-shadow v-shadow blur spread color inset;
```

Attributes:

- h-shadow - position of the horizontal shadow. Negative values are allowed
- v-shadow - position of the vertical shadow. Negative values are allowed
- blur - blur distance (optional)
- spread - positive values increase the size of the shadow, negative values decrease the size. Default is 0 (the shadow is same size as blur, optional)
- color - color of the shadow (optional)
- inset - changes the shadow from an outer shadow (outset) to an inner shadow (optional)

```css
box-shadow: 10px 10px 5px #888;
```

<div style="box-shadow: 10px 10px 5px #888;display: block;margin: 20px 10px;width: 200px;height: 100px;background-color: #ccc;"></div>

```css
box-shadow: 10px 10px 5px #888 inset;
```

<div style="box-shadow: 10px 10px 5px #888 inset;display: block;margin: 20px 10px;width: 200px;height: 100px;background-color: #ccc;"></div>

```css
box-shadow: 5px 5px #888;
```

<div style="box-shadow: 5px 5px #888;display: block;margin: 20px 10px;width: 200px;height: 100px;background-color: #ccc;"></div>

```css
box-shadow: 5px 5px 2px #888;
```

<div style="box-shadow: 5px 5px 2px #888;display: block;margin: 20px 10px;width: 200px;height: 100px;background-color: #ccc;"></div>

```css
box-shadow: 0 0 2px #888;
```

<div style="box-shadow: 0 0 2px #888;display: block;margin: 20px 10px;width: 200px;height: 100px;background-color: #ccc;"></div>

```css
box-shadow: 0 0 2px 2px #888;
```

<div style="box-shadow: 0 0 2px 2px #888;display: block;margin: 20px 10px;width: 200px;height: 100px;background-color: #ccc;"></div>

```css
box-shadow: 0 8px 6px -6px #888;
```

<div style="box-shadow: 0 8px 6px -6px #888;display: block;margin: 20px 10px;width: 200px;height: 100px;background-color: #ccc;"></div>

```css
box-shadow: 0 8px 6px -6px #888;
```

<div style="box-shadow: 0 8px 6px -6px #888;display: block;margin: 20px 10px;width: 200px;height: 100px;background-color: #ccc;"></div>

## text-shadow

```css
text-shadow: h-shadow v-shadow blur color;
```

```css
text-shadow: 2px 2px 1px #888;
```

<div style="text-shadow: 2px 2px 1px #888;font-size: 20px; margin: 20px 10px;">Lorem ipsum dolor sit amet, eu usu vidisse feugait volumus, velit congue graeci vis cu. Ex dolore tempor doming qui. Eam minim mazim et, maiorum tibique te sea. Pro an epicuri recteque inciderint, nec no salutandi quaerendum. Affert nostrum eu sit, pri at invidunt oporteat legendos. Prima harum dicunt nam ei, ut duo esse consequuntur.</div>

Mixin:
```css
.shadow {
    -moz-box-shadow:    3px 3px 5px 6px #ccc;
    -webkit-box-shadow: 3px 3px 5px 6px #ccc;
    box-shadow:         3px 3px 5px 6px #ccc;
}
```

Links:

- [http://www.w3schools.com/cssref/css3_pr_box-shadow.asp](http://www.w3schools.com/cssref/css3_pr_box-shadow.asp)
- [http://www.w3schools.com/cssref/css3_pr_text-shadow.asp](http://www.w3schools.com/cssref/css3_pr_text-shadow.asp)
- [http://css-tricks.com/snippets/css/css-box-shadow/](http://css-tricks.com/snippets/css/css-box-shadow/)
