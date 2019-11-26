def bowling_score(frames):
    pts = 0
    strike = []
    spare = 0
    last = 0
    for f, frame in enumerate(frames.split(' ')):
        for t, turn in enumerate(frame):
            if turn == 'X':
                pts += 10
                if strike:
                    pts += strike.pop() * 10
                if spare:
                    pts += 10
                    spare = 0
                if f < 9:
                    if not strike:
                        strike = [1, 1]
                    else:
                        strike[0] += 1
                        strike.insert(0, 1)
            elif turn == '/':
                inc = 10 - last
                pts += inc
                if strike:
                    pts += strike.pop() * inc
                if spare:
                    pts += inc
                    spare = 0
                if f < 9:
                    spare = 1
            else:
                inc = int(turn)
                pts += inc
                if strike:
                    pts += strike.pop() * inc
                if spare:
                    pts += inc
                    spare = 0
                last = inc
    return pts
