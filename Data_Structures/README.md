## Basic Data Structures ##

### Arrays and Linked Lists ###

------

#### Arrays ####

_Definition_   **Array**: contiguous area of memory consisting of equal-size elements indexed by contiguous integers.

_What's special about arrays?_

We have random access --> we have constant time access to any particular element in an array; constant access to read and write

_How can we figure out the address of a particular array element?_

`array_addr + element_size * ( i - first_index )`
where `i` is the index of the element of interes

_Multi-Dimensional Arrays_:
_Supposition: row-major order_

|   |   |   |   |   |   |
| - | - | - | - | - | - |
|   |   |   |   |   |   |
|   |   |   | (3,4)  |   |   |

1. Skip the rows: `(3 - 1) * 6`, 12 elements we are skipping for those rows in order to get to row 3.
2. Skip the elements in the same row: `(4 - 1)`
3. array_addr + `elem_size * ((3 - 1) * 6 + (4 - 1))`

When we layout an array as a **row-major** order, the number of columns is changing most rapidly, i.e.:

| (1, 1) |
| ------ |
| (1, 2) |
| (1, 3) |
| (1, 4) |
| (1, 5) |
| (1, 6) |
| (2, 1) |
| ... |

When we layout an array as a **column-major** order, the row index is changing most rapidly, i.e.:

| (1, 1) |
| ------ |
| (2, 1) |
| (3, 1) |
| (1, 2) |
| (2, 2) |
| (3, 2) |
| (1, 3) |
| ... |

**Times for Common Operations**

|   |  Add |  Remove |
| - | - | - |
| Beginning  | O(n)  | O(n)  |
|  End |  O(1) | O(1) |
|  Middle | O(n)  |  O(n) |

##### Summary #####
* Array: contiguous area of memory consisting of equal-size elements indexed by contiguous integers.
* Constant-time access to element.
* Constant time to add/remove at the end.
* Linear time to add/remove at an arbitrary location.

------

#### Singly-Linked Lists ####

Head pointer that points to a node that then has some data that points to another node...

Node contains:
* key
* next pointer

**List API**

|  function | description | TimeComplexity (no tail) | TimeComplexity (with tail) |   |
| - | - | - | - | - |
| PushFront(Key) | add to front | O(1) | O(1) |
| Key TopFront() | return front item | O(1) | |
| PopFront() | remove front item | O(1) | O(1) |
| PushBack(Key) | add to back _also known as Append_ | O(n) | O(1)
| Key TopBack() | return back item | O(n) | O(1) |
| PopBack() | remove back item | O(n) | O(n) |
| Boolean Find(Key) | is key in list? | O(n) | |
| Erase(Key) | remove key from list | O(n) | |
| Boolean Empty() | empty list? | O(1) | |
| AddBefore(Node, Key) | adds key before node | O(n) | |
| AddAfter(Node, Key) | adds key after node | O(1) | |


**Code**:

```
PushFont(key):
node <-- new node
node.key <-- key
node.next <-- head
head <-- node
if tail = nil:
	tail <-- head
```

```
PopFront():
if head = nil:
	ERROR: empty list
head <-- head.next
if head = nil:
	tail <-- nil
```

```
PushBack(key):
node <-- new node
node.key <-- key
node.next = nil
if tail = nil:
	head <-- tail <-- node
else:
	tail.next <-- node
	tail <-- node
```

```
PopBack():
if head = nil: ERROR: empty list
if head = tail:
	head <-- tail <-- nil
else:
	p <-- head
	while p.next.next != nil:
		p <-- p.next
	p.next <-- nil; tail <-- p
```

```
AddAfter(node, key):
node2 <-- new node
node2.key <-- key
node2.next = node.next
node.next = node2
if tail = node:
	tail <-- node2
```

------


#### Doubly-Linked Lists ####

Node contains:
* key
* next pointer
* prev pointer

```
PushBack(key):
node <-- new node
node.key <-- key; node.next = nil
if tail = nil:
	head <-- tail <-- node
	node.prev <-- nil
else:
	tail.next <-- node
	node.prev <-- tail
	tail <-- node
```

```
PopBack():
if head = nil: ERROR: empty list
if head = tail:
	head <-- tail <-- nil
else:
	tail <-- tail.prev
	tail.next <-- nil
```

```
AddAfter(node, key):
node2 <-- new node
node2.key <-- key
node2.next <-- node.next
node2.prev <-- node
node.next <-- node2
if node2.next != nil:
	node2.next.prev <-- node2
if tail = node:
	tail <-- node2
```

**List API**

|  function | description | TimeComplexity (no tail) | TimeComplexity (with tail) |   |
| - | - | - | - | - |
| PushFront(Key) | add to front | O(1) | O(1) |
| Key TopFront() | return front item | O(1) | |
| PopFront() | remove front item | O(1) | O(1) |
| PushBack(Key) | add to back _also known as Append_ | O(n) | O(1)
| Key TopBack() | return back item | O(n) | O(1) |
| PopBack() | remove back item | ~~O(n)~~ O(1) | O(n) |
| Boolean Find(Key) | is key in list? | O(n) | |
| Erase(Key) | remove key from list | O(n) | |
| Boolean Empty() | empty list? | O(1) | |
| AddBefore(Node, Key) | adds key before node | ~~O(n)~~ O(1) | |
| AddAfter(Node, Key) | adds key after node | O(1) | |

