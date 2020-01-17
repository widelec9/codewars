def encode(n, s):
    spaces = [i for i, ch in enumerate(s) if ch == ' ']
    for j in range(n):
        s = s.replace(' ', '')
        s = list(s[-n:] + s[:-n])
        for sp in spaces:
            s.insert(sp, ' ')
        s = ''.join(s).split(' ')
        for i, sub in enumerate(s):
            if sub:
                shift = n % len(sub)
                s[i] = sub[-shift:] + sub[:-shift]
        s = ' '.join(s)
    return str(n) + ' ' + s


def decode(s):
    s = s.split(' ')
    n = int(s.pop(0))
    spaces = [i for i, ch in enumerate(' '.join(s)) if ch == ' ']
    for j in range(n):
        for i, sub in enumerate(s):
            if sub:
                shift = n % len(sub)
                s[i] = sub[shift:] + sub[:shift]
        s = ''.join(s)
        s = list(s[n:] + s[:n])
        for sp in spaces:
            s.insert(sp, ' ')
        s = ''.join(s).split(' ')
    return ' '.join(s)


'''Step-by-step breakdown:
Step 1 — remove all spaces:
'Ifyouwishtomakeanapplepiefromscratch,youmustfirstinventtheuniverse.'

Step 2 — shift the order of string characters to the right by 10:
'euniverse.Ifyouwishtomakeanapplepiefromscratch,youmustfirstinventth'

Step 3 — place the spaces back in their original positions:
'eu niv erse .I fyou wi shtom ake anap plepiefr oms crat ch,yo umustf irs tinventth'

Step 4 — shift the order of characters for each space-separated substring to the right by 10:
'eu vni seer .I oufy wi shtom eak apan frplepie som atcr ch,yo ustfum sir htinventt'

Repeat the steps 9 more times before returning the string with '10 ' prepended.
'''


print(encode(7, "G!GFuOELWns, :    <9 m}AY&vZ- a GU{S)"))

# IterativeRotationCipher = {'encode': encode, 'decode': decode}
# encode_examples = [
#     [10, 'If you wish to make an apple pie from scratch, you must first invent the universe.'],
#     [14, 'True evil is a mundane bureaucracy.'],
#     [22, 'There is nothing more atrociously cruel than an adored child.'],
#     [36, 'As I was going up the stair\nI met a man who wasn\'t there!\nHe wasn\'t there again today,\nOh how I wish he\'d go away!'],
#     [29,
#      'I avoid that bleak first hour of the working day during which my still sluggish senses and body make every chore a penance.\nI find that in arriving later, the work which I do perform is of a much higher quality.']
# ]
# decode_examples = [
#     '10 hu fmo a,ys vi utie mr snehn rni tvte .ysushou teI fwea pmapi apfrok rei tnocsclet',
#     '14 daue ilev is a munbune Traurecracy.',
#     '22 tareu oo iucnaTr dled oldthser.hg hiarm nhcn se rliyet oincoa',
#     '36 ws h weA dgIaa ug owh n!asrit git \n msm phw teaI\'e tanantwhe reos\ns ther! aHeae \'gwadin\nt haw n htoo ,I\'i sy aohOy',
#     '29 a r.lht niou gwryd aoshg gIsi mk lei adwhfci isd seensn rdohy mo kleie oltbyhes a\naneu p.n rndr tehh irnne yifav t eo,raclhtc frpw IIti im gwkaidhv aicufh ima doea eruhi y io qshhcoa kr ef l btah gtrrse otnvugrt'
# ]
# for i, v in enumerate(encode_examples):
#     print(IterativeRotationCipher['encode'](v[0], v[1]), decode_examples[i])
# for i, v in enumerate(decode_examples):
#     print(IterativeRotationCipher['decode'](v), encode_examples[i][1])
