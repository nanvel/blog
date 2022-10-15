labels: Ruby
        Blog
created: 2020-07-08T12:25
modified: 2022-10-15T14:55
place: Phuket, Thailand

# Ruby notes

[TOC]

Expression oriented.

## Program structure

```ruby
#!/usr/bin/ruby -w  # shebang
# -*- coding: utf-8 -*-
# or like this (the above one can be understood by editors):
# coding: utf-8

require 'socket'
...  # code

__END__

...  # data
```

`load` and `require` serve similar purposes, though require is much more commonly used.
`require_relative` was introduced in Ruby 1.9.
`load` can also load binary extensions. `load` expects a complete filename. `load` can load the same file multiple times.

Execute code at the very beginning/end of the program:
```ruby
BEGIN {
  ... # global init
}

END {
  ... # global shutdown
}
```

Load path: `$LOAD_PATH` or `$:`.

Autoloading, register name of the undefined constant and library to load:
```ruby
autoload :TCPSocket, 'socket'
```

## Syntax

Break to new line:

```ruby
a = 1 +
2 # works because the first line contains not a complete expression

Module1::
  Submodule # same thing

a = Array.new
  .push('example') # works because the first characted is period
```

### `::`

```ruby
Encoding::Converter  # namespace
```

### `*` - splat operator

```ruby
z, y = *[1, 2]
x, y, z = 1, 2 # z = nil
x, y = 1, 2, 3 # 3 is not assigned
x, y, z = 1, *[2, 3]
x, *y = 1, 2, 3 # x = 1, y = [2, 3]
*x, y = 1, 2, 3 # x = [1, 2], y = 3
```

### Loops

Statements: while, until, and for. Also custom looping using iterators.

The loop variables of a for loop are not local to the loop, they remain defined even after the loop exits!

```ruby
for i in arr do
  puts i
end
```

The only difference between the for version of the loop and the each version is that the block of code that follows an iterator does define a new variable scope.

```ruby
1..10.each do |i|
  puts i
end
```

```ruby
loop do
  puts 1
  # next
  break
end
```

```ruby
while x > 0:
  puts x
  x = x - 1
end
```

```ruby
until x < 0:
  puts x
  x -= 1
end
```

Inline:
```ruby
x = 0
puts x = x + 1 while x < 10
```

Break out from nested loops:
```ruby
for a in aa do
  catch :my_error do
    for b in bb do
      for c in cc do
        throw :my_error
      end
    end
  end
end
```

!!! tip "Throw and return value"
    If `throw` is called, then the return value of the corresponding `catch` is, by default, nil. You can, however, specify an arbitrary return value for catch by passing a second argument to `throw`.

### Variables

```ruby
CONSTANT = 1
$global_var = 1
@@class_variable = 1
@instance_variable = 1
local_variable = 1
```

Parallel assignment:

```ruby
x, y = 1, 2
```

Constans can be defined outside class:
```ruby
MyClass::MY_CONST = 1
```

Instance and class variables are encapsulated and effectively private, and constants are effectively public.

### Functions

#### Partial

Use `lambda`.

### Global functions

Global functions are defined as private methods of the Object class.

### Methods

A method is a named block of parameterized code associated with one or more objects.

Ruby methods are not objects.

Methods are defined with the `def` keyword. The return value of a method is the value of the last expression evaluated in its body.

Methods are always invoked on an object (the receiver, and methods are called messages, messages are sent to receiver).

```ruby
def say
  # method body goes here
end
```

When a method is defined outside a class or module, it is effectively a global function (technically, becomes a private method of the Object class).

Methods can be defined on individual objects (singleton methods):
```ruby
def Math.square(x)
  x * x
end

def sefl.my_class_method(x)
  # ...
end
```

Blocks can be passed to methods:
```ruby
def take_block(&block)
  block.call
end

take_block do
  puts "Block call"
end
```

Procs are stored blocks:
```ruby
talk = Proc.new do
  puts "I am talking."
end
```

Assignment methods:
```ruby
def a=(x):
  x + 1
end

# my_object.a = 10  # => 11
```

Qustion mark suffix:
```ruby
def can_call?
  true
end
```

A question mark is used to mark predicates - methods that return a Boolean value.

