Feature: Transferencias bancarias

  Como usuario autenticado
  Quiero realizar una transferencia
  Para enviar dinero desde una de mis cuentas

  Scenario: Realizar una transferencia con datos válidos
    Given que el usuario se encuentra autenticado en Home Banking
    When navega hacia la opción de transferencias
    And completa los datos de una transferencia válida
    And confirma la operación
    Then debe visualizar la confirmación de la transferencia