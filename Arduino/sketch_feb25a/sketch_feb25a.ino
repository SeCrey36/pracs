
int ledPin = 13; // используем встроенный светодиод на выводе 13

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600); 
}

void loop() {
  // считываем показания с аналогового вывода A0
  int sensorValue = analogRead(A1);
  Serial.println(sensorValue);
  if(sensorValue < 50){
    // Если потемнело, то включаем светодиод
    digitalWrite(ledPin, HIGH);
  }
  else {
    // Если светло, то выключаем светодиод
    digitalWrite(ledPin, LOW);
  }
}
