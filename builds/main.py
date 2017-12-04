from PIL import Image
import math

sz=(1080,720)
wt=(255,255,255)
blk=(0,0,0)
def create_img():
    im = Image.new("RGB", size=sz, color=wt)
    # im.show()
    return im


if __name__=="__main__":
    im=create_img()
    (x1,y1)=map(int,input("please input x and y: ").split(' '))
    (a,b)=map(int,input("please input a and b: ").split(' '))
    print(a,b)
    x=0
    y=b
    d1=b*b+a*a*(0.25-b)
    im.putpixel((x1,y1),blk)
    while (b*b*(x+1))<(a*a*(y-0.5)):
        if d1<0:
            d1+=b*b*(2*x+3)
            x+=1
        else:
            d1+=(b*b*(2*x+3))+a*a*(-2*y+2)
            x+=1
            y-=1
        im.putpixel((x+x1,y+y1),blk)
        im.putpixel((x+x1, -y+y1), blk)
        im.putpixel((-x+x1, -y+y1), blk)
        im.putpixel((-x+x1, y+y1), blk)
    d2=math.sqrt(b*(x+0.5))+math.sqrt(a*(y-1))-math.sqrt(a*b)
    while y>0:
        if d2<0:
            d2+=b*b*(2*x+2)+a*a*(y*(-2)+3)
            x+=1
            y-=1
        else:
            d2+=a*a*(-2*y+3)
            y-=1
        im.putpixel((x + x1, y + y1), blk)
        im.putpixel((x + x1, -y + y1), blk)
        im.putpixel((-x + x1, -y + y1), blk)
        im.putpixel((-x + x1, y + y1), blk)
    im.show()