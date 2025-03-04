// Ultrasonic sensor pins
#define S1Trig 2
#define S2Trig 4
#define S3Trig 6
#define S1Echo 3
#define S2Echo 5
#define S3Echo 7
// Motor control pins
#define LEFT_MOTOR_PIN1 8
#define LEFT_MOTOR_PIN2 9
#define RIGHT_MOTOR_PIN1 10
#define RIGHT_MOTOR_PIN2 11
// Distance thresholds for obstacle detection
#define MAX_DISTANCE 40
#define MIN_DISTANCE_BACK 5
// Maximum and minimum motor speeds
#define MAX_SPEED 150
#define MIN_SPEED 75
void setup() {
  // Set motor control pins as outputs
  pinMode(LEFT_MOTOR_PIN1, OUTPUT);
  pinMode(LEFT_MOTOR_PIN2, OUTPUT);
  pinMode(RIGHT_MOTOR_PIN1, OUTPUT);
  pinMode(RIGHT_MOTOR_PIN2, OUTPUT);
  //Set the Trig pins as output pins
  pinMode(S1Trig, OUTPUT);
  pinMode(S2Trig, OUTPUT);
  pinMode(S3Trig, OUTPUT);
  //Set the Echo pins as input pins
  pinMode(S1Echo, INPUT);
  pinMode(S2Echo, INPUT);
  pinMode(S3Echo, INPUT);
  // Initialize the serial communication for debugging
  Serial.begin(9600);
}
void loop() {
  int frontDistance = sensorOne();
  int leftDistance = sensorTwo();
  int rightDistance = sensorThree();
  Serial.print("Front: ");
  Serial.print(frontDistance);
  Serial.print(" cm, Left: ");
  Serial.print(leftDistance);
  Serial.print(" cm, Right: ");
  Serial.print(rightDistance);
  Serial.println(" cm");
  // Find the sensor with the smallest distance
  if (frontDistance < MIN_DISTANCE_BACK) {
    moveBackward();
    Serial.println("backward");
  } else if (frontDistance < leftDistance && frontDistance < rightDistance && frontDistance < MAX_DISTANCE) {
    moveForward();
    Serial.println("forward");
  }else if (leftDistance < rightDistance && leftDistance < MAX_DISTANCE) {
    turnLeft();
    Serial.println("left");
  } else if (rightDistance < MAX_DISTANCE) {
    turnRight();
    Serial.println("right");   
   } else {
    stop();
    Serial.println("stop");
  }
  delay(100); // Delay for stability and to avoid excessive readings
}
// Function to measure the distance using an ultrasonic sensor
int sensorOne() {
  //pulse output
  digitalWrite(S1Trig, LOW);
  delayMicroseconds(2);
  digitalWrite(S1Trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(S1Trig, LOW);
  long t = pulseIn(S1Echo, HIGH);//Get the pulse
  int cm = t / 29 / 2; //Convert time to the distance
  return cm; // Return the values from the sensor
}
//Get the sensor values
int sensorTwo() {
  //pulse output
  digitalWrite(S2Trig, LOW);
  delayMicroseconds(2);
  digitalWrite(S2Trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(S2Trig, LOW);
  long t = pulseIn(S2Echo, HIGH);//Get the pulse
  int cm = t / 29 / 2; //Convert time to the distance
  return cm; // Return the values from the sensor
}
//Get the sensor values
int sensorThree() {
  //pulse output
  digitalWrite(S3Trig, LOW);
  delayMicroseconds(2);
  digitalWrite(S3Trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(S3Trig, LOW);
  long t = pulseIn(S3Echo, HIGH);//Get the pulse
  int cm = t / 29 / 2; //Convert time to the distance
  return cm; // Return the values from the sensor
}
// Motor control functions
void moveForward() {
  analogWrite(LEFT_MOTOR_PIN1, MAX_SPEED);
  analogWrite(LEFT_MOTOR_PIN2, LOW);
  analogWrite(RIGHT_MOTOR_PIN1, MAX_SPEED);
  analogWrite(RIGHT_MOTOR_PIN2, LOW);
}
void moveBackward() {
  analogWrite(LEFT_MOTOR_PIN1, LOW);
  analogWrite(LEFT_MOTOR_PIN2, MAX_SPEED);
  analogWrite(RIGHT_MOTOR_PIN1, LOW);
  analogWrite(RIGHT_MOTOR_PIN2, MAX_SPEED);
}
void turnRight() {
  analogWrite(LEFT_MOTOR_PIN1, LOW);
  analogWrite(LEFT_MOTOR_PIN2, MAX_SPEED);
  analogWrite(RIGHT_MOTOR_PIN1, MAX_SPEED);
  analogWrite(RIGHT_MOTOR_PIN2, LOW);
}
void turnLeft() {
  analogWrite(LEFT_MOTOR_PIN1, MAX_SPEED);
  analogWrite(LEFT_MOTOR_PIN2, LOW);
  analogWrite(RIGHT_MOTOR_PIN1, LOW);
  analogWrite(RIGHT_MOTOR_PIN2, MAX_SPEED);
}
void stop() {
  analogWrite(LEFT_MOTOR_PIN1, LOW);
  analogWrite(LEFT_MOTOR_PIN2, LOW);
  analogWrite(RIGHT_MOTOR_PIN1, LOW);
  analogWrite(RIGHT_MOTOR_PIN2, LOW);
