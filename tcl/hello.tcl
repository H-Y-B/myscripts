#!/usr/bin/tclsh 

puts {Hello, World!}
puts "Hello, World!"   ;#ghchgch


# vatiable
set a 3
puts $a


# List 
set myVariable {red green blue}
puts [lindex $myVariable 2]
set myVariable "red green blue"
puts [lindex $myVariable 1]


set  marks(english) {huangyubiao hello}
puts $marks(english)
