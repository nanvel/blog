labels: Blog
		Swift
		Mobile
		iOS
created: 2015-12-27T09:55
modified: 2015-12-28T23:17
place: Kyiv, Ukraine

# Swift language notes

![Swift logo](swift.png)

[TOC]

## Data types

### Constants vs variables

```bash
  1> let a = 1
a: Int = 1
  2> a += 1
repl.swift:2:3: error: left side of mutating operator isn't mutable: 'a' is a 'let' constant
a += 1
~ ^
repl.swift:1:1: note: change 'let' to 'var' to make it mutable
let a = 1
^~~
var

  2> var a = 1
a: Int = 1
  3> a += 1
```

Multiple variables inline:
```bash
  1> var one = 1, two = 2
one: Int = 1
two: Int = 2
```

Using unicode and reserved words for variable name:
```bash
  1> let сім = 7
сім: Int = 7
  2> var `for` = 1
for: Int = 1
```

### Type casting

```bash
  1> var a = 100
a: Int = 100
  2> a + 1.2
repl.swift:2:3: error: binary operator '+' cannot be applied to operands of type 'Int' and 'Double'
a + 1.2
~ ^ ~~~
repl.swift:2:3: note: overloads for '+' exist with these partially matching parameter lists: (Int, Int), (Double, Double), (Int, UnsafeMutablePointer<Memory>), (Int, UnsafePointer<Memory>)
a + 1.2
  ^

  2> var a: Double = 100
a: Double = 100
  3> a + 1.2
$R0: Double = 101.2
```

or:
```bash
  1> var a = 100
a: Int = 100
  2> Double(a) + 1.2
$R0: Double = 101.2
```

### Optional and default values

To mark the value as optional - add question mark (?) after the type of a value.

```bash
  1> var optionalString: String?
optionalString: String? = nil
  2> if let str = optionalString { 
  3.   print(str)
  4. } 
  5> optionalString = "Value"
  6> if let str = optionalString { 
  7.   print(str) 
  8. } 
  9.  
Value
```

Use default value:
```bash
  1> var optionalString: String?
optionalString: String? = nil
  2> optionalString ?? "Optional value"
$R0: String = "Optional value"
  3> optionalString = "Value"
  4> optionalString ?? "Optional value" 
$R1: String = "Value"
```

### Ranges

```bash
  1> 1...4
$R0: Range<Int> = 1..<5
  2> 1..<4
$R1: Range<Int> = 1..<4
```

### Tuple

```bash
  1> let a = ("One", 1, 1.2)
a: (String, Int, Double) = {
  0 = "One"
  1 = 1
  2 = 1.2
}
  2> a.0
$R1: String = "One"
```

### Array

```bash
  1> var a = ["One", "Two", "Three"]
a: [String] = 3 values {
  [0] = "One"
  [1] = "Two"
  [2] = "Three"
}
```

Create empty array:
```
  1> var a = [String]()
a: [String] = 0 values
```

### Dictionary

Empty dictionary:
```bash
  1> var a = [String: Int]()
a: [String : Int] = 0 key/value pairs
  2> a["one"] = 1
  3> a
$R0: [String : Int] = 1 key/value pair {
  [0] = {
    key = "one"
    value = 1
  }
}
```

### Function

Functions are a first-class type.

```bash
  1> func mySum(arg1: Int, arg2: Int) -> Int { 
  2.   return arg1 + arg2
  3. } 
  4> mySum(1, arg2: 2) 
$R1: Int = 3
```

Variable number or arguments:
```bash
  1> func sumOf(numbers: Int...) -> Int { 
  2.   var s = 0 
  3.   for n in numbers { 
  4.     s += n
  5.   } 
  6.   return s
  7. } 
  8. 
  8> sumOf(1, 2, 3)
$R0: Int = 6
```

### Closure

The code in a closure has access to objects that were available in the scope where the closure was created.

```bash
  1> let numbers = [1, 2, 3]
numbers: [Int] = 3 values {
  [0] = 1
  [1] = 2
  [2] = 3
}
  2> numbers.map({ 
  3.   number in 2 * number
  4. })
  5. 
$R0: [Int] = 3 values {
  [0] = 2
  [1] = 4
  [2] = 6
}
```

### Enumeration

```bash
  1> enum Numbers: Int { 
  2.   case One, Two 
  3.   case Three, Four, Five 
  4. } 
  5. 
  5> Numbers.One
$R0: Numbers = One
```

Enumerations can have methods associated with them:
```bash
  1> enum Numbers: Int { 
  2.   case One, Two 
  3.   func to_int() -> Int { 
  4.     switch self { 
  5.       case .One: 
  6.         return 1 
  7.       case .Two: 
  8.         return 2 
  9.       default: 
 10.         return 0 
 11.     } 
 12.   } 
 13. } 
 14> let one = Numbers.One
one: Numbers = One
 15> print(one.rawValue)
0
 16> print(one.to_int())
1
```

It is possible to use string or floating-point numbers as the raw type of an anumeration:
```bash
  1> enum Numbers: String { 
  2.   case One = "one", Two = "two"
  3. } 
  4. 
  4> Numbers.One.rawValue
$R0: String = "one"
```

### Structure

One of the most important differences between structures and classes is that structures are always copied when they are passed around in your code, but classes are passed by reference.

