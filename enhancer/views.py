from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .forms import ImageUploadForm
from .realesrgan_utils import enhance_image
from .image_analysis import analyze_astronomical_image  # New import
import cv2
import logging
import os

logger = logging.getLogger(__name__)

def index(request):
    context = {'form': ImageUploadForm()}
    
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            fs = FileSystemStorage()
            filename = None
            enhanced_path = None
            
            try:
                # Save original image
                image_file = form.cleaned_data['image']
                filename = fs.save(image_file.name, image_file)
                original_path = fs.path(filename)
                logger.debug(f"Original path: {original_path}")

                # Get original dimensions
                original_img = cv2.imread(original_path)
                if original_img is None:
                    raise ValueError("Could not read uploaded image file")
                
                original_height, original_width = original_img.shape[:2]
                logger.debug(f"Original dimensions: {original_width}x{original_height}")

                # Enhance image
                enhanced_path, enhanced_width, enhanced_height = enhance_image(original_path)
                logger.debug(f"Enhanced path: {enhanced_path}")
                logger.debug(f"Enhanced dimensions: {enhanced_width}x{enhanced_height}")

                # Generate AI analysis
                analysis = None
                try:
                    analysis = analyze_astronomical_image(enhanced_path)
                except Exception as e:
                    logger.error(f"AI analysis failed: {str(e)}", exc_info=True)
                    messages.warning(request, 'Enhanced image created, but analysis failed')

                # Build URLs and context
                enhanced_filename = os.path.basename(enhanced_path)
                enhanced_url = fs.url(os.path.join('enhanced', enhanced_filename))
                
                context.update({
                    'original': fs.url(filename),
                    'enhanced': enhanced_url,
                    'original_width': original_width,
                    'original_height': original_height,
                    'enhanced_width': enhanced_width,
                    'enhanced_height': enhanced_height,
                    'analysis': analysis  # Add analysis to context
                })
                messages.success(request, 'Image enhanced successfully!')

            except Exception as e:
                logger.error(f"Error processing image: {str(e)}", exc_info=True)
                messages.error(request, f'Error: {str(e)}')
                
                # Cleanup
                if filename and fs.exists(filename):
                    fs.delete(filename)
                if enhanced_path and os.path.exists(enhanced_path):
                    os.remove(enhanced_path)

    return render(request, 'enhancer/index.html', context)