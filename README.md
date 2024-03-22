# Lending Library Database/App

This was an attempt to implement a library database/app for tracking books and have them lent out to users with them able to review the books.

Some of the main 'library' pieces are still missing (Checking books in/out of a library branch). This would have been the more interesting pieces but hopefully they'll be added eventually.

API

## Reader

| Method | Name         | Description                                  | Path                | Parameters                 |
| ------ | ------------ | -------------------------------------------- | ------------------- | -------------------------- |
| GET    | Show         | Returns the user's info                      | ~/user/_id_         | -                          |
| GET    | Show Reviews | Returns the reviews created by the user      | ~/user/_id_/reviews | -                          |
| GET    | Show Loans   | Returns the books currently lent to the user | ~/user/_id_/loans   | -                          |
| POST   | Create User  | Register's new user                          | ~/user              | **username**, **password** |
| PUT    | Update User  | Change user's data                           | ~/user/_id_         | username, password         |
| DELETE | Delete User  | Removes user's account                       | ~/user/_id_         | -                          |

## Library

| Method | Name       | Description                                        | Path                           | Parameters |
| ------ | ---------- | -------------------------------------------------- | ------------------------------ | ---------- |
| GET    | Index      | Returns list of all library branches               | ~/branches                     | -          |
| GET    | Show       | Returns library branch info                        | ~/branches/_id_                | -          |
| GET    | List Books | Returns books belonging to a branch w/ # of copies | ~/branches/_id_/book_inventory | -          |

## Author

| Method | Name             | Description                         | Path                | Parameters    |
| ------ | ---------------- | ----------------------------------- | ------------------- | ------------- |
| GET    | Show             | Returns author's data               | ~/author/_id_       | -             |
| GET    | List Books       | Returns books written by the author | ~/author/_id_/books | -             |
| POST   | Create           | Adds new author                     | ~/author            | **name**, bio |
| PUT    | Edit Author Info | Changes author's data               | ~/author/_id_       | name, bio     |

## Book

| Method | Name                | Description                                  | Path                     | Parameters                                                |
| ------ | ------------------- | -------------------------------------------- | ------------------------ | --------------------------------------------------------- |
| GET    | Show                | Returns the book's info                      | ~/books/_id_             | -                                                         |
| GET    | Index               | Lists all books                              | ~/books                  | -                                                         |
| POST   | Create              | Adds new book                                | ~/books                  | **Title**, **author_id**, genre, **format**, publish_year |
| DELETE | Delete              | Removes a book                               | ~/books/_id_             | -                                                         |
| GET    | Libraries Available | Lists library branches with the book         | ~/books/_id_/libraries   | -                                                         |
| GET    | List Reviews        | Lists reviews of a book                      | ~/books/_id_/reviews     | -                                                         |
| GET    | Average Rating      | Returns average of all reader reviews (0-10) | ~/books/_id_/reviews/avg | -                                                         |

## Review

| Method | Name   | Description                           | Path           | Parameters                                      |
| ------ | ------ | ------------------------------------- | -------------- | ----------------------------------------------- |
| GET    | Show   | Returns a review's info               | ~/reviews/_id_ | -                                               |
| GET    | Index  | Returns all reviews                   | ~/reviews      | -                                               |
| POST   | Create | Generates a new review                | ~/reviews      | **reader_id**, **book_id**, review_body, rating |
| PUT    | Update | Modifies review text, rating, or both | ~/reviews/_id_ | **reader_id**, **book_id**, review_body, rating |
| DELETE | Delete | Removes a user's review               | ~/reviews/_id_ | -                                               |

## Checkin/Checkout

| Method | Name           | Description                                        | Path      | Parameters                   |
| ------ | -------------- | -------------------------------------------------- | --------- | ---------------------------- |
| POST   | Check Out Book | Adds association between the reader and input book | ~/lending | user_id, book_id, library_id |
| DELETE | Return Book    | Removes book from the reader's list                | ~/lending | book_id, user_id             |