Exclamation mark suffix: is used to indicate that caution is required with the use of the method.

```ruby
def delete!
end
```

Often exclamation mark is used in mutator method that alters the objects in place.
Example: `#sort` vs `#sort!`.

Singleton methods are available on a single object:

```ruby
o = 'message'
def o.printme
  puts self
end
```

Undefine method:

```ruby
undef my_method
```

When method name resolution algorithm fails to find a method, it looks up a method named method_missing instead.

Alias method:
```ruby
def my_method
end

alias my_method_new_name my_method
```

Params:

```ruby
def a_method(s, len=10) end
def a_method(s, *a) end
def a_method(s:, len: 10) end
```

Methods can be represented as instances of the Method class:

```ruby
m = 0.method(:succ)
p = m.to_proc

unbound_m = Fixnum.instance_method('+')
unbound_m.bind(2).call
```

Methods are not closures. The only binding is self - the object on which the method is to be invoked.

A private method is internal to the implementation of a class, and it can only be called by other instance methods of the class (or, its subclasses).

A protected method is like a private method in that it can only be invoked from within the implementation of a class or its subclasses.

Eval private methods from outside:
```ruby
obj.send(:abc)
obj.public_send(:abc)
obj.instance_eval { ... }
```

Chaining (overriding methods with original call):
```ruby
def my_method(a, b)
  super(a, b + 1)
end
```

If you use super without arguments (bare keywords) - then all the arguments that were passed to the current method are passed to the superclass method.

### Flow control

The value of `nil` is treated the same as `false` and any other value is the same as `true`!

`x = if x < y then x else y end`  - this is an expression.

```ruby
if a == 1
  puts 1
elsif a == 2
  puts 2
else
  puts 'another'
end
```

```text
&& -> and
|| -> or
! - not
```

 Ternary operator:
 ```ruby
 true ? "True" : "Not True"
 ```

Statement (or expression) modifier:
```ruby
code if expression
code unless expression
```

#### Altering control flow

`return` - method exit and return a value to its caller.

!!! tip "Nested within blocks"
    Return is remarkably consistent, it always causes the enclosing method to return, regardless of how deeply nested within blocks it is.

`break` - exit loop (or iterator).

`next` - skip the rest of the current iteration and move to the next iteration.

`redo` - restart loop (or iterator) from the beginning.

`retry` - restart an iterator, reevaluate the entire expression (can also be used in exception handling).

`throw/catch` - exception propagation and handling.

Ruby's `catch` method defines a labeled block of code, and Ruby's `throw` method causes that block to exit.

#### Case

The comparison is done using `===`!

```ruby
case a
when 1
  puts 1
when 2
  puts 2
else
  puts 3
end
```

```ruby
case
  when x == 1, y == 0 then
    'one and y is zero'
  when x == 2 then
    'two'
end
```

#### `===` - case equality

For some classes, `===` is a membership or matching operator.

```ruby
(1..10) === 5
/\d+/ === '123'
String === 's'
:s === 's'
```

#### `<=>` operator

```ruby
1 <=> 5 # -1
5 <=> 5 # 0
9 <=> 5 # 1
```

### Input/Output

```ruby
puts 'Hello!'  # prints the string and appends a newline (unless already ends with a newline)
print 'Hello!'  # prints the string (without appending a newline)
p 'Hello!'  # same a puts + converts objects to string (more programmer friendly)
```

Program args:
```ruby
x = ARGV[0]
```

### Threads

```ruby
Thread.new { File.read(f) }
```

The key feature of Queue that makes it suitable for concurrent programming is that the deq method blocks if the queue is empty and waits until the producer thread adds a value to the queue.

### Fibers

Ruby's fibers are coroutines (semicoroutines), they are no lightweight threads.

```ruby
f = Fiber.new do |message|
  message = Fiber.yield('Hello!')
end
```

### Introspection (reflection)

Set instance variable:
```ruby
obj.instance_variable_set(:@a, 0)
Math.const_set(:EPI, Math::E * Math::PI)
```

```ruby
o.public_methods
String.private_method_defined? :initialize

def add_method(c, m, &b)
  c.class_eval {
    define_method(m, &b)
  }
end
```

