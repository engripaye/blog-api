from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# TEST CREATE BLOG
def test_create_blog():
    response = client.post("/blogs/", json={"title": "Test Blog", "content": "Testing content"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Blog"
    assert data["content"] == "Testing content"
    assert "id" in data


# TEST GET ALL BLOG
def test_get_all_blogs():
    response = client.get("/blogs/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1


# TEST GET BLOG BY ID
def test_get_blog_by_id():
    # Assuming blog with ID 1 exists
    response = client.get("/blogs/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


# TEST UPDATE BLOG
def test_update_blog():
    response = client.put("/blogs/1", json={"title": "Updated Title", "content": "Updated Content"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["content"] == "Updated Content"


# TEST DELETE BLOG
def test_delete_blog():
    # first create a blog
    create_response = client.post("/blogs/", json={"title": "Delete Blog", "content": "to be deleted"})
    assert create_response.status_code == 200
    blog_id = create_response.json()["id"]

    # Then delete the blog
    response = client.delete(f"/blogs/{blog_id}")
    assert response.status_code == 200
    data = response.json()
    assert f"Blog {blog_id} deleted successfully" in data["message"]
