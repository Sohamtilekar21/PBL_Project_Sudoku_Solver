from flask import Flask
from flask import render_template
from flask import request
#import add
#import sudoku_solver

app = Flask(__name__)

@app.route("/", methods = ['POST','GET'] )
def index():

    return render_template("index.html")

@app.route("/sudoku", methods = ['POST','GET'] )



def hello():
    """if request.method == "POST":
        name =  request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)
    else:"""
    #greet = request.form['greet']
    """def add(a,b):
        c=int(a)+int(b)
        return c"""
    def solve(bo):
        find=[]
        find = find_empty(bo)
        if not find:
            return True


        else:
            row, col = find

        for i in range(1,10):
            if valid(bo, i, (row, col)):
                bo[row][col] = i

                if solve(bo):
                    return True

                bo[row][col] = 0

        return False

    def valid(bo, num, pos):
        for i in range(len(bo[0])):
            if bo[pos[0]][i] == num and pos[1] != i:
                return False
        for i in range(len(bo)):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if bo[i][j] == num and (i,j) != pos:
                    return False
        return True

    def find_empty(bo):
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    return (i, j)

        return None




    #Row 1
    hv11=int('0'+request.form['hv11'])
    hv12=int('0'+request.form['hv12'])
    hv13=int('0'+request.form['hv13'])
    hv14=int('0'+request.form['hv14'])
    hv15=int('0'+request.form['hv15'])
    hv16=int('0'+request.form['hv16'])
    hv17=int('0'+request.form['hv17'])
    hv18=int('0'+request.form['hv18'])
    hv19=int('0'+request.form['hv19'])

    #Row 2
    hv21=int('0'+request.form['hv21'])
    hv22=int('0'+request.form['hv22'])
    hv23=int('0'+request.form['hv23'])
    hv24=int('0'+request.form['hv24'])
    hv25=int('0'+request.form['hv25'])
    hv26=int('0'+request.form['hv26'])
    hv27=int('0'+request.form['hv27'])
    hv28=int('0'+request.form['hv28'])
    hv29=int('0'+request.form['hv29'])

    #Row 3
    hv31=int('0'+request.form['hv31'])
    hv32=int('0'+request.form['hv32'])
    hv33=int('0'+request.form['hv33'])
    hv34=int('0'+request.form['hv34'])
    hv35=int('0'+request.form['hv35'])
    hv36=int('0'+request.form['hv36'])
    hv37=int('0'+request.form['hv37'])
    hv38=int('0'+request.form['hv38'])
    hv39=int('0'+request.form['hv39'])

    #Row 4
    hv41=int('0'+request.form['hv41'])
    hv42=int('0'+request.form['hv42'])
    hv43=int('0'+request.form['hv43'])
    hv44=int('0'+request.form['hv44'])
    hv45=int('0'+request.form['hv45'])
    hv46=int('0'+request.form['hv46'])
    hv47=int('0'+request.form['hv47'])
    hv48=int('0'+request.form['hv48'])
    hv49=int('0'+request.form['hv49'])

    #Row 5
    hv51=int('0'+request.form['hv51'])
    hv52=int('0'+request.form['hv52'])
    hv53=int('0'+request.form['hv53'])
    hv54=int('0'+request.form['hv54'])
    hv55=int('0'+request.form['hv55'])
    hv56=int('0'+request.form['hv56'])
    hv57=int('0'+request.form['hv57'])
    hv58=int('0'+request.form['hv58'])
    hv59=int('0'+request.form['hv59'])

    #Row 6
    hv61=int('0'+request.form['hv61'])
    hv62=int('0'+request.form['hv62'])
    hv63=int('0'+request.form['hv63'])
    hv64=int('0'+request.form['hv64'])
    hv65=int('0'+request.form['hv65'])
    hv66=int('0'+request.form['hv66'])
    hv67=int('0'+request.form['hv67'])
    hv68=int('0'+request.form['hv68'])
    hv69=int('0'+request.form['hv69'])

    #Row 7
    hv71=int('0'+request.form['hv71'])
    hv72=int('0'+request.form['hv72'])
    hv73=int('0'+request.form['hv73'])
    hv74=int('0'+request.form['hv74'])
    hv75=int('0'+request.form['hv75'])
    hv76=int('0'+request.form['hv76'])
    hv77=int('0'+request.form['hv77'])
    hv78=int('0'+request.form['hv78'])
    hv79=int('0'+request.form['hv79'])

    #Row 8
    hv81=int('0'+request.form['hv81'])
    hv82=int('0'+request.form['hv82'])
    hv83=int('0'+request.form['hv83'])
    hv84=int('0'+request.form['hv84'])
    hv85=int('0'+request.form['hv85'])
    hv86=int('0'+request.form['hv86'])
    hv87=int('0'+request.form['hv87'])
    hv88=int('0'+request.form['hv88'])
    hv89=int('0'+request.form['hv89'])

    #Row 9
    hv91=int('0'+request.form['hv91'])
    hv92=int('0'+request.form['hv92'])
    hv93=int('0'+request.form['hv93'])
    hv94=int('0'+request.form['hv94'])
    hv95=int('0'+request.form['hv95'])
    hv96=int('0'+request.form['hv96'])
    hv97=int('0'+request.form['hv97'])
    hv98=int('0'+request.form['hv98'])
    hv99=int('0'+request.form['hv99'])







    #hv12=request.form['hv12']
    #greet=add.add(hv11,hv12)

    b1=[
    [hv11, hv12, hv13, hv14, hv15, hv16, hv17, hv18, hv19],
    [hv21, hv22, hv23, hv24, hv25, hv26, hv27, hv28, hv29],
    [hv31, hv32, hv33, hv34, hv35, hv36, hv37, hv38, hv39],
    [hv41, hv42, hv43, hv44, hv45, hv46, hv47, hv48, hv49],
    [hv51, hv52, hv53, hv54, hv55, hv56, hv57, hv58, hv59],
    [hv61, hv62, hv63, hv64, hv65, hv66, hv67, hv68, hv69],
    [hv71, hv72, hv73, hv74, hv75, hv76, hv77, hv78, hv79],
    [hv81, hv82, hv83, hv84, hv85, hv86, hv87, hv88, hv89],
    [hv91, hv92, hv93, hv94, hv95, hv96, hv97, hv98, hv99]
    ]
    #greet=int(hv11)+int(hv12)
    #return "<h1>{}</h1>".format(greet)
    #solved=[[],[]]
    solve(b1)
    #hv11=b1[0][0]





    return render_template("sudoku_output.html",hv11=b1[0][0],hv12=b1[0][1],hv13=b1[0][2],hv14=b1[0][3],hv15=b1[0][4],hv16=b1[0][5],hv17=b1[0][6],hv18=b1[0][7],hv19=b1[0][8],
    hv21=b1[1][0],hv22=b1[1][1],hv23=b1[1][2],hv24=b1[1][3],hv25=b1[1][4],hv26=b1[1][5],hv27=b1[1][6],hv28=b1[1][7],hv29=b1[1][8],
    hv31=b1[2][0],hv32=b1[2][1],hv33=b1[2][2],hv34=b1[2][3],hv35=b1[2][4],hv36=b1[2][5],hv37=b1[2][6],hv38=b1[2][7],hv39=b1[2][8],
    hv41=b1[3][0],hv42=b1[3][1],hv43=b1[3][2],hv44=b1[3][3],hv45=b1[3][4],hv46=b1[3][5],hv47=b1[3][6],hv48=b1[3][7],hv49=b1[3][8],
    hv51=b1[4][0],hv52=b1[4][1],hv53=b1[4][2],hv54=b1[4][3],hv55=b1[4][4],hv56=b1[4][5],hv57=b1[4][6],hv58=b1[4][7],hv59=b1[4][8],
    hv61=b1[5][0],hv62=b1[5][1],hv63=b1[5][2],hv64=b1[5][3],hv65=b1[5][4],hv66=b1[5][5],hv67=b1[5][6],hv68=b1[5][7],hv69=b1[5][8],
    hv71=b1[6][0],hv72=b1[6][1],hv73=b1[6][2],hv74=b1[6][3],hv75=b1[6][4],hv76=b1[6][5],hv77=b1[6][6],hv78=b1[6][7],hv79=b1[6][8],
    hv81=b1[7][0],hv82=b1[7][1],hv83=b1[7][2],hv84=b1[7][3],hv85=b1[7][4],hv86=b1[7][5],hv87=b1[7][6],hv88=b1[7][7],hv89=b1[7][8],
    hv91=b1[8][0],hv92=b1[8][1],hv93=b1[8][2],hv94=b1[8][3],hv95=b1[8][4],hv96=b1[8][5],hv97=b1[8][6],hv98=b1[8][7],hv99=b1[8][8]
    )
    #return render_template("sudoku_output.html",hv11=hv11,hv12=hv12)
    #return "{}".format(b1)






if __name__=="__main__":
    app.run()
