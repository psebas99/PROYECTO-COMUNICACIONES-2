int lectura = 0;
int ciclo = 0;
int n = 0;
int escribir1 = 0;
int escribir0 = 0;
int parar = 0;
int cantidad1 = 0;
int cantidad0 = 0;
int tam_mensaje = 0;
int not_pairing = 0;
bool leer = false;
String mensaje = "";
String new_mensaje;
String uno = "1";
String cero = "0";

void setup() {
  // put your setup code here, to run once:
  pinMode(2, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  Serial.println("receptor");
}

void loop() {
  // put your main code here, to run repeatedly:
  while (true){
    lectura = digitalRead(2);
    switch (lectura){
      case HIGH:
        digitalWrite(LED_BUILTIN, HIGH);
        not_pairing = 0;
        n++;
        Serial.println(n);
      break;
      default:
        n = 0;
        not_pairing = not_pairing + 1;
      break;
      }
    if(not_pairing > 2500000){
      Serial.println("nomessage");
      not_pairing = 0;
      }
    if(n >= 115){
      leer = true; 
      Serial.println("a leer");
      ciclo = 0;
      n = 0;
      break;
      }
    }
   while(leer){
     ciclo = 0;
     while(ciclo<30){
      ciclo++;
      lectura = digitalRead(2);
      switch (lectura){
        case HIGH:
          escribir1++;
          Serial.print("en1:");
          Serial.println(escribir1);
          digitalWrite(LED_BUILTIN, HIGH);
        break;
        case LOW:
          escribir0++;
          Serial.print("en0:");
          Serial.println(escribir0);
          digitalWrite(LED_BUILTIN, LOW);
        break;
        }
      }
      switch (escribir1 > escribir0){
        case true:
          mensaje.concat(uno);
        break;
        case false:
          mensaje.concat(cero);
        break;
        }
        escribir1 = escribir0 = 0;
        tam_mensaje++;
          
      if (tam_mensaje == 7){
        leer = false;
        Serial.println("Se acabo mensaje");
        Serial.println(mensaje);
        escribir1=0;
        escribir0=0;
        lectura = LOW;
        mensaje = "";
        tam_mensaje = 0;
        n = 0;
        digitalWrite(LED_BUILTIN, LOW);
        }
    }
}
