labels: Blog
        JS
created: 2016-05-02T11:12
modified: 2016-05-22T18:50
place: Kyiv, Ukraine
comments: true

# ES6 notes

[TOC]

## Variables

### Scope

```js
function f1(i) {
  if (i == 1) {
    var v = 10;
  }
  return v
}
function f2(i) {
  var v;
  if (i == 1) {
    v = 10;
  }
  return v
}
console.log(f1(0)); // undefined
console.log(f1(1)); // 10
console.log(f2(0)); // undefined
console.log(f2(1)); // 10
```

Using ```let```:
```js
function f1(i) {
  if (i == 1) {
    let v = 10;
  }
  return v
}
console.log(f1(0)); // v is not defined
```

Using ```let``` in loops:
```js
var i = 100;
for(var i=0; i<10; i++) {};
console.log(i); // 10
var i = 100;
for(let i=0; i<10; i++) {};
console.log(i); // 100
```

Global scope:
```js
var i = 100;
console.log(i); // 100
let j = 100;
console.log(window.j); // undefined
```

### Redeclaration

```js
var i = 10;
var i = 20;
let i = 30; // Identifier 'i' has already been declared
```

```js
let i = 10;
var i = 20; // Identifier 'i' has already been declared
```

## Constants

```js
const i = 10;
i = 20; // TypeError: Assignment to constant variable.
```

### Constant objects could be modified

```js
const i = {
  key: 1
};
i.key = 2;
console.log(i); // {key: 2}
```

## Strings

Multiline string:
```js
const s = `First line
Second line.`
console.log(s);
/*First line
Second line.*/
```

String interpolation:
```js
const value = 10;
console.log(`Value = ${value * 5}`); // Value = 50
```

## Functions

### Default values for parameters

```js
function f(a, b=1) {
  console.log(a, b);
}
f(10); // 10 1
f(10, 100); // 10 100
```

### Rest parameters

```js
function f(a, ...b) {
  console.log(a, b, arguments);
}
f(1); // 1 [] Object([1])
f(1, 2, 3); // 1 [2, 3] Object([1, 2, 3])
```

```js
function f(...args) {
  console.log(args);
}
f(); // []
f(1, 2, 3); [1, 2, 3]
```

### The Spread operator

```js
const values = [1, 2, 3, 4];
console.log(Math.max(...values)); // 4
console.log(Math.max(...values, 1)); // 4
console.log(Math.max(...values, 1, 10)); // 10
```

### The Function constructor

```js
const say = Function("what = `hi!`", "console.log(`Say ${what}`);");
say(); // Say hi!
say(`Hello!`) // Say Hello!
```

Also accepts ```...args```.

### Function name property

```js
function someFunction(a) {
  console.log(a)
}
console.log(someFunction.name); // someFunction
```

### Block-level functions

```js
if(true) {
  function a() {
    console.log('Call a.')
  }
  console.log(a); // function a
}
console.log(a); // Uncaught ReferenceError: a is not defined
```

### Arrow functions

```js
const sum1 = (a, b) => a + b;
const sum2 = (a, b) => {
  return a + b;
}
console.log(sum1(1, 2)); // 3
console.log(sum2(1, 2)); // 3
```

## Objects

### Property initializer

```js
function createSomething(a, b) {
  return {
    a,
    b
  }
}
console.log(createSomething(1, 2)); // Object {a: 1, b: 2}
```

### Methods

```js
const obj = {
  a: 1,
  getA() {
    return this.a;
  }
};
console.log(obj.getA()); // 1
```

### Computed property names

```js
const obj = {
  ["ab" + "cd"]: 1,
  ["ef"]: 2
}
console.log(obj); // Object {abcd: 1, ef: 2}
```

### Object.is()

```js
console.log(+0 == -0); // true
console.log(+0 === -0); // true
console.log(Object.is(+0, -0)); // false

console.log(NaN == NaN); // false
console.log(NaN === NaN); // false
console.log(Object.is(NaN, NaN)); // true

console.log(5 == 5); // true
console.log(5 == "5"); // true
console.log(5 === 5); // true
console.log(5 === "5"); // false
console.log(Object.is(5, 5)); // true
console.log(Object.is(5, "5")); // false
```

