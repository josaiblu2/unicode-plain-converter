# 🔠 Unicode Converter SaaS

A professional, minimal web platform designed to seamlessly and bidirectionally convert standard ASCII text into Unicode Mathematical Alphanumeric styled characters (e.g., Bold, Italic, Script, Fraktur) and vice-versa. 

Built with a fast Python FastAPI backend and an ultra-light Astro.js + Tailwind CSS frontend in a cohesive Monorepo architecture. 

## ✨ Features
- **Bidirectional Engine**: Converts plain text to stylized Unicode variants (for social media, marketing, or design) and safely translates styled Unicode back into searchable, clean ASCII text.
- **Strict QA Validated**: Backed by formal NFKD normalization fallbacks and exact Code Point verification.
- **Corporate Tech Aesthetic**: A sleek, clean, centered, and accessible single-column user interface.

## 🚀 Quick Start (Windows)

The easiest way to boot up both the API server and the Frontend web interface is using the provided batch script:

1. Open your File Explorer and navigate to the root folder `c:\Proyectos\unicode-plain-converter`.
2. Double-click the **`start.bat`** file.
3. Two console windows will automatically open (one for the backend on port 8003, one for the frontend). Let them run in the background.
4. Open your browser and go to: **[http://localhost:4321](http://localhost:4321)**

### Manual Start
If you prefer to start the servers manually:

**1. Start the FastAPI Backend:**
```bash
python -m uvicorn src.main:app --port 8003 --reload
```

**2. Start the Astro Frontend:**
*(In a new terminal)*
```bash
cd frontend
npm run dev
```

## 📐 Architecture & Quality Assurance
- **Requirement Design**: Learn more about the core architecture and UI aesthetic decisions in [`Requirement_Design.md`](./Requirement_Design.md).
- **QA Strategy**: We strictly maintain regressions via our Golden Test Cases approach. See [`tests/test_cases.md`](./tests/test_cases.md) for more info on Hex-level validation.
