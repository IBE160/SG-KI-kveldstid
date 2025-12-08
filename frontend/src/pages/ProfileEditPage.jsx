import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom'; // Assuming react-router-dom is used for routing
import { getCvDocument, updateCvDocument } from '../api/cv';

const ProfileEditPage = () => {
  const { cvId } = useParams(); // Get cvId from URL params
  const [cvData, setCvData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isSaving, setIsSaving] = useState(false);
  const [saveSuccess, setSaveSuccess] = useState(false);

  useEffect(() => {
    const fetchCvData = async () => {
      try {
        setLoading(true);
        const data = await getCvDocument(cvId);
        setCvData(data);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };
    fetchCvData();
  }, [cvId]);

  const handleChange = (e, section, field, index = null) => {
    const { value } = e.target;
    setCvData(prevData => {
      const newData = { ...prevData };
      if (index !== null && Array.isArray(newData.parsed_sections_json[section])) {
        newData.parsed_sections_json[section][index][field] = value;
      } else {
        newData.parsed_sections_json[section][field] = value;
      }
      return newData;
    });
  };

  const handleSave = async () => {
    setIsSaving(true);
    setSaveSuccess(false);
    setError(null);
    try {
      // Only send parsed_sections_json for update
      await updateCvDocument(cvId, { parsed_sections_json: cvData.parsed_sections_json });
      setSaveSuccess(true);
    } catch (err) {
      setError(err);
    } finally {
      setIsSaving(false);
    }
  };

  if (loading) {
    return <div style={{ fontFamily: 'Arial, sans-serif', padding: '20px' }}>Loading CV data...</div>;
  }

  if (error) {
    return (
      <div role="alert" style={{ fontFamily: 'Arial, sans-serif', padding: '20px', color: 'red' }}>
        Error: {error.message || 'Failed to load CV data.'}
      </div>
    );
  }

  if (!cvData || !cvData.parsed_sections_json) {
    return <div style={{ fontFamily: 'Arial, sans-serif', padding: '20px' }}>No parsed CV data available for editing.</div>;
  }

  const { parsed_sections_json } = cvData;

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', maxWidth: '800px', margin: 'auto', padding: '20px' }}>
      <h2>Edit Profile - CV ID: {cvId}</h2>

      {saveSuccess && (
        <div role="alert" style={{ marginTop: '20px', color: 'green', border: '1px solid green', padding: '10px', borderRadius: '5px' }}>
          <p><strong>Success!</strong> Your profile changes have been saved.</p>
        </div>
      )}

      {error && (
        <div role="alert" style={{ marginTop: '20px', color: 'red', border: '1px solid red', padding: '10px', borderRadius: '5px' }}>
          <p><strong>Error:</strong> {error.message || 'An unknown error occurred during saving.'}</p>
        </div>
      )}

      {/* Contact Info */}
      {parsed_sections_json.contact_info && (
        <div style={{ marginBottom: '20px', border: '1px solid #eee', padding: '15px', borderRadius: '5px' }}>
          <h3>Contact Information</h3>
          {Object.entries(parsed_sections_json.contact_info).map(([key, value]) => (
            <div key={key} style={{ marginBottom: '10px' }}>
              <label htmlFor={`contact-${key}`} style={{ display: 'block', marginBottom: '5px' }}>{key.replace(/_/g, ' ')}:</label>
              <input
                id={`contact-${key}`}
                type="text"
                value={value || ''}
                onChange={(e) => handleChange(e, 'contact_info', key)}
                style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
              />
            </div>
          ))}
        </div>
      )}

      {/* Summary */}
      {parsed_sections_json.summary && (
        <div style={{ marginBottom: '20px', border: '1px solid #eee', padding: '15px', borderRadius: '5px' }}>
          <h3>Summary</h3>
          <label htmlFor="summary" style={{ display: 'block', marginBottom: '5px' }}>Summary:</label>
          <textarea
            id="summary"
            value={parsed_sections_json.summary || ''}
            onChange={(e) => handleChange(e, 'summary', 'summary')} // 'summary' is both section and field for textarea
            style={{ width: '100%', padding: '8px', boxSizing: 'border-box', minHeight: '100px' }}
          />
        </div>
      )}

      {/* Experience */}
      {parsed_sections_json.experience && parsed_sections_json.experience.length > 0 && (
        <div style={{ marginBottom: '20px', border: '1px solid #eee', padding: '15px', borderRadius: '5px' }}>
          <h3>Experience</h3>
          {parsed_sections_json.experience.map((exp, index) => (
            <div key={index} style={{ marginBottom: '15px', borderBottom: '1px dashed #ccc', paddingBottom: '15px' }}>
              <h4>Job {index + 1}</h4>
              {Object.entries(exp).map(([key, value]) => (
                <div key={key} style={{ marginBottom: '10px' }}>
                  <label htmlFor={`exp-${index}-${key}`} style={{ display: 'block', marginBottom: '5px' }}>{key.replace(/_/g, ' ')}:</label>
                  <input
                    id={`exp-${index}-${key}`}
                    type="text"
                    value={value || ''}
                    onChange={(e) => handleChange(e, 'experience', key, index)}
                    style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
                  />
                </div>
              ))}
            </div>
          ))}
        </div>
      )}

      {/* Education */}
      {parsed_sections_json.education && parsed_sections_json.education.length > 0 && (
        <div style={{ marginBottom: '20px', border: '1px solid #eee', padding: '15px', borderRadius: '5px' }}>
          <h3>Education</h3>
          {parsed_sections_json.education.map((edu, index) => (
            <div key={index} style={{ marginBottom: '15px', borderBottom: '1px dashed #ccc', paddingBottom: '15px' }}>
              <h4>Degree {index + 1}</h4>
              {Object.entries(edu).map(([key, value]) => (
                <div key={key} style={{ marginBottom: '10px' }}>
                  <label htmlFor={`edu-${index}-${key}`} style={{ display: 'block', marginBottom: '5px' }}>{key.replace(/_/g, ' ')}:</label>
                  <input
                    id={`edu-${index}-${key}`}
                    type="text"
                    value={value || ''}
                    onChange={(e) => handleChange(e, 'education', key, index)}
                    style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
                  />
                </div>
              ))}
            </div>
          ))}
        </div>
      )}

      {/* Skills */}
      {parsed_sections_json.skills && parsed_sections_json.skills.length > 0 && (
        <div style={{ marginBottom: '20px', border: '1px solid #eee', padding: '15px', borderRadius: '5px' }}>
          <h3>Skills</h3>
          <label htmlFor="skills" style={{ display: 'block', marginBottom: '5px' }}>Skills (comma separated):</label>
          <input
            id="skills"
            type="text"
            value={Array.isArray(parsed_sections_json.skills) ? parsed_sections_json.skills.join(', ') : ''}
            onChange={(e) => setCvData(prevData => ({
              ...prevData,
              parsed_sections_json: {
                ...prevData.parsed_sections_json,
                skills: e.target.value.split(',').map(s => s.trim())
              }
            }))}
            style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
          />
        </div>
      )}

      <button onClick={handleSave} disabled={isSaving} style={{ padding: '10px 20px', fontSize: '16px', cursor: 'pointer' }}>
        {isSaving ? 'Saving...' : 'Save Changes'}
      </button>
    </div>
  );
};

export default ProfileEditPage;
