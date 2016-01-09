labels: Blog
        Swift
        Mobile
        iOS
created: 2015-12-27T09:55
modified: 2016-01-08T20:23
place: Kyiv, Ukraine
comments: true

# Swift language notes

![Swift logo](swift.png)

[TOC]

## Data types

### Any and AnyObject

Swift provides two special type aliases for working with non-specific types:

- AnyObject - can represent an instance of any class type
- Any - can represent an instance of any type at all, including function type

```bash
  1> var things = [Any]()
things: [Any] = 0 values
  2> things.append(1)
  3> things.append("Text")
  4> things.append(1.2)
  5> things
$R0: [Any] = 3 values {
  [0] = 1
  [1] = "Text"
  [2] = 1.2
}
```

### Tuple

Group multiple values into a single compound value. Values may be of any type.

```bash
  1> let a = (1, true, "One")
a: (Int, Bool, String) = {
  0 = 1
  1 = true
  2 = "One"
}
  2> var i: Int = 0
i: Int = 0
  3> (i, _, _) = a
  4> i
$R0: Int = 1
  5> a.0
$R1: Int = 1
```

Perhaps the most powerful use of tuples is the ability to return multiple values from a function.

#### Named tuple

```bash
  1> let a = (name: "Name", number: 1)
a: (name: String, number: Int) = {
  name = "Name"
  number = 1
}
  2> a.name
$R0: String = "Name"
  3> var t: String = ""
t: String = ""
  4> (t, _) = a
  5> t
$R1: String = "Name"
```

### Array

Array is an ordered list.

```bash
  1> var a = ["One", "Two", "Three"]
a: [String] = 3 values {
  [0] = "One"
  [1] = "Two"
  [2] = "Three"
}
```

Create an empty array:
```
  1> var a = [String]()
a: [String] = 0 values
  2> var b = Array<Int>()
b: [Int] = 0 values
```

Default value for array:
```bash
  1> var a = [Int](count: 5, repeatedValue: 10)
a: [Int] = 5 values {
  [0] = 10
  [1] = 10
  [2] = 10
  [3] = 10
  [4] = 10
}
```

#### Array usage

Edit:
```bash
  1> var a: [Int] = [1, 2, 3]
a: [Int] = 3 values {
  [0] = 1
  [1] = 2
  [2] = 3
}
  2> a.append(4)
  3> a
$R0: [Int] = 4 values {
  [0] = 1
  [1] = 2
  [2] = 3
  [3] = 4
}
  4> a[0] = 5
  5> a
$R1: [Int] = 4 values {
  [0] = 5
  [1] = 2
  [2] = 3
  [3] = 4
}
  6> a[1...2] = [4, 3]
  7> a
$R2: [Int] = 4 values {
  [0] = 5
  [1] = 4
  [2] = 3
  [3] = 4
}
  8> a.insert(1, atIndex: 3)
  9> a
$R3: [Int] = 5 values {
  [0] = 5
  [1] = 4
  [2] = 3
  [3] = 1
  [4] = 4
}
 10> a.removeAtIndex(4)
$R4: Int = 4
 11> a
$R5: [Int] = 4 values {
  [0] = 5
  [1] = 4
  [2] = 3
  [3] = 1
}
```

Iterate:
```bash
  1> let a = [1, 2, 3]
a: [Int] = 3 values {
  [0] = 1
  [1] = 2
  [2] = 3
}
  2> for item in a {
  3.   print(item)
  4. }
  5.
1
2
3
  5> for (index, item) in a.enumerate() {
  6.   print(index, item)
  7. }
  8.
0 1
1 2
2 3
```

### Set

Stores distinct values of the same type in a collection with no defined ordering.

```bash
  1> var a = Set<Int>()
a: Set<Int> = {}
  2> a.count
$R0: Int = 0
  3> a.insert(1)
  4> a.insert(2)
  5> a
$R1: Set<Int> = {
  [0] = 2
  [1] = 1
}
  6> a.insert(1)
  7> a
$R2: Set<Int> = {
  [0] = 2
  [1] = 1
}
```

Shorter form of initialization:
```
  1> var a: Set = [1, 2, 3]
a: Set<Int> = {
  [0] = 2
  [1] = 3
  [2] = 1
}
```

#### Set usage

Properties:

- count
- isEmpty

Methods:

- insert
- remove
- contains
- sort
- interset (creates a new set with only the values common to both sets)
- exclusiveOr (creates a new set with values in either set, but not both)
- union (creates a new set with all of the values in both sets)
- subtract (creates a new set with values not in the specified set)
- == (equal)
- isSubsetOf (returns true whether all of the values of a set are contained in the specified set)
- isSupersetOf (returns true whether a set contains all of the values in a specified set)
- isStrictSubsetOf/isStrictSupersetOf (returns true if set is a subset or superset but not equal to)
- isDisjointWith (returns true if both sets have any values in common)

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

