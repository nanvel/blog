labels: Draft
        JS
        React
created: 2016-05-24T19:49
modified: 2016-09-05T22:01
place: Kyiv, Ukraine
comments: true

# React notes

[TOC]

> Learn once, write anywhere.
>
> [Facebook Engineering blog](https://facebook.github.io/react/blog/2015/03/26/introducing-react-native.html)

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
  }

  onSomething() {
    // update state, it would cause rerender
    this.setState({somekey: 'anothervalue'})
  }

  render() {
    return <div
      something={this.state.something}
      onClick={this.onSomething.bind(this)}
    >{this.props.text}</div>
  }

}
```

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

http://redux.js.org/
