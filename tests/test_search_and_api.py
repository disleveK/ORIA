import requests
from src.search.search_documents import search_documents

def test_search_documents():
    """Test the search functionality of the database."""
    results = search_documents("cancer")
    assert results, "Search query returned no results!"
    print("Search function works correctly!")

def test_api_search():
    """Test the REST API endpoint for search."""
    response = requests.get("http://127.0.0.1:5000/search", params={"q": "cancer"})
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    results = response.json()
    assert isinstance(results, list), "API did not return a list!"
    assert len(results) > 0, "API returned no results!"
    print("API search endpoint works correctly!")

if __name__ == "__main__":
    # Run database and API tests
    print("Testing database search functionality...")
    test_search_documents()

    print("Testing API search functionality...")
    test_api_search()