Function is a first-class type.

```bash
  1> func mySum(arg1: Int, arg2: Int) -> Int {
  2.   return arg1 + arg2
  3. }
  4> mySum(1, arg2: 2)
$R1: Int = 3
```

#### Function usage

Function parameters are constants by default. But it is possible to make them variable:
```bash
  1> func testVarArg(var s: String) -> String {
  2.   s += " test"
  3.   return s
  4. }
  5> var i = "Word"
i: String = "Word"
  6> testVarArg(i)
$R0: String = "Word test"
  7> i
$R1: String = "Word"
```

Allow to modify parameter value (modification in-place):
```bash
  1> func testVarArg(inout s: String) {
  2.   s += " test"
  3. }
  4> var i = "Word"
i: String = "Word"
  5> testVarArg(&i)
  6> i
$R0: String = "Word test"
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
A variadic parameter accepts zero or more values of a specified type. A function may have at most one variadic parameter.

External parameter names:
```bash
  1> func testParams(externalParam localParam: Int) {
  2.   print(localParam)
  3. }
  4> testParams(externalParam: 1)
1
  5>
```
If you provide an external parameter name for a parameter, that external name must always be used when you call the function.

Omitting external parameter names:
```bash
  1> func testParams(_ firstParam:Int, _ secondParam: Int) {
  2.   print(firstParam, secondParam)
  3. }
  4> testParams(1, 2)
1 2
```
The first param omits its external parameter name by default.

Default parameters:
```bash
  1> func testParams(i: Int = 0) {
  2.   print(i)
  3. }
  4> testParams(5)
5
  5> testParams()
0
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

It is possible to use string or floating-point numbers as the raw type of an enumeration:
```bash
  1> enum Numbers: String {
  2.   case One = "one", Two = "two"
  3. }
  4.
  4> Numbers.One.rawValue
$R0: String = "one"
```

Once enum type is known, you can use a shorter dot syntax:
```bash
  1> enum Number {
  2.   case One
  3.   case Two
  4. }
  5> var number = Number.One
number: Number = One
  6> number = .Two
  7> number
$R0: Number = Two
```

You can use shorter dot syntax also in switch statement:
```bash
  1> enum Number {
  2.   case One
  3.   case Two
  4. }
  5> var number = Number.One
number: Number = One
  6> switch number {
  7.   case .One:
  8.     print("One")
  9.   case .Two:
 10.     print("Two")
 11.   default:
 12.     print("Unknown")
 13. }
 14.
One
```

#### Mutating methods

Mutating methods for enumerations can set the implicit set parameter to be a different case from the same enumeration.

```bash
  1> enum Resolution {
  2.   case VGA, XVGA
  3.   mutating func bigger() {
  4.     switch self {
  5.       case VGA:
  6.         self = XVGA
  7.       case XVGA:
  8.         print("This one is the largest.")
  9.     }
 10.   }
 11. }
 12.
 12> var resolution = Resolution.VGA
resolution: Resolution = VGA
 13> resolution.bigger()
 14> resolution
$R0: Resolution = XVGA
 15> resolution.bigger()
This one is the largest.
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

#### Memberwise Initializers

```bash
  1> struct Resolution {
  2.   var width: Int
  3.   var height: Int
  4. }
  5> var resolution = Resolution(width: 640, height: 480)
resolution: Resolution = {
  width = 640
  height = 480
}
```

#### Mutating methods

Structure are value type, so its properties are immutable by default. However, if you need to modify the property of your structure or enumeration within a particular method, you can opt in to mutating behavior for that method.

```bash
  1> struct Resolution {
  2.   var width = 640
  3.   var height = 480
  4.   mutating func resize(scale: Double) {
  5.     self.width = Int(Double(self.width) * scale)
  6.     self.height = Int(Double(self.height) * scale)
  7.   }
  8. }
  9.
 10> var resolution = Resolution()
resolution: Resolution = {
  width = 640
  height = 480
}
 11> resolution.resize(0.5)
 12> resolution
$R0: Resolution = {
  width = 320
  height = 240
}
```

#### Fallible initializer

A fallible initializer for a value type (that is, a structure or enumeration) can trigger an initialization failure at any point within its initializer implementation.
```bash
  1> class Name {
  2.   var name: String
  3.   init?(name: String) {
  4.     self.name = name
  5.     if name == "fail" {
  6.       return nil
  7.     }
  8.   }
  9. }
 10> var name = Name(name: "fail")
name: Name? = nil
 11> var name = Name(name: "ok")
name: Name? = (name = "ok") {
  name = "ok"
}
 12> if let name = Name(name: "fail") {
 13.   print(name.name)
 14. } else {
 15.   print("Fail")
 16. }
