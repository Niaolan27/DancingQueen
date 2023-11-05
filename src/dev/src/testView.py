from view import View
import cv2


if __name__ == '__main__':

    view = View()

    while True:
        print(view.showGame)
        if not view.showGame:
            view.loadStartScreen()
        else:
            view.initGame()
            while True:
                #rectList = controller.getRectList()
                rectList = [[250,350,250,350],[100,200,100,200]]
                view.loadGame(rectList)

                k = cv2.waitKey(10)
                # Press q to break  

                #ends when time == duration
                if k == ord('q'):
                    view.destroyGame()
                    view.showGame = False
                    view.loadEndScreen(5)
                    break