Built as a Python 3.7.0 duplication of [Turing School's](https://github.com/turingschool) Mythical Creature exercises([Ruby](https://github.com/turingschool/ruby-exercises/tree/master/mythical-creatures), [Javascript](https://github.com/turingschool-examples/javascript-foundations/tree/master/mythical-creatures)). These exercises serve as an excellent way to practice TDD, Classes, and basic syntax.

This iteration utilizes the built in testing of Python's 'unittest'

I recommend using pdb([documentation](https://docs.python.org/3/library/pdb.html)) for debugging as you work through.

The recommended order can be found below.

##### Note
The .gitignore file currently contains `/creatures/*.py`, which will keep your created creature classes from being pushed to GitHub. If you would like them pushed up (i.e. to submit this work to someone) simply delete the line. 

# Pythical Creatures

A collection of exercises to practice Python and TDD

## How to Run

In order to complete these exercises create a class for each of the mythical creatures that has a test file.

Navigate to the `pythical-creatures` directory in your terminal, and then run your first test:

```
python3 test_unicorn.py
```

That will likely produce an error saying `ModuleNotFoundError: No module named 'creatures.unicorn'`.

Create that file in the `creatures` directory (`touch creatures/unicorn.py`) and then run your test again. Continue to follow the errors that your test provides until the test passes. Then, unskip the next test by removing the line that says `@unittest.skip('Skipped Test')`. Continue until all tests pass for all creatures.

## Suggested Order

* `test_unicorn.py`
* `test_vampire.py`
* `test_dragon.py`
* `test_hobbit.py`
* `test_pirate.py`
* `test_wizard.py`
* `test_medusa.py`
* `test_werewolf.py`
* `test_centaur.py`

## Extra Challenges
Coming soon!

* `test_direwolf.py`
* `test_fairy.py`
* `test_ogre.py`
* `test_sphinx.py`

### Testing with pytest

Documentation can be found [here](https://docs.pytest.org/en/latest/announce/release-3.7.0.html).

### The Dreaded `if` Statement

Can you complete implementations of each of the creatures without using `if`
statements? Think about how removing them affects your code. Remember that
a `case` is just a different form of `if`, so don't use it.

### Imagine Two Creatures

Can you add two new creatures to the repository? How about a Hydra? Add unittest
tests exercising some of the following concepts:

* Passing data into `__init__`
* Using functions to change the internal state of an instance
* Using functions to query the internal state of an instance
* Functionality that necessitates the internal use of an Array
