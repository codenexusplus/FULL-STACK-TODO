# Data Model: Todo App with Authentication

## Entity: User

**Description**: Represents a registered user in the system

**Fields**:
- `id`: Integer (Primary Key, Auto-increment)
- `email`: String (Unique, Required, Max length: 255)
- `hashed_password`: String (Required, Max length: 255)
- `created_at`: DateTime (Auto-generated on creation)
- `updated_at`: DateTime (Auto-generated on update)
- `is_active`: Boolean (Default: true)

**Validation Rules**:
- Email must be a valid email format
- Email must be unique across all users
- Password must be hashed before storage
- Email and password are required for account creation

**Relationships**:
- One-to-Many: A User can have many Todo items (via user_id foreign key)

## Entity: Todo

**Description**: Represents a todo item in the system

**Fields**:
- `id`: Integer (Primary Key, Auto-increment)
- `title`: String (Required, Max length: 255)
- `description`: Text (Optional)
- `is_completed`: Boolean (Default: false)
- `user_id`: Integer (Foreign Key to User.id, Required)
- `created_at`: DateTime (Auto-generated on creation)
- `updated_at`: DateTime (Auto-generated on update)

**Validation Rules**:
- Title is required
- User_id must reference an existing User
- Only the owner (user_id) can modify the todo item

**Relationships**:
- Many-to-One: A Todo belongs to one User (via user_id foreign key)

## State Transitions

**Todo Entity**:
- When created: `is_completed` = false
- When completed: `is_completed` = true
- When uncompleted: `is_completed` = false

## Constraints

- Foreign key constraint on `user_id` in Todo table referencing User.id
- Unique constraint on `email` in User table
- Not null constraints on required fields
- Proper indexing on frequently queried fields (user_id in Todo table)