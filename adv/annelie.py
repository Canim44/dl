from core.advbase import *

def module():
    return Annelie

        # `s1, s2.charged<=10000
        # `s1, s=2
        # `s2
        # `s3
        # `fs, seq=5 

class Annelie(Adv):
    comment = '1121'
    a1 = ('s',0.35,'hp70')
    a3 = ('energized_att', 0.20)
    conf = {}
    conf['acl'] = """
        `dragon
        `s1, s2.charged<=10000
        `s1, s=2
        `s2
        `s3
        `fs, seq=5 
        """
    coab = ['Halloween_Elisanne','Dagger','Peony']

    def prerun(self):
        self.stance = 0

    @staticmethod
    def prerun_skillshare(adv, dst_key):
        adv.stance = 0

    def s1_proc(self, e):
        if self.stance == 0:
            self.dmg_make(e.name,0.1+8.14)
            self.energy.add(1)
            self.hits += 2
            self.stance = 1
        elif self.stance == 1:
            self.dmg_make(e.name,2*(0.1+4.07))
            self.energy.add(2)
            self.hits += 4
            self.stance = 2
        elif self.stance == 2:
            self.dmg_make(e.name,3*0.1)
            self.dmg_make(e.name,3*3.54)
            self.hits += 6
            self.stance = 0

    def s2_proc(self, e):
        self.energy.add(2, team=True)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)