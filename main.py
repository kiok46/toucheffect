from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Ellipse, Line
import time

class TouchEffect(BoxLayout):
    pass

class TouchCircle(FloatLayout):
    _default_size = [20,20]
        
    '''
    This one is for circle animation.
    '''
    
    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            try:
                ud = touch.ud
                ud['group'] = n = str(touch.uid)
                self.DoTheTrick(touch)
                
                with self.canvas:
                    Color(rgba = (.949,.470,.294,.4),group = n),
                    Line(width = 2., circle =(touch.x, touch.y, min(self.width, self.height)
                / 2 ),group = n)
                print "area1"
                
                return super(TouchCircle,self).on_touch_down(touch)
            except:
                import traceback
                traceback.print_exc()
                
    def on_touch_up(self, touch):
        '''
        I want this function to wait till DoTheTrick finction finishes.
        Find how to do it.
        '''
        if self.collide_point(touch.x, touch.y):
            try:
                touch.ungrab(self)
                ud = touch.ud
                self.canvas.remove_group(ud['group'])
                return super(TouchCircle,self).on_touch_up(touch)
            except:
                pass
    
    def DoTheTrick(self,touch):
        ud = touch.ud
        handle_size_x = 0
        handle_size_y = 0
        handle_touch_x = 0
        handle_touch_y = 0
        ud['group'] = g = str(touch.uid)
        '''
        Increase the diameter of the circle and remove the previously formed circle.
        add a calculation method for that.
        
        '''
        '''
        #for a special effect.
        with self.canvas:
            Color(rgba = (.949,.470,.294,.4),group = g),
            Ellipse(pos = [touch.x-10, touch.y-10], size = [self._default_size[0],self._default_size[1]], group = g)
        '''
        for i in range(60):
            '''
            It shall take time to animate.
            '''
            print "here"
            ud['group'] = g = str(touch.uid)
            with self.canvas:
                Color(rgba = (.949,.470,.294,.4),group = g),
                Ellipse(pos = [touch.x-10, touch.y-10], size = [self._default_size[0],self._default_size[1]], group = g)
            
            with self.canvas:
                    Color(rgba = (.949,.470,.294,.4),group = g),
                    Line(width = 2., circle =(touch.x, touch.y, min(handle_size_x,handle_size_y)
                / 2 ),group = g)
                    
            time.sleep(.001)
            self.canvas.remove_group(ud['group'])
            handle_size_x += 3
            handle_size_y += 3
            handle_touch_x += 1
            handle_touch_y += 1
            

class TouchRectangle(FloatLayout):
    
    '''
    This one is for rectangle animation.
    '''
    
    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            try:
                print "area2"
                return super(TouchRectangle,self).on_touch_down(touch)
            except:
                pass

class TouchTriangle(FloatLayout):
    
    '''
    This one is for triangle animation.
    '''
    
    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            try:
                print "area3"
                return super(TouchTriangle,self).on_touch_down(touch)
            except:
                pass

class MainApp(App):
    def build(self):
        return TouchEffect()

if __name__ == "__main__":
    app = MainApp()
    app.run()
