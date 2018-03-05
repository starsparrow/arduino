#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 13, 5, 4, 3, 2);

int redPin = 9;
int greenPin = 10;
int bluePin = 11;
int delayDuration = 500; // ms
bool lightsEnabled = true;


void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // initialize the serial communications:
  Serial.begin(9600);

  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

}

void loop() {
  char msg;
  if (Serial.available()) {
    delay(50); 
    lcd.clear();
    lcd.setCursor(0,0);
     if (Serial.available() > 16) { 
      int i;
      while (i < 16) {
        msg = Serial.read();
        lcd.write(msg);
        i++;
      }
      lcd.setCursor(0,1);
      while (Serial.available() > 0) {
        msg = Serial.read();
        lcd.write(msg);
      }
    } else {
        while (Serial.available() > 0) {
          msg = Serial.read();
          lcd.write(msg);
        }
      }
  }
  if (lightsEnabled) {
   setColor(0x0,0x0,0xFF);
   }
}

void setColor(int red, int green, int blue)
{
  #ifdef COMMON_ANODE
    red = 255 - red;
    green = 255 - green;
    blue = 255 - blue;
  #endif
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
  delay(delayDuration);
}

