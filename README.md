# SchemeSavvy

![SchemeSavvy Logo](https://via.placeholder.com/150x150.png?text=SchemeSavvy)

An AI-powered platform to help citizens find and apply for government schemes they're eligible for.

## 🌟 Overview

SchemeSavvy is a web application designed to bridge the gap between citizens and government welfare schemes. Many citizens are unaware of the numerous benefits they're eligible for, and the application process can be complex. SchemeSavvy simplifies this by:

1. Matching users with schemes based on their profile
2. Providing clear information about benefits and eligibility
3. Guiding users through the application process
4. Building a supportive community of applicants

## 🚀 Features

### Core Features

- **Personalized Scheme Matching**: Answer a few questions about yourself to discover schemes you're eligible for
- **Scheme Discovery**: Browse and search through a comprehensive database of government schemes
- **Document Checklist**: Get a clear list of documents required for each application
- **Official Portal Links**: Direct links to official government portals for application

### Planned Features

- **AI Chatbot**: Get instant answers to your questions about schemes and applications
- **Document Scanner**: Scan and verify your documents before applying
- **Community Forum**: Connect with others applying for the same schemes
- **Application Tracking**: Track the status of your applications in one place

## 🛠️ Tech Stack

### Frontend
- React.js
- Chakra UI for responsive design
- React Router for navigation
- Axios for API communication

### Backend
- FastAPI (Python)
- Pydantic for data validation
- SQLAlchemy (conceptual model for future database integration)

### Deployment
- GitHub Actions for CI/CD
- Backend: Render
- Frontend: Netlify

## 📋 Project Structure

```
├── .github/workflows/      # CI/CD pipelines
├── backend/                # FastAPI server
│   ├── api/                # API endpoints
│   ├── core/               # Core configurations
│   ├── models/             # Database models
│   └── services/           # Business logic
├── data/                   # Scheme data and scripts
├── docs/                   # Documentation
└── frontend/              # React application
    ├── public/             # Static files
    └── src/                # Source code
        ├── api/            # API client
        ├── components/     # Reusable components
        ├── features/       # Feature modules
        └── pages/          # Page components
```

## 🚦 Getting Started

### Prerequisites

- Node.js (v14+)
- Python (v3.8+)
- npm or yarn

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app:app --reload
```

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
# or
yarn install

# Start the development server
npm start
# or
yarn start
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Team

- [Your Name](https://github.com/yourusername)
- [Team Member 2](https://github.com/teammember2)
- [Team Member 3](https://github.com/teammember3)

## 🙏 Acknowledgements

- Government of India for providing open data on schemes
- [Chakra UI](https://chakra-ui.com/) for the beautiful components
- [FastAPI](https://fastapi.tiangolo.com/) for the efficient backend framework