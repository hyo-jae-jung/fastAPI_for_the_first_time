import sys
sys.path.append('/mnt/c/Users/hyoja/OneDrive/문서/GitHub/fastAPI_for_the_first_time/part3/src')

import os
import pytest 
from error import Missing, Duplicate 
from model.explorer import Explorer 

os.environ["CRYPTID_SQLITE_DB"] = ":memory:"

from data import explorer

@pytest.fixture
def sample() -> Explorer:
    return Explorer(
        name="a",
        country="b",
        description="c",
    )

def test_create(sample):
    resp = explorer.create(sample)
    assert resp == sample 
    
def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = explorer.create(sample)

def test_get_one_missing():
    with pytest.raises(Missing):
        _ = explorer.get_one("aa")

def test_modify(sample):
    explorer.country = "bb"
    resp = explorer.modify(sample.name, sample)
    assert resp == sample

def test_modify_missing():
    one: Explorer = Explorer(name="aa", country="b")
    with pytest.raises(Missing):
        _ = explorer.modify(one.name, one)

def test_delete(sample):
    resp = explorer.delete(sample.name)
    assert resp is True  

def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = explorer.delete(sample.name)