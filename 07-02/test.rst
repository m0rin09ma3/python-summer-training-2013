===================
Document Title Text
===================

Section Title
=============

.. comment

Subsection Title
----------------
A paragraph for the subsection.

- Item 1
- Item 2
- Item 3

1. Item 1 text
2. Item 2 text

1. New item 1
#. New item 2
#. New item 3

term 1
    Definition 1.

term 2
    Definition 2, paragraph 1.

term 3 : classifier 1
    Definition 3

-a             Output all.
-b             Output both (this description is quite long).
-c arg         Output just arg
--long         Output all day long.

::

    for a in [5,4,3,2,1]:    # this is program 
        print a
    print "it's..."
    # a literal block continues until the indent

Normal plain text paragraph.

>>> print 'this is a Doctest block'
this is a Doctest block

=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

+------------------------+------------+
| Header row, column 1   | Header 2   |
| (header rows optional) |            |
+========================+============+
| body row 1, column 1   | column 2   |
+------------------------+------------+
| body row 2   Cells may span columns |
+------------------------+------------+
| body row 3             | Cells may  |
+------------------------+ span rows  +
| body row 4             |            |
+------------------------+------------+

This is a  `link <http://kushaldas.in>`_

.. `Python programming language`_ is very nice.
.. _Python programming language:

.. note:: This is a note.
   - List item 1
   - List item 2

This is *emphasized text*.

Please RTFM [#]_ or you can read [#]_.

.. [#] Read The Fine Manual
.. [#] The next fine manual

