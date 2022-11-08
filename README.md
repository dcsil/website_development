# website_development
website frontend and backend

### Setup environment and dependencies
1. run `chmod +x script/bootstrap`
2. run `./script/bootstrap`

### Setup alternative (if already has python3.10 and node.js)
#### Frontend: Vue
run `npm install`(automatically `npm run build` after)

#### Backend: Flask -> Python  
run `pip3 install -r requirements.txt`

### test
1. test both frontend and backend:
run `num run test`  

2. Test backend
run `pytest ./test_flask` to test backend

3. Test frontend
run `vitest --watch false` to test frontend

### server
1. run `num run start` for integrated frontend and backend  

2. run `npm run serve` for frontend development

3. run `flask (--debug run)` for backend development




