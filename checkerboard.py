from flask import Flask  , render_template, redirect

app = Flask(__name__)    

@app.route('/')          
def board1():
   board= create_board(8,8)

   return render_template('checkerboard.html',board=board)

@app.route('/<int:height>')
def board2(height):
    board= create_board(8,height)
    return render_template('checkerboard.html', board=board)

@app.route('/<int:width>/<int:height>')
def board3(height,width):
    board= create_board(height,width)
    return render_template('checkerboard.html', board=board)

@app.route('/<int:width>/<int:height>/<string:color1>/<int:color2>')
def color(x,y, color1,color2):

 return render_template('checkerboard.html', x=int(x), y=int(y),new_color1=color1,new_color2=color2)


def create_board(width, height ):
   board = []
   for y in range(0 , height):
       new_row = []
       for x in range( 0 , width ):
         if  (x + y) %2 == 0:
             new_row.append( 0 )
         else:
             new_row.append( 1 )
   
       board.append(new_row)
   return board


if __name__=="__main__":      
    app.run(debug = True) 