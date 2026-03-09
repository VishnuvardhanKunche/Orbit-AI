import os
import sys

def check_env():
    print("--- [Orbit AI Diagnostic] ---")
    
    # 1. Check Python Version
    print(f"Python Version: {sys.version}")
    
    # 2. Check dependencies
    try:
        import fastapi
        import uvicorn
        import langchain
        import langchain_text_splitters
        import langgraph
        import google.generativeai as genai
        print("[OK] Core dependencies found.")
    except ImportError as e:
        print(f"[ERROR] Missing dependency: {e.name}. Run: pip install -r requirements.txt")
        return

    # 3. Check .env file
    root_env = os.path.exists(".env")
    backend_env = os.path.exists("backend/.env")
    
    if root_env:
        print("[OK] Found .env in project root.")
    elif backend_env:
        print("[OK] Found .env in backend/ folder.")
    else:
        print("[ERROR] No .env file found! Please create one in the root folder.")
        return

    # 4. Check API Keys
    from dotenv import load_dotenv
    load_dotenv(".env")
    load_dotenv("backend/.env")
    
    keys = ["GEMINI_API_KEY", "TAVILY_API_KEY", "WEATHER_API_KEY"]
    for key in keys:
        val = os.getenv(key)
        if val:
            print(f"[OK] {key} is set.")
        else:
            print(f"[ERROR] {key} is MISSING in .env!")

    print("\nEnvironment looks good! Try starting the server with:")
    print("cd backend")
    print("python main.py")

if __name__ == "__main__":
    check_env()
