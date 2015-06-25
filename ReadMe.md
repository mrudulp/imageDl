# ReadMe

## Introduction

This repository contains two files *myhtmlparser.py* and *myhtmlparsertest.py*

* Myhtmlparser.py

It is the main code which reads xhtml page, extracts *img* tag and downloads the images.
Downloaded files are saved in directory with current timestamp

* Myhtmlparsertest.py

It contains unittest code for Myhtmlparser.py
Any new unittest code should be added here.

## How to use

* Running Code

    + Myhtmlparser expects <url> input. Format of the command is as follows -
    `python myhtmlparser.py <url>`

    **Note** - Url should be in http format. Anything other than http format would be marked as exception. 

    + Code outline

    *start_parser* method is the one which does all the bullwork of parsing and downloading image files
    Other methods are helper methods.

* Running Tests

    + Tests are run by giving command --
    `python myhtmlparsertest.py`

    At the end of test run, results of the run would be shown