Fail
```

### Class

Unlike other programming languages, Swift does not required you to create separate interface and implementation files for custom classes and structures.

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

#### Class vs Structure

Classes have additional capabilities that structures do not:

- Inheritance enables one class to inherit the characteristics of another
- Type casting enables you to check and interpret the type of a class instance at runtime
- Deinitializers enable an instance of a class to free up any resources it has assigned
- Reference counting allows more than one reference to a class instance

Structures are always copied when they are passed around in your code, and do not use reference counting.

When to choose structures:

- The structure's primary purpose is to encapsulate a few relatively simple data values
- It is reasonable to expect that the encapsulated values will be copied rather than referenced when you assign or pass around an instance of that structure
- Any properties stored by the structure are themselves value types, which would also be expected to be copied rather than referenced
- The structure does not need to inherit properties or behavior from another existing type

#### Init / deinit

Initialization is the process of preparing an instance of a class, structure, or enumeration for use. Instances of class types can also implement a deinitializer, which performs any custom cleanup just before an instance of that class is deallocated.

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

Deinit example:
```bash
  1> class Name {
  2.   var name = "Name"
  3.   deinit {
  4.     print("Deinit.")
  5.   }
  6. }
  7.
  7> var name1: Name? = Name()
name1: Name? = (name = "Name") {
  name = "Name"
}
  8> var name2 = name1
name2: Name? = (name = "Name") {
  name = "Name"
}
  9> name2 = nil
 10> name1 = nil
Deinit.
 11> func writeName() {
 12.   var name = Name()
 13.   print(name.name)
 14. }
 15.
 15> writeName()
Name
Deinit.
```

Swift provides two ways to resolve strong reference cycles when you work with properties of class type: weak references and unowned references.

Classes and structures must set all of their stored properties to an appropriate initial value. Stored properties cannot be left in an indeterminate state:
```bash
  1> class TestInit {
  2.   var a: Int
  3. }
  4.
repl.swift:2:7: note: stored property 'a' without initial value prevents synthesized initializers
  1> class TestInit {
  2.   var a: Int
  3.   init() {
  4.     self.a = 0
  5.   }
  6. }
  7.
```
If your custom type has a stored property that is logically allowed to have "no value" - declare the property with an optional type. Properties with of optional type are automatically initialized with value of nil.

Alternative initializers and initializers without external names:
```bash
  1> class TestInit {
  2.   var a: Int
  3.   init(a aVal: Int) {
  4.     print("Init 1")
  5.     self.a = aVal
  6.   }
  7.   init(_ aVal: Int) {
  8.     print("Init 2")
  9.     self.a = aVal
 10.   }
 11. }
 12.
 12> var testInit1 = TestInit(10)
Init 2
testInit1: TestInit = {
  a = 10
}
 13> var testInit2 = TestInit(a: 10)
Init 1
testInit2: TestInit = {
  a = 10
}
```

#### Designated and convenience initializers

Designated initializers are default.

A designated initializer must call a designated initializer from its immediate superclass.

A convenience initializer must call another initializer from the same class. A convenience initializer must ultimately call a designated initializer.

```bash
  1> class Name {
  2.   var name: String
  3.   init(name: String) {
  4.     print("Init.")
  5.     self.name = name
  6.   }
  7.   convenience init() {
  8.     print("Convenience init.")
  9.     self.init(name: "Unnamed")
 10.   }
 11. }
 12> var name = Name()
Convenience init.
Init.
name: Name = {
  name = "Unnamed"
}
 13> var name = Name(name: "Haruhi")
Init.
name: Name = {
  name = "Haruhi"
}
```

#### Inheritance

A class can inherit methods, properties, and other characteristics from another class.

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

Any class that does not inherit from another class is known as a base class.

Override methods:
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

Using ```super``` keyword:
```
  1> class Name {
  2.   var fname = "Ryuko"
  3.   var lname = "Matoi"
  4.   func name() -> String {
  5.     return "\(self.fname) \(self.lname)"
  6.   }
  7. }
  8> class LongName: Name {
  9.   override func name() -> String {
 10.     return "This is long name of \(super.name())"
 11.   }
 12. }
 13> let name = Name()
name: Name = {
  fname = "Ryuko"
  lname = "Matoi"
}
 14> let longName = LongName()
longName: LongName = {
  __lldb_expr_1.Name = {
    fname = "Ryuko"
    lname = "Matoi"
  }
}
 15> name.name()
$R0: String = "Ryuko Matoi"
 16> longName.name()
