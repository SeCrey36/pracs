#include "Lpf2HubEmulation.h"
#include "PowerFunctions.h"
#include "LegoinoCommon.h"
#include <ESP32Servo.h>

// create a hub instance
Lpf2HubEmulation myEmulatedHub("CONTROL_PLUS_HUB", HubType::CONTROL_PLUS_HUB);
//Lpf2HubEmulation myEmulatedHub("TrainHub", HubType::CONTROL_PLUS_HUB);

// create a power functions instance (IR LED on Pin 12, IR Channel 0)
//PowerFunctions pf(12, 0);
static const int servoPin = 4;

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

int Hod;
void writeValueCallback(byte port, byte value)
{
  Serial.print("writeValueCallback: ");
  Serial.print("   PORT: ");
  Serial.print(port);
  Serial.print("   Hod: ");
  Serial.print(value);
  Serial.println("   ----------------------------");
  if (value < 101)
    {
      Hod = value * 0.9;
      Hod = Hod + 90; 
    }
  if (value > 150)
     {
      Hod = value - 256;
      Hod = Hod * 0.9;
      Hod = Hod + 90;
     }
  if (value == 127) 
    {  
      Hod = 90;
    }
  if (port == 0x00)
  {
    //pf.single_pwm(PowerFunctionsPort::RED, pf.speedToPwm(value)); 
     Serial.print("motor A  ");
     Serial.print("Value: ");
     Serial.print(value); 
     Serial.print("   Hod: ");
     Serial.println(Hod);
     servo1.write(Hod);
  }
  if (port == 0x01)
  {
   // pf.single_pwm(PowerFunctionsPort::BLUE, pf.speedToPwm(value));
     Serial.print("motor B  ");
     Serial.print("Value: ");
     Serial.print(value); 
     Serial.print("   Hod: ");
     Serial.println(Hod);
     servo2.write(Hod);
  }
  if (port == 0x02)
  {
   // pf.single_pwm(PowerFunctionsPort::RED, pf.speedToPwm(value)); 
     Serial.print("motor C  ");
     Serial.print("Value: ");
     Serial.print(value); 
     Serial.print("   Hod: ");
     Serial.println(Hod);
     servo3.write(Hod);   
  }
  if (port == 0x03)
  {
  //  pf.single_pwm(PowerFunctionsPort::RED, pf.speedToPwm(value)); 
     Serial.print("motor D  ");
     Serial.print("Value: ");
     Serial.print(value); 
     Serial.print("   Hod: ");
     Serial.println(Hod); 
     servo4.write(Hod);  
  }
  if (port == 0x32)
  {
    Serial.print("Hub LED command received with color: ");
    Serial.println(LegoinoCommon::ColorStringFromColor(value).c_str());
  }
}
void setup()
{
  Serial.begin(115200);
  // define the callback function if a write message event on the characteristic occurs
  myEmulatedHub.setWritePortCallback(&writeValueCallback); 
  myEmulatedHub.start();
  servo1.attach(13);
  servo2.attach(14);
  servo3.attach(4);
  servo4.attach(15);
}
// main loop
void loop()
{
  // if an app is connected, attach some devices on the ports to signalize 
  // the app that values could be received/written to that ports
  if (myEmulatedHub.isConnected && !myEmulatedHub.isPortInitialized)
  {
    delay(1000);
    myEmulatedHub.isPortInitialized = true;
    delay(1000);
    myEmulatedHub.attachDevice((byte)ControlPlusHubPort::A, DeviceType::TRAIN_MOTOR);
    delay(1000);
    myEmulatedHub.attachDevice((byte)ControlPlusHubPort::B, DeviceType::TRAIN_MOTOR);
    delay(1000);
    myEmulatedHub.attachDevice((byte)ControlPlusHubPort::C, DeviceType::TRAIN_MOTOR);
    delay(1000);
    myEmulatedHub.attachDevice((byte)ControlPlusHubPort::D, DeviceType::TRAIN_MOTOR);
    delay(1000);
    myEmulatedHub.attachDevice((byte)ControlPlusHubPort::LED, DeviceType::HUB_LED);
    delay(1000);
  }
} 
// End of loop
