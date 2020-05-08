#stepchart[] keys notes to value of semitones
stepchart = {'C':0,'Cs':1,'Db':1,'D':2,'Ds':3,'Eb':3,'E':4,'Es':5,'Fb':4,
             'F':5,'Fs':6,'Gb':6,'G':7,'Gs':8,
             'Ab':8,'A':9,'Bb':10,'B':11,'Bs':12,'Cb':11}
#interval[] keys value of semitones to names of intervals
interval={-11:'minor second',-10:'second',-9:'minor third',-8:'third',
          -7:'perfect fourth',-6:'tritone',
          -5:'perfect fifth',-4:'minor sixth',-3:'sixth',
          -2:'minor seventh',-1:'seventh',
          0:'first or octave',1:'second minor',2:'second',3:'minor third',
          4:'third',5:'perfect fourth',6:'tritone, augmented fourth or diminished fifth',7:'perfect fifth',
          8:'minor sixth or augmented fifth',9:'sixth',10:'minor seventh or augmented sixth',11:'seventh'}
def func():
    a=stepchart[input('Enter first note (tonic):')]
    b=stepchart[input('Enter second note:')]
    v=b-a
    print(interval[v])
    func()
func()
