function setup() {
  createCanvas(400, 400);
}
  
function segmento(A, B) {
  line(A.x, A.y, B.x, B.y);
}
  
function combina(A, B, t) {
  return { x: (1 - t) * A.x + t * B.x, y: (1 - t) * A.y + t * B.y };
}
  
function draw() {
  let p1, p2, p3, p4;
  background(200);
  p1 = { x: 10, y: height / 2 };
  p2 = { x: mouseX, y: mouseY};
  p3 = { x: width - 100, y: 2*height / 3 };
  p4 = { x: width - 10, y: height / 2};
  segmento(p1,p2);
  segmento(p2,p3);
  segmento(p3,p4);
  noFill();
  beginShape();
  for (let t = 0; t <= 1; t += 0.01) {
    R1 = combina(p1, p2, t);
    R2 = combina(p2, p3, t);
    R3 = combina(p3, p4, t);
    C1 = combina(R1, R2 ,t);
    C2 = combina(R2, R3, t);
    F = combina(C1, C2, t);
    vertex(F.x, F.y);
  }
  endShape();
}
