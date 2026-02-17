# 🤖 AI Wealth Advisor

A full-stack AI-powered wealth management application with real-time stock quotes, portfolio tracking, and AI financial advice.

## Features

- 📊 Real-time stock market data
- 💬 AI financial advisor chatbot
- 📈 Portfolio tracking and analytics
- 💰 Investment recommendations
- 🔄 Live market updates

## Tech Stack

**Backend:**
- FastAPI (Python)
- PostgreSQL
- Redis
- Alpha Vantage API

**Frontend:**
- React
- Axios
- CSS3

## Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL 15+
- Redis 7+
- Homebrew (Mac)

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/ai-wealth-advisor.git
cd ai-wealth-advisor
```

### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env and add your API keys

# Initialize database
python init_db.py

# Start backend server
python main.py
```

Backend will run on http://localhost:8000

### 3. Frontend Setup
```bash
cd ../frontend

# Install dependencies
npm install

# Start development server
npm start
```

Frontend will run on http://localhost:3000

## Environment Variables

Create a `.env` file in the `backend` folder:
```env
DATABASE_URL=postgresql://postgres@localhost:5432/wealth_advisor
REDIS_URL=redis://localhost:6379
ALPHA_VANTAGE_API_KEY=your_key_here
SECRET_KEY=your-secret-key
ENVIRONMENT=development
LOG_LEVEL=INFO
```

## API Endpoints

### Health Check
```
GET /health
```

### Get Stock Quote
```
GET /api/v1/quote/{ticker}
```

### Chat with AI Advisor
```
POST /api/v1/chat
Body: {"message": "your question"}
```

## Database Setup

The application uses PostgreSQL. Tables are created automatically when you run `init_db.py`.

**Tables:**
- `users` - User accounts
- `portfolios` - User portfolios
- `holdings` - Stock holdings
- `transactions` - Buy/sell transactions

## Getting API Keys

1. **Alpha Vantage** (Stock Data):
   - Visit: https://www.alphavantage.co/support/#api-key
   - Free tier: 25 requests/day

## Project Structure
```
ai-wealth-advisor/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── init_db.py           # Database initialization
│   ├── requirements.txt     # Python dependencies
│   └── .env                 # Environment variables
├── frontend/
│   ├── src/
│   │   ├── App.js          # Main React component
│   │   └── App.css         # Styles
│   ├── public/
│   └── package.json        # Node dependencies
└── README.md
```

## Usage

1. **View Stock Quotes**: Enter a ticker symbol (e.g., AAPL, MSFT) and get real-time price data
2. **Chat with AI Advisor**: Ask questions about retirement planning, portfolio allocation, investing strategies
3. **Track Portfolio**: Add your holdings and monitor performance

## Features Coming Soon

- [ ] User authentication
- [ ] Portfolio analytics dashboard
- [ ] Tax-loss harvesting recommendations
- [ ] Retirement planning calculator
- [ ] Mobile app (React Native)
- [ ] Real-time portfolio updates
- [ ] Advanced AI with Claude integration

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Acknowledgments

- Alpha Vantage for market data API
- FastAPI for the amazing Python framework
- React team for the frontend library

## Support

For support, email your-email@example.com or open an issue.

## Screenshots


