|travis|_ |coveralls|_ |pypi|_ |womm|_

.. |travis| image:: https://img.shields.io/travis/wimglenn/oyaml.svg?branch=master
.. _travis: https://travis-ci.org/wimglenn/oyaml

.. |coveralls| image:: https://img.shields.io/coveralls/wimglenn/oyaml.svg
.. _coveralls: https://coveralls.io/github/wimglenn/oyaml?branch=master

.. |pypi| image:: https://img.shields.io/pypi/v/oyaml.svg
.. _pypi: https://pypi.python.org/pypi/oyaml

.. |womm| image:: https://cdn.rawgit.com/nikku/works-on-my-machine/v0.2.0/badge.svg
.. _womm: https://github.com/nikku/works-on-my-machine


oyaml
=====

oyaml is a drop-in replacement for `PyYAML <http://pyyaml.org/wiki/PyYAML>`_ which preserves dict ordering.  Both Python 2 and Python 3 are supported. Just ``pip install oyaml``, and import as shown below:

.. code-block:: python

   import oyaml as yaml

You'll no longer be annoyed by screwed-up mappings when dumping/loading.
