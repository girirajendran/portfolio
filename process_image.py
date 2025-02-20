from PIL import Image
import os

def process_profile_image(input_path, output_path):
    try:
        # Get the absolute path of the script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construct absolute paths
        input_path = os.path.join(script_dir, input_path)
        output_path = os.path.join(script_dir, output_path)
        
        print(f"Looking for image at: {input_path}")
        
        # Open the image
        img = Image.open(input_path)
        
        # Create a square crop (taking the center portion)
        width, height = img.size
        size = min(width, height)
        left = (width - size) // 2
        top = (height - size) // 2
        right = left + size
        bottom = top + size
        
        # Crop the image to square
        img = img.crop((left, top, right, bottom))
        
        # Resize to desired dimensions
        img = img.resize((400, 400), Image.LANCZOS)
        
        # Enhance the image slightly
        from PIL import ImageEnhance
        
        # Adjust contrast
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.1)
        
        # Adjust brightness
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1.05)
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Save the processed image
        img.save(output_path, quality=95, optimize=True, format='JPEG')
        print(f"Image processed and saved to: {output_path}")
        
    except FileNotFoundError:
        print(f"Error: Could not find the image file. Please make sure '{input_path}' exists.")
    except Exception as e:
        print(f"Error processing image: {str(e)}")

# Process the image
process_profile_image('profile.jpg', 'static/images/profile.jpg') 