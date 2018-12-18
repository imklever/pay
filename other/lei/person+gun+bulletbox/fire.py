#coding:utf-8
from person import Person
from gun import Gun
from  bulletbox import BulletBox


#弹夹
bulletBox = BulletBox(5)

#枪
gun = Gun(bulletBox)

#人
per = Person(gun)

per.fire()
per.fire()
per.fire()
per.fire()
per.fire()

per.fillBullet(2)

per.fire()
per.fire()
per.fire()