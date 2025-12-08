import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { MemoryRouter, Route, Routes } from 'react-router-dom';
import ProfileEditPage from './ProfileEditPage';
import * as cvApi from '../api/cv'; // Import all exports from cv.js to mock

// Mock the API functions
jest.mock('../api/cv', () => ({
  getCvDocument: jest.fn(),
  updateCvDocument: jest.fn(),
}));

const mockCvData = {
  id: 1,
  filename: "test.pdf",
  content_type: "application/pdf",
  raw_text_content: "raw text",
  s3_file_path: "s3://mock-bucket/test.pdf",
  upload_date: "2023-01-01T00:00:00Z",
  parsed_sections_json: {
    contact_info: { name: "Test User", email: "test@example.com", phone: "123-456-7890" },
    summary: "A brief summary.",
    experience: [{ title: "Dev", company: "ABC", dates: "2020-2023", description: "Worked here" }],
    education: [{ degree: "CS", university: "XYZ", year: 2023 }],
    skills: ["React", "Node", "Python"]
  }
};

describe('ProfileEditPage', () => {
  beforeEach(() => {
    // Reset mocks before each test
    cvApi.getCvDocument.mockReset();
    cvApi.updateCvDocument.mockReset();
  });

  const renderWithRouter = (cvId = '1') => {
    return render(
      <MemoryRouter initialEntries={[`/profile/${cvId}/edit`]}>
        <Routes>
          <Route path="/profile/:cvId/edit" element={<ProfileEditPage />} />
        </Routes>
      </MemoryRouter>
    );
  };

  test('displays loading state initially', () => {
    cvApi.getCvDocument.mockReturnValueOnce(new Promise(() => {})); // Never resolve to keep it loading
    renderWithRouter();
    expect(screen.getByText(/loading cv data/i)).toBeInTheDocument();
  });

  test('displays error message if fetching fails', async () => {
    cvApi.getCvDocument.mockRejectedValueOnce({ message: 'Failed to fetch CV' });
    renderWithRouter();
    await waitFor(() => {
      expect(screen.getByRole('alert')).toBeInTheDocument();
      expect(screen.getByText(/error: failed to fetch cv/i)).toBeInTheDocument();
    });
  });

  test('displays no data message if parsed_sections_json is empty', async () => {
    cvApi.getCvDocument.mockResolvedValueOnce({ ...mockCvData, parsed_sections_json: null });
    renderWithRouter();
    await waitFor(() => {
      expect(screen.getByText(/no parsed cv data available for editing/i)).toBeInTheDocument();
    });
  });

  test('renders CV data correctly and allows editing', async () => {
    cvApi.getCvDocument.mockResolvedValueOnce(mockCvData);
    renderWithRouter();

    await waitFor(() => {
      expect(screen.getByLabelText(/name:/i)).toHaveValue('Test User');
      expect(screen.getByLabelText(/email:/i)).toHaveValue('test@example.com');
      expect(screen.getByLabelText(/summary:/i)).toHaveValue('A brief summary.');
      expect(screen.getByLabelText(/job title:/i)).toHaveValue('Dev');
      expect(screen.getByLabelText(/degree:/i)).toHaveValue('CS');
      expect(screen.getByLabelText(/skills \(comma separated\):/i)).toHaveValue('React, Node, Python');
    });

    const nameInput = screen.getByLabelText(/name:/i);
    await userEvent.clear(nameInput);
    await userEvent.type(nameInput, 'New Name');
    expect(nameInput).toHaveValue('New Name');

    const saveButton = screen.getByRole('button', { name: /save changes/i });
    cvApi.updateCvDocument.mockResolvedValueOnce({ ...mockCvData, parsed_sections_json: { ...mockCvData.parsed_sections_json, contact_info: { ...mockCvData.parsed_sections_json.contact_info, name: 'New Name' } } });
    
    await userEvent.click(saveButton);

    await waitFor(() => {
      expect(cvApi.updateCvDocument).toHaveBeenCalledWith('1', { parsed_sections_json: expect.objectContaining({ contact_info: expect.objectContaining({ name: 'New Name' }) }) });
      expect(screen.getByText(/success! your profile changes have been saved./i)).toBeInTheDocument();
    });
  });

  test('displays error message if saving fails', async () => {
    cvApi.getCvDocument.mockResolvedValueOnce(mockCvData);
    renderWithRouter();

    await waitFor(() => {
      expect(screen.getByLabelText(/name:/i)).toHaveValue('Test User');
    });

    const saveButton = screen.getByRole('button', { name: /save changes/i });
    cvApi.updateCvDocument.mockRejectedValueOnce({ message: 'Failed to save' });

    await userEvent.click(saveButton);

    await waitFor(() => {
      expect(screen.getByRole('alert')).toBeInTheDocument();
      expect(screen.getByText(/error: failed to save/i)).toBeInTheDocument();
    });
  });
});
