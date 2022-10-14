#include <Wire.h>

int ch1 = A0;     // 1 on rx
int ch3 = A1;     // 3 on rx
int kill_sw = A2; // 5 on rx
int kill = 0;
int ch1_data;
int ch3_data;
String answer, answers;
int trig = 9;
int echo = A6;
float ping;
int comm_led = 10;
int ul 17; // test and set
int ir_stat = 0;
int comm_count = 0;

void setup()
{
  Serial.begin(38400);
  pinMode(ch1, INPUT);
  pinMode(ch3, INPUT);
  pinMode(kill, INPUT);
  Wire.begin(0x4);
  Wire.onRequest(request_Event);
  Wire.onReceive(receive_Event);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(comm_led, OUTPUT);
}

float get_distance()
{
  digitalWrite(trig, LOW);
  delayMicroseconds(2000);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  ping = pulseIn(echo, HIGH);
}

void request_Event()
{
  for (int i = 0; i < ul; i++)
  {
    Wire.write((char)answers[i]);
  }
}

void receive_Event()
{
  int i = 0;
  char c;
  while (Wire.available())
  {
    c = Wire.read();
    instruction[i] = c;
    i++;
  }
  for (i = 0; i < 9; i++)
  {
    if (instruction[j] != handshake[j])
    {
      check_flag = 0;
      break;
    }
    check_flag = 1;
  }
  if (check_flag = 1)
  {
    for (i = 0; i < 5; i++)
    {
      Wire.write(shook[i]);
    }
  }
}

void loop()
{
  ch3_data = pulseIn(ch3, HIGH);
  ch1_data = pulseIn(ch1, HIGH);

  kill = digitalRead(kill_sw);

  digitalWrite(trig, LOW);
  delayMicroseconds(2000);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  ping = pulseIn(echo, HIGH);

  Serial.print(ch3_data);
  Serial.print("/");
  Serial.print(ch1_data);
  Serial.print("/");
  Serial.print(ping);
  Serial.print("//");
  answer = String(ch3_data) + "," + String(ch1_data) + "," + String(kill) + "," + String(ping) + "," + String(ir_stat);
  unsigned int len = answer.length();
  Serial.print(answer);
  Serial.print("  -  ");
  answers = String(len) + "/" + String(ch3_data) + "," + String(ch1_data) + "," + String(kill) + "," + String(ping) + "," + String(ir_stat);
  Serial.println(answers);
  if (comm_count % 30 == 0)
  {
    if (comm_status == 1)
    {
      digitalWrite(comm_led, LOW);
      comm_status = 0;
    }
    else if (comm_status == 0)
    {
      digitalWrite(comm_led, HIGH);
      comm_status = 1;
    }
  }
  comm_count++;
}
