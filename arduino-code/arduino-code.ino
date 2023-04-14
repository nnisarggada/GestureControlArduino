const int trigger = 3;  //Trigger pin of the Sensor
const int echo = 4;     //Echo pin of the Sensor

long time_taken;
int dist, distR;

long duration;
float r;
unsigned long temp = 0;
int temp1 = 0;
int l = 0;

void find_distance(void);

void find_distance(void) {

  digitalWrite(trigger, LOW);
  delayMicroseconds(2);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);
  duration = pulseIn(echo, HIGH, 5000);
  r = 3.4 * duration / 2;
  distR = r / 100.00;
  delay(100);
}

void setup() {
  Serial.begin(9600);
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
}

void calculate_distance(int trigger, int echo) {
  digitalWrite(trigger, LOW);
  delayMicroseconds(2);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);
  time_taken = pulseIn(echo, HIGH);
  dist = time_taken * 0.034 / 2;
  if (dist > 50)
    dist = 50;
}

void loop() {

  calculate_distance(trigger, echo);
  distR = dist;

  if (distR >= 10 && distR <= 20) {
    delay(50);  //Hand Hold Time
    calculate_distance(trigger, echo);
    distR = dist;
    if (distR >= 10 && distR <= 20) {
      Serial.println("Locked");
      while (distR <= 40) {
        calculate_distance(trigger, echo);
        distR = dist;
        if (distR < 15) {
          Serial.println("Volume Down");
          delay(300);
        }
        if (distR > 20) {
          Serial.println("Volume Up");
          delay(300);
        }
      }
    }
  }

  if (distR <= 8 && distR >= 0) {
    temp = millis();
    while (millis() <= (temp + 300))
      find_distance();

    {
      Serial.println("Play/Pause");
    }
  }

  delay(200);
}