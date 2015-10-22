## Q1:  
(ex8)  
不赋值的串也可以输出？  
针对如下代码：
<pre><code>
formatter="%r %r %r %r"  
print formatter %(formatter,formatter,formatter,formatter)
</pre></code>

## Q2: 
(ex15)  
<pre><code>
from sys import argv

script, filename = argv
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
</pre></code>

为什么注释掉import也可以运行？  

## Q3: 
(ex16)  
<pre><code>
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
</pre></code>

为什么将truncate注释之后还是会清空文件呢？  

### Answer：
15.10.21 'w'会清空，'a'则不会。

## Q4: 
(ex17)  
<pre><code>
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

\# we could do these two on one line too, how?
input = open(from_file)
indata = input.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Alright, all done."

output.close()
input.close()
</pre></code>

为什么只能用print indata而不能用output.read()或open(to_file).read()？给出的提示信息是：File not open for reading.

## Q5: 
(ex20)  
<pre><code>
from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
</pre></code>

怎么才能让readline()所读取的内容与行号参数有关？

## Q6: 
(ex20)  
起始行号为什么不是0而是1？

## Q7: 
raw_input中出现“小”和“大”字无法打印出来，但直接print“小”和“大”可以。why？
