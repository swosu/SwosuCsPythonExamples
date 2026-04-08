# Teaching Notes: `zybooks_python_examples/ch01/magic_welcome.py`

## What This Code Is Teaching

This example teaches several beginner-friendly Python ideas in one short program:

- how to import a module with `import random`
- how to define and call a function
- how to store multiple strings in a list
- how to get user input with `input()`
- how to print formatted output with f-strings
- how a program can produce slightly different results each time using randomness

Because the script is short and readable, students can see how input, processing, and output connect in a complete program.

## Run Result

I ran the program with the name `Ada` as input.

Observed output:

```text
Enter your first name: Hey Ada
The world is your oyster, welcome to zyBooks!
```

Note: the second line may change on different runs because the script chooses a random welcome phrase from a list.

## Teacher-Facing Class Use

This is a strong early-class example because it feels more personal than `Hello, World!` while still staying very manageable. A good classroom flow is to first trace the script top to bottom, then ask students to predict what each line does before running it.

After that, invite students to extend the list of responses, change the greeting format, or add a second input such as favorite color or major. That turns the example into a small guided exercise that reinforces functions, lists, input, and string formatting without overwhelming beginners.
