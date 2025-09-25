int buttonPins[3] = {4, 5, 18};
int analogPins[2] = {34, 35};

void setup() {
  Serial.begin(115200);
  for (int i = 0; i < 3; i++) {
    pinMode(buttonPins[i], INPUT_PULLUP);  // Botones con pull-up
  }
}

void loop() {
  // Si recibe petición de Python
  if (Serial.available()) {
    char c = Serial.read();
    if (c == 'R') { // Python manda "R" de request
      int b1 = digitalRead(buttonPins[0]);
      int b2 = digitalRead(buttonPins[1]);
      int b3 = digitalRead(buttonPins[2]);
      int a1 = analogRead(analogPins[0]);
      int a2 = analogRead(analogPins[1]);

      // Enviamos en formato CSV
      Serial.printf("%d,%d,%d,%d,%d\n", b1, b2, b3, a1, a2);
    }
  }
}
