#include "Wire.h"

int ch1 = A0;     // 1 on rx
int ch3 = A1;     // 3 on rx
int kill_sw = A2; // 4 on rx
int kill_data = 69;
int ch1_data;
int ch3_data;
String answer, answers;
int trig = 2;
int echo = A3;
int ping;
int comm_led = 3;
int ul = 26; // test and set
int ir_stat = 0;
int comm_count = 0;
int comm_status = 0;
void setup()
{
    Serial.begin(38400);
    pinMode(ch1, INPUT);
    pinMode(ch3, INPUT);
    pinMode(kill_sw, INPUT);
    Wire.begin(0x4);
    Wire.onRequest(request_Event);
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

void loop()
{
    ch3_data = pulseIn(ch3, HIGH);
    ch1_data = pulseIn(ch1, HIGH);
    kill_data = pulseIn(kill_sw, HIGH);

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
    Serial.print(kill_data);
    Serial.print("/");
    Serial.print(ping);
    Serial.print("/");
    Serial.print(ir_stat);
    Serial.print("//");
    answer = String(ch3_data) + "," + String(ch1_data) + "," + String(kill_data) + "," + String(ping) + "," + String(ir_stat);
    unsigned int len = answer.length();
    Serial.print(answer);
    Serial.print("  -  ");
    answers = String(len) + "/" + String(ch3_data) + "," + String(ch1_data) + "," + String(kill_data) + "," + String(ping) + "," + String(ir_stat);
    Serial.println(answers);
    if (comm_count % 30 == 0)
    {
        if (comm_status == 1)
        {
            digitalWrite(comm_led, comm_status);
            comm_status = !comm_status;
        }
        else if (comm_status == 0)
        {
            digitalWrite(comm_led, comm_status);
            comm_status = !comm_status;
        }
    }
    comm_count++;
}
