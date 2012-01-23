# Aphasia Treatment Program Activity Generator

There are three components to this package right now:

1. Microsoft Word template, which is the basis of the activity packet

2. Python scripts that generate:
    1. Word scramble puzzle
    2. Word search puzzle
    3. Arithmetic problems

3. OS X 10.7 apps which can be used in place of the raw Python scripts

The general workflow is to use the apps or the Python scripts to generate the raw output which can then be pasted directly (for the most part) into the Word document based on the template.

Here are the general steps to creating a complete packet:

1. Double click `Aphasia Treatment Program.dot` to create a new document in Word based on the template.
2. Customize the packet according to your needs. Note that styles are used strictly throughout the document. *For best results, you should change your formatting through the use of styles*.
3. Use the Python scripts or the OS X apps to generate the word scramble, word search, and math practice activities.

## Word scramble

Input
: A list of words separated by any non-alphanumeric character. Some valid inputs are:

        template, generator, word
        
    or
    
        template
        generator
        word
        
    Note that words such as "New Year" and "low-budget" will be split up into separate words: new, year, low, budget.
    
Output
: The generated output consists of three parts:

    * Word bank
    * Scrambled words
    * Answer key

### Word bank

## Word search

## Math practice

---

These steps have only been tested on two platforms:

* OS X 10.7 using Microsoft Office 2011
* Microsoft XP using Microsoft Office 2003
