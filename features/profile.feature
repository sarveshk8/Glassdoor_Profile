Feature: Profile

    Background:  common steps
      Given launch the browser
      When open glassdoor loginpage
      And enter login details

    Scenario: fill the profile details
      And click on profile icon
      Then verify profile page is displayed or not
       And select employement status
      Then verify that status is selected or not
      And enter first name and last name details
      Then verify that full name is saved successfully
      And enter current job title
      Then verify that job title entered successfully
      And enter company name
      Then verify that company name entered successfully
      And enter current location
      Then verify that current location entered successfully
      And click on checkbox
      Then verify that checkbox is being checked or unchecked
      And enter desired job title
      Then verify that job title is entered succesfully or not
      And enter desired location
      Then verify that location is entered successfully
      And click and upload resume
      Then verify that resume uploaded successfully or not
