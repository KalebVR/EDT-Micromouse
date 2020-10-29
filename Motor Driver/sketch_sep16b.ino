int enablePin = 11;
int in1Pin = 10;
int in2Pin = 9;

void setup()
{
  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
}

void setMotor(int speed, boolean reverse)
{
  analogWrite(enablePin, speed);
  digitalWrite(in1Pin, ! reverse);
  digitalWrite(in2Pin, reverse);
}
 
void loop()
{
  int speed = 100;
  boolean reverse = HIGH;
  setMotor(speed, reverse);
  delay(5000);
  speed = 100;
  reverse = LOW;
  setMotor(speed, reverse);
  delay(5000);
}
 
