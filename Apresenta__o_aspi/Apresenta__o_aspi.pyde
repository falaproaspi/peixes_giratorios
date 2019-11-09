from __future__ import division # para divisão "moderna" precisa ser a primeira coisa
 
def setup():
    size(500, 500)
    
def draw():
    strokeWeight(5)
    background(200, 200, 0)
    fill(50)
    #fill(0, 50, 100)
    estrela(350, 250, 200, 100, mouseX / 5)
    estrela2(200, 250, 100, 100, mouseX / 35)
    estrela3(250, 350, 200, 100, mouseX / 20)
    estrela4(150, 150, 200, 100, mouseX / 40)
    estrela5(85, 350, 200, 100, mouseX / 17)
    
def estrela(x, y, largura, largurinha, rot):    
    M, m = largura / 5, largurinha / 5
    pushMatrix()   # salva o sistema atual de coordenadas
    translate(x, y)
    rotate(rot)
    fill(0, 50, 200)
    beginShape()
    vertex(-M, -M)
    vertex(-m,  90)
    vertex(-M, +M)
    vertex( 90, +m)
    vertex(+M, +M)
    vertex( m, 90)
    vertex(+M, -M)
    vertex( 90, -m)
    endShape(CLOSE)
    popMatrix() # retorna ao sistema de coordenadas anterior

def estrela2(x, y, largura, largurinha, rot):    
    M, m = largura / 6, largurinha / 5
    pushMatrix()   # salva o sistema atual de coordenadas
    translate(x, y)
    rotate(rot)
    fill(50, 50, 100)
    beginShape()
    vertex(-M, -M)
    vertex(-m,  60)
    vertex(-M, +M)
    vertex( 60, +m)
    vertex(+M, +M)
    vertex( m, 60)
    vertex(+M, -M)
    vertex( 60, -m)
    endShape(CLOSE)
    popMatrix() # retorna ao sistema de coordenadas anterior

def estrela3(x, y, largura, largurinha, rot):    
    M, m = largura / 6, largurinha / 5
    pushMatrix()   # salva o sistema atual de coordenadas
    translate(x, y)
    rotate(rot)
    fill(100, 80, 150)
    beginShape()
    vertex(-M, -M)
    vertex(-m,  50)
    vertex(-M, +M)
    vertex( 50, +m)
    vertex(+M, +M)
    vertex( m, 50)
    vertex(+M, -M)
    vertex( 50, -m)
    endShape(CLOSE)
    popMatrix() # retorna ao sistema de coordenadas anterior
    
def estrela4(x, y, largura, largurinha, rot):    
    M, m = largura / 6, largurinha / 5
    pushMatrix()   # salva o sistema atual de coordenadas
    translate(x, y)
    rotate(rot)
    fill(100, 0, 250)
    beginShape()
    vertex(-M, -M)
    vertex(-m,  40)
    vertex(-M, +M)
    vertex( 70, +m)
    vertex(+M, +M)
    vertex( m, 70)
    vertex(+M, -M)
    vertex( 40, -m)
    endShape(CLOSE)
    popMatrix() # retorna ao sistema de coordenadas anterior

def estrela5(x, y, largura, largurinha, rot):    
    M, m = largura / 6, largurinha / 5
    pushMatrix()   # salva o sistema atual de coordenadas
    translate(x, y)
    rotate(rot)
    fill(200, 200, 250)
    beginShape()
    vertex(-M, -M)
    vertex(-m,  40)
    vertex(-M, +M)
    vertex( 70, +m)
    vertex(+M, +M)
    vertex( m, 70)
    vertex(+M, -M)
    vertex( 40, -m)
    endShape(CLOSE)
    popMatrix() # retorna ao sistema de coordenadas anterior
