#The dictionary assigns notes to number ob tones.
stepchart = {'C':0,'Cs':1,'Db':1,'D':2,'Ds':3,'Eb':3,'E':4,'Es':5,'Fb':4,
             'F':5,'Fs':6,'Gb':6,'G':7,'Gs':8,
             'Ab':8,'A':9,'Bb':10,'B':11,'Bs':12,'Cb':11}
interval={0:'first or octave',1:'second minor',2:'second',3:'minor third',
          4:'third',5:'perfect fourth',6:'tritone',7:'perfect fifth',
          8:'minor sixth',9:'sixth',10:'minor seventh',11:'seventh'}
def func():
    a=stepchart[input('Enter first note:')]
    b=stepchart[input('Enter second note:')]
    val=abs(a-b)
    print(interval[val])
while True:
    func()
