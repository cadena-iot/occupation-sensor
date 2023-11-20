#include "VL53L1XDUAL.h"
/*
bool start(Adafruit_VL53L1X sensor, uint8_t address, int8_t shut_pin, int i)
{
    if (!sensor.begin(address, &Wire, true))
    {
        Serial.print(F("Error on init of VL sensor_"));
        Serial.print(i);
        Serial.println(": " + sensor.vl_status);
        return false;
    }
    //    sensor.VL53L1X_SetI2CAddress(address);
    Serial.print(F("Sensor_"));
    Serial.print(i);
    Serial.println(" OK!");
    Serial.print(F("Sensor_"));
    Serial.print(i);
    Serial.print(" ID: 0x");
    Serial.println(sensor.sensorID(), HEX);
    if (!sensor.startRanging())
    {
        Serial.print(F("Couldn't start ranging: "));
        Serial.println(sensor.vl_status);
        return false;
    }
    Serial.println(F("Ranging started"));
    // Valid timing budgets: 15, 20, 33, 50, 100, 200 and 500ms!
    sensor.setTimingBudget(500);
    Serial.print(F("Timing budget (ms): "));
    Serial.println(sensor.getTimingBudget());

    //    sensor.clearInterrupt();
    //    sensor.VL53L1X_SetDistanceThreshold(50, 1000, 0, 1);
    //    vl.VL53L1X_SetInterruptPolarity(0);

    digitalWrite(shut_pin, LOW);
    return true;
}
*/

// VL53L1XDUAL::VL53L1XDUAL(uint8_t shutdown_pin, uint8_t irq_pin) : VL53L1X(NULL, irq_pin) {
//   _shutdown_pin = shutdown_pin;
//   _irq_pin = irq_pin;
// }

VL53L1XDUAL::VL53L1XDUAL(uint8_t shutdown_pin, uint8_t irq_pin) : VL53L1X(NULL, irq_pin) {
{
    Wire.begin();
    IRQ_PIN_1 = 26;
    IRQ_PIN_2 = 14;
    XSHUT_PIN_1 = 27;
    XSHUT_PIN_2 = 13;
    // sensor_1 = Adafruit_VL53L1X(XSHUT_PIN_1, IRQ_PIN_1);
    // sensor_2 = Adafruit_VL53L1X(XSHUT_PIN_2, IRQ_PIN_2);
//    sensor_1 = VL53L1X(&Wire, XSHUT_PIN_1);
    // sensor_2 = Adafruit_VL53L1X(XSHUT_PIN_2, IRQ_PIN_2);
    pinMode(IRQ_PIN_1, INPUT);
    pinMode(IRQ_PIN_2, INPUT);
    pinMode(XSHUT_PIN_1, OUTPUT);
    pinMode(XSHUT_PIN_2, OUTPUT);
    digitalWrite(XSHUT_PIN_1, LOW);
    digitalWrite(XSHUT_PIN_2, LOW);
}
/*
void VL53L1XDUAL::init(bool *res)
{
    // res[0] = start(sensor_1, 0x29, XSHUT_PIN_1, 1);
    // res[1] = start(sensor_2, 0x30, XSHUT_PIN_2, 2);
    //    Serial.println(sensor_1.VL53L1X_GetSensorId(0x0029));
}

void VL53L1XDUAL::clearInterrupts()
{
    //    sensor_1.clearInterrupt();
    //    sensor_2.clearInterrupt();
}

void VL53L1XDUAL::getMeasures(int16_t *measures)
{
    /*
    digitalWrite(XSHUT_PIN_1, HIGH);
    digitalWrite(XSHUT_PIN_1, LOW);
    delay(5);
    digitalWrite(XSHUT_PIN_1, HIGH);
    delay(5);

    Serial.println("Getting Measures...");
    int16_t distance;

    if (sensor_1.dataReady())
    {
        // new measurement for the taking!
        distance = sensor_1.distance();
        if (distance == -1)
        {
            // something went wrong!
            Serial.print(F("Couldn't get distance: "));
            Serial.println(sensor_1.vl_status);
            return;
        }
        Serial.print(F("Distance: "));
        Serial.print(distance);
        Serial.println(" mm");

        // data is read out, time for another reading!
        sensor_1.clearInterrupt();
    }

    //    measures[0] = sensor_1.distance();
    // Serial.println("Hasta aqui llegue 4");
    // measures[1] = sensor_2.distance();
    
}
*/