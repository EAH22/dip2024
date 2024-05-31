 /*
 Controlling a servo with Push button with Arduino
 this is code #1 to control servo with push button by Robojax (Robojax.com )

code #1 when push button the servo goes from 0° to 180° (or set your angle) and returns back
    Watch video for code #1: https://youtu.be/fPrPRZlGdvA
code #2 when push button the servo goes from either from 0° to 180° or from 180° to 0° (or set your angle)
    Watch video for code #1: 
code #3 when push button pressed AND keep pressed the servo goes from 0° to 180° (or set your angle)
    Watch video for code #3: 
code #4 two Push button used one is used to move servo to LEFT direction and the other for RIGHT direciton 
    Watch video for code #4: 
    

 *  
 * Written by Ahmad Shamshiri for Robojax Video channel www.Robojax.com
 * Date: Dec 13, 2018 at 23:39  in Ajax, Ontario, Canada
 * Permission granted to share this code given that this note is kept with the code.
 * 
 * Disclaimer: this code is "AS IS" and for educational purpose only.
 * this code has been downloaded from http://robojax.com/learn/arduino/
 
 * Get this code and other Arduino codes from Robojax.com
Learn Arduino step by step in structured course with all material, wiring diagram and library
all in once place. Purchase My course on Udemy.com http://robojax.com/L/?id=62

****************************
Get early access to my videos via Patreon and have  your name mentioned at end of very 
videos I publish on YouTube here: http://robojax.com/L/?id=63 (watch until end of this video to list of my Patrons)
****************************

If you found this tutorial helpful, please support me so I can continue creating 
content like this using PayPal http://robojax.com/L/?id=64

 *  * This code is "AS IS" without warranty or liability. Free to be used as long as you keep this note intact 
 * This code has been download from Robojax.com
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    aaaaaaaa
 */


#include <Servo.h>

Servo myservo;  // create servo object to control a servo
#define servoPin 3 //~
#define pushButtonPin 2 

int angle =90;    // initial angle  for servo (beteen 1 and 179)
int angleStep =10;
const int minAngle = 40;
const int maxAngle = 180;

const int type =1;//watch video for details. Link is at the top of this code (robojax)

int buttonPushed =0;

void setup() {
  // Servo button demo by Robojax.com
  Serial.begin(9600);          //  setup serial
  myservo.attach(servoPin);  // attaches the servo on pin 3 to the servo object
  pinMode(pushButtonPin,INPUT_PULLUP);
   Serial.println("Robojax Servo Button ");
   myservo.write(angle);//initial position
}

void loop() {
  if(digitalRead(pushButtonPin) == LOW){
    buttonPushed = 1;
  }
   if( buttonPushed ){
  // change the angle for next time through the loop:
  angle = angle + angleStep;

    // reverse the direction of the moving at the ends of the angle:
    if (angle >= maxAngle) {
      angleStep = -angleStep;
        if(type ==1)
        {
            buttonPushed =0;                   
        }
    }
    
    if (angle <= minAngle) {
      angleStep = -angleStep;
       if(type ==2)
        {
            buttonPushed =0;       
        }
    }
    
    myservo.write(angle); // move the servo to desired angle
      Serial.print("Moved to: ");
      Serial.print(angle);   // print the angle
      Serial.println(" degree");    
  delay(50); // waits for the servo to get there
   }

  
}
