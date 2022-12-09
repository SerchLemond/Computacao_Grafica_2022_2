const raioG = 150;
const raioP = 50;
let n = 4;

function setup() {
    createCanvas(400, 400);
}

function draw() {
    background(200);
    translate(width / 2, height / 2);
    let [mx, my] = relativeMouse();
    let v = createVector(1, 0)
    let u = createVector((0.2)*mx, (0.2)*my);
    n = floor(map(u.mag(), 0, width / 2, 4, 20));
    beginShape();
    for (let i = 0; i < (2 * n); i++) {
        let angle = map(i, 0, 2 * n, 0, TWO_PI);
        if (i % 2 === 0) { // vertices externos
            vertex(raioG * cos(angle), raioG * sin(angle));
        } else { //vertices internos
            vertex(raioP * cos(angle), raioP * sin(angle));
        }
    }
    endShape(CLOSE);
}

function relativeMouse() {
    let mx = mouseX;
    let my = mouseY;
    let matrix = drawingContext.getTransform()
    let pd = pixelDensity()
    let rp = matrix.inverse().transformPoint(new DOMPoint(mx * pd, my * pd));
    return [rp.x, rp.y];
}
