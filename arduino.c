#include <WiFi.h>
#include <HTTPClient.h>

// Replace these with your WiFi credentials
const char* ssid = "Rajee";
const char* password = "rajee0585";

// Your Flask server endpoint - change IP and port as needed
const char* serverName = "http://192.168.10.207:5000/update";

// Sensor pins
#define TRIG_PIN 18
#define ECHO_PIN 17
#define TDS_PIN 35
#define MQ_PIN 34

// Tank height in centimeters
const float tankHeight = 10.0;

long readUltrasonicDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duration = pulseIn(ECHO_PIN, HIGH, 30000);  // Timeout of 30 ms
  if (duration == 0) return -1; // No echo received
  long distance = duration * 0.034 / 2;  // Convert duration to cm
  return distance;
}

void setup() {
  Serial.begin(115200);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  analogReadResolution(12);  // 12-bit ADC resolution

  Serial.println("Connecting to WiFi...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    long distance = readUltrasonicDistance();
    float waterLevel = (distance >= 0 && distance <= tankHeight) ? tankHeight - distance : -1;

    int tdsValue = analogRead(TDS_PIN);
    int mqValue = analogRead(MQ_PIN);

    // Construct a JSON payload string
    String jsonPayload = "{";
    jsonPayload += "\"distance\":" + String(distance) + ",";
    jsonPayload += "\"waterLevel\":" + String(waterLevel) + ",";
    jsonPayload += "\"tds\":" + String(tdsValue) + ",";
    jsonPayload += "\"mq\":" + String(mqValue);
    jsonPayload += "}";

    HTTPClient http;
    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");
    int httpResponseCode = http.POST(jsonPayload);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println("Data sent: " + jsonPayload);
      Serial.println("Server response: " + response);
    } else {
      Serial.print("Error sending POST: ");
      Serial.println(httpResponseCode);
    }
    http.end();
  } else {
    Serial.println("WiFi Disconnected");
  }

  delay(2000);  // Send data every 2 seconds
}
