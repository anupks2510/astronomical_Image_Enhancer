import cv2
import os
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer
from django.conf import settings

def enhance_image(img_path):
    """Enhance image using Real-ESRGAN model and return dimensions"""
    try:
        # Model configuration
        model_path = os.path.join(settings.BASE_DIR, 'weights', 'RealESRGAN_x4plus.pth')
        output_dir = os.path.join(settings.MEDIA_ROOT, 'enhanced')
        
        # Create model components
        model = RRDBNet(
            num_in_ch=3, num_out_ch=3,
            num_feat=64, num_block=23,
            num_grow_ch=32, scale=4
        )
        
        upsampler = RealESRGANer(
            scale=4,
            model_path=model_path,
            model=model,
            tile=0,
            tile_pad=10,
            pre_pad=0,
            half=False
        )

        # Process image
        img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        if img is None:
            raise ValueError("Could not read input image")
            
        output, _ = upsampler.enhance(img, outscale=4)

        # Get enhanced dimensions
        enhanced_height, enhanced_width = output.shape[:2]

        # Save output
        os.makedirs(output_dir, exist_ok=True)
        filename = f"enhanced_{os.path.basename(img_path)}"
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, output)

        return output_path, enhanced_width, enhanced_height

    except Exception as e:
        raise RuntimeError(f"Enhancement failed: {str(e)}")