import uvicorn

if __name__ == '__main__':
    uvicorn.run("PaltaTest.asgi:application", reload=True)