# Entity types, properties and relations

* **COMPANY**
  * *self* (what)
  * name (what)
  * founder (who)
  * address (where)
  * website (what)
  * type of business (what)
  * stage (what)
  * jobs -> JOBs

* **JOB**
  * function (what)
  * location (where)
  * company -> a COMPANY

* **INVESTOR**
  * *self* (who)
  * name (what)

* **POST**
  * title (what)
  * author (who)
  * category (what)

* **PODCAST**
  * title (what)
  * author (who)
  * category (what)

* **A16Z** : COMPANY
  * portfolio -> COMPANYs
  * team -> INVESTORs
  * posts -> POSTs
  * podcasts -> PODCASTs

# Questions 

## Basic questions for all entity types

* About self
  * Q: *[wh-type] is [entity-name]*
  * Q: *information about [entity-name]*
  * Q: *tell me about [entity-name]*
  * Q: *show me [entity-name]*
  * Q: *I want to know about [entity-name]*
  * quora questions associated with the topic about this entity
  * auto-generated questions from the wikipedia page about this entity
  * questions on related concepts (auto-suggested search queries) that could be out-sourced to Google search
    * Q: *where can I find [suggested-query]*
    * Q: *tell me about [suggested-query]*
    * Q: *show me [suggested-query]*
    * Q: *I want to know about [suggested-query]*

* About a property
  * Q: *[wh-type] is the [property-name] of [entity-name]*
  * Q: *show me the [property-name] of [entity-name]*

* About a one-to-one relation

* About a one-to-many relation


## Questions about COMPANY 

* self
  * Q: *what does [entity-name] do*

* name
  * Q: *what is [entity-name] called*

* founder
  * Q: *who founded [entity-name]*
  * Q: *who are the founders of [entity-name]*

## Questions about a16z

* auto-generated questinos from the /about page
* About job openings
  * Q: *show me portfolio company job openings*
  * Q: *request job in portfolio company*
  * Q: *I want to join your portfolio company*

