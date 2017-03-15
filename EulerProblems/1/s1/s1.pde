void setup() {
  size(1920,1200);
  noStroke();
  background(0);
}

int z=0;

void draw() {
  fill(0, 20);
  rect(0,0, width, height);
  z++;
  translate(width/2, height/2);

  for (int r=1; r < 18; r++) {
    for (int i=1; i < r* 15; i++) {
      pushMatrix();
      rotate(radians(z*3));
      rotate(radians( map(i, 0,r*15, 0, 360) ) );
      translate(r*30 + sin(radians(z))*100 ,0);
      fill(map(r,0,20, 100,255) ,i,r);
      if ( i % 3 == 0 && i % 5 == 0) {  ellipse(0,0, 20,20); }
      else if (i%5 == 0) { rect(0,0, 10,10); }
      else if (i%3 ==0 ) { rect(0,0, 3,5); }
      popMatrix();

    }
  }
}
