#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // initialize the serial communications:
  Serial.begin(9600);
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
}
