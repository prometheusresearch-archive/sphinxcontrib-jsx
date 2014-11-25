sphinxcontrib.jsx
=================

JSX_ (JavaScript superset used in React_) extension for Sphinx_.

Installation
------------

::

  % pip install sphinxcontrib-jsx

Usage
-----

Add ``sphinxcontrib.jsx`` to ``extensions`` in ``conf.py``::

  ...
  extensions = ['sphinxcontrib.jsx']
  ...

Now you can use ``jsx`` directive in your documentation::

  .. jsx::

    var x = <div>Hello!</div>

Snippet above will be shown as literal block and automatically executed on page
load.

If you don't want to show source and only execute script, add ``hidesource``
options::

  .. jsx::
    :hidesource:

    var x = <div>Hello!</div>

Alternatively if you only want to show source and not execute script, use
``showsourceonly`` option::

  .. jsx::
    :showsourceonly:

    var x = <div>Hello!</div>

To activate ES6 transforms use ``harmony`` option::

  .. jsx::
    :harmony:

    <ul>
      {children.map(item => <li>{item}</li>)}
    </ul>

To strip type declarations from source code use ``striptypes`` option::

  .. jsx::
    :striptypes:

    var x: Number = 1

.. _JSX: http://facebook.github.io/react/docs/jsx-in-depth.html
.. _Sphinx: http://sphinx-doc.org/
.. _React: http://facebook.github.io/react/
