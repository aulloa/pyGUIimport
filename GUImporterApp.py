
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
import numpy
from numpy import loadtxt
from io import StringIO
from ast import literal_eval
from functools import partial

from kivy.lang import Builder


Builder.load_string('''
<GridLayout>
    canvas.before:
        BorderImage:
            # BorderImage behaves like the CSS BorderImage
            border: 10, 10, 10, 10
            source: 'grey-gradient-background.jpg'
            pos: self.pos
            size: self.size
            ''')

class GUImporterApp(App):
    def build(self):
        self.layout = GridLayout(cols=2,row_force_default=True, row_default_height=40)
        l  = Label(text='Start Row')
        l2 = Label(text='Columns (Comma Separated)')
        self.layout.add_widget(l)
        self.layout.add_widget(l2)
        self.txt1 = TextInput(text='0', multiline=False)
        self.txt2 = TextInput(text='0,1', multiline=False)
        self.layout.add_widget(self.txt1)
        self.layout.add_widget(self.txt2)
        btn1 = Button(text="RUN")
        btn1.bind(on_press=self.buttonClicked)
        self.layout.add_widget(btn1)
        btn1.background_color = 73.7/255,89.4/255,59.6/255,1
        btn1.background_normal = 'forg.JPG'
        #l3 = Label(text='Data File')
        #self.layout.add_widget(l3)
        #self.txt1.bind(text = self.importdatfile)
        #self.txt1.bind(text = l3.setter('text'))
#        self.txt1.bind(text=partial(self.importdatfile,self))
##      
        
        return self.layout

##    def importdatfile(self,*args):
##        Rows = self.txt1.text
##        Cols = self.txt2.text
##        l = literal_eval(Cols)
##        #print(l)
##        x = numpy.loadtxt('ET.csv',
##                      comments='#',
##                      delimiter=',',
##                      converters=None,
##                      skiprows=int(float(Rows)),
##                      usecols=l,
##                      unpack=False,
##                      ndmin=0)
##        x2 = " ".join("\t".join(map(str,l)) for l in x)
##        print(type(x2))
##        l3 = Label(text=x2)
##        self.layout.add_widget(l3)
##        print(x2)
        

    def buttonClicked(self,btn):
        Rows = self.txt1.text
        Cols = self.txt2.text
        b    = len(Cols)
        l = literal_eval(Cols)
        print(l)
        x = numpy.loadtxt('ET.csv',
                      comments='#',
                      delimiter=',',
                      converters=None,
                      skiprows=int(float(Rows)),
                      usecols=l,
                      unpack=False,
                      ndmin=2)
        print(x)
        numpy.savetxt('VT.csv',
                      x,
                      fmt='%d',
                      delimiter=',',
                      newline='\r\n',
                      header='',
                      footer='',
                      comments='# ')
        

if __name__ == "__main__":
    GUImporterApp().run()