### Mixins

```js
const mixin = {
  saySomething(something) {
    console.log(something);
  }
}

const obj = {
  a: "Hi!",
};

const o = Object.assign(obj, mixin);

o.saySomething(o.a); // Hi!
```

### Duplicate object literals

```js
const a = {
  b: 1,
  b: 2
};
console.log(a); // Object {b: 2}
```

### Object keys (ordered)

```js
const a = {
  b: 1,
  c: 2
};
console.log(Object.getOwnPropertyNames(a)); // ["b"]
```

### Object prototype

```js
const proto = {
  b: 1,
  f() {
    console.log(this.b);
  },
}
const obj = Object.create(proto);
obj.b = 2;
obj.f(); // 2
proto.f(); // 1
```

New in ES6: ```Object.setPrototypeOf()```.

### Super reference

```js
const proto = {
  b: 1,
  f() {
    console.log(this.b);
  },
}
const obj = {
  f() {
    super.f();
    console.log("And some text.");
  }
}
Object.setPrototypeOf(obj, proto);
obj.f(); // 1\nAdd some text.
```

### Object destructing

```js
const obj = {
  attr1: 1,
  attr2: 2
};
const {attr1, attr2} = obj;
console.log(attr1, attr2); // 1 2
```

With default values:
```js
const obj = {
  attr1: 1,
  attr2: 2
};
const {attr1=0, attr2=0, attr3=0, attr4} = obj;
console.log(attr1, attr2, attr3, attr4); // 1 2 0 undefined
```

Custom local variable name:
```js
const obj = {
  attr1: 1,
  attr2: 2
};
const {attr1: localAttrName1=0, attr2=0} = obj;
console.log(localAttrName1); // 1
```

Nested destructuring:
```js
const obj = {
  attr1: 1,
  attr2: {
    attr3: 2
  }
};
const {attr1: localAttrName1=0, attr2: {attr3}} = obj;
console.log(attr3); // 2
```

### Private attributes

All object properties are public in ES6.

### Spread syntax

!!! attention "ES7"
    Awailable with Babel.

```js
return Object.assign({}, state, {
  didInvalidate: true
})
```

Is equal to:
```js
return { ...state, didInvalidate: true }
```

## Arrays

### Array destructuring

```js
const a = ["one", "two", "three"];
const [a1, ,a3, a4] = a;
console.log(a1, a3, a4); // one three undefined
```

Supports defaults and nested destructuring.

### Rest items

```js
const a = ["one", "two", "three"];
const [a1, ...aRest] = a;
console.log(a1, aRest); // one ["two", "three"]
```

Clone list:
```js
const a = ["one", "two", "three"];
const [...aClone] = a
console.log(aClone, a === aClone); // ["one", "two", "three"] false
```

### Array.of and Array.from

```js
let a = Array.of(1);
console.log(a); // [1]
a = Array.of(1, 2);
console.log(a); // [1, 2]
```

Converting an Array-like object (or iterable) into the Array:
```js
function f() {
  let a = Array.from(arguments);
  console.log(a);
}
f(1, 2, 3); // [1, 2 ,3]
```

### find and findIndex methods

```js
const a = [1, 2, 3, 4, 5]
console.log(a.find(i => i > 3), a.findIndex(i => i > 3)); // 4 3
```

### fill method

Changes all values to specified one.

```js
const a = [1, 2, 3];
a.fill(10);
console.log(a); // [10, 10, 10]
```

The method accepts start and end indexes.

### Generate a range

```bash
> const START = 1, NUMBER = 2
undefined
> let pages = Array.from(new Array(NUMBER), (x, i) => i + START)
undefined
> pages
[ 1, 2 ]
```

## Sets

