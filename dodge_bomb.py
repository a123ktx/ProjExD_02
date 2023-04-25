import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    tmr = 0
    # 練習1:半径10,色：赤の円で爆弾を作成する
    bb_img = pg.Surface((20, 20))  # ボムのサーフェイスを作成する
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  # ボムを描画する
    bb_img.set_colorkey((0, 0, 0)) #背景を透明にする

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()