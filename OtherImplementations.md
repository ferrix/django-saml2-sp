# Introduction #

Even using Google Search, you won't find all of these right away. This list is posted here with the hope that we can come together as a community on SAML 2.0 for Python and Django.


# Disclaimer #

This list was obtained from my own personal experience and may not be up-to-date or accurate. Please help me update it.

# Other Implementations #

| **IdP** | **SP** | **Target** | **What** | **Link** | **Comment** |
|:--------|:-------|:-----------|:---------|:---------|:------------|
| No      | Yes    | Python     | PySAML2  | http://packages.python.org/pysaml2/html/ |             |
| No      | Yes    | Django     | djangosaml2 | http://packages.python.org/djangosaml2/ | Builds on PySAML2 |
| Yes     | Yes    | Python     | python-saml2 | http://code.google.com/p/python-saml2/ |             |
| Yes     | No(?)  | Django     | GHeimdall2 | https://bitbucket.org/tmatsuo/gheimdall2/ | Builds on python-saml2 |
| Yes     | Yes    | Python     | python-lasso | http://lasso.entrouvert.org/ | python bindings into a C++ library; poor python documentation and difficult to grok |
| Yes     | Yes    | Python     | PySAML   | http://github.com/tachang/PySAML | Very incomplete, but inspired this project. |
| Yes     | Yes    | Django     | SAML 2.0 Example Code | http://robinelvin.wordpress.com/2009/09/04/saml-with-django/ | The foundation for this project; uses PySAML. |

# The State of SAML 2.0 in Python/Django #

Sadly, none of these implementations (this one included) are very complete or easy to use. Can we combine our efforts to produce a SAML 2.0 implementation that is:
  * Pythonic
  * Django-esque
  * as complete as simpleSAMLphp and Shibboleth