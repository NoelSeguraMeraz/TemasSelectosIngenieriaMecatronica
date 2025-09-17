#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "TemasSelectos";
const char* password = "mecatronica2025";

WiFiServer server(1234);

void setup() {
  Serial.begin(115200);
    // Initialize the output variables as outputs
  pinMode(26, OUTPUT);
  pinMode(27, OUTPUT);
  // Set outputs to LOW
  digitalWrite(26, LOW);
  digitalWrite(27, LOW);


  // Conectar WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  server.begin();
  Serial.println("Servidor iniciado");
  Serial.println(WiFi.localIP());
}

void loop() {
  WiFiClient client = server.available();
  
  if (client) {
    while (client.connected()) {
      if (client.available()) {
        String command = client.readStringUntil('\n');
        processCommand(command);
      }
    }
    client.stop();
  }
}

void processCommand(String cmd) {
  if (cmd == "AZUL") Azul();
  else if (cmd == "VERDE") Verde();
  else if (cmd == "ROJO") Rojo();
}


void Azul() {
  neopixelWrite(RGB_BUILTIN,0,0,RGB_BRIGHTNESS);
}

void Verde() {
  neopixelWrite(RGB_BUILTIN,0,RGB_BRIGHTNESS,0);
}

void Rojo() {
  neopixelWrite(RGB_BUILTIN,RGB_BRIGHTNESS,0,0);
}

