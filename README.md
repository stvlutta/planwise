# PlanWise Application

A modern full-stack project management platform built with Flask (backend) and React (frontend).

## Features

### Database Models
- **User**: Stores user information (username, email)
- **Project**: Groups related tasks (title, description, owner)
- **Task**: Individual tasks (title, description, status, priority, due date)
- **ProjectCollaborator**: Many-to-many relationship between users and projects with roles

### Relationships
- User → Tasks (one-to-many)
- User → Projects (one-to-many as owner)
- Project → Tasks (one-to-many)
- User ↔ Project via ProjectCollaborator (many-to-many with role attribute)

### API Features
- Full CRUD operations for all resources
- RESTful API endpoints
- Data validation
- Foreign key relationships

### Frontend Features
- React with React Router (3+ routes)
- Formik forms with Yup validation
- Responsive design
- Task filtering and status updates
- Project management

## Setup Instructions

### Backend Setup
1. Install dependencies:
   ```bash
   pipenv install
   pipenv shell
   ```

2. Initialize database:
   ```bash
   cd server
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

3. Seed database:
   ```bash
   python seed.py
   ```

4. Start Flask server:
   ```bash
   python app.py
   ```
   Server runs on http://localhost:5555

### Frontend Setup
1. Install dependencies:
   ```bash
   cd client
   npm install
   ```

2. Start React app:
   ```bash
   npm start
   ```
   App runs on http://localhost:3000

## API Endpoints

### Users
- GET `/users` - List all users
- POST `/users` - Create new user
- GET `/users/:id` - Get user by ID
- PATCH `/users/:id` - Update user
- DELETE `/users/:id` - Delete user

### Tasks
- GET `/tasks` - List all tasks
- POST `/tasks` - Create new task
- GET `/tasks/:id` - Get task by ID
- PATCH `/tasks/:id` - Update task
- DELETE `/tasks/:id` - Delete task

### Projects
- GET `/projects` - List all projects
- POST `/projects` - Create new project
- GET `/projects/:id` - Get project by ID
- PATCH `/projects/:id` - Update project
- DELETE `/projects/:id` - Delete project

### Project Collaborators
- GET `/project-collaborators` - List all collaborations
- POST `/project-collaborators` - Add collaborator to project
- GET `/project-collaborators/:id` - Get collaboration by ID
- PATCH `/project-collaborators/:id` - Update collaboration
- DELETE `/project-collaborators/:id` - Remove collaborator

## Requirements Met

✅ Flask API backend with React frontend  
✅ Three models: User, Task, Project, ProjectCollaborator  
✅ Two one-to-many relationships: User→Tasks, Project→Tasks  
✅ One many-to-many relationship: User↔Project (with role attribute)  
✅ Full CRUD for Task resource  
✅ Create/Read for all other resources  
✅ Formik forms with validation  
✅ Data type validation (string length, email format, dates)  
✅ Three client-side routes: Dashboard, Tasks, Projects  
✅ Navigation bar for route switching  
✅ Fetch API for client-server communication  

## Technologies Used

### Backend
- Flask
- SQLAlchemy
- Flask-Migrate
- Flask-CORS
- SQLAlchemy-Serializer

### Frontend
- React
- React Router
- Formik
- Yup (validation)
- CSS3

## Sample Data

PlanWise comes pre-seeded with:
- 3 users (alice, bob, charlie)
- 3 projects (Website Redesign, Mobile App, Database Migration)
- 10 tasks with various statuses and priorities
- 4 project collaborations with different roles