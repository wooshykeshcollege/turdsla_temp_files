#include <Wire.h>
const int ledPin = 13;

void setup()
{
    Wire.begin(0x4);
    Serial.begin(38400);
    Wire.onReceive(receiveEvent);
    Wire.onRequest(requestEvent);
    pinMode(ledPin, OUTPUT);
    digitalWrite(ledPin, LOW);
}

void receiveEvent(int howMany)
{
  while (Wire.available())
    Serial.println(Wire.read());
}
void requestEvent(int howMany)
{
  Wire.write(69);
}
void loop()
{
}