$R1: String = "This is long name of Ryuko Matoi"
```

You can prevent a method, property, pr subscript from being overridden by marking it as final:
```bash
  1> class Name {
  2.   var fname = "Ryuko"
  3.   var lname = "Matoi"
  4.   final func name() -> String {
  5.     return "\(self.fname) \(self.lname)"
  6.   }
  7. }
  8.
  8> class LongName: Name {
  9.   override func name() -> String {
 10.     return "This is long name of \(super.name())"
 11.   }
 12. }
 13.
repl.swift:9:17: error: instance method overrides a 'final' instance method
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

#### Identity operators

```bash
  1> class Resolution {
  2.   var width = 640
  3.   var height = 480
  4. }
  5> let resolution1 = Resolution()
resolution1: Resolution = {
  width = 640
  height = 480
}
  6> let resolution2 = Resolution()
resolution2: Resolution = {
  width = 640
  height = 480
}
  7> resolution1 === resolution2
$R0: Bool = false
  8> resolution1 !== resolution2
$R1: Bool = true
  9> let resolution3 = resolution1
resolution3: Resolution = {
  width = 640
  height = 480
}
 10> resolution3 === resolution1
$R2: Bool = true
```

```Identical to``` (```===```) vs ```Equal to``` (```==```): ```Identical to``` means that two constants or variables of class type refer to exactly the same class instance, ```Equal to``` means that they are considered equal or equivalent in value.

#### Lazy properties

A lazy stored property is a property whose initial value is not calculated until the first time it is used.

```bash
  1> class AnotherCls {
  2.   init() {
  3.     print("AnotherCls init ...")
  4.   }
  5. }
  6.
  6> class MainCls {
  7.   lazy var anotherObj = AnotherCls()
  8.   init() {
  9.     print("MainCls init ...")
 10.   }
 11. }
 12> let main_obj = MainCls()
MainCls init ...
main_obj: MainCls = {
  anotherCls.storage = nil
}
 13> main_obj.anotherObj
AnotherCls init ...
$R0: AnotherCls = {}
```

#### Computed properties

Classes, structures and anumerations can define computed properties, which do not actually store a value, they provide a getter and an optional setter instead.

```bash
  1> class Resolution {
  2.   var width = 640
  3.   var height = 480
  4.   var title: String {
  5.     return("Resolution: \(self.width):\(self.height)")
  6.   }
  7. }
  8> var resolution = Resolution()
resolution: Resolution = {
  width = 640
  height = 480
}
  9> resolution.title
$R0: String = "Resolution: 640:480"
 10> resolution.width = 1000
 11> resolution.title
$R1: String = "Resolution: 1000:480"
```

If a computed property's setter does not define a name for the new value to be set, a default name of newValue is used.

A computer property with a getter but no setter known as a read-only computed property.

#### Property observers

Property observers observe and respond to chnges in a property's value.

It is possible to specify name for changed parameter value, default names are newValue and oldValue.

```bash
  1> class Resolution {
  2.   var width = 640 {
  3.     willSet {
  4.       print("New value: \(newValue)")
  5.     }
  6.     didSet {
  7.       print("Old value: \(oldValue)")
  8.     }
  9.   }
 10. }
 11.
 11> var resolution = Resolution()
resolution: Resolution = {
  width = 640
}
 12> resolution.width = 1000
New value: 1000
Old value: 640
```

#### Type properties

Belongs to type, not instance.

```bash
  1> class Resolution {
  2.   static let dpi = 300
  3.   var width = 640
  4.   var height = 480
  5. }
  6> var resolution = Resolution()
resolution: Resolution = {
  width = 640
  height = 480
}
  7> resolution.dpi
repl.swift:8:1: error: static member 'dpi' cannot be used on instance of type 'Resolution'
resolution.dpi
^~~~~~~~~~~ ~~~
  7> Resolution.dpi
$R0: Int = 300
```

#### Type methods

```bash
  1> class TestTypeMtehod {
  2.   static let message = "Static method."
  3.   static func type_method() {
  4.     print(self.message)
  5.   }
  6. }
  7> TestTypeMethod.type_method()
Static method.
```

#### Declaration modifiers

Declaration modifiers are keywords context-sensitive keywords that modify the behavior or meaning of a declaration.

Available modifiers:

- dynamic - Apply this modifier to any member of a class that can be represented by Objective-C
- final - Apply this modifier to a class or to a property, method, os subscript member of a class. It's applied to a class to indicate that the class can't be subclassed. It's applied to a property, method, or subscript of a class to indicate that a class member can't be overridden in any subclass
- lazy - Apply this modifier to a stored variable property of a class or structure to indicate that the property's initial value is calculated and stored at most once, when the property is first accessed
- optional - Apply this modifier to a protocol's property, method, or subscript members to indicate that a conforming type isn't required to implement those members
- required - Apply this modifier to designated or convenience initializer of a class to indicate that every subclass must implement that initializer
- weak - The weak modifier is applied to a variable or a stored variable property to indicate that variable or property has a week reference to the object stored as its value

