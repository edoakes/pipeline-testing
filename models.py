import ray

@ray.remote
class Model:
    def __init__(self, *, multiply_by: int):
        self._k = multiply_by

    def forward(self, inp: int):
        return inp * self._k

@ray.remote
def combine(*args):
    return list(args)

async def get_num(request) -> int:
    return int(request.query_params.get("num", 1))
