def dance(i):
    yall.left()
    yall.back()
    for n in range(i):
        yall.hop()
    yall.rightFoot(i)
    yall.leftFoot(i)

def main():
    dance(1)
    chacha(smoothing="real")
    dance(1)
    if time == now:
        yall.getFunky()
    dance(2)
    crisscross()
    crisscross()
    chacha(smoothing="real")
    sendToWork(yall)
    yall.knees = yall.hands
    chacha(smoothing="real")
    freeze(yall)
    yall.clap