##### Summary #####

Linked lists have:
* Constant time to insert at or remove from the front
* With tail and doubly-linked, constant time to insert at or remove from the back
* O(n) time to find arbitrary element
* List elements need not be contiguous
* With doubly-linked list, constant time to insert between nodes or remove a node

------

#### References ####
See the chapter 10.2 in [CLRS] Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein. Introduction to Algorithms (3rd Edition). MIT Press and McGraw-Hill. 2009.

------


### Stacks and Queues ###

------

#### Stacks ####

_Definition_  **Stack**: Abstract data type with the following operations:
* Push(Key): adds key to collection
* Key Top(): returns most recently-added key
* Key Pop(): removes and returns most recently-added key
* Boolean Empty(): are there any elements?

Example:

**Balanced Brackets**

_Input_: A string str consisting of '(', ')', '[', ']' characters

_Output_: Return whether or not the string's parentheses and square brackets are balanced

* Balanced:
	* ''([])[]()''
	* ''((([([])]))())''
* Unbalanced:
	* ''([]])()''
	* ''][''

```
IsBalanced(str):
Stack stack
for char in str:
	if char in ['(', '[']:
		stack.Push(char)
	else:
		if stack.Empty(): return False
		top <-- stack.Pop()
		if (top = '[' and char != ']') or (top = '(' and char != ')'):
			return False
return stack.Empty()
```

##### Stack Implementation with Arrays #####

array = [ , , , , ]  
Push(a) --> [a, , , , ]  
Push(b) --> [a, b, , , ]  
Top() --> a  
Push(c) --> [a, b, c, , ]  
Pop() --> c --> [a, b, , , ]  
Push(d) --> [a, b, d, , ]  
Push(e) --> [a, b, d, e, ]  
Push(f) --> [a, b, d, e, f]  
Push(g) --> ERROR

##### Stack Implementation with Linked Lists #####

linkedlist = [/]head\s\s
Push(a) --> [head]->[a][/]  
Push(b) --> [head]->[b][]->[a][/]  
Top() --> b\s\s
Push(b) --> [head]->[c][]->[b][]->[a][/]  
Pop() --> [head]->[b][]->[a][/]  

_There is no  priori limit as to the number of elements you can add._


##### Summary #####
* Stacks can be implemented with either an array or a linked list
*  Each stack operation is O(1): Push, Pop, Top, Empty
* Stacks are ocassionaly known as LIFO queues (last in, first out)

------

#### Queues ####

_Definition_  **Queue**: Abstract data type with the following operations:
* Enqueue(Key): adds key to collection
* Key Dequeue(): removes and returns least recently-added key
* Boolean Empty(): are there any elements?

**FIFO**: First-In, First-Out = First-come, First-serve\s

##### Queue Implementation with Linked List #####

linkedlist = [/]head [/]tail  
Enqueue(a) --> [head]->[a][/]  
Enqueue(b) --> [head]->[a][]->[b][/]  
Enqueue(c) --> [head]->[a][]->[b][]->[c][/]  
Dequeue() --> [head]->[b][]->[c][/] _[a][] is going to be removed because it has been there the longest_  


* Enqueue: use List.PushBack
* Dequeue: use List.TopFront and List.PopFront
* Empty: use List.Empty()

##### Queue Implementation with Array #####

array = [ , , , , ]\s\s
Enqueue(a) --> [a, , , , ]  	_0=read, 1=write_  
Enqueue(b) --> [a, b, , , ] 	_0=read, 2=write_  
Enqueue(c) --> [a, b, c, , ] 	_0=read, 3=write_  
Empty() --> _no: read_index != write_index_  
Dequeue() --> [ , b, c, , ] 	_1=read, 3=write_  
Dequeue() --> [ , , c, , ]		_2=read, 3=write_  
Enqueue(d) --> [ , , c, d, ] 	_2=read, 3=write_  
Enqueue(e) --> [ , , c, d, e] 	_2=read, 4=write, then write index wraps back around to the initial element, 0=write_  
Enqueue(f) --> [ f, , c, d, e] 	_2=read, 1=write_  
Enqueue(g) --> ERROR _if we did enqueue g the read and write index would be the same_  
Dequeue() --> [ f, , , d, e] 	_3=read, 1=write_  
Dequeue() --> [ f, , , , e] 	_4=read, 1=write_  
Dequeue() --> [ f, , , , ] 		_0=read, 1=write_  
Dequeue() --> [ , , , , ] 		_1=read, 1=write_  

##### Summary #####
* Queues can be implemented with either a linked list (with tail pointer) or an array
* Each queue operation is O(1): Enqueue, Dequeue, Empty

------

#### References ####
See the chapter 10.1 in [CLRS] Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein. Introduction to Algorithms (3rd Edition). MIT Press and McGraw-Hill. 2009

------