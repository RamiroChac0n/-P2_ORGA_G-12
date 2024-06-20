 
  void setup() {
  // Configuración de los pines como salida
  for (int i = 2; i <= 12; i++) {
    pinMode(i, OUTPUT);
  }

  // Iniciar la comunicación serie
  Serial.begin(9600);
}

void loop() {
  // Verificar si hay datos disponibles en la serie
  if (Serial.available() > 0) {
    // Leer los datos enviados desde Python
    String datos = Serial.readStringUntil('\n');

    // Asegurarse de que los datos tengan la longitud esperada
    if (datos.length() == 11) {
      // Separar los datos recibidos
      String operacion = datos.substring(0, 3);
      String A_bin = datos.substring(3, 7);
      String B_bin = datos.substring(7, 11);

      // Asignar la operación a los pines correspondientes (2, 3, 4)
      for (int i = 0; i < 3; i++) {
        digitalWrite(2 + i, operacion.charAt(i) - '0');
      }

      // Asignar A_bin a los pines correspondientes (5, 6, 7, 8)
      for (int i = 0; i < 4; i++) {
        digitalWrite(5 + i, A_bin.charAt(i) - '0');
      }

      // Asignar B_bin a los pines correspondientes (9, 10, 11, 12)
      for (int i = 0; i < 4; i++) {
        digitalWrite(9 + i, B_bin.charAt(i) - '0');
      }
    }
  }
}
