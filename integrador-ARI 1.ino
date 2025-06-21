#include <WiFi.h>
#include <WiFiClientSecure.h>

// Credenciais da rede Wi-Fi
const char* ssid     = "WIFI_EDUC_CFP501";
const char* password = "SENAICAMPINAS501";

// ID do script Google Apps
const char *GScriptId = "AKfycbzVVKaJerYkW5v5DDj01ra9yXYIY61LAWLcUzV1_OcjRDoAeQ5jNVSminq26UUW9Q-q";

// Comando e nome da planilha
String payload_base = "{\"command\": \"insert_row\", \"sheet_name\": \"Sheet1\", \"values\": ";
String payload = "";

// Host e porta HTTPS
const char* host = "script.google.com";
const int httpsPort = 443;
String url = String("/macros/s/") + GScriptId + "/exec";

// Variáveis a serem publicadas
int esteira1 = 0;
int esteira2 = 0;
int esteira3 = 0;

// Cliente seguro
WiFiClientSecure client;

void setup() {
  Serial.begin(9600);
  delay(1000);

  // Conectar ao Wi-Fi
  WiFi.begin(ssid, password);
  Serial.print("Conectando-se à rede: ");
  Serial.println(ssid);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }

  Serial.println("\nConectado!");
  Serial.print("Endereço IP: ");
  Serial.println(WiFi.localIP());

  client.setInsecure();  // Ignora verificação do certificado (não recomendado para produção)
}

void loop() {
  esteira1 = random(0, 4);
  esteira2 = random(0, 4);
  esteira3 = random(0, 4);

  payload = payload_base + "\"" + esteira1 + "," + esteira2 + "," + esteira3 + "\"}";

  Serial.println("Publicando dados...");
  Serial.println(payload);

  if (!client.connect(host, httpsPort)) {
    Serial.println("Falha na conexão");
    delay(5000);
    return;
  }

  // Construir o request POST
  String request = String("POST ") + url + " HTTP/1.1\r\n" +
                   "Host: " + host + "\r\n" +
                   "Content-Type: application/json\r\n" +
                   "Content-Length: " + payload.length() + "\r\n\r\n" +
                   payload;

  client.print(request);

  // Ler a resposta do servidor
  while (client.connected()) {
    String line = client.readStringUntil('\n');
    if (line == "\r") break; // Cabeçalho HTTP finalizado
  }

  String response = client.readString();
  Serial.println("Resposta:");
  Serial.println(response);

  client.stop();
  delay(5000); // Aguardar antes de enviar novamente
}