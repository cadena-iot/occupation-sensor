#include "driver/gpio.h"
#include "VL53L1XDUAL.h"

// Define los pines a utilizar
#define RED_PIN 33
#define GREEN_PIN 25
#define BLUE_PIN 32

// Función para encender el LED en rojo
void red()
{
    digitalWrite(RED_PIN, HIGH);
    digitalWrite(GREEN_PIN, LOW);
    digitalWrite(BLUE_PIN, LOW);
}

// Función para encender el LED en verde
void green()
{
    digitalWrite(RED_PIN, LOW);
    digitalWrite(GREEN_PIN, HIGH);
    digitalWrite(BLUE_PIN, LOW);
}

// Función para encender el LED en azul
void blue()
{
    digitalWrite(RED_PIN, LOW);
    digitalWrite(GREEN_PIN, LOW);
    digitalWrite(BLUE_PIN, HIGH);
}

// Función para encender el LED en amarillo (rojo y verde)
void yellow()
{
    digitalWrite(RED_PIN, HIGH);
    digitalWrite(GREEN_PIN, HIGH);
    digitalWrite(BLUE_PIN, LOW);
}

// Función para encender el LED en cian (verde y azul)
void cyan()
{
    digitalWrite(RED_PIN, LOW);
    digitalWrite(GREEN_PIN, HIGH);
    digitalWrite(BLUE_PIN, HIGH);
}

// Función para encender el LED en magenta (rojo y azul)
void magenta()
{
    digitalWrite(RED_PIN, HIGH);
    digitalWrite(GREEN_PIN, LOW);
    digitalWrite(BLUE_PIN, HIGH);
}

// Función para encender el LED en blanco (rojo, verde y azul)
void white()
{
    digitalWrite(RED_PIN, HIGH);
    digitalWrite(GREEN_PIN, HIGH);
    digitalWrite(BLUE_PIN, HIGH);
}
/*
void setup() {
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);
  //cualquier otra configuración necesaria
}

//Secuencia de colores
void loop() {
  red();

  delay(1000);
  green();
  delay(1000);
  blue();
  delay(1000);
  yellow();
  delay(1000);
  cyan();
  delay(1000);
  magenta();
  delay(1000);
  white();
  delay(1000);

}
*/

VL53L1XDUAL dual_sensor;
bool res[2];
int value = 0;
int count = 0;
//int16_t measures[2];
int16_t* measures = new int16_t[2];

void setup()
{
    Serial.begin(115200);
    while (!Serial)
        delay(10);
    Serial.println(F("Adafruit VL53L1X sensor demo"));
    dual_sensor.init(res);
    Serial.print(res[0]);
    Serial.println(res[1]);
}

void loop()
{
    delay(1000);
    dual_sensor.getMeasures(measures);
    Serial.print(F("Interruption Value: "));
    Serial.println(value);
    Serial.print(F("Distance 1: "));
    Serial.println(measures[0]);
    Serial.print(F("Distance 2: "));
    Serial.println(measures[1]);
    value = digitalRead(dual_sensor.IRQ_PIN_1);
    count += 1;
    if (count == 5){
        count = 0;
        dual_sensor.clearInterrupts();
    }
    /*
    int16_t distance;

    if (sensor1.dataReady())
    {
        // new measurement for the taking!
        distance = sensor1.distance();
        if (distance == -1)
        {
            // something went wrong!
            Serial.print(F("Couldn't get distance: "));
            Serial.println(sensor1.vl_status);
            return;
        }
        Serial.print(F("Distance: "));
        Serial.print(distance);
        Serial.println(" mm");

        // data is read out, time for another reading!
        sensor1.clearInterrupt();
    }
    */
}