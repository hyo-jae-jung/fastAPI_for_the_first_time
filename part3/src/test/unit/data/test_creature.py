import sys
sys.path.append('/mnt/c/Users/hyoja/OneDrive/문서/GitHub/fastAPI_for_the_first_time/part3/src')

import os
import pytest 
from error import Missing, Duplicate 
from model.creature import Creature 

os.environ["CRYPTID_SQLITE_DB"] = ":memory:"

from data import creature

@pytest.fixture 
def sample() -> Creature:
    return Creature(
        name="yeti", 
        aka="Abominable Snowman",
        country="CN", 
        area="Himalayas", 
        description="Hapless Himalayan",
        )

def test_create(sample):
    resp = creature.create(sample)
    assert resp == sample 

def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = creature.create(sample)

def test_get_one(sample):
    resp = creature.get_one(sample.name)
    assert resp == sample

def test_get_one_missing():
    with pytest.raises(Missing):
        resp = creature.get_one("boxturtle")

def test_modify(sample):
    creature.country = "JP" # Japan!
    resp = creature.modify(sample.name, sample)
    assert resp == sample

def test_modify_missing():
    thing: Creature = Creature(
                        name="snurfle", 
                        description="some thing",
                        country="somewhere",
                        area="",
                        aka="",
                        )
    with pytest.raises(Missing):
        _ = creature.modify(thing.name, thing)

def test_delete(sample):
    resp = creature.delete(sample.name)
    assert resp is True

def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = creature.delete(sample.name)

