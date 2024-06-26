#include <SoftwareSerial.h>
#include <Time.h>

int gLedPin = 13;
int gRxPin = 10;
int gTxPin = 11;

SoftwareSerial BTSerial(gRxPin, gTxPin);

void setup() {
  
  BTSerial.begin(38400);
  Serial.begin(38400);
  delay(500);
}

void loop() {
  if (BTSerial.available()) {
    Serial.write(BTSerial.read());
  }
  if (Serial.available()) {
    BTSerial.write(Serial.read());
  }
}
