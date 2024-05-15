#include <Servo.h>
Servo servo1;
int ledPin = 13;
byte incomingByte;

void setup() {
  servo1.attach(9);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char data = Serial.read();

    if(data == '1'){
      digitalWrite(ledPin, HIGH);
      servo1.write(90);

    }
    else if (data == '0'){
      digitalWrite(ledPin, LOW); 
      servo1.write(180);

    }
    
      Serial.print("I received: ");
      Serial.println(data);
  }
  delay(10);
}
