# Step 1
In this step your goal is to parse a valid simple JSON object, specifically: ‘{}’ and an invalid JSON file and correctly report which is which. So you should build a very simple lexer and parser for this step.

Your program should report to the standard output stream a suitable message and exit with the code 0 for valid and 1 for invalid. 
It is conventional for CLI tools to return 0 for success and between 1 and 255 for an error and allows us to combined CLI tools to create more powerful programs.

You can test your code against the files in the folder tests/step1. 
Consider automating the tests so you can run them repeatedly as you progress through the challenge.
# Step 2
In this step your goal is to extend the parser to parse a simple JSON object containing string keys and string values, i.e.:

{"key": "value"}

You can test against the files in the folder tests/step2.
