# class for mutations !!
from settings import BIN
import random
class mutations:
    def __init__(self):
        self.select = {1: self.random_mutate, 2: self.swap_mutate, 3: self.insertion_mutate, BIN: self.distroy_mutate}

    def random_mutate(self, target_size, member, character_creation):
        ipos = random.randint(0, target_size - 1)
        delta = character_creation(target_size)
        member.object = member.object[:ipos] + [delta] + member.object[ipos + 1:]

    def swap_mutate(self, target_size, member, character_creation):
        ipos = random.randint(0, target_size - 2)
        ipos2 = random.randint(ipos + 1, target_size - 1)
        member.object = member.object[:ipos] + [member.object[ipos2]] + member.object[ipos + 1:ipos2] + [
            member.object[ipos]] + member.object[ipos2 + 1:]

    def insertion_mutate(self, target_size, member, character_creation):
        ipos = random.randint(0, target_size - 2)
        ipos2 = random.randint(ipos + 1, target_size - 1)
        member.object = member.object[:ipos] + member.object[ipos + 1:ipos2] + [member.object[ipos]] + member.object[
                                                                                                       ipos2:]

    def distroy_mutate(self, target_size, member, character_creation):
        # ipos = random.randint(0, len(member.object) - 1)
        # member.remove_bin(ipos)
        # ipos2 = random.randint(0, len(member.object) - 1)
        # member.remove_bin(ipos2)
        # ipos3 = random.randint(0, len(member.object) - 1)
        # member.remove_bin(ipos3)
        pass
