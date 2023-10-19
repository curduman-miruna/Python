def compose(musical_notes, moves, start_position):
    song = []
    current_position = start_position
    song.append(musical_notes[start_position])
    for move in moves:
        current_position = (current_position + move) % len(musical_notes)
        song.append(musical_notes[current_position])

    return song


musical_notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start_position = 2

composed_song = compose(musical_notes, moves, start_position)
print(composed_song)