```js
const mySet = new Set();
mySet.add(1);
mySet.add(2);
mySet.add(1);
console.log(mySet); // Set {1, 2}
console.log(mySet.size); // 2
console.log(mySet.has(1)); // true
mySet.delete(1);
console.log(mySet); // Set {2}
mySet.clear();
console.log(mySet); // Set {}
```

### Weak sets

```js
let myWeakSet = new WeakSet();
let obj = {};
myWeakSet.add(obj);
obj = null;
console.log(myWeakSet); // WeakSet {Object {}}
// obj can be garbage collected
```

### Maps

An ordered list of key-value pairs. Key and the value can have any type.

```js
const myMap = new Map();
myMap.set("key1", "value1");
myMap.set("key2", "value2");
console.log(myMap, myMap.get("key1")); // Map {"key1" => "value1", "key2" => "value2"} "value1"
```

Methods:

- ```set(key, value)```
- ```get(key)```
- ```has(key)```
- ```delete(key)```
- ```clear()```

There is ```WeakMap``` exists (**un** ordered list of key-value pairs).

## Iterators and generators

```js
const items = [1, 2, 3];
function *createIterator(items) {
  for (let i=0; i< items.length; i++) {
    yield items[i];
  }
}
let iterator = createIterator(items);
console.log(iterator.next()); // Object {value: 1, done: false}
console.log(iterator.next()); // Object {value: 2, done: false}
console.log(iterator.next()); // Object {value: 3, done: false}
console.log(iterator.next()); // Object {value: undefined, done: true}

iterator = createIterator(items);
for (let i of iterator) {
  console.log(i); // 1\n2\n3
}
```

### Iterables

Built-in iterables:

- lists
- strings
- maps (except WeakMap)
- sets (except WeakSet)

Creating an iterable:
```js
const myIterable = {
  *[Symbol.iterator]() {
    for (let i in [1, 2, 3]) {
      yield i;
    }
  }
}
for (let i of myIterable) {
  console.log(i); // 0\n1\n2
}
```

Methods of an iterable:
```js
const map = new Map([['key1', 'value1'], ['key2', 'value2']]);
console.log(map.entries()); // MapIterator {["key1", "value1"], ["key2", "value2"]}
console.log(map.values()); // MapIterator {"value1", "value2"}
console.log(map.keys()); // MapIterator {"key1", "key2"}
```

### Coroutines

```js
function *myIterator() {
  let i = yield 1;
  yield i;
}
let iterator = myIterator();
console.log(iterator.next(10)); // Object {value: 1, done: false}
console.log(iterator.next(20)); // Object {value: 20, done: false}
console.log(iterator.next(30)); // Object {value: undefined, done: true}
```

### Throwing an error inside iterator

```js
function *myIterator() {
  try {
    yield 1;
    yield 2;
    yield 3;
  } catch (e) {
    yield 100;
  }
}
let iterator = myIterator();
console.log(iterator.next()); // Object {value: 1, done: false}
console.log(iterator.throw(new Error("Some error."))); // Object {value: 100, done: false}
console.log(iterator.next()); // Object {value: undefined, done: true}
```

### Return statement inside a generator

```js
function *myIterator() {
  yield 1;
  return 100;
  yield 2;
  yield 3;
}
let iterator = myIterator();
console.log(iterator.next()); // Object {value: 1, done: false}
console.log(iterator.next()); // Object {value: 100, done: true}
console.log(iterator.next()); // Object {value: undefined, done: true}
```

### Delegating (yield from)

```js
function *myIterator() {
  yield *[1, 2];
  yield 3;
}
let iterator = myIterator();
console.log(iterator.next()); // Object {value: 1, done: false}
console.log(iterator.next()); // Object {value: 2, done: false}
console.log(iterator.next()); // Object {value: 3, done: false}
```

## Classes

```js
class MyClass {
  constructor(value) {
    this.value = value
  }

  printValue() {
    console.log(this.value);
  }
}
const obj = new MyClass(10);
obj.printValue(); // 10
```

Classes are first-class objects.

