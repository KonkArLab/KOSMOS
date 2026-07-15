/*
Programme "kosmos_control_motor" à installer dans l'Arduino Nano du caisson moteur
Auteurs : Tristan Séchaud & Antoine Jégu
Date de création : 01_07_24
Date de mise à jour : 20_01_26
*/

#include "AccelStepper.h"
#include "avr/sleep.h"
#include <Wire.h>

// ===================== PARAMÈTRES MOTEUR =====================
const float stepsPerRevMotor = 200.0;
const float gearRatio        = 100.0;
const int   directionSign    = -1;
// =============================================================

#define SLAVE_ADDRESS 0x08

#define dirPin 4
#define stepPin 5
#define SleepModePin 6
#define wakeUpPin 3
#define LedPin A3

#define interrupt_pin 2
#define motorInterfaceType 1

volatile unsigned long button_time = 0;
volatile unsigned long last_button_time = 0;
int debounce = 500;

bool state_auto = 0;
bool state_i2c = 0;
bool i2c_detected = false;
bool rotation_done = true;
bool goToSleep = 0;

int Data = 1;
int Data_indent = 0;
int i2cData[6] = {};

// ===== LED =====
bool ledState = false;
unsigned long ledPrev = 0;
const unsigned long ledPeriod = 1000; // ms

// ===== I2C =====
int   target_degrees   = 60;
int   max_speed        = 1000;
int   max_acceleration = 1500;
int   pause_time       = 30;
int   step_mode        = 1;

AccelStepper stepper = AccelStepper(motorInterfaceType, stepPin, dirPin);

// ===== AUTO =====
bool autoPauseActive = false;
unsigned long autoPauseStart = 0;

// ===== moteur non bloquant =====
bool motorMoving = false;

long stepsFromDegrees(float deg) {
  float totalStepsPerRev = stepsPerRevMotor * step_mode * gearRatio;
  float stepsFloat = deg * (totalStepsPerRev / 360.0f);
  return (long)(stepsFloat + (stepsFloat >= 0 ? 0.5f : -0.5f));
}

void setup() {
  pinMode(wakeUpPin, INPUT);
  pinMode(SleepModePin, OUTPUT);
  pinMode(LedPin, OUTPUT);
  digitalWrite(SleepModePin, LOW);
  digitalWrite(LedPin, LOW);

  stepper.setMaxSpeed(max_speed * step_mode);
  stepper.setAcceleration(max_acceleration * step_mode);
  stepper.disableOutputs();

  attachInterrupt(digitalPinToInterrupt(interrupt_pin), change_state, RISING);

  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
}

// lance une rotation NON bloquante
void startMotorRotation() {
  digitalWrite(SleepModePin, HIGH);

  long steps = stepsFromDegrees(target_degrees) * directionSign;
  stepper.move(steps);

  motorMoving = true;
  // on ne touche pas à la LED ici, elle est gérée dans loop()
}

void loop() {

  // =====================================================
  // 1) LED : clignote SI état moteur ACTIF (même en pause)
  // =====================================================
  bool motorStateActive =
      (!i2c_detected && state_auto)    // mode auto activé
      || (i2c_detected && state_i2c)   // ordre I2C actif
      || motorMoving;                  // ou moteur tourne vraiment

  if (motorStateActive) {
    unsigned long now = millis();
    if (now - ledPrev >= ledPeriod) {
      ledPrev = now;
      ledState = !ledState;
      digitalWrite(LedPin, ledState);
    }
  } else {
    ledState = false;
    digitalWrite(LedPin, LOW);
  }

  // =========================================
  // 2) faire avancer le moteur si en cours
  // =========================================
  if (motorMoving) {
    stepper.run();

    if (stepper.distanceToGo() == 0) {
      motorMoving = false;
      digitalWrite(SleepModePin, LOW);
      rotation_done = true;

      // si on était en mode auto: on démarre la pause
      if (!i2c_detected && state_auto) {
        autoPauseActive = true;
        autoPauseStart = millis();
      }
    }
  }

  // =========================================
  // 3) MODE AUTO (pas d'I2C)
  // =========================================
  if (!i2c_detected && state_auto) {
    if (!motorMoving && !autoPauseActive) {
      startMotorRotation();
    } else if (autoPauseActive) {
      if (millis() - autoPauseStart >= (unsigned long)pause_time * 1000UL) {
        autoPauseActive = false;
      }
    }
  } else {
    autoPauseActive = false;
  }

  // =========================================
  // 4) MODE I2C
  // =========================================
  if (i2c_detected) {
    if (state_i2c && !rotation_done && !motorMoving) {
      startMotorRotation();
      // rotation_done sera mis à true à la fin
    }

    if (goToSleep) {
      goToSleep = 0;
      attachInterrupt(digitalPinToInterrupt(wakeUpPin), wakeUp, HIGH);
      set_sleep_mode(SLEEP_MODE_PWR_DOWN);
      sleep_enable();
      sleep_cpu();
      sleep_disable();
      detachInterrupt(digitalPinToInterrupt(wakeUpPin));

      if (!digitalRead(wakeUpPin)) {
        goToSleep = 1;
      }
    }
  }
}

void wakeUp() {}

void change_state() {
  button_time = millis();
  if (button_time > last_button_time + debounce) {
    state_auto = !state_auto;
    last_button_time = button_time;
    // on ne touche pas à la LED ici
  }
}

void receiveData(int byteCount) {
  while (Wire.available()) {
    if (!i2c_detected) {
      i2c_detected = true;
      detachInterrupt(digitalPinToInterrupt(interrupt_pin));
    }
    Data = Wire.read();
    if (!Data) {
      Data_indent = 0;
    } else {
      i2cData[Data_indent] = Data;
      Data_indent += 1;
    }
    if (Data_indent == 6) {
      state_i2c = bool(i2cData[0] - 1);
      target_degrees = i2cData[1];
      stepper.setMaxSpeed(i2cData[2] * step_mode * 10);
      stepper.setAcceleration(i2cData[3] * step_mode * 10);
      goToSleep = bool(i2cData[4] - 1);
      step_mode = i2cData[5];
      rotation_done = !state_i2c;
    }
  }
}

void sendData() {
  Wire.write(rotation_done);
}
