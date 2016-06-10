#!/usr/bin/python3

from __future__ import absolute_import, division, print_function
import six
import context
from hypothesis import given, example
from hypothesis.strategies import text

from new_acsemble.hypothesis_example import encode, decode


@given(text())
@example('')
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s


if __name__ == "__main__" :
    import sys
    from numpy.testing import run_module_suite
    run_module_suite(argv=sys.argv)