```bash
  1> struct Example { 
  2.   var text: String 
  3.   let one = 1
  4. } 
  5> let example = Example(text: "Some text")
example: Example = {
  text = "Some text"
  one = 1
}
```

### Class

```bash
  1> class Point { 
  2.   var x: Int = 0
  3.   var y: Int = 0
  4. } 
  5> var point = Point()
point: Point = {
  x = 0
  y = 0
}
```

#### Init / deinit

Initializer:
```bash
 1> class Point { 
 2.   var x: Int = 0 
 3.   var y: Int = 0 
 4.   init(x: Int, y: Int) {
 5.     self.x = x 
 6.     self.y = y 
 7.   } 
 8.   deinit {
 9.     print("Deinit ...")
 10.  }
 11.} 
 12. 
 13.> var point = Point(x: 1, y: 1)
point: Point = {
  x = 1
  y = 1
}
```

#### Inheritance

```bash
  1> class Point { 
  2.   var x: Int = 0 
  3.   var y: Int = 0 
  4.   init(x: Int, y: Int) { 
  5.     self.x = x 
  6.     self.y = y
  7.   } 
  8. } 
  9> class NamedPoint: Point { 
 10.   var name: String = "Noname" 
 11.   init(x: Int, y: Int, name: String) { 
 12.     super.init(x: x, y: y) 
 13.     self.name = name 
 14.   } 
 15. } 
 16> let namedPoint = NamedPoint(x: 1, y: 1, name: "Name") 
namedPoint: NamedPoint = {
  __lldb_expr_1.Point = {
    x = 1
    y = 1
  }
  name = "Name"
}
```

#### Override methods

```bash
  1> class Point { 
  2.   var x = 0 
  3.   var y = 0 
  4.   func name() -> String {
  5.     return "(\(self.x), \(self.y))" 
  6.   } 
  7. } 
  8. 
  8> class LongNamePoint: Point { 
  9.   override func name() -> String { 
 10.     return "Long name of (\(self.x), \(self.y))."
 11.   } 
 12. } 
 13> let point = LongNamePoint()
point: LongNamePoint = {
  __lldb_expr_2.Point = {
    x = 0
    y = 0
  }
}
 14> print(point.name())
Long name of (0, 0).
```

#### Property getter/setter

```bash
 1> class Point { 
 2.   var x = 0 
 3.   var y = 0 
 4.   var name: String { 
 5.     get { 
 6.       print("Get value ...") 
 7.       return "Get name for (\(self.x), \(self.y))" 
 8.     } 
 9.     set { 
 10.       print("Set name")
 11.     } 
 12.   } 
 13. } 
 14> let point = Point()
point: Point = {
  x = 0
  y = 0
}
 15> print(point.name)
Get value ...
Get name for (0, 0)
 16> point.name = "New name"
Set name
```

## Syntax

### Comments

Comments can include Markdown syntax to add rich text and embedded images that display in Xcode’s Quick Help.

One line comment (two forward-slashes):
```bash
// comment cotent
```

Multiline comment:
```bash
/* multiple line
comment */
```
Multiline comments can be nested (allows to comment large blocks of code even if them already contain comments).

### Std output

```bash
  1> print(123)
123
  2> print("Hello!")
Hello!
  3> let a = 1
a: Int = 1
  4> print("a = \(a).")
a = 1.
```

### Flow control

#### If condition

In a ```if``` statement, the conditional must be a Boolean expression.

#### switch condition

### Loops

#### for-in loop

```bash
  1> var a = ["One", "Two"]
a: [String] = 2 values {
  [0] = "One"
  [1] = "Two"
}
  2> for i in a { 
  3.   print(i)
  4. } 
  5. 
One
Two
```

#### for loop

Classic c++ like for loop:
```bash
  1> for var i=0; i<3; i++ {
  2.   print(i) 
  3. } 
  4. 
0
1
2
```

#### while loop

#### repeat-while loop

## Vocabulary

### Type-safe language

The language helps you to be clear about the types of values your code can work with.

```bash
  1> var a = 1
a: Int = 1
  2> a = "1"
repl.swift:2:5: error: cannot assign value of type 'String' to type 'Int'
a = "1"
    ^~~
```

### Type annotation

Providing type explicitly:

```bash
  1> let one: Double = 1
one: Double = 1
```

## Instruments

### REPL and Interactive Playground

To open playground: ```Xcode -> File -> New -> Playground ...```.

REPL stands for **R**ead **E**val **P**rint **L**oop.

```bash
nanvel$ swift
Welcome to Apple Swift version 2.1.1 (swiftlang-700.1.101.15 clang-700.1.81). Type :help for assistance.
  1> var s = 0
s: Int = 0
  2> for i in 1...5 { 
  3.     s += i 
  4. }    
  5> print(s)
15
```

### Executing code from a source file

```bash
nanvel$ echo 'print("Hello World!")' > main.swift
nanvel$ swift main.swift 
Hello World!
```

## Links

- [Swift. A modern programming language that is safe, fast, and interactive.](https://developer.apple.com/swift/)
- [The Swift Programming Language](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/)
- [iOS 8 App Development Essentials - Second Edition: Learn to Develop iOS 8 Apps using Xcode and Swift 1.2](http://www.amazon.com/iOS-App-Development-Essentials-Edition-ebook/dp/B00R1QW0S6)
- [Swift home page](https://swift.org)
