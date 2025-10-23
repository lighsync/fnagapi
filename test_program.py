# FNAG Education Edition, API Test Program
from fnagapi import entity, session
from time import sleep
from constants import *

session.start_program()
session.set_level(6)

entity.ai_ignore(ENTITY_WANDARMO)
entity.ai_ignore(ENTITY_FSTER)

print(entity.get_ai_ignored_list())

sleep(25)
entity.ai_unignore(ENTITY_WANDARMO)
sleep(10)
entity.ai_unignore(ENTITY_FSTER)

sleep(5)
entity.ai_disable()
session.end_program()
