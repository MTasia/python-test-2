import os
import sys
import pytest

import dir_reader as d_r
import file_reader as f_r


def test_DirReader():
    for file in d_r.DirReader("test_dir"):
        assert(file=="test_dir"+"\\test.txt")
