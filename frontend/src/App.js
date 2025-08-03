// FILE: frontend/src/App.js
// The main application router, now using the AppLayout component.
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ChakraProvider, extendTheme } from '@chakra-ui/react';
import AppLayout from './components/AppLayout';
import HomePage from './pages/HomePage';
import FutureFeaturesPage from './pages/FutureFeaturesPage';

const theme = extendTheme({
  styles: {
    global: {
      'body': {
        bg: 'gray.50',
      },
    },
  },
});

function App() {
  return (
    <ChakraProvider theme={theme}>
      <Router>
        <AppLayout>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/vision" element={<FutureFeaturesPage />} />
          </Routes>
        </AppLayout>
      </Router>
    </ChakraProvider>
  );
}

export default App;