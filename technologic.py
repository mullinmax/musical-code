import DaftPunk as D

def process(it):
    it.purchase() #Buy it
    it.use() # use it
    try:
        raise Exception(it)# break it
    except:
        it.fix() # fix it

    del(it)#Trash it
    it = D.it()# change it
    it.send('stakeholder@company.com') # mail
    it += 1# upgrade it

    it.convict() #Charge it
    it.oreint((0, 1))# point it
    it.scale((1.5, 1.5))# zoom it
    it.scale((.5, .5))# press it

    it.ljust(10)# Snap it
    it.work()# work it
    del(it.work())# quick erase it

    w = ''
    with open('it.txt', 'w') as f:
        w = str(it)                # write it
        w = w.strip()              # cut it
        w = '-{it}-'.format(it = w)# paste it
        f.write(w)                 # save it

    r = ''
    with open('it.txt') as f:
        r = ''.join(f.readlines())# Load it
        assert(r == s)# check it
    with open('it.txt', 'w') as f:
        f.write(r) # quick rewrite it
    
    # Plug it
    # play it
    # burn it
    # rip it

    it = it.drag(10, 15).drop() # Drag and drop it
    it = list(zip(it))          # zip
    it = zip(*it)               # unzip it

    # Lock it
    # fill it
    # curl it
    # find it

    # View it
    # code it
    # jam
    # unlock it
    # Surf it
    # scroll it
    # pose it
    # click it
    # Cross it
    # crack it
    # twitch
    # update it

    # Name it
    # read it
    # tune it
    # print it

    # Scan it
    # send it
    # fax
    # rename it

    # Touch it
    # bring it
    # pay it
    # watch it

    it.rotate(90)   # Turn it
    it = it         # leave it
    exit()          # stop
                    # format it.

def main():
    it = D.it()
    process(it)

if __name__ == '__main__':
    main()
