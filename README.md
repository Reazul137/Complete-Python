1. <b>Introduction and setting Up Python.</b>
<p> At first we need to download to Python itself so that we can access it.
Go to python website(www.python.org) and download the latest python file 3.5(version) or more. And install the file,
Then we need to setup an IDE(Integrated development environment), in IDE we can run our python program, some IDE are, pycharm, spyder etc. </p>

2. <b>Comments.</b>
<p> Using comments within your Python programs helps to make your programs more readable for humans, including your future self. Including appropriate comments that are relevant and useful can make it easier for others to collaborate with you on programming projects and make the value of your code more obvious. Comments in Python begin with a <b>hash mark (#)</b> and <b>whitespace
character</b> and continue to the end of the line </p>

I. <b>Understanding Data Types</b>
<p>In Python, like in all programming languages, data types are used to classify one particular type of data. This is important because the specific data type you use will determine what values you can assign to it and what you can do to it (including what operations you can perform on it). </p>
<b>Data Types in Python : </b>
<p> 1. <b>Python Numbers : </b><br>
    <p>Integers, floating point numbers and complex numbers falls under Python numbers category. They are defined as <b>int</b>, <b>float</b> and <b>complex</b> class in Python.</p>
    2. <b>Python List : </b><br>
    <p>List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible. All the items in a list do not need to be of the same type.</p>
    3. <b>Python Tuple : </b><br>
    <p>Tuple is an ordered sequence of items same as list.The only difference is that tuples are immutable. Tuples once created cannot be modified. Tuples are used to write-protect data and are usually faster than list as it cannot change dynamically. It is defined within parentheses () where items are separated by commas.</p>
    4. <b>Python Strings : </b><br>
    <p>String is sequence of Unicode characters. We can use single quotes or double quotes to represent strings. Multi-line strings can be denoted using triple quotes, <b>'''</b> or <b>"""</b>.</p>
    5. <b>Python Set : </b><br>
    <p>Set is an unordered collection of unique items. Set is defined by values separated by comma inside braces { }. Items in a set are not ordered.</p>
    6. <b>Python Dictionary : </b><br>
    <p>Dictionary is an unordered collection of key-value pairs. It is generally used when we have a huge amount of data. Dictionaries are optimized for retrieving data. We must know the key to retrieve the value. In Python, dictionaries are defined within braces {} with each item being a pair in the form key:value. Key and value can be of any type.</p>
    7. <b>Conversion between data types : </b><br>
    <p>We can convert between different data types by using different type conversion functions like <b>int()</b>, <b>float()</b>, <b>str()</b> etc.</p>

3. <b>Displaying Input / Output / Data With The Print Function and more.</b>
<p>when we build interactive software applications. We want the end users to enter some data or to input some data that our application will use. And at some point our application will send some data back to the end user or display some output to the user.
so, to perform these two input and output operations in a standalone python program we use the <b>input()</b> function and the <b>print()</b> functions.</p>

4. <b>Variables.</b>
<p>Python is dynamically typed, which means that you don't have to declare what
type each variable is. In Python, variables are a storage placeholder for texts and numbers. It must have a name so that you are able to find it again. The variable is always assigned with the equal sign, followed by the value of the variable.</p>

5. <b>Variable Naming Rules.</b>
<p>Must begin with a letter <b>(a - z, A - B) or underscore (_)</b> Other characters can be letters, numbers or _
Case Sensitive. Can be any (reasonable) length. There are some reserved words which you cannot use as a variable name because Python uses them for other things.</p>

6. <b>Operators</b>
<p>Operators are special symbols in Python that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.<br>
<b>Arithmatic operators</b>
    <p>Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication etc.</p>
Add two operands or unary plus <b>"+"</b>.<br>
Subtract right operand from the left or unary minus <b>"-"</b>.<br>
Multiply two operands <b>"*"</b>.<br>
Divide left operand by the right one (always results into float) <b>"/"</b>.<br>
Modulus - remainder of the division of left operand by the right <b>"%"</b>.<br>
Floor division - division that results into whole number adjusted to the left in the number line <b>"//"</b>.<br>
Exponent - left operand raised to the power of right <b>"**"</b>.</p><br>

<b>Comparison operators</b>
<p>Comparison operators are used to compare values. It either returns True or False according to the condition.</p>
Greater that - True if left operand is greater than the right <b>">"</b>.<br>
Less that - True if left operand is less than the right <b>"<"</b>.<br>
Equal to - True if both operands are equal <b>"=="</b>.<br>
Not equal to - True if operands are not equal <b>"!="</b>.<br>
Greater than or equal to - True if left operand is greater than or equal to the right <b>">="</b>.<br>
Less than or equal to - True if left operand is less than or equal to the right <b>"<="</b>.<br>
    
 <b>Logical operators</b>
 <p>Logical operators are the and, or, not operators.</p>
 and - True if both the operands are true.<br>
 or  - True if either of the operands is true.<br>
 not - True if operand is false (complements the operand).<br>
 
 <b>Bitwise operators</b>
 <p>Bitwise operators act on operands as if they were string of binary digits. It operates bit by bit, hence the name.</p>
 & - Bitwise AND.<br>
 | - Bitwise OR.<br>
 ~ - Bitwise NOT.<br>
 ^ - Bitwise XOR.<br>
 >> - Bitwise right shift.<br>
 << - Bitwise left shift.<br>
 
 <b>Assignment operators</b>
 <p>Assignment operators are used in Python to assign values to variables.</p>

 <b>Special operators</b>
 <p>Python language offers some special type of operators like the identity operator or the membership operator.</p>
 
<b>Identity operators</b>
is - True if the operands are identical (refer to the same object)<br>
is not - True if the operands are not identical (do not refer to the same object)<br>
