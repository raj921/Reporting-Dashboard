"""
Setup script for Therapy Session Dashboard
Installs dependencies and generates sample data
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def generate_sample_data():
    """Generate sample data for the dashboard"""
    print("Generating sample data...")
    try:
        subprocess.check_call([sys.executable, "data_generator.py"])
        print("✅ Sample data generated successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error generating sample data: {e}")
        return False

def main():
    """Main setup function"""
    print("🏥 Therapy Session Dashboard Setup")
    print("=" * 40)
    
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    success = True
    
    # Install requirements
    if not install_requirements():
        success = False
    
    # Generate sample data
    if success and not generate_sample_data():
        success = False
    
    if success:
        print("\n🎉 Setup completed successfully!")
        print("\nTo run the dashboard:")
        print("   streamlit run dashboard.py")
        print("\nThe dashboard will open in your web browser.")
    else:
        print("\n❌ Setup failed. Please check the error messages above.")

if __name__ == "__main__":
    main()