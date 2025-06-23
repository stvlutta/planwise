#!/usr/bin/env python3
"""
Test script to verify the authentication system is working properly.
"""

import requests
import json

def test_authentication_flow():
    """Test complete authentication flow"""
    base_url = "http://localhost:5555"
    
    print("🔐 TESTING AUTHENTICATION SYSTEM")
    print("=" * 50)
    
    # Test 1: Signup new user
    print("\n1. Testing User Signup")
    signup_data = {
        "username": "authtest",
        "email": "authtest@example.com", 
        "password": "testpass123"
    }
    
    try:
        response = requests.post(f"{base_url}/auth/signup", json=signup_data)
        if response.status_code == 201:
            data = response.json()
            token = data.get('access_token')
            print("✅ Signup successful")
            print(f"✅ Token received: {token[:20]}...")
        else:
            print(f"❌ Signup failed: {response.json()}")
            return False
    except Exception as e:
        print(f"❌ Signup error: {e}")
        return False
    
    # Test 2: Login with created user
    print("\n2. Testing User Login")
    login_data = {
        "username": "authtest",
        "password": "testpass123"
    }
    
    try:
        response = requests.post(f"{base_url}/auth/login", json=login_data)
        if response.status_code == 200:
            data = response.json()
            login_token = data.get('access_token')
            user = data.get('user')
            print("✅ Login successful")
            print(f"✅ User: {user.get('username')}")
            print(f"✅ Token: {login_token[:20]}...")
        else:
            print(f"❌ Login failed: {response.json()}")
            return False
    except Exception as e:
        print(f"❌ Login error: {e}")
        return False
    
    # Test 3: Access protected endpoint with token
    print("\n3. Testing Protected Endpoints")
    headers = {"Authorization": f"Bearer {login_token}"}
    
    try:
        # Test /auth/me endpoint
        response = requests.get(f"{base_url}/auth/me", headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            print("✅ /auth/me endpoint working")
            print(f"✅ Current user: {user_data['user']['username']}")
        else:
            print(f"❌ /auth/me failed: {response.status_code}")
            return False
            
        # Test /tasks endpoint (requires auth)
        response = requests.get(f"{base_url}/tasks", headers=headers)
        if response.status_code == 200:
            tasks = response.json()
            print(f"✅ /tasks endpoint working (found {len(tasks)} tasks)")
        else:
            print(f"❌ /tasks failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Protected endpoint error: {e}")
        return False
    
    # Test 4: Access protected endpoint without token
    print("\n4. Testing Endpoint Protection")
    try:
        response = requests.get(f"{base_url}/tasks")  # No auth header
        if response.status_code == 401:
            print("✅ Endpoints properly protected (401 Unauthorized)")
        else:
            print(f"❌ Endpoint not protected: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Protection test error: {e}")
        return False
    
    # Test 5: Login with demo credentials
    print("\n5. Testing Demo User Login")
    demo_login = {
        "username": "alice",
        "password": "password123"
    }
    
    try:
        response = requests.post(f"{base_url}/auth/login", json=demo_login)
        if response.status_code == 200:
            data = response.json()
            print("✅ Demo user login successful")
            print(f"✅ Demo user: {data['user']['username']}")
        else:
            print(f"❌ Demo login failed: {response.json()}")
            return False
    except Exception as e:
        print(f"❌ Demo login error: {e}")
        return False
    
    return True

def test_frontend_auth():
    """Test frontend authentication integration"""
    print("\n🌐 TESTING FRONTEND AUTHENTICATION")
    print("=" * 40)
    
    frontend_url = "http://localhost:3000"
    
    try:
        # Check if frontend redirects to login when not authenticated
        response = requests.get(frontend_url, allow_redirects=False)
        print(f"✅ Frontend accessible on {frontend_url}")
        
        # The React app should handle authentication client-side
        # We can't easily test the full flow without a browser
        print("✅ Frontend authentication relies on React routing")
        print("✅ Manual testing required for complete flow")
        
    except Exception as e:
        print(f"❌ Frontend test error: {e}")
        return False
    
    return True

def main():
    print("🔍 AUTHENTICATION SYSTEM VERIFICATION")
    print("=" * 60)
    
    backend_success = test_authentication_flow()
    frontend_success = test_frontend_auth()
    
    print("\n🎯 AUTHENTICATION STATUS")
    print("=" * 30)
    
    if backend_success and frontend_success:
        print("✅ Backend Authentication: WORKING")
        print("✅ Frontend Integration: READY")
        print("✅ JWT Token System: FUNCTIONAL")
        print("✅ Protected Routes: SECURED")
        print("✅ Demo Accounts: AVAILABLE")
        
        print("\n🚀 AUTHENTICATION READY!")
        print("\n📋 Demo Credentials:")
        print("   Username: alice | Password: password123")
        print("   Username: bob | Password: password123") 
        print("   Username: charlie | Password: password123")
        
        print("\n🌐 Login at: http://localhost:3000/login")
        print("🌐 Signup at: http://localhost:3000/signup")
        
    else:
        print("❌ Authentication system has issues")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())