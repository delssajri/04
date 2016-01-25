Feature: Abbility to confirm payment

  Scenario: As a user I can enter card info. When I press Done button payment request is transfered to server and Done changes to "Confirmed"
    Given payment server
    When I enter "4042692503977148"
    When I enter "0417"
    When I enter "123"
    When I touch Done
    When I wait 5 sec
    Then I see "CONFIRMED"
    Then I find db entry
    Then I check button Prev disabled
    Then I check button Next disabled
    Then I check button Done disabled

 
