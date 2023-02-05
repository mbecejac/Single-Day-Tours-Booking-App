ITBC Project 2: SINGLE-DAY TOURS BOOKING APP

Description: 
This is a Python app to manage single-day tours and local walking tours. 

Through the app, clients can search for available tours based on the tour date, location, whether it is a walking tour 
or not, and the language the tour will be conducted in. They can also apply for the tour.

Employees can create new tours, create new clients, make changes to tours, assign guide to tour, assign bus carrier to tour... 

All users sign in with a unique email address and password.

The app has the following entities (for now):

    Users
    Employees
    Tour Guides
    Languages used by tourist guides
    Clients
    Tours
    Bus Carriers
    Tour Applications



The list of endpoints that the app will implement (preliminary):

    Add new employee
    Add new guide
    Add new client
    Display available tours based on tour date
    Display available tours based on tour location
    Display available tours based on the language the tour is conducted in
    Client application for tour
    Assign bus carrier to tour (if it is not a walking tour)
    Assign guide to tour
    Change the guide who will lead the tour
    Delete client from tour application if they cancel
    Display all tours led by a guide
    Display all tours attended by a client
    Display all clients applied for a tour
    Change the payment status of a client for the tour
    Send email notification to client who has not made payment for tour
    Delete client from tour application if they do not make payment
    Send email to bus carrier with list of passengers for tour.