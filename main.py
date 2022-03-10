from ray import serve
from ray.serve import pipeline
from ray.serve.application import Application
from ray.serve.pipeline.api import build
from ray.serve.pipeline.pipeline_input_node import PipelineInputNode

from models import Model, get_num, combine

serve.start(detached=True)

with PipelineInputNode(get_num) as inp:
    a = Model.bind(multiply_by=2)
    b = Model.bind(multiply_by=4)
    output = combine.bind(a.forward.bind(inp), b.forward.bind(inp))

app = Application(build(output))
app.run()
