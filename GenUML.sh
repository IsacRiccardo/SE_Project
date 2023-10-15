#!/usr/bin/env bash

tools/py2uml.py CarBoard_Logic.py | dot -T png -o UML/UML.puml