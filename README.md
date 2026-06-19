# NutriScan AI

NutriScan AI is a premium, full-stack React Native Expo mobile application and Node.js backend. It leverages OCR, NLP, and a custom health scoring algorithm to analyze food labels, calculate personalized health scores, detect allergens, suggest healthier alternatives, and provide an AI-powered chat assistant.

## Features
- **Smart Scanning**: Extract ingredients and nutrition facts.
- **Personalized Scoring**: Adjusts product health scores based on user BMI, health conditions, and allergies.
- **Product Comparison**: Compare multiple products side-by-side to easily locate the healthiest option.
- **AI Assistant**: Conversational bot embedded right into the result screen.
- **Premium UI**: Dark-mode glassmorphism styling, SVG dynamic rings, and fluid 60FPS Reanimated transitions.

## Prerequisites
- Node.js (v18+)
- MongoDB instance (local or Atlas)
- OpenAI API Key (optional, defaults to intelligent mock fallback)
- Expo CLI

## Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   npm install
   ```
2. Create a `.env` file in the `backend/` directory:
   ```env
   PORT=5000
   MONGO_URI=mongodb://127.0.0.1:27017/food_label
   JWT_SECRET=supersecret123
   OPENAI_API_KEY=your_key_here
   CLIENT_URL=http://localhost:8081
   ```
3. Start the server:
   ```bash
   npm start
   ```

## Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   npm install --legacy-peer-deps
   ```
2. The `api.js` service automatically routes requests to `http://localhost:5000/api` for Web and iOS simulators, and `10.0.2.2` for Android emulators. If you are using a physical device, update `getBaseURL` in `src/services/api.js` to your computer's LAN IP.
3. Start the Expo development server:
   ```bash
   npx expo start
   ```
4. Press `w` to view the web version, `a` for Android, or scan the QR code with your iPhone's camera / Expo Go app.

## Project Architecture
- `backend/src/routes/` - Express routers mapping to endpoints.
- `backend/src/services/` - Business logic (Scoring, NLP, External OpenFoodAPI).
- `frontend/src/components/` - Reusable UI components (GlassCard, AnimatedRing).
- `frontend/src/screens/` - Major application screens linked via React Navigation.
- `frontend/src/store/` - Centralized `useApp()` context for state management.
