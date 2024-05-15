#define M1 3
#define M2 6
#define DIRECTION1 9
#define DIRECTION2 12
 
void setup() {
   pinMode(M1, OUTPUT);
   pinMode(M2, OUTPUT);
   pinMode(DIRECTION1, OUTPUT);
   pinMode(DIRECTION2, OUTPUT);
}
 
void loop() {
  analogWrite(M1, 100);
  digitalWrite(DIRECTION1, LOW);
  analogWrite(M2, 100);
  digitalWrite(DIRECTION2, LOW);
  delay(1000);
   
  analogWrite(M1, 200);
  digitalWrite(DIRECTION1, LOW);
  analogWrite(M2, 200);
  digitalWrite(DIRECTION2, LOW);
  delay(2000);
   
  analogWrite(M1, 155);
  digitalWrite(DIRECTION1, HIGH);
  analogWrite(M2, 155);
  digitalWrite(DIRECTION2, HIGH);
  delay(2000);
   
  analogWrite(M1, 55);
  digitalWrite(DIRECTION1, HIGH);
  analogWrite(M2, 55);
  digitalWrite(DIRECTION2, HIGH);
  delay(1000);
}
