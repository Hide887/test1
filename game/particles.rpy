init -1 python:

    class Fog(object):
        def __init__(self):
            self.sm = SpriteManager(update=self.update)
            self.stars = [ ]
            
            d = "images/particles/clouds/cloud1HD.png"
            for i in range(0, 35):
                self.add(d, (renpy.random.randint(30, 75)*renpy.random.choice([1,-1])), (renpy.random.randint(30, 75)*renpy.random.choice([1,-1])))
            
            d = "images/particles/clouds/cloud2HD.png"
            for i in range(0, 35):
                self.add(d, (renpy.random.randint(30, 75)*renpy.random.choice([1,-1])), (renpy.random.randint(30, 75)*renpy.random.choice([1,-1])))
            
            d = "images/particles/clouds/cloud3HD.png"
            for i in range(0, 35):
                self.add(d, (renpy.random.randint(30, 75)*renpy.random.choice([1,-1])), (renpy.random.randint(30, 75)*renpy.random.choice([1,-1])))
        
        def add(self, d, yspeed, xspeed):
            s = self.sm.create(d)
            ystart = renpy.random.randint(0, 4160)
            xstart = renpy.random.randint(0, 7840)
            self.stars.append((s, xstart, ystart, yspeed, xspeed))
        def update(self, st):
            for s, xstart, ystart, yspeed, xspeed in self.stars:
                s.y = (ystart + yspeed * -0.7 * st) % 4160 -1000
                s.x = (xstart + xspeed * 1.8 * st) % 7840 -2000
            return 0



    class Fireflies(object):
        def __init__(self):
            self.sm = SpriteManager(update=self.update)
            self.stars = [ ]
            
            d = Transform(im.Twocolor("images/particles/star.png", "#ff6", "#ff6"), zoom=0.3)
            for i in range(0, 55):
                self.add(d, renpy.random.randint(4, 20), renpy.random.randint(-20, 20))
            
            d = Transform(im.Twocolor("images/particles/star.png", "#ff6", "#ff6"), zoom=0.4)
            for i in range(0, 40):
                self.add(d, renpy.random.randint(6, 30), renpy.random.randint(-30, 30))
            
            d = Transform(im.Twocolor("images/particles/star.png", "#ff6", "#ff6"), zoom=0.6)
            for i in range(0, 30):
                self.add(d, renpy.random.randint(8, 40), renpy.random.randint(-40, 40))
            
            d = Transform(im.Twocolor("images/particles/star.png", "#ff6", "#ff6"), zoom=0.8)
            for i in range(0, 25):
                self.add(d, renpy.random.randint(12, 60), renpy.random.randint(-60, 60))
            
            d = im.Twocolor("images/particles/star.png", "#ff6", "#ff6")
            for i in range(0, 15):
                self.add(d, renpy.random.randint(16, 80), renpy.random.randint(-80, 80))
        
        def add(self, d, yspeed, xspeed):
            s = self.sm.create(d)
            ystart = renpy.random.randint(0, 1120)
            xstart = renpy.random.randint(0, 1960)
            self.stars.append((s, xstart, ystart, yspeed, xspeed))
        def update(self, st):
            for s, xstart, ystart, yspeed, xspeed in self.stars:
                s.y = (ystart + yspeed * -1.2 * st) % 1120 -20
                s.x = (xstart + xspeed / 3 * st) % 1960 -20
            return 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
