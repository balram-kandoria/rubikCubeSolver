/* Define Each Motor Direction and Step Pin */
const int stepPin1 =  1;
const int dirPin1 =   0;

const int stepPin2 =  3;
const int dirPin2 =   2;

const int stepPin3 =  5;
const int dirPin3 =   4;

const int stepPin4 =  7;
const int dirPin4 =   6;

const int stepPin5 =  9;
const int dirPin5 =   8;

const int stepPin6 =  11;
const int dirPin6 =   10;

int led = 13;
int runloop;
const int ONOFFPin = 23;
const int delayTime = 10;
bool Dir = HIGH;
int Byte = '0';
String Motor_info;

void setup() {
  Serial.begin(9600);

   /* Inputs */
  pinMode(ONOFFPin, INPUT);

  /* Outputs */
  pinMode(stepPin6,OUTPUT);
  pinMode(dirPin6,OUTPUT);
  pinMode(stepPin5,OUTPUT);
  pinMode(dirPin5,OUTPUT);
  pinMode(stepPin4,OUTPUT);
  pinMode(dirPin4,OUTPUT);
  pinMode(stepPin3,OUTPUT);
  pinMode(dirPin3,OUTPUT);
  pinMode(stepPin2,OUTPUT);
  pinMode(dirPin2,OUTPUT);
  pinMode(stepPin1,OUTPUT);
  pinMode(dirPin1,OUTPUT);
}

void loop() {
  runloop = digitalRead(ONOFFPin);
  
  if (runloop == HIGH) {
    
    // Turn off the Standby Light
    digitalWrite(led, LOW);

    // Activate if Serial Data is being transmitted
    if (Serial.available() > 0) {
  
      Motor_info = Serial.readString();
      
      Serial.println(Motor_info);
      
      if ((Motor_info == String(1)) or (Motor_info == String(2))) {
        
        //Serial.println("Motor 1");
        
        if (Motor_info == String(1)){
          Dir = LOW;
        }
        else {
          Dir = HIGH;
        }
        
        MoveMotor(dirPin1, stepPin1, Dir);
      }
      else if ((Motor_info == String(3)) or (Motor_info == String(4))) {
        //Serial.println("Motor 2");
        if (Motor_info == String(3)){
          Dir = LOW;
        }
        else {
          Dir = HIGH;
        }
        
        MoveMotor(dirPin2, stepPin2, Dir);
      }
      else if ((Motor_info == String(5)) or (Motor_info == String(6))) {
        //Serial.println("Motor 3");
        if (Motor_info == String(5)){
          Dir = LOW;
        }
        else {
          Dir = HIGH;
        }
        
        MoveMotor(dirPin3, stepPin3, Dir);
      }
      else if ((Motor_info == String(7)) or (Motor_info == String(8))) {
        //Serial.println("Motor 4");
        if (Motor_info == String(7)){
          Dir = LOW;
        }
        else {
          Dir = HIGH;
        }
        
        MoveMotor(dirPin4, stepPin4, Dir);
      }
      else if ((Motor_info == String(9)) or (Motor_info == String(10))) {
        //Serial.println("Motor 5");
        if (Motor_info == String(9)){
          Dir = LOW;
        }
        else {
          Dir = HIGH;
        }
        
        MoveMotor(dirPin5, stepPin5, Dir);
      }
      else if ((Motor_info == String(11)) or (Motor_info == String(12))) {
        //Serial.println("Motor 6");
        if (Motor_info == String(11)){
          Dir = LOW;
        }
        else {
          Dir = HIGH;
        }
        
        MoveMotor(dirPin6, stepPin6, Dir);
      }
  
      digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
      //delay(1000);                       // wait for a second
      digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
      //delay(1000);                       // wait for a second
      
    }
  } else {
    // Turn on Standby Light
    digitalWrite(led, HIGH);
  }
}

void MoveMotor(int DirPin, int StepPin, bool Direction) {
  
  
  digitalWrite(DirPin, Direction);

  for(int x=0; x < 100; x++){
    digitalWrite(StepPin, HIGH);
    delayMicroseconds(500);
    digitalWrite(StepPin, LOW);
    delayMicroseconds(500);
  }
}
