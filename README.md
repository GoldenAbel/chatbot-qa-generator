# Entity types, properties and relations

* **COMPANY** (what)
  * name (what)
  * founder (who)
  * address (what)
  * website (what)
  * type of business (what)
  * stage (what)
  * jobs -> JOBs

* **JOB** (what)
  * function (what)
  * location (what)
  * company -> a COMPANY

* **INVESTOR** (who)
  * name (what)

* **POST** (what)
  * title (what)
  * author (who)
  * category (what)

* **PODCAST** (what)
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
  * questions on related concepts (auto-suggested search queries) that could be outsourced to Google search
    * Q: *where can I find [suggested-query]*
    * Q: *tell me about [suggested-query]*
    * Q: *show me [suggested-query]*
    * Q: *I want to know about [suggested-query]*

* About a property
  * Q: *[wh-type] is the [property-name] of [entity-name]*
  * Q: *show me the [property-name] of [entity-name]*

* About a one-to-one relation
  * Q: *[wh-type] is the [relation-name] of [entity-name]*
  * Q: *show me the [relation-name] of [entity-name]*

* About a one-to-many relation
  * Q: *[wh-type] are the [relation-name] of [entity-name]*
  * Q: *list all [relation-name] of [entity-name]*
  * Q: *show me all [relation-name] of [entity-name]*
  * Q: *show me one [relation-name] of [entity-name]*


## Questions about COMPANY 

* self
  * Q: *what does [entity-name] do*

* name
  * Q: *what is [entity-name] called*

* founder
  * Q: *who founded [entity-name]*
  * Q: *who created [entity-name]*
  * Q: *who started [entity-name]*
  * Q: *what is the founding team of [entity-name]*
  * Q: *who are the founders of [entity-name]*
  * Q: *show me the founders of [entity-name]*

* address
  * Q: *where is [entity-name]*
  * Q: *where is [entity-name] located*
  * Q: *show direction to [entity-name]*

* website
  * Q: *take me to the website of [entity-name]*
  * Q: *more information about [entity-name]*
  * Q: *do you have a link to the wesite of [entity-name]*
  * Q: *show me the link to the website of [entity-name]*
  * Q: *I want to checkout more about [entity-name]*

* type of business
  * Q: *what business is [entity-name] about*
  * Q: *what is the industry of [entity-name]*
  * Q: *in what industry does [entity-name] work on*
  * Q: *in what area does [entity-name] work on*
  * Q: *what kind of problem does [entity-name] solve*

* stage
  * Q: *current stage of [entity-name]*
  * Q: *is [entity-name] funded*
  * Q: *is [entity-name] seeded*
  * Q: *how is [entity-name] doing*
  * Q: *has [entity-name] raised any capital*

* jobs
  * Q: *[wh-type] are the job openings at [entity-name]*
  * Q: *[wh-type] are the jobs available at [entity-name]*
  * Q: *list all job openings at [entity-name]*
  * Q: *show me all job openings at [entity-name]*
  * Q: *show me one job opening at [entity-name]*
  * Q: *I want to join [entity-name]*
  * Q: *how can I join [entity-name]*
  * Q: *I want to apply for job at [entity-name]*
  * Q: *how can I apply for job at [entity-name]*
  

## Questions about a16z

* auto-generated questinos from the /about page
* About job openings
  * Q: *show me portfolio company job openings*
  * Q: *request job in portfolio company*
  * Q: *I want to join a portfolio company*

