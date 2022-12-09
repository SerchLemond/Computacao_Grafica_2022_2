function setup() {
    createCanvas(400, 400);
  }
  
  function segmento(A, B) {
    line(A.x, A.y, B.x, B.y);
  }
  
  function ponto(A) {
    circle(A.x, A.y, 10);
  }
  
  function combina(A, B, t) {
    return { x: (1 - t) * A.x + t * B.x, y: (1 - t) * A.y + t * B.y };
  }
  
  function draw() {
    let p1, p2, p3, p4;
    background(200);
    p1 = { x: 10, y: height / 2 };
    p2 = { x: width - 10, y: height / 2 };
    p3 = { x: mouseX + 25, y: mouseY };
    p4 = { x: mouseX - 25, y: mouseY };
    segmento(p1,p4);
    segmento(p4,p3);
    segmento(p3,p2);
    noFill();
    beginShape();
    for (let t = 0; t <= 1; t += 0.01) {
      A = combina(p1, p3, t);
      B = combina(p3, p4, t);
      C = combina(p4, p2, t);
      D = combina(A, B, t);
      E = combina(D, C, t);
      vertex(E.x, E.y);
    }
    endShape();
  }
  