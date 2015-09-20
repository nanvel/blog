labels: Blog
        Accessibility
created: 2013-05-19T00:00

# 10 steps to improve site accessibility

Main:

- Add page with accessibility documentation
- Add skip to main content link
- To hide some text but leave it visible for screen readers use:
```css
.hidden { position:absolute; left:-10000px; top:auto; width:1px; height:1px; overflow:hidden; }
```
```html
<a href="/viev/?pages=10"><span class="hidden">View items per page: </span>10</a>
```
- Use alt attribute for images and title for links
- Use right order for Hx elements: top header element should be H1
- Use role attribute
- Use aria-labelledby attribute to name regions
- Use caption element and summary attribute in tables
- Use headers attribute in complex tables
- Use fieldset and legend elements for groups of radiobuttons and checkboxes

Additional:

- Check that all works fine in JAWS and NVDA screen readers
- Pages should have different titles and descriptions

Links:

- [http://webaim.org/techniques/screenreader/](http://webaim.org/techniques/screenreader/)
- [http://www.w3.org/TR/wai-aria/states_and_properties#aria-hidden](http://www.w3.org/TR/wai-aria/states_and_properties#aria-hidden)
- [http://www.clarissapeterson.com/2012/11/html5-accessibility/](http://www.clarissapeterson.com/2012/11/html5-accessibility/)
- [http://webaim.org/techniques/tables/data](http://webaim.org/techniques/tables/data)
- [http://webaim.org/articles/jaws/](http://webaim.org/articles/jaws/)
- [http://webaim.org/articles/nvda/](http://webaim.org/articles/nvda/)

Place: Starobilsk, Ukraine
