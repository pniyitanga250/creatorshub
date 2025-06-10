from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from services.storage_service import SupabaseStorageService
import json

def upload_file(request):
    if request.method == 'POST':
        if request.FILES.get('file'):
            file = request.FILES['file']
            storage_service = SupabaseStorageService(use_admin_client=True)  # Use admin for uploads
            
            # Upload to 'media' bucket with custom folder
            result = storage_service.upload_file(
                file, 
                folder='user_uploads',  # Will be stored as media/user_uploads/filename
                filename=None  # Auto-generate unique filename
            )
            
            if result['success']:
                messages.success(request, f'File uploaded successfully! URL: {result["public_url"]}')
                
                # If this is an AJAX request, return JSON
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({
                        'success': True,
                        'file_url': result['public_url'],
                        'file_path': result['file_path']
                    })
            else:
                messages.error(request, f'Upload failed: {result["error"]}')
                
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({
                        'success': False,
                        'error': result['error']
                    })
    
    return render(request, 'upload.html')

def delete_file(request):
    if request.method == 'POST':
        file_path = request.POST.get('file_path')
        if file_path:
            storage_service = SupabaseStorageService(use_admin_client=True)
            result = storage_service.delete_file(file_path)
            
            if result['success']:
                messages.success(request, 'File deleted successfully!')
            else:
                messages.error(request, f'Delete failed: {result["error"]}')
    
    return redirect('upload_file')

def list_files(request):
    storage_service = SupabaseStorageService()
    result = storage_service.list_files(folder='user_uploads')
    
    context = {
        'files': result.get('files', []) if result['success'] else [],
        'error': result.get('error') if not result['success'] else None
    }
    
    return render(request, 'file_list.html', context)