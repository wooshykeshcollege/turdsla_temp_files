#include <Wire.h>

int FW_IN1 = 2;
int FW_IN2 = 3;
int FW_IN3 = 4;
int FW_IN4 = 5;
int FW_ENA = A0;
int FW_ENB = A1;

int RW_IN1 = 6;
int RW_IN2 = 7;
int RW_IN3 = 8;
int RW_IN4 = 9;
int RW_ENA = A2;
int RW_ENB = A3;

int kill_Switch = 10;

int comm_led = 10;
int comm_count = 0;

int idrive[6] = {0};
string sdrive = "";
int check_flag = 0;

void setup()
{
    Serial.begin(38400);
    Wire.begin(0x8);
    Wire.onReceive(receive_Event);
    pinMode(FW_IN1, OUTPUT);
    pinMode(FW_IN2, OUTPUT);
    pinMode(FW_IN3, OUTPUT);
    pinMode(FW_IN4, OUTPUT);
    pinMode(RW_IN1, OUTPUT);
    pinMode(RW_IN2, OUTPUT);
    pinMode(RW_IN3, OUTPUT);
    pinMode(RW_IN4, OUTPUT);
    pinMode(FW_ENA, OUTPUT);
    pinMode(FW_ENB, OUTPUT);
    pinMode(RW_ENA, OUTPUT);
    pinMode(RW_ENB, OUTPUT);
    pinMode(kill_Switch, OUTPUT);
    digitalWrite(kill_Switch, HIGH);
}

void receive_Event()
{
    char c = Wire.read();
    switch (c)
    {
    case 2: // handshake
        Wire.write(1);
        break;
    case 3: // drive
        for (int i = 0; i < 6; i++)
        {
            drive[i] = wire.read();
            if(drive[i]==
        }

        break;
    case 4: // stop
        digitalWrite(FW_ENA, LOW);
        digitalWrite(FW_ENB, LOW);
        digitalWrite(RW_ENA, LOW);
        digitalWrite(RW_ENB, LOW);
        break;
    case 5: // kill
        digitalWrite(FW_ENA, LOW);
        digitalWrite(FW_ENB, LOW);
        digitalWrite(RW_ENA, LOW);
        digitalWrite(RW_ENB, LOW);
        digitalWrite(kill_Switch, LOW);
        break;

    case 5: // init
        digitalWrite(kill_Switch, HIGH);
        break;
    }
}
/// work with this first, run tests then use switch with one bit instruction input
void loop()
{
    ////
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
