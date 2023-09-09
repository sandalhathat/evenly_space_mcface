This program takes a string, including all spaces between terms, and 
evenly distributes the amount of space between each of those terms,
but excluding putting any space before the first term or any space after
the last term. 

The result is such that a string like this:<br> 

'apple---orange----------pear-banana-------------',<br>

where each '-' represents a blank space, (which I couldn't write
without the dashes due to markdown not including blank spaces), 
and turns it into this: <br> 

'apple---------orange---------pear---------banana'<br> 

As you can see, even though the terms are different in length, and in the input string, the spaces between each term is different, the output evenly distributes those spaces.