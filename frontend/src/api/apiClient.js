// FILE: frontend/src/api/apiClient.js

import axios from 'axios';

// Backend URL from environment variables for flexibility, with a fallback for local dev
const API_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:8000/api/v1';

const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

/**
 * Finds schemes based on user profile.
 * @param {object} profileData - { age, state, occupation, income, gender }
 */
export const findSchemes = (profileData) => {
  // The endpoint path must match what's in your backend router
  return apiClient.post('/schemes/find-schemes', profileData);
};

export default apiClient;