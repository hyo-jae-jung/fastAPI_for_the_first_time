import sys
sys.path.append('/mnt/c/Users/hyoja/OneDrive/문서/GitHub/fastAPI_for_the_first_time/part3/src')

from model.creature import Creature  
from service import creature as code  

sample = Creature(
    name="Yeti",
    country="CN",
    area="Himalayas",
    description="Hirsute Himalayan",
    aka="Abominable Snowman"
)

def test_create():
    resp = code.create(sample)
    assert resp == sample 

def test_get_exists():
    resp = code.get_one("Yeti")
    assert resp == sample  

def test_get_missing(): # 10장 기준 실패하지만 이후 수정 예정
    resp = code.get_one("boxturtle")
    assert resp is None
    