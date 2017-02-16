//#include <toneAC.h>


//#include "pitches.h"

const int trigPin = 6;
const int echoPin = 7;
const int trigPin2 = 2;
const int echoPin2 = 3;




int pitch,pitch2;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
long duration1,duration2,inches,cm,cm2;


pinMode(trigPin, OUTPUT);
digitalWrite(trigPin,LOW);
delayMicroseconds(2);

digitalWrite(trigPin, HIGH);
delayMicroseconds(10);

digitalWrite(trigPin, LOW);

pinMode(echoPin,INPUT);

duration1 = pulseIn(echoPin, HIGH);

pinMode(trigPin2, OUTPUT);
digitalWrite(trigPin2,LOW);
delayMicroseconds(2);

digitalWrite(trigPin2, HIGH);
delayMicroseconds(10);

digitalWrite(trigPin2, LOW);

pinMode(echoPin2,INPUT);

duration2 = pulseIn(echoPin2, HIGH);

//inches = microsecondsToInches(duration);
cm = microsecondsToCentimeters(duration1);
cm2 = microsecondsToCentimeters(duration2);

/*if( cm >= 5 && cm < 10)
Serial.print("a");
else if(cm >= 10 && cm < 20)
Serial.print("b");
else if(cm >=20 && cm<30)
Serial.print("c");
else if(cm >=30 && cm < 40)
Serial.print("d");
else if (cm>=40 && cm<50)
Serial.print("e");
else if(cm>=50 && cm<60)
Serial.print("f");
else if(cm>=60 && cm<70)
Serial.print("g");
else if(cm>=70 && cm<80)
Serial.print("h");
else if(cm>=80 && cm<90)
Serial.print("i");
else if(cm>=90 && cm <100)
Serial.print("j");*/

if(cm>=5 && cm<40)
Serial.print("a");
else if(cm>=40 && cm<60)
Serial.print("b");
else if(cm>=60 && cm<100)
Serial.print("c");
else
Serial.print("d");

delay(50);

if( cm2 >= 2 && cm2 < 7)
Serial.print("k");
else if(cm2 >= 7 && cm2 < 12)
Serial.print("l");
else if(cm2 >=12 && cm2<17)
Serial.print("m");
else if(cm2 >=17 && cm2 < 22)
Serial.print("n");
else if (cm2>=22 && cm2<27)
Serial.print("o");
else if(cm2>=27 && cm2<32)
Serial.print("p");
else if(cm2>=32 && cm2<37)
Serial.print("q");
else if(cm2>=37 && cm2<42)
Serial.print("r");
else if(cm2>=42 && cm2<47)
Serial.print("s");
else if(cm2>=47 && cm2 <55)
Serial.print("t");
else
Serial.print("z");
}

long microsecondsToCentimeters(long microseconds)
{
  return microseconds/ 29 / 2;
}


/*if(cm<100 && cm2<100)
{//Serial.print(inches);
//Serial.print("in, ");
Serial.print(cm);
Serial.print("cm");
Serial.println();
Serial.print(cm2);
Serial.print("cm1");
Serial.println();
pitch = map(cm, 4,99, 120,15000);
pitch2 = map(cm2, 4,99, 1,10);
toneAC(pitch,pitch2);

}*/
//else
//toneAC();

