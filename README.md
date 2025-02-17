# 🌍 Global ESG Analysis System

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![ESG Data: Refinitiv](https://img.shields.io/badge/ESG%20Data-Refinitiv-green.svg)](https://www.refinitiv.com)

## 🎯 Overview

The Global ESG Analysis System provides institutional-grade Environmental, Social, and Governance analytics powered by Refinitiv data. Get detailed ESG insights for companies across 150+ global exchanges with real-time monitoring and comprehensive reporting.

## ⚡ Quick Start

```bash
# Clone repository
git clone https://github.com/yourusername/global-esg.git

# Install dependencies
pip install -r requirements.txt

# Run the analysis system
python esg.py start
```

## 🔧 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Refinitiv API credentials
- Bing Search API credentials for AI-assisted report retrieval
- OpenAI, Claude, and Google Gemini API credentials for enhanced AI capabilities

### Step-by-Step Setup

1. **Set up your environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure your API keys**
   
Create `.env` in the project root:
```env
REFINITIV_API_KEY=your_refinitiv_key_here
BING_API_KEY=your_bing_search_key_here
OPENAI_API_KEY=your_openai_key_here
CLAUDE_API_KEY=your_claude_key_here
GEMINI_API_KEY=your_gemini_key_here
CONFIG_ENCRYPTION_KEY=your_encryption_key
```

### Example .env File
```env
REFINITIV_API_KEY=abc123xyz
BING_API_KEY=def456uvw
OPENAI_API_KEY=ghi789rst
CLAUDE_API_KEY=jkl012mno
GEMINI_API_KEY=pqr345stu
CONFIG_ENCRYPTION_KEY=vwx678yz
```

## 🌟 Features

### Core Capabilities
- **Global Coverage** 
  - 150+ exchanges worldwide
  - Multi-currency support
  - Real-time data updates

- **ESG Analytics**
  - Refinitiv scoring methodology
  - Environmental metrics
  - Social responsibility indicators
  - Governance assessment

- **Rich Reporting**
  - Interactive terminal display
  - Excel export
  - PDF reports
  - Custom formatting

- **AI-Assisted Report Retrieval**
  - Use NLP to interpret high-level queries
  - Search web for relevant ESG reports
  - Integrate with official company reports

- **Public Data Access**
  - Utilize public datasets for financial data
  - Access data without needing personal API keys

- **Web Scraping Capabilities**
  - Extract ESG data from company websites
  - Utilize machine learning for data extraction

## 📊 Usage

### AI-Assisted Report Retrieval
1. Select option 3 from the main menu
2. Enter a high-level query (e.g., "Tesla ESG report")
3. View and access the list of relevant reports

### Public Data Analysis
The system now includes the capability to analyze financial data using public datasets like Yahoo Finance, accessible through `pandas_datareader`.

### Basic Analysis
```bash
python esg.py start
```

### Symbol Formats

| Exchange | Format | Example |
|----------|---------|---------|
| NYSE/NASDAQ | SYMBOL.US | AAPL.US |
| Tokyo SE | SYMBOL.TSE | 7203.TSE |
| London SE | SYMBOL.L | BARC.L |

### Sample Output
```
┌─────────────────────┬────────┐
│ ESG Category        │ Score  │
├─────────────────────┼────────┤
│ Overall Score      │ 85.2   │
│ Environmental      │ 88.4   │
│   • Resource Use   │ 90.1   │
│   • Emissions      │ 87.2   │
│   • Innovation     │ 88.0   │
└─────────────────────┴────────┘
```

## 🤔 FAQ

### Common Issues

**Q: Why am I getting API errors?**
- Check your API key in `.env`
- Verify internet connection
- Ensure symbol format is correct

**Q: How do I export to Excel?**
1. Select option 2 from the main menu
2. Enter your symbols
3. Specify the output filename

**Q: What's the symbol format?**
- Use `SYMBOL.EXCHANGE` format
- Example: `AAPL.US`, `7203.TSE`

## 🔐 Security

- API keys are encrypted at rest
- Secure connection to Refinitiv
- No data persistence by default

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Submit a pull request

## 📞 Support

- 📧 Email: support@example.com
- 💬 Discord: [Join our server](https://discord.gg/example)
- 📚 Documentation: [Read the docs](https://docs.example.com)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by Your Organization