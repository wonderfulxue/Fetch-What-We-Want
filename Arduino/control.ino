//********************************************
//* Robotic Arm with BLE control v1
//* for robotic arm 0
//* By Benny Lo
//* Jan 14 2018
//********************************************
#include <CurieBLE.h>
#include <Servo.h>
#include <string.h>  
#define ROBOT_NAME "BRobot-0"
#define CRAW_MIN 0 //open 
#define CRAW_MAX 58 //close
#define ELBOW_MIN   0
#define ELBOW_MAX 140
#define SHOULDER_MIN 0
#define SHOULDER_MAX 165
#define WRIST_X_MIN 0
#define WRIST_X_MAX 180
#define WRIST_Y_MIN 0
#define WRIST_Y_MAX 90
#define WRIST_Z_MIN 0
#define WRIST_Z_MAX 180
#define BASE_MIN 0
#define BASE_MAX 180
#define ELBOW_DEFAULT 60
#define SHOULDER_DEFAULT 100
#define WRIST_X_DEFAULT 80
#define WRIST_Y_DEFAULT 90
#define WRIST_Z_DEFAULT 66
#define BASE_DEFAULT 90
#define CRAW_DEFAULT CRAW_MIN //fully opened
Servo myservoA;  
Servo myservoB;
Servo myservoC;
Servo myservoD;
Servo myservoE;
Servo myservoF;
Servo myservoG;//the craw
int i,pos,myspeed;
int sea,seb,sec,sed,see,sef,seg;


void myservosetup()  //set up the servo motors
{
   sea=myservoA.read();
   seb=myservoB.read();
   sec=myservoC.read();
   sed=myservoD.read();
   see=myservoE.read();
   sef=myservoF.read();
   seg=myservoG.read();
   
   myspeed=500;
   for(pos=0;pos<=myspeed;pos+=1)
   {
    myservoA.write(int(map(pos,1,myspeed,sea,ELBOW_DEFAULT)));
    myservoB.write(int(map(pos,1,myspeed,seb,SHOULDER_DEFAULT)));
    myservoC.write(int(map(pos,1,myspeed,sec,WRIST_X_DEFAULT)));
    myservoD.write(int(map(pos,1,myspeed,sed,WRIST_Y_DEFAULT)));
    myservoE.write(int(map(pos,1,myspeed,see,WRIST_Z_DEFAULT)));
    myservoF.write(int(map(pos,1,myspeed,sef,BASE_DEFAULT)));
    myservoG.write(int(map(pos,1,myspeed,seg,CRAW_DEFAULT)));    
    delay(1);
   }
}

void movement(int elbow_pos)
{
   sea=myservoA.read();


   for(pos=0;pos<=myspeed;pos+=1)
   {
    myservoA.write(int(map(pos,1,myspeed,sea,elbow_pos)));
    delay(1);
   }
}

void setup() 
{ 
  Serial.begin(9600);
  //pinMode(13, OUTPUT);   LED control
  
  myservoA.attach(2);  
  myservoB.attach(3); 
  myservoC.attach(4); 
  myservoD.attach(5); 
  myservoE.attach(6); 
  myservoF.attach(8);
  myservoG.attach(7); 
  
  myservosetup();

}

void loop() 
{ 
  	String readString = "";
  	while(!Serial.available()){}
 	while(Serial.available()){
 		if (Serial.available() >0){
      		char c = Serial.read();  //gets one byte from serial buffer
      		readString += c; //makes the string readString
    	}
 	}

 	if (readString.length() >0){
    	Serial.print("Arduino received: ");  
		Serial.println(readString); //see what was received
  	}

 	String devNo = readString.substring(0,1);
 	String devAngle = readString.substring(2,readString.length());

 	int devno = devNo.toInt();
 	int devangle = devAngle.toInt();

   sea=myservoA.read();
   seb=myservoB.read();
   sec=myservoC.read();
   sed=myservoD.read();
   see=myservoE.read();
   sef=myservoF.read();
   seg=myservoG.read();

 	switch(devno){
 		case 1:
 			for(pos=0;pos<=myspeed;pos+=1){
    			myservoA.write(int(map(pos,1,myspeed,sea,devangle)));   
    			delay(1);
   			}
   			break;
 		case 2:
 			for(pos=0;pos<=myspeed;pos+=1){
    			myservoB.write(int(map(pos,1,myspeed,seb,devangle)));   
    			delay(1);
   			}
   			break;
 		case 3:
 			for(pos=0;pos<=myspeed;pos+=1){
    			myservoC.write(int(map(pos,1,myspeed,sec,devangle)));   
    			delay(1);
   			}
   			break;
		case 4:
 			for(pos=0;pos<=myspeed;pos+=1){
    			myservoD.write(int(map(pos,1,myspeed,sed,devangle)));   
    			delay(1);
   			}
   			break;
 		case 5:
 			for(pos=0;pos<=myspeed;pos+=1){
    			myservoE.write(int(map(pos,1,myspeed,see,devangle)));   
    			delay(1);
   			}
   			break;
 		case 6:
 			for(pos=0;pos<=myspeed;pos+=1){
    			myservoF.write(int(map(pos,1,myspeed,sef,devangle)));   
    			delay(1);
   			}
   			break;
 		case 7:
 			for(pos=0;pos<=myspeed;pos+=1){
    			myservoG.write(int(map(pos,1,myspeed,seg,devangle)));   
    			delay(1);
   			}
   			break;
 	}

}

