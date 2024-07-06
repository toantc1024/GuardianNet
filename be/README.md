# GuardianNet Backend

## **Setup**

### **Local Setup**

```python
git clone https://github.com/toantc1024/GuardianNet.git

# either using conda, venv or env
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
cd be
touch .env # copy the env format from the .env.example. For specific key, please refer to the team

# install requirement packages
pip install -r requirements-dev.txt

# run fastapi docs page
uvicorn main:app --reload
# open http://127.0.0.1:8000/api/guardiannet/docs
```
