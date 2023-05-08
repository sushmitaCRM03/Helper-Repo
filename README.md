# Test
python3 -m venv blog-env
source blog-env/bin/activate
pip3 install fastapi
python3 -m pip install --upgrade pip
uvicorn main:app --reload
uvicorn blog.main:app --reload
