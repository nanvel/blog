labels: Draft
        JS
        React
created: 2016-05-24T19:49
modified: 2018-08-13T11:05
place: Kyiv, Ukraine
comments: true

# React notes

[TOC]

> Learn once, write anywhere.
>
> [Facebook Engineering blog](https://facebook.github.io/react/blog/2015/03/26/introducing-react-native.html)

## Create a project

Use `create-react-app`.

```bash
npm install -g create-react-app
create-react-app <app name>
```

## Basics

### Props vs state

**props** stores read-only data is passed from the parent.
It belongs to the parent and cannot be changed by its children.
This data should be considered immutable.

**state** stores data that is private to the component.
It can be changed by the component.
The component will rerender itself when the state is updated.

```js
import React from 'react'


export class MyComponent extends React.Component {

  constructor(props) {
    super(props)

    this.state = {
      somekey: 'somevalue'
    }

    this.onSomething.bind(this)
  }

  onSomething() {
    // update state, it would cause rerender
    this.setState({somekey: 'anothervalue'})
  }

  render() {
    return <div
      something={this.state.something}
      onClick={this.onSomething}
    >{this.props.text}</div>
  }
}
```

Setting the state:
```js
this.setState({ foo: bar });

this.setState((prevState, props) => { ... })
```

```js
onChange(e) {
  e.preventDefault();
  this.setState({[e.target.name]: e.target.value});
}
```

### Bindings

The best place for methods bindings is class constructor:
```js
class User {
  constructor(fname, lname) {
    this.fname = fname;
    this.lname = lname;
    this.getName.bind(this);
  }
  getName() {
    return this.fname + ' ' + this.lname;
  }
}
```

Or use arrow function:
```js
class User {
  constructor(fname, lname) {
    this.fname = fname;
    this.lname = lname;
    this.getName.bind(this);
  }
  getName = () => {
    return this.fname + ' ' + this.lname;
  }
}
```

## JSX

```text
<div className="App">
  {this.state.list.map(
    item =>
    <p>
      {item.title}
    </p>
  )}
</div>
```

### Lifecycle methods

Mountilg:

- `constructor`
- `componentWillMount`
- `render`
- `componentDidMount`

`constructor` - is called when an instance of the component is created and inserted in the DOM (component mounting).

`render` - is called during the mount process and when the component updates (when state or props changes).

`componentWillMount` - is called before the render method.

`componentDidMount` - is called after the render method, perfect for asynchronous requests.

Update (when the state changes):

- `componentWillReceiveProps`
- `shouldComponentUpdate`
- `componentWillUpdate`
- `render`
- `componentDidUpdate`

Unmount:

- `componentWillUnmount`

### Communication with a server

Use fetch:
```js
fetch("http://example.com").then(
  response => response.json()
).then(
  result => this.parse(result)
).atch(
  error => error
)
```

Or axious.

### ENV variables

Add variables to `.env`:
```text
REACT_APP_SOKE_KEY=somevalue
```

Access in js with `${process.env.REACT_APP_SOME_KEY}`.

## Project structure

```text
src/
  index.js
  index.css
  components/
    App/
      index.js
      test.js
      index.css
    Button/
      index.js
      test.js
      index.css
```

## Testing

For unittests use Enzyme.

## Redux

[Redux](http://redux.js.org/) is a predictable state container for JavaScript apps.

### Store

### Actions

Async actions. FB login example.

### Reducer

Composition.

### react-redux

## React native

## Libraries

### material-ui

### co

The ultimate generator based flow-control goodness.

See [https://github.com/tj/co](https://github.com/tj/co).

```js
co(function* () {

  let result = yield someFunc()
  
  return result

}).then(function (value) {
  console.log(value)
}, function (err) {
  console.error(err)
})
```

Where `someFunc` returns a promise.

## Code snippets

### FB login

A fb login redux action:
```js
function fbLoginAction() {

  const fbElementID = 'fb-root'
  const scope = 'public_profile, email'

  const _login = (dispatch) => {
    FB.login(({authResponse, status}) => {
      if (status == 'connected') {
        let {accessToken, userID} = authResponse
        return axios(
          {
            url: `${SERVER_URL}/fb`,
            method: 'POST',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json; charset=utf-8'
            },
            data: {
              accessToken,
              userID
            }
          }
        ).then(response => dispatch(initializeUserAction(response.data)))
      }
    }, { scope })
  }

  return dispatch => {
    /* load fb SDK */

    let fbRoot = document.getElementById(fbElementID)
    if (!fbRoot) {
      fbRoot = document.createElement('div')
      fbRoot.id = 'fb-root'
      document.body.appendChild(fbRoot)

      window.fbAsyncInit = () => {
        FB.init({
          appId: FB_APP_ID,
          xfbml: false,
          cookie: false,
          version: 'v2.3',
        })
        _login(dispatch)
      }

      ((d, s, id) => {
        const element = d.getElementsByTagName(s)[0];
        const fjs = element;
        let js = element;
        if (d.getElementById(id)) {return;}
        js = d.createElement(s); js.id = id;
        js.src = '//connect.facebook.net/en_US/sdk.js';
        fjs.parentNode.insertBefore(js, fjs);
      })(document, 'script', 'facebook-jssdk');
    } else {
      _login(dispatch)
    }
  }
}
```

## Instruments

### babel, webpack

See [ES6 notes / ES6(ES7) -> ES5](/2016/05/es6-notes#es6-es5).

### Development server using node/express

```bash
npm install --save-dev express
```

`server.js`:
```js
const express = require('express')
const path = require('path')


const staticFolder = path.join(__dirname, 'build')


const app = express()


app.use(express.static(staticFolder, {index: 'index.html'}))


app.listen(8000, function () {
  console.log('Listening on port 8000!')
})
```

## Vocabulary

### Isomorphic

### React native

## Links

[React.js Essentials](https://www.amazon.com/React-js-Essentials-Artemij-Fedosejev-ebook/dp/B00YSILZRW) by Artemij Fedosejev
[The Road to learn React](https://www.amazon.com/Road-learn-React-pragmatic-React-js-ebook/dp/B077HJFCQX) by Robin Wieruch
http://redux.js.org/
