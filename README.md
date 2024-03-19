# Lending Library Database/App

This was an attempt to implement a library database/app for tracking books and have them lent out to users with them able to review the books. 

Some of the main 'library' pieces are still missing (Checking books in/out of a library branch). This would have been the more interesting pieces but hopefully they'll be added eventually.

API 
## Reader
| Method | Name | Description | Path | Parameters |
| ------ | ---- | ----------- | ---- | ---------- |
| GET | Show | Returns the user's info | ~/user/<id> | - |
| GET | Show Reviews | Returns the reviews created by the user | ~/user/<id>/reviews | - |
| GET | Show Loans | Returns the books currently lent to the user | ~/user/<id>/loans | - |
| POST | Check Out Book | Adds association between the reader and input book | ~/user | book_id, user_id |
| DELETE | Return Book | Removes book from the reader's list | ~/user/<id>/loans | book_id |

## Library
| Method | Name | Description | Path | Parameters |
| ------ | ---- | ----------- | ---- | ---------- |
| GET | Index | Returns list of all library branches | ~/branches | - |
| GET | Show | Returns library branch info | ~/branches/<id> | - |
| GET | List Books | Returns books belonging to a branch | ~/branches/<id>/book_inventory | - |
| ***GET*** | Copies of | Returns number of available copies *(unimplimented)* | - | - |
| ***GET*** | Member List | Lists users under this library *(unimplimented)* | - | - |

## Book
| Method | Name | Description | Path | Parameters |
| ------ | ---- | ----------- | ---- | ---------- |
| GET | Show | Returns the book's info | ~/books/<id> | - |
| GET | Index | Lists all books | ~/books | - |
| POST | Create | Adds new book | ~/books | **Title**, **author_id**, genre, format, publish_year |
| DELETE | Delete | Removes a book | ~/books/<id> | - |
| GET | Libraries Available | Lists library branches with the book | ~/books/<id>/libraries | - |
| GET | List Reviews | Lists reviews of a book | ~/books/<id>/reviews | - |
| GET | Average Rating | Returns average of all reader reviews (0-10) | ~/books/<id>/reviews/avg | - |

## Review
| Method | Name | Description | Path | Parameters |
| ------ | ---- | ----------- | ---- | ---------- |
| GET | Show | Returns a review's info | ~/reviews/<id> | - |
| GET | Index | Returns all reviews | ~/reviews | - |
| POST | Create | Generates a new review | ~/reviews | **reader_id**, **book_id**, review_body, rating |
| PUT | Update | Modifies review text, rating, or both | ~/reviews/<id> | **reader_id**, **book_id**, review_body, rating |
| DELETE | Delete | Removes a user's review | ~/reviews/<id> | - |