### Setters and getters

```js
class MyClass {
  constructor(value) {
    this._value = value
  }

  set value(value) {
    this._value = value
  }

  get value() {
    return this._value
  }

  printValue() {
    console.log(this._value);
  }
}
const obj = new MyClass(10);
obj.printValue(); // 10
obj.value = 20;
obj.printValue(); // 20
```

Computed member names may be handy here to keep setter and getter names the same.

### Static methods

```js
class MyClass {
  static printSomething(something) {
    console.log(something);
  }
}
MyClass.printSomething('Hi!'); // Hi!
const obj = new MyClass();
obj.printSomething('Hi!'); // Uncaught TypeError: obj.printSomething is not a function
```

Static members are not accessible from instances.

### Constructor

Equal to ```__init__``` in Python.

```js
class MyClass {
  constructor(something) {
    this._something = something;
  }
  printSomething() {
    console.log(this._something);
  }
}

const obj = new MyClass("Something.");
obj.printSomething(); // Something.
```

### Inheritance

```js
class Say {
  printSomething(something) {
    console.log(something);
  }
}
class SayPlus extends Say {
  printSomething(something) {
    super.printSomething(something + " Plus.")
  }
}
const obj = new SayPlus();
obj.printSomething("Something"); // Something Plus.
```

### ABC

```js
class MyABC {
  constructor(something) {
    if (new.target === MyABC) {
        throw new Error("ABC can't be instantiated directly.");
    }
  }
  saySomething() {
    throw new Error("Override me.");
  }
}

class MyClass extends MyABC {
  saySomething() {
    console.log("Something.");
  }
}

const obj = new MyClass();
obj.saySomething(); // Something.
const abc_obj = new MyABC(); // Uncaught Error: ABC can't be instantiated directly.
```

## Promise

Also known as "future". A promise is a placeholder for the result of an asynchronous operation.

Related:

- Fulfillment: callbacks are called with the value once a successful promise has been fulfilled
- Rejection: when it is impossible for a promise to be fulfilled, invokes the errbacks
- Progressback: a function which has been executed so as to show that progress has been made towards the resolution of a promise
- Callback: a function which has been executed once a promise has been fulfilled with a value
- Resolution: a promise which has been resolved, and then it makes progress towards a fulfillment or a rejection
- Errback: a function which has been executed if a promise has been rejected
- Deferred: an object which can be used for creation and manipulation of promises (similar to ```gen.Engine``` in Python/Tornado)

The Promise lifecycle:

- pending (operation is not completed yet)
- fulfilled or rejected

```js
const promise = new Promise(function(resolve, reject) {
  setTimeout(
    function() {
      resolve("Done!");
    },
    500
  )
});
promise.then(function(result) {
  console.log(result); // Done! (in 0.5s)
});
```

## Symbols

A js primitive value. Harder to accidentally change or override than strings or numbers.

## Modules

### Imports

```js
import React from './react'
/* is equal to */
var React = require('./react');
```

```js
import {foo, bar} from 'someModule'
```

### export keyword

Makes an object available for import.

```js
export let name = "Name";
export function f() {
	console.log("Hi!");
}
function f1() {
	return 1;
}
export f;
```

### export as / import as

```js
export {a as b};
import {a as b} from "file.js";
```

### Export default

```js
export default function() {
    return 1;
}
```

The default keyword indicates that this is a default export and the function doesn’t require a name because the module itself represents the function.

## Style guide

[Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript).

Linter: [ESLint](http://eslint.org/) with [babel-eslint](https://github.com/babel/babel-eslint).
[Atom ESLint plugin](https://atom.io/packages/linter-eslint).

[React style guide](https://github.com/airbnb/javascript/tree/master/react).

## Links

[Moving to ES6 from CoffeeScript](https://gist.github.com/danielgtaylor/0b60c2ed1f069f118562) by Daniel G. Taylor
[Understanding ECMAScript 6](https://leanpub.com/understandinges6/read) by Nicholas C. Zakas
