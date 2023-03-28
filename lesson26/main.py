from musicbox import Muzicbox

mb = Muzicbox()
n= None

while n != '':
    mb.play()
    n = input('шо ты услышал? :').upper()
    mb.check(n)
    
