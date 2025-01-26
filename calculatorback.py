lblx=0
lbly=0
nul=0
zeronul=0
def q(number=1):
    global nul
    global zeronul
    global lblx
    global lbly
    if nul == 0:
        nul = 1
        Label_division["text"] = str(number)
    else:
        Label_division["text"] += str(number)
        if zeronul == 0:
            lblx = int(Label_division["text"])
        else:
            lbly = int(Label_division["text"])

