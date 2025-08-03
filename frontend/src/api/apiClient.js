// FILE: frontend/src/api/apiClient.js

import axios from 'axios';

// Get the root URL of the backend. Fallback to localhost for local development.
const API_ROOT = process.env.REACT_APP_API_URL || 'http://127.0.0.1:8000';

// The specific versioned endpoint for your API
const API_URL = `${API_ROOT}/api/v1`;

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
  // The path here is now relative to `/api/v1`
  return apiClient.post('/schemes/find-schemes', profileData);
};

export default apiClient;