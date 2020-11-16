# -*- coding: UTF-8 -*-
# Import from standard library
import os
import second_pack
# Import from our lib
from second_pack.first_function import first_function
import pytest

"hi my purpose in life is to help Anton complete this challenge because he's tired."

def test_fist_function():
  test = "hi my purpose in life is to help Anton complete this challenge because he's tired."
  result = first_function()
  assert test == result
