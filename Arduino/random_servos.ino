#include <Servo.h>

Servo servo1;
Servo servo2;

int position1;
int position2;

void setup() {
  servo1.attach(9);  // первый сервопривод к пину 9
  servo2.attach(10); // второй сервопривод к пину 10
  
  position1 = 90; // Среднее положение для первого
  position2 = 90; // Среднее положение для второго
  
  // Устанавливаем начальные положения
  servo1.write(position1);
  servo2.write(position2);
  
  // Небольшая задержка для стабилизации
  delay(500);
}

void loop() {
  // Выбираем случайный сервопривод (1 или 2)
  int chosenServo = random(1, 3);
  
  // Выбираем случайное направление (влево или вправо)
  int direction = random(0, 2); // 0 = влево, 1 = вправо
  
  // Выбираем случайный угол поворота от 30 до 70 градусов
  int randomAngle = random(30, 71);
  
  // Определяем конечное положение для выбранного сервопривода
  int targetPosition;
  
  if (chosenServo == 1) {
    // Плавный поворот для первого сервопривода
    if (direction == 0) {
      targetPosition = position1 - randomAngle;  // Поворот влево
    } else {
      targetPosition = position1 + randomAngle;  // Поворот вправо
    }
    
    // Ограничиваем диапазон углов между 0 и 180 градусов
    if (targetPosition > 180) targetPosition = 180;
    if (targetPosition < 0) targetPosition = 0;
    
    // Плавно поворачиваем к новому положению
    smoothMove(servo1, position1, targetPosition);
    
    // Обновляем текущее положение
    position1 = targetPosition;
    
  } else {
    // Плавный поворот для второго сервопривода
    if (direction == 0) {
      targetPosition = position2 - randomAngle;  // Поворот влево
    } else {
      targetPosition = position2 + randomAngle;  // Поворот вправо
    }
    
    // Ограничиваем диапазон углов между 0 и 180 градусов
    if (targetPosition > 180) targetPosition = 180;
    if (targetPosition < 0) targetPosition = 0;
    
    // Плавно поворачиваем к новому положению
    smoothMove(servo2, position2, targetPosition);
    
    // Обновляем текущее положение
    position2 = targetPosition;
  }
  
  // Задержка перед следующим поворотом
  delay(2000); // 2 секунды задержки
}

// Функция для плавного движения сервопривода
void smoothMove(Servo &servo, int startPos, int endPos) {
  int stepDelay = 20; // Задержка между шагами (20 мс)
  int stepSize = 1;   // Шаг изменения угла
  
  if (startPos < endPos) {
    // Плавное увеличение угла
    for (int pos = startPos; pos <= endPos; pos += stepSize) {
      servo.write(pos);
      delay(stepDelay);
    }
  } else {
    // Плавное уменьшение угла
    for (int pos = startPos; pos >= endPos; pos -= stepSize) {
      servo.write(pos);
      delay(stepDelay);
    }
  }
}