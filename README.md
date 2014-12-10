one2oner
=====

Surveyer
=====
Apllication is purposed for Survey creation and storing them for future using

Surveyer - Models:
* Survey
 * name - char field
 * questions - M2M link on Question
* Question
 * question_text

Record
=====
Application is purposed to perform some one-2-one session and record it's result

Record - Models:
* Record
 * interviewer = current user
 * employee - FK to User
 * survey - FK to Survey
 * date - date field, pre-populated Today
* Answer
 * record - FK to Record
 * question - FK on Question
 * mark - char field + choices
 * explanation - text field, nullable and can be blank

Dossier
=====
Application is made only with one purpose, to use OneToOneField relationship

Dossier - Models:
* Address
 * zip - integer
 * country - Char Field
 * region - Char Field
 * district - Char Field
 * street - Char Field
 * building - Char Field

* Dossier
 * address - O2O on Address