### Integer

```bash
  1> let a: Int = 1
a: Int = 1
  2> let a: UInt = 1  // Unsigned integer
a: UInt = 1
  3> Int.max
$R0: Int = 9223372036854775807
```

### Float and Double

Double represents a 64-bit floating-point number (precision of at least 15 decimal digits).
Float represents a 32-bit floating-point number (precision can be as little as 6 decimal digits).

Numeric literals:
```bash
  1> 10
$R0: Int = 10
  2> 0b1010
$R1: Int = 10
  3> 0o12
$R3: Int = 10
  4> 0x0A
$R5: Int = 10
  5> 0x0a
$R6: Int = 10
  6> 1e2
$R7: Double = 100
  7> 1e-2
$R8: Double = 0.01
 8> 10_000
$R10: Int = 10000
```

### String

#### Empty string

```bash
  1> let s1 = ""
s1: String = ""
  2> let s2 = String()
s2: String = ""
  3> s1 == s2
$R0: Bool = true
  4> s1.isEmpty
$R1: Bool = true
```

#### String interpolation

```bash
  1> var a = 1
a: Int = 1
  2> "a = \(a)"
$R0: String = "a = 1"
  3> "a = \(a * 5)"
$R1: String = "a = 5"
  4> "a = \(Double(a) * 5)"
$R2: String = "a = 5.0"
```

#### Special characters aka escape sequences

These special characters are identified by prefixing the character with a backslash (escaping).

Commonly used special characters:

- ```\n``` - New line
- ```\r``` - Carriage return
- ```\t``` - Horizontal tab
- ```\\``` - Backslash
- ```\"``` - Double quote
- ```\'``` - Single quote
- ```\u{nn}``` - Single by Unicode scalar
- ```\u{nnnn}``` - Double byte Unicode scalar
- ```\u{nnnnnnnn}``` - Four byte Unicode scalar

#### Unicode

```bash
  1> "\u{24}"
$R0: String = "$"
  2> "\u{1f496}"
$R1: String = "💖"
```

### nil

Special value allows to set an optional variable to a valueless state:
```bash
  1> var i: Int? = 10
i: Int? = 10
  2> i
$R0: Int? = 10
  3> i = nil
  4> i
$R1: Int? = nil
```

In Swift, ```nil``` is not a pointer - it is the absence of a value of a certain type.

## Data manipulation

### Constants vs variables

For greater code efficiency and execution performance, Apple recommends the use of constants rather than variables whenever possible.

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

Using unicode and reserved words as variable name:
```bash
  1> let сім = 7
сім: Int = 7
  2> var `for` = 1
for: Int = 1
```

### Type annotation and type inference

