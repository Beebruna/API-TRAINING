from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


async def return_data():
    with open('JUSTIFICATIVA-1.pdf', 'rb') as fp:
        data = 'start'

        while data:
            data = fp.readline()
            yield data


@app.get('/test')
async def test():
    data_iter = return_data()
    return StreamingResponse(data_iter)
