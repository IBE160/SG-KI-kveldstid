import axios from 'axios';

// Use environment variable for API_URL. For Vite, environment variables are exposed via import.meta.env.
// Make sure to prefix your environment variables with VITE_ (e.g., VITE_API_URL) in your .env file.
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'; // Fallback to localhost for development

const handleApiError = (error) => {
  if (axios.isAxiosError(error) && error.response) {
    // Backend errors typically have a 'detail' field
    const message = error.response.data.detail || 'An unexpected error occurred from the server.';
    return { status: error.response.status, message: message };
  } else {
    // Network errors or other unexpected issues
    return { status: 500, message: error.message || 'An unexpected network error occurred.' };
  }
};

export const uploadCv = async (file, onUploadProgress) => {
  const formData = new FormData();
  formData.append('file', file);

  try {
    const response = await axios.post(`${API_URL}/cv_documents`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      onUploadProgress,
    });
    return response.data;
  } catch (error) {
    throw handleApiError(error);
  }
};

export const getCvDocument = async (cvId) => {
  try {
    const response = await axios.get(`${API_URL}/cv_documents/${cvId}`);
    return response.data;
  } catch (error) {
    throw handleApiError(error);
  }
};

export const updateCvDocument = async (cvId, data) => {
  try {
    const response = await axios.put(`${API_URL}/cv_documents/${cvId}`, data);
    return response.data;
  } catch (error) {
    throw handleApiError(error);
  }
};