Module, Class and Object implement several callback methods, or hooks. These methods are not defined by default.
Using hooks we can extend Ruby's behavior when classes are subclassed, when modules are included, or when methods are defined.

For tracing: `__FILE__`, `__LINE__`.

### Metaprogramming

```ruby
o.class
o.class.superclass
o.instance_if? String # o.class == String
o.is_a? String # instance of any subclass os String, String === o
```

Example of metaprogramming in ruby: attr_readers/attr_accessor.

Attributes (creates methods to access `@x`, `@y`):
```ruby
class Point
  # attributes :x => 0, :y => 0
  attributes x:0, y:0  # Ruby 1.9
end
```

The goal of metaprogramming in Ruby is often the creation of domain-specific languages, or DSLs.

### Debugging

Run inline:
```bash
ruby -e 'puts "Hello world!"'
```

```bash
irb  # interactive ruby
irb --simple-prompt
pry
```

[pry](https://github.com/pry/pry)

```ruby
require 'pry'
binding.pry
```

Documentation:
```bash
ri Math::sqrt
```

## Types

Type of an object - set of behaviors that characterize the object (the set of methods it responds to).

TRUE, FALSE, NIL constants, but lowercase is preferred.

### Literals

Literals = appear directly in source code:

- numbers
- strings
- regular expressions

### Boolean

Evaluates to false: nil, false. Other - true.

`and`, `or` and `not` are low-precedence versions of `&&`, `||`, `!`.

Bool operators precedence:

- `&&`
- `||`
- `and`
- `or`

### Arrays

Ruby's arrays are untyped and mutable.

`<<` - append operator.

Last element:
```ruby
s[s.length - 1]
```

`%w` and `%W` - array literals.

Creation:
```ruby
Array.new(3) # [nil, nil, nil]

Array.new(2, 0) # [0, 0]

Array.new(3) {|i| i + 1} # [1, 2, 3]
```

Ranges:
```ruby
x..y # Range.new(x, y)
x...y # Range.new(x, y, true)
```

```ruby
a[-2..-1] # last 2 elements

a[-2,2] = nil # delete last 2 elements
```

Operations:
```ruby
a | b
a & b

# clear, compact!, delete_if, each_index, empty?, fill, flatten!, include?, 
# index, join, pop, push, reverse,reverse_each, rindex, sort, sort!, uniq!, unshift.
```

### Set

```ruby
require 'set'

(1..5).to_set
Set.new(1..5)
Set.new(1. 2, 3)

s.subset? t
```

### Strings

Strings are mutable.
Use freeze to prevent future modification.

```ruby
"Some text"
"Some text with \""

'Some string'  # no interpolation

# interpolation
"Some text #{1 + 1}"
"Some test #$global_variable_name"
# also can be used sprintf("pi is about %.4f", Math::PI)

%|Some text|

# using %, %q, %Q
# %i - array of symbols
# %q (%Q or % for double quoted rules) - string follows single quoted rules
# %r - regular expression
# %s - symbol
# %w - array of strings
# %x - backtick (can use instead backtick) - it will be executed, for example `ls`

# multiline
result = <<HEREDOC
This would contain specially formatted text.

That might span many lines
HEREDOC

# heredoc starts with << or <<-, the text begins in the next line
# ends when text of the delimiter appears on the line by itself

# Python 2 style
"%d %s" % [3, 'rubies']
```

Embedded documents as multiline comments:
```ruby
=begin Multiline comment ...
Another line ...
=end
```

Multiline:
```ruby
with_newline = 'line 1 \
line2'

without_newline = 'line 1 '\
'line 2'

a = "This string literal
has two lines \
but is written on three."
```

Double quoted `"` string literals support `\t`, `\n`, `\r`, `\"`.

Unicode:
```ruby
"\u{A5}"  # same as \u00A5
```

Edit string:
```ruby
s[-1] = 'x'

s[5,0] = 'y' # insert without deleting

s[5,2] = '' # delete 2 positions 
```

Ranges:
```ruby
s[0,2]  # first 2 letters (psition, length)

s[2..3] # positions 2 and 3
s[2...3] # position 2 only
```

Contains:
```ruby
s['x'] # contails L

while(s['x'])
  s['x'] = 'y'
end
```

Regular expressions:
```ruby
/\d+/

"powerball" =~ /b/

s[/[aeiou]/] = '*' # replace
```

`sub` (substitute - replace the first occurrence), `gsug` (global substitute - replace all), `sub!`, `gsub!` for replace:
```ruby
phone.sub!(/#.*$/, '')
```

Regular expression modifier characters:

- `i`: Ignore case
- `m`: Matched against multiline text, treat newline as an ordinary character
- `x`: Extended syntax (allow space and comments)
- `o`: Perform `#{}` interpolation only once
- `u`, `e`, `s`, `n`: Interpret as Unicode (UTF-8), EUC, SJIS, ASCII

Regular rxpression syntax:
```text
. - Any single character except newline.
\w - Word characters.
\W - Non word characters.
\s - Whitespaces (\t,\n,\r,\f).
\S - Non whitespace.
\d - Digits.
\D - Non digits.
a | b - Expression a or b.
() - Group into syntactic groups and captures text.
(?:) - Groups without capturing text.
(?<name> re) - Groups, captures text, labels.
\k<name> - Matches the same text that matched the named captured group name.
re* - Matches zero or more occurrences.
re+ - Matches one or more occurrences.
re? - Matches zero or one occurrences.
re{n} - Matches exactly n occurrences.
re{n,} - Matches n or more occurrences.
re{n,m} - Matches n to m occurrences.
^ - Beginning of line anchor.
$ - End of line.
\A - Beginning of string.
\z or \Z (before newline) - End of string.
\G - Last match finished.
```

Conversion:
```ruby
"1".to_i
"1.1".to_f
```

Character literals:
```
?A # equal to char('A')
```

Succ method:
```ruby
'a'.succ # 'b'
'b'.succ # 'c'
```

Encodings:
```ruby
Encoding.list
```

### Numbers

Numeric:

- Integer (Fixnum (31 bits), Bignum)
- Float
- Complex
- BigDecimal
- Rational

Examples:

- `1_000`
- `0.1`
- `6.02e5` (6.02 * 10^5)
- `0377` (octal)
- `0b1101`
- `0xff`

`1 / 0` -> ZeroDivisionError
`1. / 0` -> Infinity
`0.0 / 0.0` -> NaN

#### Conversion

```ruby
a = 1
Float(a)
a.to_f
```

### Symbols

Symbols - immutable interned strings. Can be compared by identity rather than by textual content.
Immutable and not garbage-collected strings.

```ruby
:my_symbol

:'my_symbol'

name = 'my_symbol'
:"#{name}"

%s[""] # :'"'
```

### Hashes

```ruby
{ "a" => 1 }
{ a: 1 } # same as { :a => 1 }, just colon moves to the end of the hash key and replaces the arrow.
```

Hash keys must be hashable (should have method `hash`, returns fixnum hashcode).

Methods:
```ruby
h = Hash.new(-1) # -1 is default value
h.default = -2 # h['two'] == -2
h.delete(:b)
h.select {|k, v| v % 2 == 0}
h.values_at(:a, :b)
h.delete_if {|k, v| k.to_s < 'b'}
h.invert # swap keys and values
h.clear
h.each_key
h.each_value
```

#### Strings as keys

In order for an object to be used as a hash key, it must have a hash method that returns an integer "hashcode" for the object.

Because strings are mutable but commonly used as hash keys, Ruby treats them as a special case and makes private copies of all strings used as keys.

Consider making a private copy or calling the freeze method. If you must use mutable hash keys, call the rehash method of the Hash every you mutate a key.

### Ranges

```ruby
(1..2)  # includes ending values
(1...2)  # excludes ending values
```

`==` test equally.
`===` for matching and membership.

### Procs (procedures)

```ruby
-> { 1 + 1 }
->(a) { a + 1 }
```

#### Procs vs Lambdas

Blocks are syntactic structures in Ruby, can not be manipulated as objects.

Depending on how the block is created, it is called a proc or lambda.

Procs have block-like behavior and lambdas - method-like behavior.

```ruby
p = Proc.new { |x, y| x + y }
l = lambda { |x, y| x + y }
l = ->(x, y) { x + y }
l = ->(x, y; z=1, c) { x + y } # z and c - local variables
l.call(1, 2)
p[1, 2]
p.(1, 2)

lambda?(p) # false
lambda?(l) # true
```

`proc` method in `lambda` in 1.8 and `Proc.new` in 1.9.

A Proc is like a block, if you call return - it will return from the method that encloses the block.

Proc and lambda are closures. Methods are not closures.

### Blocks

Unlike methods, blocks do not have names, and they can only be invoked indirectly through an iterator method.

Define variable scope.

Block parameters are always local to their block, never assigns values to existing variables (Ruby 1.9).

Use `{ }` or `do/end`.

```ruby
do |var|
  put 123
end
```

Accept block:

```ruby
def print_message(&b)
  puts(b.call)
end
```

Check if block given:

```ruby
yield y if block_given? # iterator?
```

Block local variables:
```ruby
1.upto(4) { |x; y, z| p x } # y and z - are block local variables
```

#### Proc object

A proc object represents a block.

Both procs and lambdas are functions rather than methods invoked on an object.

### Struct

Similar to namedtuple in Python.

[Struct](https://ruby-doc.org/core-2.5.0/Struct.html)

```ruby
Customer = Struct.new(:name, :address) do
  def greeting
    "Hello #{name}!"
  end
end

dave = Customer.new("Dave", "123 Main")
```

Making immutable:
```ruby
Point = Struct.new('Point', :x, :y)
class Point
  undef x=, y=, []=
end
```

Open and add a method:
```ruby
class << Point
  def sum(*points)
    x = y = 0
    points.each {|p| x += p.x; y += p.y}
    Point.new(x, y)
  end
end
```

### Enumerable

Rhyming methods:

- `collect`
- `select`
- `reject`
- `inject`

Turn array into enumerable when passing for processing:
```ruby
process(data.to_enum)
```

Usage:
```ruby
for line, number in text.each_line.with_index
  p "#{number + 1}: #{line}"
end
```

Turning externally iterable into an Enumerable:

```ruby
module Iterable
  include Enumerable

  def each
    loop { yield self.next }
  end
end
```

### Iterators

In Ruby, the iterator method is in control and "pushes" values to the block that wants them. The most of other languages do the opposite: the client code that uses the iterator is in control and "pulls" values from the iterator when it needs them.

```ruby
numbers = [1, 2, 3]
numbers.each { |n| puts n }
```

Use `next` instead of return if want to return specific value(s) from the block.

### Exceptions

```ruby
begin
	pass
rescue
	pass
end

begin
    answer = number / divisor
rescue ZeroDivisionError => e
  	puts e.message
else
  # when none of the rescue clauses are needed
  # exceptions here will not be handler
ensure
  # code that always runs
end
```

!!! tip "return in ensure"
    If an `ensure` clause includes a `return` statement, then exception propagation stops, and the containing method returns. `break` and `next` have similar effects.

    If the body of a begin statement includes a return statement, the code in the ensure clause will be run before the method can actually return to its caller. Furthermore, if an ensure clause contains a return statement of its own, it will change the return value of the method.

"Normal" errors, which typical Ruby programs try to handle, are subclasses of `StandardError`.
If called with Exception object as a single argument - it raises that exception.
If with string - created `StandardError` with messages = given text and raises it.
Excption class can be given as argument because it has `exception` method, also string can be passed as the second argument and will be used as message.
The third argument is backtrace (array if strings).

```ruby
raise ValueError
raise ValueError, 'value error'
```

`$!` refers to the Exception object that is being handled.

`rescue` does not define a new variable scope.

```ruby
rescue ValueError, TypeError => e
rescue Exception # catch all
rescue StandardError # retry
  retry
end
```

The code in the ensure clause is guaranteed to run, but it does not affect the value of the begin statement.

#### Raise

If raise is called without arguments - it creates a new RuntimeError without message and raises it.

### Modules

Similar to class but can not be instantiated and can not be subclassed.

Modules are used as namespaces and as mixins.
If a module defines instance methods instead of the class methods, those instance methods can be mixed into other classes.

```ruby
class MyCls
  include Enumerable
end

# or

MyCls.new.extend(Enumerable)
```

It is legal to include one module into another.

Modules can contain constants.

Class is a subclass of Module, so classes can be used as namespace, but can not be used as mixins.

Methods inside module:
```ruby
module Base64
  MY_CONST = 1

  def self.encode
  end
end

Base64.encode(data)
Base64::MY_CONST
```

Creating modules like Math or Kernel: define your methods as instance methods of the module. Then use module_function to convert those methods to "modulefunctions" (module_function is similar to private, protected).

### Classes

A class is a collection of related methods that operate on the state of an object.

Class instances may encapsulate any number of internal instances, but they expose only methods to the outside world.

Assignment to an attribute of array element is actually Ruby shorthand for method invocation.

Classes and modules are "open", and can be modified and extended at runtime.

Classes can include or inherit methods from modules.

It is possible to define getters and setters for accessing state directly. These pairs of accessor methods are known as attributes and distinct from instance variables.

Any ruby program can add methods to existing classes, and it is even possible to add "singleton methods" to individual objects.

`self` - within the body of the class, but outside of any instance methods defined by the class, refers to the class being defined.

Class variables are visible to, and shared by, the class methods and the instance methods of a class, and also by the class definition itself.

```ruby
class Customer
   @@no_of_customers = 0  # class variable
   def initialize(id, name, addr)  # when we call new
      @cust_id = id  # instance variables
      @cust_name = name
      @cust_addr = addr
   end
end
```

Class can be reopened (take existing class and open it).

Extending a class:

```ruby
class Sequence
  include Enumerable
end
```

Overriding methods:

```ruby
def [](index)
end

def *(factor)
end
```

`new` method - allocates memory to hold the new object, initializes the state of that newly allocated "empty" object by invoking `initialize` method with `new` arguments.

Getter/setter:
```ruby
class Value
  def initialize(x)
    @x = x
  end

  def x # getter
    @x
  end

  def x=(value) # setter
    @x = value
  end
end
```

Using setter within class:
```ruby
self.x=1
```

attr_reader/attr_accessor can be used:
```ruby
class Value
  attr_accessor :x

  def initialize(x)
    @x = x
  end
end
```

Class attr_reader/attr_accessor:
```ruby
class Value
  class << self
    attr_reader :a, :b
  end
end
```

If a subclass assigns a value to a class variable already in use by a superclass, it does not create its own private copy of the class variable, but instead alters the value seen by the superclass.

If a constant is averrided in a subclass - a new constant will be created instead, so the class and its parent will have different constants.

#### Self

In singleton methods - refers to the class:
```ruby
class Dog
  def self.about
    self  # Dog
  end
end
```

#### Singleton

```ruby
require 'singleton'

class ExampleState
  include Singleton

  def initialize
    @a = 1
  end

  def inc
    @a += 1
  end
end

ExampleState.instance.inc
```

#### Memoization

```ruby
def something
  @something = Something.new()
end
```

#### Copy

Shallow copy:
```ruby
obj.clone
obj.dup
```

If an object defines `initialize_copy` - it will be used to create a copy.

Clone: copies both frozen and tainted objects.
Dup: copies tainted state, copying a frozen object - returns an unfrozen copy.
Clone: copies any singleton methods.
Dup: does not copy singleton methods of an object.

Deep copy:
```ruby
Marshal.load(Marshal.dump(o))
```

#### Subclassing

In Ruby, you should only subclass when you are familiar with the implementation of the superclass. If you only want to depend on the public API of a class and not on its implementation, then you should extend the functionality of the class by encapsulating and delegating to it, not by inheriting from it.

## Zen

[The Zens of Python and Ruby](https://www.automation-excellence.com/blog/zens-python-and-ruby)

| The Zen of Python by Tim Peters                                       | The Zen of Ruby by Eric Pierce                                           |
|-----------------------------------------------------------------------|--------------------------------------------------------------------------|
| Beautiful is better than ugly.                                        | Beauty is in the eye of the beholder.                                    |
| Explicit is better than implicit.                                     | Implicit is preferable to explicit.                                      |
| Simple is better than complex.                                        | Simple is boring.                                                        |
| Complex is better than complicated.                                   | Complex is interesting.                                                  |
| Flat is better than nested.                                           | Delegate the details to someone else.                                    |
| Sparse is better than dense.                                          | If possible, make it a one-liner.                                        |
| Readability counts.                                                   | Readability is sometimes nice.                                           |
| Special cases aren't special enough to break the rules.               | Special cases are everywhere; the rules can't cover them all.            |
| Although practicality beats purity.                                   | When in doubt, monkeypatch.                                              |
| Errors should never pass silently.                                    | Errors should be suppressed.                                             |
| Unless explicitly silenced.                                           | Unless whiny nils is turned on.                                          |
| In the face of ambiguity, refuse the temptation to guess.             | When in doubt, make assumptions about what the user wanted.              |
| There should be one- and preferably only one -obvious way to do it.   | There should be many- preferably dozens -of non-obvious ways to do it.   |
| Although that way may not be obvious at first unless you're Dutch.    | What's obvious to you may be completely unintuitive to someone else.     |
| Now is better than never.                                             | Now is better than later.                                                |
| Although never is often better than *right* now.                      | And later is better than never.                                          |
| If the implementation is hard to explain, it's a bad idea.            | If the design is flawed, explain why in the implementation docs.         |
| If the implementation is easy to explain, it may be a good idea.      | If the design is good, don't bother with implementation docs.            |
| Namespaces are one honking great idea - let's do more of those!       | Namespaces are completely unnecessary - let's make everything global!    |

## Vocabulary

The `arity` of an operator - the number of operands it operates on.

Iterator - any method that uses the `yield` statement.

External iterator - when the client controls the iteration (we call next when we need the next element, raises `StopIteration` when no more elements).

Internal iterator - when the iterator controls the iteration.

Lambda - a function that can be manipulated as objects.

A singleton - a class that has only a single instance. Singletons can be used to store global program state within an object-oriented framework and can be useful alternatives to class methods and class variables.

Metaprogramming - writing programs that help you write programs. Is a set of techniques for extending Ruby's syntax in ways that make programming easier.

Weak reference - object which holds a reference to a value without preventing the value from being garbage collected if they become otherwise unreachable.

Deadlock - is the condition that occurs when all threads are waiting to acquire a resource held by another thread.

## Libs

### Standard

#### Time

```ruby
Time.now # (same as Time.new)
Time.local(2007, 7, 8)
Time.utc(2007, 7, 7, 9, 10)
```

#### Files

```ruby
File.unlink('fname') # remove file
```

#### Threads

Long-running compute-bound threads should periodically call Thread.pass to ask the scheduler to yield the CPU to another thread.

Thread states:

- run (runnable)
- sleep (sleeping)
- aborting (aborting)
- false (terminated normally)
- nil (terminated with exception)

### External

[Dry-rb](https://dry-rb.org/)

#### RSpec

Run:
```bash
rspec spec/folder
rspec spec/folter/test_spec.rb
rspec spec/folder/test_spec.rb --example(-e) name
rspec spec/folder/test_spec.rb:25 (code line)
rspec --only-failures (requires config)
```

Pending:
```ruby
if 'does something' do
  pending 'Not implemented yet ...'
  expect().to be()
end
```

##### Testing

Expect:
- `.to`
- `.not_to`

Arrays:
```ruby
expect().to match_array
```

`describe` and `it` - organization.
`expect` - verification.
`let` - initializes data on demand.
`context` (lias to `describe`) - grouping for setup and examples.
`before` hook - run before each example (can be inside context).

Expect:
- be_empty
- eq

### Tools

`rvm` - ruby version manager.

`gem install rails` - package manager.

## Compare to Python

Objects in ruby do not expose attributes, only methods.

The fact that top-level methods are private means that they must be invoked like functions, without an explicit receiver. In this way, Ruby mimics a procedural programming paradigm within its strictly object-oriented framework.

Blocks in Ruby is a powerful and popular. A similar, less functional thing in Python is lambda.

Braces in method calls are optional.

Ruby does not use space to define code blocks.

Ruby iterators = Python generators.

Ruby sequences = Python iterators.

Python namedtuple = Ruby Struct.new.

Python coroutines = Ruby fibers.

String are mutable in Ruby.

## Links

[Ruby at LaunchSchool](https://launchschool.com/books/ruby/read/introduction)
Learn Ruby the Hard Way by Zed Shaw (to read)
[The Ruby Programming Language](https://www.amazon.com/Ruby-Programming-Language-Everything-Need/dp/0596516177) by David Flanagan, Yukihiro Matsumoto
