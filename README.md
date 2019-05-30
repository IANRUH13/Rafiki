# Rafiki
Rafiki offers a safe heaven to talk about daily stress that's weighing heavily on the mind. It achieves this through offering anonymous communication among users since a personal account will not be required. This eradicates fear of judgment enabling users to open up about their well-being in order to get reliable feedback. Rafiki is a user who is not anonymous and have excellent counseling hence making them more knowledgeable to reply concerns such as stress,depression,anxiety disorders among others. 




### api End points
Method | Endpoint | Function |
| ------ | -------------| --------------- |
|USER| . |   .   |
|GET| `/api/v1/rafiki` | Show all post. |
|POST| `/api/v1/rafiki/share` | Post anonymously.|
|POST| `/api/v1/rafiki/share_id/counsel` | respond anonymously . |
|POST| `api/v1/rafiki/search/share_id` | Search for posts based on keyword. |
|POST| `api/v1/rafiki/share_id/report` | Report an offensive post anonymously. |
|Rafiki| . |   .   |
|POST| `api/v1/rafiki/register` |  set up a Rafiki account . |
|POST| `/api/v1/rafiki/share_id/rafiki_name` |  Login to a Rafiki account. |
|POST| `api/v1/rafikiki/login` |  Respond with a Rafiki account. |
|POST| `/api/v1/rafiki/share_id/edit/rafiki_name` | Edit a respond with a Rafiki account.|


## Installation

Clone the Github repository and use pip to install the dependencies
1. ` git clone https://github.com/bmugenya/Rafiki.gitt`
2. ` cd Rafiki`
3. ` Set up a virtual environment`
4. ` pip install -r requirements.txt`


