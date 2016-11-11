import micro
import numpy as np

def test_all_zeros():
    img = np.zeros([2, 2])
    assert(micro.specimen_ratio(img, 0.5) == 0.0)

def test_all_ones():
    img = np.ones([2, 2])
    assert(micro.specimen_ratio(img, 0.5) == 1.0)

def test_half_ones():
    img = np.eye(2)
    assert(micro.specimen_ratio(img, 0.5) == 0.5)

def test_rectangular():
    img = np.zeros([2, 3])
    assert(micro.specimen_ratio(img, 0.5) == 0.0)

def test_rectangular_2():
    img = np.zeros([3, 2])
    assert(micro.specimen_ratio(img, 0.5) == 0.0)
