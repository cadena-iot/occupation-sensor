/*!
 * @file VL53L1XDUAL.h

 ****************************************************/

#ifndef _VL53L1XDUAL
#define _VL53L1XDUAL

#include "Adafruit_VL53L1X.h"
#include "Wire.h"
#include "vl53l1x_class.h"

#define VL53L1X_I2C_ADDR 0x29 ///< Default sensor I2C address

/**************************************************************************/
/*!
    @brief  Class that stores state and functions for interacting with VL53L1X
   time-of-flight sensor chips
*/
/**************************************************************************/
class VL53L1XDUAL : public VL53L1X
{
public:
    int8_t IRQ_PIN_1, IRQ_PIN_2;
    void init(bool* res);
    void clearInterrupts();
    void getMeasures(int16_t* measures);

  VL53L1XDUAL(uint8_t shutdown_pin = -1, uint8_t irq_pin = -1);
  bool begin(uint8_t i2c_addr = VL53L1X_I2C_ADDR, TwoWire *theWire = &Wire,
             bool debug = false);
  uint16_t sensorID(void);
  bool startRanging(void);
  bool stopRanging(void);
  bool setTimingBudget(uint16_t ms);
  uint16_t getTimingBudget(void);
  bool dataReady(void);
  int16_t distance(void);
  bool clearInterrupt(void);
  bool setIntPolarity(bool polarity);
  bool getIntPolarity(void);
  VL53L1X_ERROR vl_status; /**< VL53L1X API Error Status */

private:
    int8_t XSHUT_PIN_1, XSHUT_PIN_2;
};

#endif
