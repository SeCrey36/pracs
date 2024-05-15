#include <Servo.h> 
 
#define PIN_SERVO_LR 7
#define PIN_SERVO_UD 6
#define PIN_SERVO_UD2 5
#define PIN_SERVO_CATCH 4
#define PIN_VRX A0
#define PIN_VRY A1
#define PIN_VRX2 A2
#define PIN_VRY2 A3

Servo servoLR;  
Servo servoUD;  
Servo servoUD2; 
Servo servoCATCH; 

int joyX, joyY, joyX2, joyY2;
int angleX, angleY, angleX2, angleY2;

void setup() { 
   Serial.begin (9600);             
   servoLR.attach(PIN_SERVO_LR);  
   servoUD.attach(PIN_SERVO_UD);
   servoUD2.attach(PIN_SERVO_UD2);
   servoCATCH.attach(PIN_SERVO_CATCH); 

   angleX = 50;
   angleY = 50;
   angleX2 = 50;
   angleY2 = 100;
   servoLR.write(angleX);
   servoUD.write(angleY);
   servoUD2.write(angleX2);
   servoCATCH.write(angleY2);
} 

void loop () {
   joyX=analogRead(PIN_VRX);
   joyY=analogRead(PIN_VRY);
   joyX2=analogRead(PIN_VRX2);
   joyY2=analogRead(PIN_VRY2);
   Serial.print(" x = ");            
   Serial.print(joyX); 
   Serial.print(" y = ");
   Serial.println(joyY);  

   if(joyX<400) {
       angleX = angleX-1;
       if (angleX < 20){ angleX = 20;}
       servoLR.write(angleX);}
   if(joyX>620) {
       angleX = angleX+1;
       if (angleX > 115){ angleX = 115;}
       servoLR.write(angleX);}
       
   if(joyY>620) {
       angleY = angleY+2;
       if (angleY > 130){ angleY = 130;}
       servoUD.write(angleY);}
   if(joyY<400) {
       if (angleY < 20){ angleY = 20;}
       angleY = angleY-2;
       servoUD.write(angleY);}

   if(joyX2<400) {
       angleX2 = angleX2+2;
       if (angleX2 > 175){ angleX2 = 175;}
       servoUD2.write(angleX2);}
   if(joyX2>620) {
       angleX2 = angleX2-2;
       if (angleX2 < 35){ angleX2 = 35;}
       servoUD2.write(angleX2);}
       
   if(joyY2>620) {
       angleY2 = angleY2+2;
       if (angleY2 > 120){ angleY2 = 120;}
       servoCATCH.write(angleY2);}
   if(joyY2<400) {
       angleY2 = angleY2-2;
       if (angleY2 < 60){ angleY2 = 60;}
       servoCATCH.write(angleY2);}
   delay(30); 

}
