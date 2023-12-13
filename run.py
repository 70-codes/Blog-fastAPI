import uvicorn


def main():
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8080,
        reload=1,
    )


if __name__ == "__main__":
    main()
