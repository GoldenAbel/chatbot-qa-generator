# Q-gen spec

## Entity types, properties and relations

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
  * role (what)

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

## Questions 

### Basic questions for all entity types

* About self
  * Q: *[wh-type] is [entity-name]*
  * Q: *information about [entity-name]*
  * Q: *tell me about [entity-name]*
  * Q: *show me [entity-name]*
  * Q: *I want to know about [entity-name]*
  * data-driven approach
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


### Questions about COMPANY 

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

* jobs (see "job query" section)

### Questions about JOB

* job query
  * Q: *[wh-type] are the job openings [condition]*
  * Q: *[wh-type] are the jobs available [condition]*
  * Q: *list all job openings [condition]*
  * Q: *show me all job openings [condition]*
  * Q: *show me one job opening [condition]*
  * Q: *I want to apply for job [condition]*
  * Q: *how can I apply for job [condition]*
  * Q: *I want to join [company]*
  * Q: *how can I join [company]*
  * Q: *show me portfolio company job openings*
  * Q: *request job in portfolio company*
  * Q: *I want to join a portfolio company*
  * ...where conditions can be any one of or a combination of the following units
    * in [company]
    * for [company]
    * for [function]
    * that require [function]
    * in [location]
    * that is located in [location]

* function
  * Q: *what is the position for [entity-name]*
  * Q: *what do I work on for [entity-name]*
  * Q: *what expertise do I need for [entity-name]*
  * Q: *what is the requirement for [entity-name]*

* location
  * Q: *where is the office for [entity-name]*
  * Q: *where do I need to work for [entity-name]*

* company
  * Q: *who is the employer of [entity-name]*
  * Q: *which company is [entity-name] for*

### Questions about INVESTOR

  * self
    * data-driven approach
      * auto-generated questions from the investor profile page
  
  * role

### Questions about A16Z

* self
  * data-driven approach
    * auto-generated questions from the /about page

* portfolio
  * Q: *show me all the portfolio companies*
 
* team
  * Q: *show me all the investors*
  * Q: *show me all the people in charge of investing*
  * Q: *show me all the people in charge of market development*
  * Q: *show me all the people in charge of technical talent*
  * Q: *show me all the people in charge of executive talent*
  * Q: *show me all the people in charge of marketing*
  * Q: *show me all the people in charge of corporate development*


