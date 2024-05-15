#define M11 2
#define M12 4
#define M21 8
#define M22 7
int speed_motor_1 = 5;
int speed_motor_2 = 6;

#include "Ultrasonic.h"
Ultrasonic dalnomer(10,11);
float dist;
int predel = 20;


void setup() {
Serial.begin(9600);
pinMode(M11, OUTPUT);
pinMode(M12, OUTPUT);
pinMode(M21, OUTPUT);
pinMode(M22, OUTPUT);
}

void loop() {
dist = dalnomer.Ranging(CM);

Serial.println(dist);
delay(80);
goPered();

if (dist < 15) {
  goLevo();
  delay(200);
}
}









int goPered(){
    digitalWrite(M12,LOW);
    digitalWrite(M21,LOW);
    digitalWrite(M11,HIGH);
    digitalWrite(M22,HIGH);
    analogWrite(speed_motor_1, 80);
    analogWrite(speed_motor_2, 80);
    }
int goNazad(){
    digitalWrite(M11,LOW);
    digitalWrite(M22,LOW); 
    digitalWrite(M12,HIGH);
    digitalWrite(M21,HIGH);
    analogWrite(speed_motor_1, 80);
    analogWrite(speed_motor_2, 80);
    }
int goLevo(){
    digitalWrite(M11,LOW);
    digitalWrite(M21,LOW); 
    digitalWrite(M12,HIGH);
    digitalWrite(M22,HIGH);
    analogWrite(speed_motor_1, 80);
    analogWrite(speed_motor_2, 80);
    }
int goPravo(){
    digitalWrite(M12,LOW);
    digitalWrite(M22,LOW); 
    digitalWrite(M11,HIGH);
    digitalWrite(M21,HIGH);
    analogWrite(speed_motor_1, 80);
    analogWrite(speed_motor_2, 80);
    }








 
