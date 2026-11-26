int sensorPinTemp = A4;
float temperaturaC;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int valorSensorTemp = analogRead(sensorPinTemp);

  temperaturaC = (valorSensorTemp / 1024.0) * 500 - 50;

  Serial.print("Temperatura: ");
  Serial.print(temperaturaC);
  Serial.print(char(176));
  Serial.print("C");
  Serial.print("\n");

  delay(1000);
}