Swift is a [type safe](#type-safe) programming language.

There are two ways in which the the type may be identified:

- type annotation at the point of constant or variable declaration
- type inference - the compiler looks to see what type of value is being assigned at the point that it is initialized and uses that as the type

```bash
  1> let a: String = "string"
a: String = "string"
  2> let a = "string"
a: String = "string"
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

#### is and as

Type casting is a way to check the type of an instance, or to treat that instance as a different superclass or subclass from somewhere else in its own class hierarchy.

Use ```is``` to check whether an instance is of a certain subclass type:
```bash
  1> class Cat {}
  2> class Dog {}
  3> let cat = Cat()
cat: Cat = {}
  4> cat is Cat
$R0: Bool = true
  5> cat is Dog
$R1: Bool = false
```

There are two forms for downcasting operator: the conditional form (```as?``` - returns an optional value of the type you are trying to downcast) and the forced (```as!``` - attempts to downcast and force-unwraps the result).
```bash
  1> class Animal {}
  2> class Cat: Animal {}
  3> class Dog: Animal {}
  4> let cat = Cat()
cat: Cat = {
  __lldb_expr_1.Animal = {}
}
  5> if let c = cat as? Cat { 
  6.   print("works")
  7. } 
  8. 
works
  8> if let c = cat as? Dog {
  9.   print("works") 
 10. } 
 11. 
 11> if let c = cat as? Animal {
 12.   print("works") 
 13. } 
 14. 
works
```

### Type aliases

Defines an alternative name for an existing type.

```bash
  1> typealias MyInt = UInt32
  2> let a: MyInt = 10
a: MyInt = 10
```

### Optional type and default values

The purpose of the optional type is to provide a safe and consistent approach to handling situations where a variable or constant may not have any value assigned to it.

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

### Generic

Generic code enables you to write reusable functions and type that can work with any type.

```bash
  1> func doublePrint<T>(a: T) { 
  2.   print("\(a) \(a)")
  3. } 
  4> doublePrint(42)
42 42
  5> doublePrint("Hi")
Hi Hi
```

### Closure

Closures in Swift are similar to lambdas in other programming languages.
Closures can capture and store references to any constants and variables from the context in which they are defined. This is known as closing over those constants and variables, hence the name "closures".
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

### Subscripts

Classes, structures, and enumerations can define subscripts, which are shortcuts for accessing the member elements of a collection, list, or sequence.

```bash
  1> class Resolution { 
  2.   subscript(width: Int, height: Int) -> String {
  3.     get { 
  4.       return("Resolution: \(width):\(height)") 
  5.     } 
  6.     set { 
  7.       print("Set resolution \(width):\(height) to \(newValue)") 
  8.     } 
  9.   } 
 10. } 
 11. 
 11> var resolution = Resolution()
resolution: Resolution = {}
 12> resolution[640, 480]
$R0: String = "Resolution: 640:480"
 13> resolution[640, 480] = "New value"
Set resolution 640:480 to New value
```

A class or structure can provide as many subscript implementations as it needs, and the appropriate subscript to be used will be inferred based on the types of the value or values that are contained within the subscript brackets at the point that the subscript is used (subscript overloading).

#### Optional chaining

You can use optional chaining to try to retrieve and set a value from a subscript on an optional value, and to check whether that subscript call is successful.

### Extension

Extensions add new functionality to an existing class, structure, enumeration, or protocol type (but cannot override existing functionality).

Extensions in Swift can:

- Add computed properties and computed type properties
- Define instance methods and type methods
- Provide new initializers
- Define subscripts
- Define and use new nested types
- Make an existing type conform to a protocol

```bash
  1> class Name { 
  2.   var firstName = "Ryuko"
  3.   var lastName = "Matoi"
  4. } 
  5> extension Name { 
  6.   var fullName: String {
  7.     return "\(self.firstName) \(self.lastName)" 
  8.   } 
  9. } 
 10> let name = Name()
name: Name = {
  firstName = "Ryuko"
  lastName = "Matoi"
}
 11> name.fullName
$R0: String = "Ryuko Matoi"
```

An extension can extend an existing type to make it adopt one or more protocols:
```bash
extension SomeType: SomeProtocol, AnotherProtocol {
  ...
}
```

Extension works with native types:
```bash
  1> extension Int { 
  2.   func say(fraze: String) {
  3.     for _ in 0..<self { 
  4.       print(fraze)
  5.     } 
  6.   } 
  7. } 
  8> 3.say("Hello world!")
Hello world!
Hello world!
Hello world!
```

### Protocol

A protocol defines a blueprint of methods, properties, and other requirements that suit a particular task or piece of functionality. The protocol can be adopted by a class, structure, or enumeration.

```bash
  1> protocol MyProtocol { 
  2.   var setableVariable: String { get set } 
  3. } 
  4> class MyClass: MyProtocol {}
repl.swift:4:7: error: type 'MyClass' does not conform to protocol 'MyProtocol'
class MyClass: MyProtocol {}
      ^
repl.swift:2:7: note: protocol requires property 'setableVariable' with type 'String'
  var setableVariable: String { get set }
      ^

  4> class MyClass: MyProtocol { 
  5.   var setableVariable: String = "Test"
  6. } 
  7>  
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

### Optional value unwrapping

```bash
  1> var v: String? = "Test"
v: String? = "Test"
  2> if let message = v { 
  3.   print(message)
  4. } 
  5. 
Test
  5> v = nil
  6> if let message = v { 
  7.   print(message) 
  8. } 
  9.  
  9>  
```

Forced unwrapping:
```bash
  1> var v: String? = "Test"
v: String? = "Test"
  2> v!
$R0: String = "Test"
```

### Flow control

#### If statement

In a ```if``` statement, the conditional must be a Boolean expression.

```bash
  1> if true { 
  2.   print("true") 
  3. } else { 
  4.   print("false")
  5. } 
  6. 
true
```

#### Guard statement

Unlike an if statement, a guard statement always has an else clause.

```bash
  1> enum MyError: ErrorType { 
  2.   case Error1
  3. } 
  4> guard true else { 
  5.   throw MyError.Error1  // must transfer control to exit the code block, use one of: return, break, continue or throw
  6. } 
  7. 
  7> guard false else { 
  8.   throw MyError.Error1 
  9. } 
 10. 
$E0: MyError = Error1
```

It lets you write the code that's typically executed without wrapping it in an ```else``` block, and it lets you keep the code that handles a violated requirement next to the requirement.

#### Switch statement

Considers a value and compares it against several posible matching patterns. It then executes an appropriate block of code, based on the first pattern that matches successfully.

```bash
  1> func check(i: Int) { 
  2.   switch i { 
  3.     case 1: 
  4.       print("1")
  5.     case 2, 4: 
  6.       print("2 or 4")
  7.     case 5...10: 
  8.       print("Between 5 and 10")
  9.     default: 
 10.       print("Other")
 11.   } 
 12. } 
 13. 
 13> check(1)
1
 14> check(4)
2 or 4
 15> check(6)
Between 5 and 10
 16> check(3)
Other
```

Matching tuples:
```bash
  1> let point = (10, 2)
point: (Int, Int) = {
  0 = 10
  1 = 2
}
  2> switch point { 
  3.   case (_, 2): 
  4.     print("The second element is 2") 
  5.   default: 
  6.     print("Not found")
  7. } 
  8. 
The second element is 2
  8> switch point { 
  9.   case (100...200, 2): 
 10.     print("100..200 and 2") 
 11.   case (1...20, 1...20): 
 12.     print("1..20, 1..20")
 13.   default: 
 14.     print("Not found") 
 15. } 
 16. 
1..20, 1..20
```

Value binding:
```bash
  1> let point = (10, 2) 
point: (Int, Int) = {
  0 = 10
  1 = 2
}
  2> switch point { 
  3.   case (10, let b):  // case let (x, y) where x == y:
  4.     print("10, \(b)") 
  5.   default: 
  6.     print("Default")
  7. } 
10, 2
```

Break causes the switch statement to end it's execution immediately, and to transfer controlto the first line after the switch statement's closing brace:
```bash
  1> let i = 1
i: Int = 1
  2> switch i { 
  3.   case 0: 
  4.     print("0") 
  5.   default: 
  6.     break 
  7.     print("After break")
  8. } 
  9>  
```

Using ```fallthrough```:
```bash
  1> let i = 10
  2> switch i { 
  3.   case 10, 11: 
  4.     print("10 or 11") 
  5.     fallthrough 
  6.   case 1...100: 
  7.     print("Between 1..100") 
  8.   default: 
  9.     break 
 10. } 
 11.  
10 or 11
Between 1..100
```

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

```bash
  1> var i = 2
i: Int = 2
  2> while i > 0 { 
  3.   print(i) 
  4.   i -= 1
  5. } 
2
1
```

#### repeat-while loop

```bash
  1> var i = 2
i: Int = 2
  2> repeat { 
  3.   print(i) 
  4.   i -= 1
  5. } while i > 0
2
1
```

#### Labels

Works with break and continue.

```bash
  1> label1: for i in 1...3 { 
  2.   label2: for j in 1...3 { 
  3.     if j == 2 { 
  4.       break label1
  5.     } 
  6.     print(i, j) 
  7.   }  
  8. } 
  9. 
1 1
  9> label1: for i in 1...3 { 
 10.   label2: for j in 1...3 { 
 11.     if j == 2 { 
 12.       break label2
 13.     } 
 14.     print(i, j) 
 15.   }  
 16. } 
 17. 
1 1
2 1
3 1
```

### Error handling

See [Error Handling in Swift 2.0](https://www.bignerdranch.com/blog/error-handling-in-swift-2/) by Juan Pablo Claude.

In Swift, errors are represented by values of types that conform to the ErrorType protocol. This empty protocol indicates that a type can be used for error handling.

Enumerations are used for classifying errors:
```bash
  1> enum MyError: ErrorType { 
  2.   case Bad 
  3.   case Worse 
  4. }
```

Throwing an error lets you indicate that something unexpected happened:
```bash
  1> class MyError: ErrorType { 
  2.   var message: String
  3.   init(message: String) { 
  4.     self.message = message
  5.   } 
  6. } 
  7> throw MyError(message: "Something bad happened :(")
$E0: MyError = {
  message = "Something bad happened :("
}
```

Functions must be marked with throws to be able to propagate an error:
```bash
  1> enum MyError: ErrorType { 
  2.   case Bad 
  3.   case Worse 
  4. }
  5> func not_throws() { 
  6.   throw MyError.Bad
  7. } 
repl.swift:6:3: error: error is not handled because the enclosing function is not declared 'throws'
  throw MyError.Bad
  ^

  5> func throws_bad() throws {
  6.   throw MyError.Bad 
  7. } 
  > try throws_bad()
$E0: MyError = Bad
```

A throwing function propagates errors that are thrown inside of it to the scope from which it's called. Any errors thrown inside a nonthrowing function must be handled inside the function.

There are four ways to handle errors in Swift. You can:

- propagate the error from a function to the code that calls that function
- handle the error using a do-catch statement
- handle the error as an optional value
- assert that the error will not occur

Catching errors with do/catch:
```bash
  1> enum MyError: ErrorType { 
  2.   case Bad 
  3.   case Worse 
  4. } 
  5> do { 
  6.   throw MyError.Bad
  7. } catch MyError.Bad { 
  8.   print("Bad error")
  9. } catch MyError.Worse { 
 10.   print("Worse error")
 11. } 
Bad error
```

If you mark a throwing call with ```try!```, you are promising the compiler that that error will never happen and you do not need to catch it. If the statement does produce an error, the application will stop execution and you should start debugging:
```bash
  1> enum MyError: ErrorType { 
  2.   case Bad 
  3.   case Worse 
  4. } 
  5> func throws_bad() throws { 
  6.   throw MyError.Bad 
  7. } 
  8. 
  8> try! throws_bad()
fatal error: 'try!' expression unexpectedly raised an error: MyError.Bad: file /Library/Caches/com.apple.xbs/Sources/swiftlang/swiftlang-700.1.101.15/src/swift/stdlib/public/core/ErrorType.swift, line 50
```

Converting errors to Optional Values:
```bash
// If an error is thrown while evaluating the try? expression, the value of the expression is nil.
  1> class MyError: ErrorType {} 
  2> func funcThrows() throws -> Int {
  3.   throw MyError() 
  4.   return 1
  5. } 
  6. 
  7> var i: Int?
i: Int? = nil
  8> i = try? funcThrows()
  9> i
$R0: Int? = nil
```

#### A deffer statement

You use a defer statement to execute a set of statements just before code execution leaves the current block. Performs regardless of how execution leaves the current block of code: error, return or break.

```bash
  1> class MyError: ErrorType {}
  2> func raisesError() throws { 
  3.   defer { 
  4.     print("Call anyway") 
  5.   } 
  6.   print("Before error")
  7.   throw MyError() 
  8. } 
  9> try raisesError() 
Before error
Call anyway
$E2: MyError = {}
```

#### Assert

```bash
  1> assert(1 == 1)
  2> assert(1 == 2)
assertion failed: : file /var/folders/ds/mbjdvd2n3qlcck8x3s694n5h0000gn/T/./lldb/11395/repl4.swift, line 2
Execution interrupted. Enter Swift code to recover and continue.
Enter LLDB commands to investigate (type :help for assistance.)
```

### Access Control

Access control restricts access to parts of your code from other source files and modules.

Swift provides three different access levels for entities within your code:

- Public access enables entities to be used within any source file from their defining module, and also in a source file from another module that imports the defining module. You typically use public access when specifying the public interface to a framework
- Internal access enables entities to be used within any source file from their defining module, but not in any source file outside of that module. You typically use internal access when defining an app's or a framework's internal structure (default)
- Private access restricts the use of an entity to its own defining source file. Use private access to hide the implementation details of a specific piece of functionality

Guiding principle of access levels: No entity can be defined in terms of another entity that has lower (more restrictive) access level.

```bash
public class SomePublicClass {}
internal func SomeInternalFunction() {}
private var somePrivateVariable = 0
```

### Operator overloading

Classes and structures can provide their own implementations of existing operators.

```bash
  1> struct Vector { 
  2.   var x: Double 
  3.   var y: Double
  4. } 
  5> func + (left: Vector, right: Vector) -> Vector { 
  6.   return Vector(x: left.x + right.x, y: left.y + right.y)
  7. } 
  8> let v1 = Vector(x: 10, y: 10)
v1: Vector = {
  x = 10
  y = 10
}
  9> let v2 = Vector(x: 0, y: 2)
v2: Vector = {
  x = 0
  y = 2
}
 10> v1 + v2
$R0: Vector = {
  x = 10
  y = 12
}
```

### Literal expression

```bash
  1> __FILE__
$R0: String = "/var/folders/ds/mbjdvd2n3qlcck8x3s694n5h0000gn/T/./lldb/13457/repl2.swift"
  2> __LINE__
$R1: Int = 2
  3> __COLUMN__
$R2: Int = 1
  4> __FUNCTION__
$R3: String = "__lldb_expr_8"
```

#### A wildcard expression

```bash
  1> var x = 0
x: Int = 0
  2> (x, _) = (10, 20) 
  3> x
$R0: Int = 10
```

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

### A value type

A ```value type``` is a type whose value is copied when it is assigned to variable or constant, or when it is passed to a function.

Structures and enumerations are value type, classes are reference types.

### Unary/Binary/Ternary operators

**Unary** operator operate on a single target (```!a```).
**Binary** operator operate on two targets (```a + b```).
**Ternary** operator operate on three targets (```a ? b : c```).

### A module

A module is a single unit of code distribution - a framework or application that is built and shipped as a single unit and that can be imported by another module with Swift's ```import``` keyword.

### String interpolation

A concept allows to construct string using combination of strings, variables, constants, expressions, and functions calls.

### Type safe

Type safe programming language means that once the data type of a variable has been identified, that variable cannot subsequently be used to store data of any other type without inducing a compilation error.

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
