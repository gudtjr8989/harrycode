class board:
    def __init__(self,t,c):
        self.t = t
        self.c = c
    def __repr__(self)->str:
        return f'{self.t} | {self.c}'

x=board("타이틀","컨텐츠")
print(x)
