/*
  Analog input, analog output, serial output
 
 Reads an analog input pin, maps the result to a range from 0 to 255
 and uses the result to set the pulsewidth modulation (PWM) of an output pin.
 Also prints the results to the serial monitor.
 
 The circuit:
 * potentiometer connected to analog pin 0.
   Center pin of the potentiometer goes to the analog pin.
   side pins of the potentiometer go to +5V and ground
 * LED connected from digital pin 9 to ground
 
 created 29 Dec. 2008
 modified 9 Apr 2012
 by Tom Igoe
 
 This example code is in the public domain.
 
 */

// These constants won't change.  They're used to give names
// to the pins used:
const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
const int analogInPin1 = A1;  // Analog input pin that the potentiometer is attached to
const int analogInPin2 = A2;  // Analog input pin that the potentiometer is attached to
const int analogInPin3 = A3;  // Analog input pin that the potentiometer is attached to
const int analogOutPin = 9; // Analog output pin that the LED is attached to

int sensorValue = 0;        // value read from the pot
int outputValue = 0;        // value output to the PWM (analog out)
float conta=0;
void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600); 
}

void loop() {
  // read the analog in value:
   conta=0;
  for(int x = 0; x < 1000; x++) {
    sensorValue = analogRead(analogInPin);
    conta=conta+sensorValue;

    }
  //Serial.print(conta ); 
  sensorValue = conta/1000; 
  //sensorValue = analogRead(analogInPin);            
  // map it to the range of the analog out:
  //outputValue = map(sensorValue, 0, 1023, 0, 255);  
  // change the analog out value:
  //analogWrite(analogOutPin, outputValue);           

  // print the results to the serial monitor:
  Serial.print("Sensor0 = " );                       
  Serial.println(sensorValue);
   conta=0;
  for(int x = 0; x < 1000; x++) {
    sensorValue = analogRead(analogInPin1);
    conta=conta+sensorValue;

    }
  //Serial.print(conta ); 
  sensorValue = conta/1000;   
  //sensorValue = analogRead(analogInPin1);            
  // map it to the range of the analog out:
  //outputValue = map(sensorValue, 0, 1023, 0, 255);  
  // change the analog out value:
  //analogWrite(analogOutPin, outputValue);           

  // print the results to the serial monitor:
  Serial.print("Sensor1 = " );                       
  Serial.println(sensorValue); 
   conta=0;
  for(int x = 0; x < 1000; x++) {
    sensorValue = analogRead(analogInPin2);
    conta=conta+sensorValue;

    }
  //Serial.print(conta ); 
  sensorValue = conta/1000; 
  //sensorValue = analogRead(analogInPin2);            
  // map it to the range of the analog out:
  //outputValue = map(sensorValue, 0, 1023, 0, 255);  
  // change the analog out value:
  //analogWrite(analogOutPin, outputValue);           

  // print the results to the serial monitor:
  Serial.print("Sensor2 = " );                       
  Serial.println(sensorValue);
  conta=0;
  for(int x = 0; x < 1000; x++) {
    sensorValue = analogRead(analogInPin3);
    conta=conta+sensorValue;

    }
  //Serial.print(conta ); 
  sensorValue = conta/1000;         
  // map it to the range of the analog out:
  //outputValue = map(sensorValue, 0, 1023, 0, 255);  
  // change the analog out value:
  //analogWrite(analogOutPin, outputValue);           

  // print the results to the serial monitor:
  Serial.print("Sensor3 = " );                       
  Serial.println(sensorValue);
   //Serial.print("\t output = ");      
   //Serial.println(outputValue);   

  // wait 2 milliseconds before the next loop
  // for the analog-to-digital converter to settle
  // after the last reading:
  delay(1000);                     
}
