import React, { useState } from 'react';
import { uploadCv } from '../api/cv';

const ProfileCreationPage = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [isUploading, setIsUploading] = useState(false);
  const [uploadProgress, setUploadProgress] = useState(0);
  const [uploadResponse, setUploadResponse] = useState(null);
  const [error, setError] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
    setUploadResponse(null);
    setError(null);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setError({ detail: 'Please select a file first.' });
      return;
    }

    setIsUploading(true);
    setUploadProgress(0);
    setError(null);

    try {
      const response = await uploadCv(selectedFile, (progressEvent) => {
        const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
        setUploadProgress(percentCompleted);
      });
      setUploadResponse(response);
    } catch (err) {
      setError(err);
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', maxWidth: '600px', margin: 'auto', padding: '20px' }}>
      <h2>Upload Your CV</h2>
      <p>Please upload your CV in .txt or .pdf format.</p>
      
      <div style={{ border: '1px solid #ccc', padding: '20px', borderRadius: '5px' }}>
        <label htmlFor="cv-upload" style={{ marginRight: '10px' }}>CV File:</label>
        <input id="cv-upload" type="file" onChange={handleFileChange} accept=".txt,.pdf" />
        <button onClick={handleUpload} disabled={isUploading} style={{ marginLeft: '10px' }}>
          {isUploading ? 'Uploading...' : 'Upload'}
        </button>
      </div>

      {isUploading && (
        <div style={{ marginTop: '20px' }}>
          <p id="progress-label">Progress: {uploadProgress}%</p>
          <div
            role="progressbar"
            aria-valuenow={uploadProgress}
            aria-valuemin="0"
            aria-valuemax="100"
            aria-labelledby="progress-label"
            style={{ width: '100%', backgroundColor: '#eee', borderRadius: '5px' }}
          >
            <div style={{ width: `${uploadProgress}%`, height: '20px', backgroundColor: 'green', borderRadius: '5px' }}></div>
          </div>
        </div>
      )}

      {error && (
        <div role="alert" style={{ marginTop: '20px', color: 'red', border: '1px solid red', padding: '10px', borderRadius: '5px' }}>
          <p><strong>Error:</strong> {error.detail || 'An unknown error occurred.'}</p>
        </div>
      )}

      {uploadResponse && (
        <div role="alert" style={{ marginTop: '20px', color: 'green', border: '1px solid green', padding: '10px', borderRadius: '5px' }}>
          <p><strong>Success!</strong> Your CV has been processed.</p>
          <pre style={{ backgroundColor: '#f9f9f9', padding: '10px', borderRadius: '5px' }}>
            {JSON.stringify(uploadResponse, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
};

export default ProfileCreationPage;
