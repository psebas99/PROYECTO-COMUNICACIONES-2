String input;
int n = 0;
int envio = 0;
int enviar1 = 0;
int enviar0 = 0;

void setup() {
   // put your setup code here, to run once:
   pinMode(LED_BUILTIN, OUTPUT);
   pinMode(2, OUTPUT);
   Serial.begin(9600);
   Serial.println("transmisor");
}
void loop() {
   // put your main code here, to run repeatedly:
     if(Serial.available()>0){
      input = Serial.readString();
      input.trim();
      n = input.length();
      if(n == 7){
             digitalWrite(LED_BUILTIN, HIGH);
             digitalWrite(2, HIGH);
             while(envio<4200000){
              envio++;
              }
             envio=0;
            digitalWrite(LED_BUILTIN, LOW);
            digitalWrite(2, LOW);
   for(int i = 0; i<n; i++){
    switch (input[i]){
      case '1':
          digitalWrite(LED_BUILTIN, HIGH);
          digitalWrite(2, HIGH);
          enviar1=0;
          while(enviar1<3360000){
            enviar1++;
            }        
      break;
      case '0':
          digitalWrite(LED_BUILTIN, LOW);
          digitalWrite(2, LOW);
          enviar0=0;
          while(enviar0<3360000){
            enviar0++;
            }
      break;}
      digitalWrite(LED_BUILTIN, LOW);
      digitalWrite(2, LOW);
   }
   n = 0;
    digitalWrite(LED_BUILTIN, LOW);
    digitalWrite(2, LOW);
        }else{
          digitalWrite(LED_BUILTIN, LOW);
          digitalWrite(2, LOW);}
    }
    
}
