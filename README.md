# 🎬 Cinema Ticket Sales Platform

A Django-based cinema ticket sales platform developed as an educational backend project.

The application provides a complete workflow for managing **movies, cinemas, showtimes, users, balances, and ticket purchases**. Users can browse movies and cinemas, search for available showtimes using multiple filters, and purchase tickets using their account balance.

---

## ✨ Features

### 🎥 Movie Management

- Create and manage movie information
- Store movie name, director, release year, duration, and description
- View movie lists and detailed information

### 🏢 Cinema Management

- Manage cinema information
- Store cinema code, name, city, capacity, contact information, and address
- Browse active cinemas and view cinema details

### 🕐 Showtime Management

- Create and manage movie showtimes
- Associate each showtime with a movie and cinema
- Define:
  - Start time
  - Ticket price
  - Seat availability
  - Sale status

### 🎟️ Ticket Sales

- Purchase tickets for available showtimes
- Reserve seats
- Track ticket status
- Handle different sale states such as:
  - 🟢 Sale Open
  - 🔴 Sold Out
  - ⚫ Canceled

### 👤 User Management

- User authentication
- User profile management
- User balance management
- Use account balance to purchase tickets

### 🔎 Showtime Search

Showtimes can be searched and filtered using multiple criteria, including:

- Movie name
- Cinema
- Sale status
- Movie duration
- Minimum/maximum ticket price

### 💰 Balance Management

Each user has an account balance that can be used for ticket purchases.

### ⚙️ Django Admin

The built-in Django Admin interface can be used to manage:

- Movies
- Cinemas
- Showtimes
- Tickets
- Users and related data

---

## 🧩 Application Workflow

The general ticket purchasing workflow looks like this:

```text
                    ┌──────────────┐
                    │     User     │
                    └──────┬───────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Browse Movies   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Browse Cinemas  │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Search Showtimes│
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Select Showtime │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Select Seat(s)  │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Check Balance   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Purchase Ticket │
                  └─────────────────┘
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Backend programming language |
| 🎯 Django | Web framework |
| 🗄️ SQLite | Default database |
| 🌐 HTML | Server-rendered templates |
| 📝 Markdown | Documentation |

---

## 🏗️ Project Architecture

The project follows Django's application-based structure and separates functionality into dedicated applications.

### Main Django Applications

- `accounts` — Authentication and user profile functionality
- `ticketing` — Movies, cinemas, showtimes, and ticket-related functionality
- `cinema` — Main Django project configuration

This structure keeps user-related functionality separated from the core ticketing domain.

---

## 📂 Project Structure

```text
cinema/
│
├── accounts/
│   ├── migrations/
│   ├── templates/
│   │   └── accounts/
│   │       ├── login.html
│   │       ├── logout.html
│   │       └── profile_details.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── urls.py
│
├── cinema/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── ticketing/
│   ├── migrations/
│   ├── templates/
│   │   └── ticketing/
│   │       ├── cinema_details.html
│   │       ├── cinema_list.html
│   │       ├── movie_details.html
│   │       ├── movie_list.html
│   │       ├── showtime_details.html
│   │       ├── showtime_list.html
│   │       ├── ticket_details.html
│   │       └── ticket_list.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── urls.py
│
├── templates/
│   └── base.html
│
├── manage.py
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Before running the project, make sure you have:

- Python 3.x
- pip
- Git

---

### 1. Clone the Repository

```bash
git clone https://github.com/Mahdiwav/cinema.git
cd cinema
```

### 2. Create a Virtual Environment

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install Django
```

> The project currently uses Django as its primary framework. If a `requirements.txt` file is added in the future, dependencies can be installed using `pip install -r requirements.txt`.

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

The application will then be available through the local Django development server.

---

## 📖 Usage

After starting the development server, the main application workflows include:

### 🎥 Browse Movies

Access the movie listing and view detailed information about individual movies.

```text
/ticketing/movie/list/
```

### 🏢 Browse Cinemas

View available cinemas and their details.

```text
/ticketing/cinema/list/
```

### 🕐 Browse Showtimes

View available showtimes and their related movie and cinema information.

```text
/ticketing/showtime/list/
```

### 🎟️ Purchase Tickets

Users can authenticate, select an available showtime, choose a seat, and purchase a ticket using their available account balance.

### 👤 Manage Profile

Authenticated users can access their profile and view/manage their account-related information and balance.

---

## 🧪 Testing

The project contains Django test modules within the applications:

```text
accounts/tests.py
ticketing/tests.py
```

Tests can be executed using Django's test runner:

```bash
python manage.py test
```

---

## ⚙️ Django Admin

The project uses Django's built-in administration interface for managing application data.

After creating a superuser:

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

The Django Admin interface can then be used to manage the project's core entities.

---

## 🔍 Search & Filtering

The showtime search functionality allows users to narrow down available showtimes based on different criteria.

Supported filtering criteria include:

```text
Movie
Cinema
Sale Status
Movie Duration
Price Range
```

This makes it easier for users to find suitable showtimes without manually browsing every available option.

---

## 🔐 User & Ticket Flow

The application connects user management with the ticket purchasing process:

```text
User
 │
 ├── Authentication
 │
 ├── Profile
 │
 ├── Account Balance
 │
 └── Ticket Purchase
       │
       ├── Select Showtime
       ├── Select Seat
       ├── Check Availability
       └── Complete Purchase
```

---

## 📌 Project Status

🚧 **Educational Project**

This project was developed for learning and practicing Django backend development concepts, including:

- Django project structure
- Django applications
- Models and relationships
- Forms
- Templates
- URL routing
- Authentication
- Django Admin
- Database migrations
- Ticket purchasing workflows
- Search and filtering

It is intended primarily as a learning and portfolio project rather than a production-ready cinema ticketing system.

---

## 🔮 Potential Improvements

The following features could be added in future iterations:

- [ ] PostgreSQL support
- [ ] REST API using Django REST Framework
- [ ] Online payment gateway
- [ ] Email/SMS ticket confirmation
- [ ] More advanced seat management
- [ ] Cinema hall and seat layout management
- [ ] Ticket cancellation and refund workflow
- [ ] Automated test coverage
- [ ] Docker support
- [ ] Production deployment configuration
- [ ] API documentation with Swagger/OpenAPI

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you would like to improve the project:

1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Run the test suite
5. Commit your changes
6. Open a Pull Request

---

## 📄 License

No license has currently been specified for this project.

---

## 👨‍💻 Author

**Mahdi Faghani**

Backend Developer focused on Python and Django.

---

## ⭐ Support

If you find this project useful or interesting:

⭐ Star the repository  
🍴 Fork the project  
🐛 Report bugs or suggest improvements  
💡 Open an issue with your ideas

---

<p align="center">
  Built with ❤️ using Python & Django
</p>
