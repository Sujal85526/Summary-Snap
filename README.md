# 📸 Summary Snap

An AI-powered application that instantly captures the essence of PDF documents through intelligent summarization and enables interactive Q&A conversations using Google Gemini and LangChain.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.38.0-red.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.3.1-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

- **📝 Instant Summarization**: Snap comprehensive summaries of PDF documents using Google Gemini's advanced language model
- **💬 Interactive Chat**: Ask questions about your PDF and get context-aware answers
- **🔍 Semantic Search**: Uses ChromaDB vector database for intelligent document retrieval
- **🎯 Context-Aware Responses**: Maintains chat history for natural conversations
- **📥 Export Options**: Download summaries as text files
- **🔒 Secure**: API keys handled securely with environment variables
- **🎨 Clean UI**: Modern, intuitive interface built with Streamlit

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **LangChain** | Framework for building LLM applications |
| **Google Gemini** | Large Language Model (Free API tier) |
| **ChromaDB** | Vector database for semantic search |
| **Streamlit** | Web application framework |
| **PyPDF** | PDF text extraction |

## 📋 Prerequisites

- Python 3.10 or higher
- Google Gemini API key (free from [ai.google.dev](https://ai.google.dev))
- pip package manager

## 🚀 Installation

### 1. Clone the Repository

git clone https://github.com/yourusername/summary-snap.git
cd summary-snap


### 2. Create Virtual Environment

### 3. Install Dependencies

### 4. Set Up Environment Variables

Create a `.env` file in the project root:

**Get your free API key:**
1. Visit [Google AI Studio](https://ai.google.dev/)
2. Sign in with your Google account
3. Click "Get API Key"
4. Copy and paste into `.env` file

### Docker Deployment

#### Using Docker

1. Build the image:

2. Run the container:

3. Access at `http://localhost:8501`

#### Using Docker Compose

1. Make sure `.env` file has your API key
2. Run:
3. Access at `http://localhost:8501`


## 📂 Project Structure

```
summary-snap/
├── .github/
│   └── workflows/
│       └── docker-deploy.yml    ← New file
├── app.py
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

### Key Components

1. **PDF Processing**: PyPDFLoader extracts text from uploaded PDFs
2. **Text Splitting**: Documents are split into manageable chunks with overlap
3. **Embeddings**: Google's embedding model converts text to vectors
4. **Vector Store**: ChromaDB stores and searches embeddings efficiently
5. **Retrieval**: Semantic search finds most relevant chunks for questions
6. **Generation**: Gemini generates summaries and answers based on context
7. **Memory**: Conversation history maintained for contextual responses

## 🎯 Use Cases

- **Research**: Quickly understand lengthy academic papers
- **Legal**: Summarize legal documents and contracts
- **Business**: Extract insights from reports and presentations
- **Education**: Study materials and textbooks more efficiently
- **Documentation**: Navigate technical documentation faster

## 🔐 Security & Privacy

- API keys stored securely in `.env` file (never committed to Git)
- PDFs processed temporarily and not stored permanently
- All processing happens locally except API calls to Gemini
- No data retention on external servers

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'dotenv'`

**Issue**: Protobuf version conflict

**Issue**: ChromaDB installation fails


**Issue**: API key not working
- Ensure no extra spaces in `.env` file
- Verify key is valid at [ai.google.dev](https://ai.google.dev)
- Check you haven't exceeded free tier limits (25 requests/day)

## 📈 Future Enhancements

- [ ] Support for multiple PDF uploads
- [ ] Export summaries as PDF with formatting
- [ ] Support for images and tables in PDFs
- [ ] Multi-language support
- [ ] Docker containerization
- [ ] Cloud deployment (AWS/GCP/Azure)
- [ ] User authentication
- [ ] Chat history persistence
- [ ] Batch processing for multiple documents

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- [LangChain](https://python.langchain.com/) for the amazing framework
- [Google Gemini](https://ai.google.dev/) for providing free API access
- [Streamlit](https://streamlit.io/) for the intuitive UI framework
- [ChromaDB](https://www.trychroma.com/) for the vector database

## 👤 Author

**Sujal Singh Rajput**

- GitHub: [Sujal85526](https://github.com/Sujal85526)

## 📞 Support

If you have any questions or run into issues, please:
- Open an issue on GitHub
- Contact me at your.email@example.com

---

⭐ **Star this repository if you found it helpful!**

**SummarySnap** - Snap the essence of any document instantly! 📸

Built with ❤️ using LangChain and Google Gemini



