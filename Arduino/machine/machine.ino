#define M12 5
#define M11 6
#define M22 9
#define M21 10

int datafromUser=0;
int mspeed = 150;

float time;

void setup(){
  Serial.begin(9600);
  pinMode(M11, OUTPUT);
  pinMode(M12, OUTPUT);
  pinMode(M21, OUTPUT);
  pinMode(M22, OUTPUT);
}
 
void loop() {
  if(Serial.available() > 0){
    datafromUser=Serial.read();}
  
  if(datafromUser == '1'){
    goPered();
    delay(1000);}
  else if(datafromUser == '2'){
    goLevo();}
  else if(datafromUser == '3'){
    goNazad();
    delay(100);
    goStop();}
  else if(datafromUser == '4'){
    goPravo();
    delay(100);
    goStop();}
}

int goPered(){
    analogWrite(M12,LOW);
    analogWrite(M21,LOW);
    analogWrite(M11, mspeed);
    analogWrite(M22, mspeed);}
    
int goNazad(){
    analogWrite(M11,LOW);
    analogWrite(M22,LOW);
    analogWrite(M12, mspeed);
    analogWrite(M21, mspeed);}
    
int goLevo(){
    analogWrite(M12,LOW);
    analogWrite(M22,LOW);
    analogWrite(M11, mspeed);
    analogWrite(M21, mspeed);}
    
int goPravo(){
    analogWrite(M11,LOW);
    analogWrite(M21,LOW);
    analogWrite(M12, mspeed);
    analogWrite(M22, mspeed);}
    
int goStop(){
    analogWrite(M12,LOW);
    analogWrite(M21,LOW);
    analogWrite(M11, LOW);
    analogWrite(M22, LOW);}
    
