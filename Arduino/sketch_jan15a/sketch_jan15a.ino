#include <Servo.h>
int datafromUser=0;
Servo myservo1;

void setup() {
  Serial.begin(9600);
  myservo1.attach(9);
}

void loop() {
  if(Serial.available() > 0)
  {
    datafromUser=Serial.read();
  }

  if(datafromUser == '1')
  {
    Serial.println('w');
  }
  else if(datafromUser == '2')
  {
    Serial.println('a');
  }
  else if(datafromUser == '3')
  {
    Serial.println('s');
  }
  else if(datafromUser == '4')
  {
    Serial.println('d');
  }
  
}
