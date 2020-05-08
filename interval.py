# stepchart[] keys notes to value of semitones
stepchart = {
    "C": 0,
    "C#": 1,
    "DB": 1,
    "D": 2,
    "D#": 3,
    "EB": 3,
    "E": 4,
    "E#": 5,
    "FB": 4,
    "F": 5,
    "F#": 6,
    "GB": 6,
    "G": 7,
    "G#": 8,
    "AB": 8,
    "A": 9,
    "A#": 10,
    "BB": 10,
    "B": 11,
    "B#": 12,
    "CB": 11,
}
# interval[] keys value of semitones to names of intervals
interval = {
    -11: "minor second",
    -10: "second",
    -9: "minor third",
    -8: "third",
    -7: "perfect fourth",
    -6: "tritone",
    -5: "perfect fifth",
    -4: "minor sixth",
    -3: "sixth",
    -2: "minor seventh",
    -1: "seventh",
    0: "first or octave",
    1: "second minor",
    2: "second",
    3: "minor third",
    4: "third",
    5: "perfect fourth",
    6: "tritone",
    7: "perfect fifth",
    8: "minor sixth",
    9: "sixth",
    10: "minor seventh",
    11: "seventh",
}


def func():
    note1 = input("Enter first note (tonic): ")
    note2 = input("Enter second note: ")
    first_semitone = stepchart[note1.upper()]
    second_semitone = stepchart[note2.upper()]
    distance = second_semitone - first_semitone
    print(interval[distance])
    func()


print(
    """Type note (i.e. C, D, E, etc.) followed by
'#' for sharp or 'b' for flat
"""
)
func()
