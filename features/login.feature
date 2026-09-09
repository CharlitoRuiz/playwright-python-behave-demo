Feature: Inicio de sesión en Home Banking

  Como usuario del Home Banking
  Quiero iniciar sesión con mis credenciales
  Para acceder a mis productos bancarios

  Scenario: Inicio de sesión exitoso
    Given que el usuario se encuentra en la página de inicio de sesión
    When ingresa credenciales válidas
    And selecciona la opción de iniciar sesión
    Then debe ingresar correctamente al Home Banking