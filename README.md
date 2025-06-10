# File Management App with Supabase Storage

This Django web application allows users to upload, list, and delete files using Supabase as the backend storage service.

## Features

- Upload files to Supabase storage under the `user_uploads` folder.
- List all uploaded files.
- Delete files from Supabase storage.
- Supports both standard form submissions and AJAX requests for file uploads.
- Provides user feedback via Django messages framework.

## Setup

1. Ensure you have Python and Django installed.
2. Configure your Supabase credentials in the `services/storage_service.py` file.
3. Install required Python packages listed in `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```
4. Run Django migrations and start the development server:
   ```
   python manage.py migrate
   python manage.py runserver
   ```

## Usage

- Navigate to the upload page to upload files.
- View the list of uploaded files on the file list page.
- Delete files using the provided interface.

## Project Structure

- `app/views.py`: Contains views for uploading, deleting, and listing files.
- `services/storage_service.py`: Handles interaction with Supabase storage.
- `app/templates/`: Contains HTML templates for upload and file list pages.

## Notes

- The app uses Supabase's admin client for upload and delete operations.
- Uploaded files are stored in the `user_uploads` folder within the Supabase storage bucket.
- my supabase uses [match] as my database and storage 
